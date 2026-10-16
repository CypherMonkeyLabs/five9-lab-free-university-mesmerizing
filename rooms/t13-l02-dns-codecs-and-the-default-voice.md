# DNS, codecs, and the default voice

- The requirements prefer DNS SRV for the SIP targets. G.711 is the default codec, and the PDF describes it as uncompressed. Do not invent a packetization time. A 20 millisecond ptime shows up in practitioner notes about Cisco gateways. It is not a number this lab will attribute to the Five9 PDF.
- RFC 3261 is the SIP signaling baseline. RFC 4733 is the telephone-event way digits often ride once the call is up. DTMF design is a separate sentence from the codec.
- Prefer DNS SRV
- Keep G.711 as the default you can cite

## Sources and go deeper

- [Technical requirements PDF](https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf). vendor. last checked 2026-10. Fetched for this lab in October 2026. Re-read before you buy hardware or open a firewall.
- [SIP trunk options chapter](https://documentation.five9.com/bundle/technical-reqs/page/technical-reqs/SIP-trunk-options/_ch-five9-sip-trunk-options.htm). vendor. last checked 2026-10.
- [RFC 3261](https://www.rfc-editor.org/rfc/rfc3261). rfc. last checked 2026-10.
- [RFC 4733](https://www.rfc-editor.org/rfc/rfc4733). rfc. last checked 2026-10.
- [RFC 3550, RTP](https://www.rfc-editor.org/rfc/rfc3550). rfc. last checked 2026-10.
- [RFC 3551, RTP profile for audio and video](https://www.rfc-editor.org/rfc/rfc3551). rfc. last checked 2026-10.
- [ITU-T G.711](https://www.itu.int/rec/T-REC-G.711). standard. last checked 2026-10.
- [RFC 1035, domain names](https://www.rfc-editor.org/rfc/rfc1035). rfc. last checked 2026-10.
- [RFC 2782, DNS SRV](https://www.rfc-editor.org/rfc/rfc2782). rfc. last checked 2026-10.
- confirm. A 20 ms packet time is a practitioner note about Cisco gateways, not a figure quoted from the Five9 technical requirements in this lab. last checked 2026-10.
