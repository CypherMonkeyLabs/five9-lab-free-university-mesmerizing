# Visual IVR and frames

- The technical requirements say administrators can apply web page security so a Visual IVR script is not embedded in a frame where the user can be hijacked. The mechanism named is the X-Frame-Options header. The browser table in that PDF lists old versions and tells you to test others.
- A visual script is still a script: prompts, branches, and a handoff. Framing is an extra threat. Do not treat a 2016-era browser row as the current support list. The PDF says to retest.
- Protect visual IVR from hostile frames
- Retest browsers

## Sources and go deeper

- [Technical requirements PDF](https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf). vendor. last checked 2026-10. Fetched for this lab in October 2026. Re-read before you buy hardware or open a firewall.
- [IVR modules](https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/_ch-modules.htm). vendor. last checked 2026-10.
- [Interactive voice response](https://en.wikipedia.org/wiki/Interactive_voice_response). wikipedia. last checked 2026-10.
- confirm. The PDF's browser matrix is historical. Current browser behavior has to be tested. last checked 2026-10.
