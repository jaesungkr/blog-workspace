#!/usr/bin/env python3
"""Capture independent focused evidence for each mobile table state."""

from __future__ import annotations

import base64
import hashlib
import json
import sys
import uuid
from pathlib import Path


POST_DIR = Path(__file__).resolve().parents[4]
REPO_ROOT = POST_DIR.parents[1]
SCRIPT_DIR = (
    REPO_ROOT
    / ".agents/skills/dev-log-rich-post-workspace/scripts"
)
sys.path.insert(0, str(SCRIPT_DIR))

from capture_rich_qa import (  # noqa: E402
    CDPClient,
    ChromeProcess,
    WebSocket,
    evaluate_page,
    find_chrome,
    validate_page_measurements,
)


SLUG = "gyeonggi-finance-crisis-fact-check"
PREVIEW = (
    POST_DIR
    / "artifacts/qa/independent-rendered"
    / f"{SLUG}-rich-preview.html"
)
OUTPUT_DIR = Path(__file__).resolve().parent


def evaluate(client: CDPClient, expression: str):
    response = client.call(
        "Runtime.evaluate",
        {
            "expression": expression,
            "awaitPromise": True,
            "returnByValue": True,
            "userGesture": False,
        },
    )
    if response.get("exceptionDetails"):
        raise RuntimeError(response["exceptionDetails"])
    return response["result"].get("value")


def screenshot(client: CDPClient, path: Path) -> str:
    response = client.call(
        "Page.captureScreenshot",
        {
            "format": "png",
            "fromSurface": True,
            "captureBeyondViewport": False,
        },
    )
    payload = base64.b64decode(response["data"], validate=True)
    path.write_bytes(payload)
    return hashlib.sha256(payload).hexdigest()


def element_screenshot(client: CDPClient, path: Path, rect: dict) -> str:
    response = client.call(
        "Page.captureScreenshot",
        {
            "format": "png",
            "fromSurface": True,
            "captureBeyondViewport": True,
            "clip": {
                "x": rect["x"],
                "y": rect["y"],
                "width": rect["width"],
                "height": rect["height"],
                "scale": 1,
            },
        },
    )
    payload = base64.b64decode(response["data"], validate=True)
    path.write_bytes(payload)
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    preview_uri = PREVIEW.resolve().as_uri()
    preview_sha256 = hashlib.sha256(PREVIEW.read_bytes()).hexdigest()
    session = str(uuid.uuid4())
    records = []

    with ChromeProcess(find_chrome(None), 10) as chrome:
        with WebSocket(chrome.page_websocket_url, 30) as websocket:
            client = CDPClient(websocket, 30)
            client.call("Page.enable")
            client.call("Runtime.enable")

            for width, height in ((1280, 900), (390, 844), (360, 800)):
                client.call(
                    "Emulation.setDeviceMetricsOverride",
                    {
                        "width": width,
                        "height": height,
                        "deviceScaleFactor": 1,
                        "mobile": width < 735,
                        "screenWidth": width,
                        "screenHeight": height,
                        "positionX": 0,
                        "positionY": 0,
                        "dontSetVisibleSize": False,
                    },
                )
                client.discard_events("Page.loadEventFired")
                client.call("Page.navigate", {"url": preview_uri})
                client.wait_event("Page.loadEventFired", timeout=30)
                page = evaluate_page(client, 20)
                validate_page_measurements(page, preview_uri, width, height)

                tables = []
                if width < 735:
                    table_count = evaluate(
                        client,
                        "document.querySelectorAll('.rich-table-wrap').length",
                    )
                    for index in range(table_count):
                        states = []
                        for side in ("left", "right"):
                            state = evaluate(
                                client,
                                f"""
(() => {{
  const wrapper = document.querySelectorAll('.rich-table-wrap')[{index}];
  const table = wrapper.querySelector('table');
  const headers = Array.from(table.querySelectorAll('th')).map((node) => node.innerText.trim());
  const firstRow = Array.from(table.querySelectorAll('tbody tr:first-child td')).map((node) => node.innerText.trim());
  wrapper.scrollLeft = {"0" if side == "left" else "wrapper.scrollWidth - wrapper.clientWidth"};
  wrapper.scrollIntoView({{block: 'center', inline: 'nearest'}});
  return new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => {{
    const style = getComputedStyle(wrapper);
    const root = document.documentElement;
    resolve({{
      side: {json.dumps(side)},
      document_client_width: root.clientWidth,
      document_scroll_width: root.scrollWidth,
      wrapper_client_width: wrapper.clientWidth,
      wrapper_scroll_width: wrapper.scrollWidth,
      wrapper_scroll_left: wrapper.scrollLeft,
      wrapper_max_scroll_left: wrapper.scrollWidth - wrapper.clientWidth,
      overflow_x: style.overflowX,
      font_size: getComputedStyle(table).fontSize,
      line_height: getComputedStyle(table).lineHeight,
      headers,
      first_row: firstRow
    }});
  }})));
}})()
""",
                            )
                            shot = OUTPUT_DIR / f"table-{index + 1}-{width}-{side}.png"
                            state["screenshot"] = shot.relative_to(POST_DIR).as_posix()
                            state["screenshot_sha256"] = screenshot(client, shot)
                            states.append(state)
                        tables.append({"index": index + 1, "states": states})

                figure = evaluate(
                    client,
                    """
(() => {
  const figure = document.querySelector('.devlog-rich__figure');
  const image = figure.querySelector('img');
  const caption = figure.querySelector('figcaption');
  const rect = figure.getBoundingClientRect();
  return {
    rect: {
      x: rect.left + window.scrollX,
      y: rect.top + window.scrollY,
      width: rect.width,
      height: rect.height
    },
    image_complete: image.complete,
    image_natural_width: image.naturalWidth,
    image_natural_height: image.naturalHeight,
    image_display_width: image.getBoundingClientRect().width,
    image_display_height: image.getBoundingClientRect().height,
    alt: image.alt,
    caption: caption.innerText.trim(),
    caption_font_size: getComputedStyle(caption).fontSize,
    caption_line_height: getComputedStyle(caption).lineHeight
  };
})()
""",
                )
                figure_shot = OUTPUT_DIR / f"figure-{width}.png"
                figure["screenshot"] = figure_shot.relative_to(POST_DIR).as_posix()
                figure["screenshot_sha256"] = element_screenshot(
                    client,
                    figure_shot,
                    figure.pop("rect"),
                )

                list_metrics = evaluate(
                    client,
                    """
(() => {
  const list = document.querySelector('.devlog-rich__section ol');
  const items = list ? Array.from(list.children) : [];
  const following = list ? list.nextElementSibling : null;
  return {
    ordered_list_found: Boolean(list),
    marker_style: list ? getComputedStyle(list).listStyleType : null,
    item_displays: items.map((item) => getComputedStyle(item).display),
    item_margin_tops: items.map((item) => getComputedStyle(item).marginTop),
    list_margin_bottom: list ? getComputedStyle(list).marginBottom : null,
    following_tag: following ? following.tagName : null
  };
})()
""",
                )
                records.append(
                    {
                        "width": width,
                        "height": height,
                        "page": page,
                        "figure": figure,
                        "tables": tables,
                        "list": list_metrics,
                    }
                )

        browser_version = chrome.version.get("Browser")

    output = {
        "version": 1,
        "reviewer": "Hegel",
        "session": session,
        "browser": browser_version,
        "preview": PREVIEW.relative_to(POST_DIR).as_posix(),
        "preview_sha256": preview_sha256,
        "viewports": records,
    }
    (OUTPUT_DIR / "table-review.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
