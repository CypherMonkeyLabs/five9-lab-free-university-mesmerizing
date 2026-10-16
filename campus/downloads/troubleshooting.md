# Troubleshooting tree

- The DNIS does not answer. First check: Is the inbound campaign running, or only built?
- Callers land on a queue nobody staffed. First check: Open the Skill Transfer module.
- The agent hears silence, or the caller does. First check: Confirm signaling is up. A 200 OK does not prove RTP.
- Voice is live and the CRM pane is blank. First check: The adapter uses HTTPS and Secure WebSocket.
- The agent cannot paste a phone number. First check: Check whether the campaign is in TCPA manual touch.
- Customers hear a click and no agent. First check: Name the mode. Preview does not outdial. Predictive does.
- A test 911 call would send responders to the old HQ. First check: The address has to be the room the person is in.
- Standard reports are missing for a supervisor. First check: The user needs the reporting role and a reporting permission.
- The audio you need is gone. First check: Name which clock: audio, E911 recording, agent data, campaign state, the call log, or the DID.
- The IVA will not return the caller to a person. First check: Confirm the Studio region matches the task you copied.

## Sources and go deeper

- [Inbound campaigns](https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/creating-campaigns/types-of-campaigns/inbound-campaigns.htm). vendor. last checked 2026-10.
- [Skill Transfer functions](https://community.five9.com/s/article/Administrator-IVR-Skill-Transfer-Module-Functions-and-Features). community. last checked 2026-10.
- [Community port article](https://community.five9.com/s/article/Network-Port-Requirements-for-Softphone-Gateway-PSTN-Customers?language=en_US). community. last checked 2026-10.
- [Technical requirements PDF](https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf). vendor. last checked 2026-10.
- [TCPA manual touch](https://community.five9.com/s/article/Administrator-TCPA-Manual-Touch-Dialing-Mode?language=en_US). community. last checked 2026-10.
- [Default campaign settings](https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-dialing-modes/default-campaign-settings.htm). vendor. last checked 2026-10.
- [E911 data sheet](https://www.five9.com/sites/default/files/2022-11/Data-sheet-Five9-emergency-services%20%28E911%29.PDF). vendor. last checked 2026-10.
- [Generating standard reports](https://community.five9.com/s/article/Reporting-I-Generating-Standard-Reports). community. last checked 2026-10.
- [Data retention](https://www.five9.com/legal/dataretention). vendor. last checked 2026-10.
- [Studio digital IVA with VCC](https://community.five9.com/s/article/Studio-7-Integrate-Digital-IVA-in-Studio-with-VCC?language=en_US). community. last checked 2026-10.
- [RFC 3550, RTP](https://www.rfc-editor.org/rfc/rfc3550). rfc. last checked 2026-10.
- [RFC 3551, RTP profile for audio and video](https://www.rfc-editor.org/rfc/rfc3551). rfc. last checked 2026-10.
- [ITU-T G.711](https://www.itu.int/rec/T-REC-G.711). standard. last checked 2026-10.
- [RFC 6455, The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455). rfc. last checked 2026-10.
- [ITU-T E.164, international public telecommunication numbering](https://www.itu.int/rec/T-REC-E.164). standard. last checked 2026-10.
- [Enhanced 9-1-1](https://en.wikipedia.org/wiki/Enhanced_9-1-1). wikipedia. last checked 2026-10.
- [Telephone Consumer Protection Act of 1991](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991). wikipedia. last checked 2026-10.
