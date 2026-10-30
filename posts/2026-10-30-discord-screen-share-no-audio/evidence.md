# Evidence — Discord screen share no audio

Checked 2026-10-30. Researcher: assistant. No end-to-end Windows/Discord audio reproduction.

| ID | Claim | Basis | Limit |
|---|---|---|---|
| stream-volume | Viewer can unmute stream and change Stream Volume | https://support.discord.com/hc/en-us/articles/360040816151-Go-Live-and-Screen-Share (updated June 19 2026), viewer troubleshooting + actual image https://support.discord.com/hc/article_attachments/19155533433495 | Published UI example; Korean translation provided as explanation |
| app-selection | Share application or whole screen; option includes app/system audio | https://discord.com/blog/how-to-stream-to-discord-from-desktop-or-mobile (Dec 17 2024), paragraphs Share Application vs Share Entire Screen; July 1 2024 patch notes corroborates system audio both modes | Do not claim whole-screen audio universally unavailable; installed current UI not tested |
| windows-volume-mixer | Windows 11 app volume and app-specific output device | https://support.microsoft.com/en-us/windows/hardware/audio/fix-app-audio-not-working-while-system-sounds-work-in-windows | Exact Win11 path supplied by Microsoft; no Windows10 path promise |
| windows-volume-mixer-image | Native published mixer example | https://support.microsoft.com/en-us/windows/hardware/audio/fix-sound-or-audio-problems-in-windows image https://support.microsoft.com/en-us/windows/media/sound-settings-volume-mixer-png.png | Example shows system sounds, not a fabricated game entry; body directs reader to own app |
| restart | Full exit and restart supported troubleshooting | https://support.discord.com/hc/en-us/articles/360045138471-Discord-Voice-and-Video-Troubleshooting-Guide | Avoid indiscriminate microphone/hardware acceleration/reset fixes for narrow audio-only symptom |
| diagnosis | One viewer vs all viewers; one source app vs multiple source apps | Editorial diagnostic framework synthesized from above separate controls | Routes investigation, does not prove exact root cause |
| related | Existing blog Bluetooth article checked via web open, title and article matched | https://dop3n.tistory.com/entry/게임·디스코드에서-블루투스-이어폰-음질이-나빠지는-이유와-해결-순서 | Distinct symptom: voice-triggered quality degradation not missing shared-app audio |

## Asset provenance and rights

Official educational UI excerpts are used for specific settings commentary with nearby official-source attribution. No claim of public-domain or unrestricted reuse. No generated UI. app-selection.png retains original red highlight and macOS window chrome. Volume mixer retains Microsoft original greyed device details. Unused GIF/source images remain in artifacts only. User review precedes any public upload.
