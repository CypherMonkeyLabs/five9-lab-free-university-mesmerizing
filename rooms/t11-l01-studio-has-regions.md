# Studio has regions

- The technical requirements publish Studio portal hosts by region: five9.us, five9.au, five9.ca, five9.uk, and five9.br studioportal.io, plus older inferencecommunications.com names. A task built in the wrong region will not be the task your VCC domain can call.
- SIP notes in that same part of the PDF, including UDP 5060 and a beta TCP 5061, are labeled next to Studio SBC material. Do not paste those ports onto every VCC trunk without checking which SBC family the domain uses. DNS SRV is the preferred way to find Five9 SIP resources.
- Match Studio region to the domain
- Prefer DNS SRV over a pinned IP

## Sources and go deeper

- [Technical requirements PDF](https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf). vendor. last checked 2026-10. Fetched for this lab in October 2026. Re-read before you buy hardware or open a firewall.
- [IANA service names and port numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml). ports. last checked 2026-10.
- [RFC 3261, SIP: Session Initiation Protocol](https://www.rfc-editor.org/rfc/rfc3261). rfc. last checked 2026-10.
- [RFC 1035, domain names](https://www.rfc-editor.org/rfc/rfc1035). rfc. last checked 2026-10.
- [RFC 2782, DNS SRV](https://www.rfc-editor.org/rfc/rfc2782). rfc. last checked 2026-10.
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293). rfc. last checked 2026-10.
- [RFC 768, User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768). rfc. last checked 2026-10.
- confirm. Studio signaling ports in the PDF are easy to misread as universal VCC trunk ports. Confirm which SBC your domain uses. last checked 2026-10.
