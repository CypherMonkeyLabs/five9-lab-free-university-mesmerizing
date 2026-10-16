# NAT, idle timers, and split tunnels

- NAT and PAT are acceptable. Double NAT is not. UDP bindings that idle out cause one-way audio. The requirements use a 30 second UDP idle timeout as the planning number, and they tell you to send keepalives when the binding is shorter.
- On a VPN, translate RFC 1918 space to a public address the far side can route. Do not exclude Five9 domains from a split tunnel and then wonder why signaling dies. Do not restrict SIP or RTP between sites.
- Reject double NAT
- Keep Five9 inside the VPN

## Sources and go deeper

- [Technical requirements PDF](https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf). vendor. last checked 2026-10. Fetched for this lab in October 2026. Re-read before you buy hardware or open a firewall.
- [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918). rfc. last checked 2026-10.
- [RFC 3261](https://www.rfc-editor.org/rfc/rfc3261). rfc. last checked 2026-10.
- [RFC 3550, RTP](https://www.rfc-editor.org/rfc/rfc3550). rfc. last checked 2026-10.
- [RFC 3551, RTP profile for audio and video](https://www.rfc-editor.org/rfc/rfc3551). rfc. last checked 2026-10.
- [ITU-T G.711](https://www.itu.int/rec/T-REC-G.711). standard. last checked 2026-10.
- [RFC 768, User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768). rfc. last checked 2026-10.
- [RFC 4787, NAT behavior for UDP](https://www.rfc-editor.org/rfc/rfc4787). rfc. last checked 2026-10.
