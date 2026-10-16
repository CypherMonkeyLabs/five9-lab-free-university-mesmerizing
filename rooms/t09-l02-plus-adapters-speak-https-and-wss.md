# Plus adapters speak HTTPS and WSS

- The technical requirements say Plus adapters use HTTPS and Secure WebSocket. If a proxy is in the path, it must support WSS. The PDF also says Five9 does not support TLS 1.1, and that browsers need TLS 1.2. Unencrypted API connections are refused.
- A screen pop that fails while voice still works is often this path: the media is fine and the websocket is not. Do not replace the headset first.
- Separate voice from the pop channel
- Require TLS 1.2 and WSS

## Sources and go deeper

- [Technical requirements PDF](https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf). vendor. last checked 2026-10. Fetched for this lab in October 2026. Re-read before you buy hardware or open a firewall.
- [Web adapter requirements](https://documentation.five9.com/bundle/technical-reqs/page/technical-reqs/agent-integrations/web-based-adapters/application-requirements.htm). vendor. last checked 2026-10.
- [RFC 8446, TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446). rfc. last checked 2026-10.
- [RFC 6455, The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455). rfc. last checked 2026-10.
