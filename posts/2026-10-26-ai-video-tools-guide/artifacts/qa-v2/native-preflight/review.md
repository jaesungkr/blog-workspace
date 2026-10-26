# Native attachment preflight

The actual Tistory preview recognized both original uploaded images, approved alt text, captions, and ordering. Editor content was copied through the normal UI and matched the provisional fragment byte-for-byte (24,391 characters). No source changes were made.

Desktop 1280 and fresh mobile 360 were inspected in light and dark hELLO themes. Fresh mobile had document width 360 and scroll width 360; both images loaded at 1280 pixels natural width after scrolling them into view. Tables remain in their local horizontal scroll regions. The preview has no thumbnail cover behind its title; live cover needs verification after publication.

Separate resize limitation: resizing an already-loaded desktop preview to 360 left Google ad hosts aswift_7_host and aswift_8_host at 736 pixels, increasing document scroll width to 772. Fresh 360 loading did not reproduce it. No page-wide overflow suppression was added. Clicking a relative TOC anchor in the new-post srcdoc preview navigates to the editor base URL; all targets exist, and actual navigation must be checked on the public page.
