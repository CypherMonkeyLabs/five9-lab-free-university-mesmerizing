# A DNIS answers only while the campaign runs

- An inbound campaign receives calls for a DNIS and processes them with that campaign's IVR script. The inbound topic is blunt about state: if the campaign is not running, callers hear a busy signal.
- Greetings, skills, and hold music never get a chance to run in that state. The first check on a new number is the campaign state, not the carrier.
- Tie DNIS, run state, and IVR together
- Check state before the carrier

## Sources and go deeper

- [Inbound campaigns](https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/creating-campaigns/types-of-campaigns/inbound-campaigns.htm). vendor. last checked 2026-10.
- [ITU-T E.164, international public telecommunication numbering](https://www.itu.int/rec/T-REC-E.164). standard. last checked 2026-10.
- [Interactive voice response](https://en.wikipedia.org/wiki/Interactive_voice_response). wikipedia. last checked 2026-10.
