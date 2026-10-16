# Ports and protocols

- 80 TCP Outbound: HTTP for sign-in, reporting, and support pages.
- 443 TCP Outbound: HTTPS for sign-in, reporting, and support.
- 1024-65535 UDP Outbound: RTP between Five9 applications. Without a stateful firewall, allow the return path. WebRTC also sends STUN on these ports.
- 2200-2300 TCP Outbound: Encrypted Java RMI on the community softphone table. Java Agent and Supervisor desktops left the customer portal after 1 August 2026. Confirm whether your site still launches Java admin.
- 5060-5067 UDP Outbound: SIP for the agent application.
- 5080 UDP Outbound: SIP signaling on the Five9 SIP proxy.
- 5081 TCP Outbound: SIP over TLS on the Five9 SIP proxy.
- 8000-8015 UDP Outbound: Source ports the article lists for desktop RTP.
- 8080/8081 TCP Outbound: Network assessment at quality.five9.com.
- 8083 TCP Local: Five9 Softphone Service. The article says to keep other processes off it, and to open it on the host firewall when VDI needs it.
- 8843 TCP Outbound: HTTPS download of Five9 applications and API.
- 8880 TCP Outbound: HTTP download of Five9 applications.
- 443 TCP Outbound: Supervisor PC to WEM cloud, application access.
- 4443 TCP Outbound: Supervisor or admin workstation to the VO cloud for the Interaction Analytics UI.

## Sources and go deeper

- [Community port article](https://community.five9.com/s/article/Network-Port-Requirements-for-Softphone-Gateway-PSTN-Customers?language=en_US). community. last checked 2026-10.
- [WebRTC community article](https://community.five9.com/s/article/VCC-Five9-WebRTC). community. last checked 2026-10.
- [Java application requirements](https://documentation.five9.com/bundle/technical-reqs/page/technical-reqs/agent-supervisor-apps/java-based-application-reqs.htm). vendor. last checked 2026-10.
- [IANA service names and port numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml). ports. last checked 2026-10.
- [RFC 3261, SIP: Session Initiation Protocol](https://www.rfc-editor.org/rfc/rfc3261). rfc. last checked 2026-10.
- [RFC 3550, RTP](https://www.rfc-editor.org/rfc/rfc3550). rfc. last checked 2026-10.
- [RFC 3551, RTP profile for audio and video](https://www.rfc-editor.org/rfc/rfc3551). rfc. last checked 2026-10.
- [ITU-T G.711](https://www.itu.int/rec/T-REC-G.711). standard. last checked 2026-10.
- [RFC 8446, TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446). rfc. last checked 2026-10.
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293). rfc. last checked 2026-10.
- [RFC 768, User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768). rfc. last checked 2026-10.
- [RFC 8825, WebRTC overview](https://www.rfc-editor.org/rfc/rfc8825). rfc. last checked 2026-10.
