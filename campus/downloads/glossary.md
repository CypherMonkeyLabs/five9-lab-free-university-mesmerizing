# Glossary starter

- Domain: The VCC tenant. Skills, users, lists, and campaigns stay inside it.
- Skill group: Agents or supervisors who can take a campaign's work. A user and a campaign can have more than one.
- User profile: The permission template for a person. Not a campaign profile.
- Campaign profile: Overrides defaults such as ANI. One profile is assigned to a campaign. The same profile can be reused.
- Campaign: Inbound, outbound, or autodial. Blended is staffing language, not a fourth type.
- DNIS: The number an inbound campaign answers. A stopped campaign does not answer.
- Disposition: The outcome code on a call. Final disposition stops the other numbers on that record for the campaign.
- List penetration: The default list walk: first number on every record, then the next number.
- Vertical dialing: Finishes the numbers on one record before moving on. Community notes say the compass wording is easy to misread.
- Preview: The agent sees CRM history before the dial.
- Progressive: The outbound page describes one customer call per available agent. The dialer page also says adaptive pace. Quote the page you mean.
- Power: A configured number of calls per agent, with an abandon throttle.
- Predictive: Algorithmic pacing. Product guidance talks about teams larger than about ten agents.
- Manual touch: No automatic dial. TCPA manual touch adds typing, blocks paste, and enables Dial on a match.
- Max Abandoned Call Percentage: A campaign field with a warning if you change it. This lab does not state a numeric default.
- IVR module: A named block in the IVR Administrator's Guide, such as Menu, Play, If/Else, or Skill Transfer.
- Skill Transfer: Sends the call toward one or more skills. No skill selected means the Default queue in the community write-up.
- Default queue: Where a Skill Transfer with no skill goes, per the community article.

## Sources and go deeper

- [Planning your implementation](https://documentation.five9.com/bundle/basic-admin/page/basic-admin/intro/planning-your-implementation.htm). vendor. last checked 2026-10.
- [Skill groups](https://documentation.five9.com/bundle/basic-admin/page/basic-admin/skill-groups/_ch-skill-groups.htm). vendor. last checked 2026-10.
- [Campaign profiles](https://documentation.five9.com/bundle/basic-admin/page/basic-admin/campaign-profiles/_ch-campaign-profiles.htm). vendor. last checked 2026-10.
- [Inbound campaigns](https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/creating-campaigns/types-of-campaigns/inbound-campaigns.htm). vendor. last checked 2026-10.
- [List dialing modes](https://community.five9.com/s/article/Administrator-List-Dialing-Modes-and-its-Differences?language=en_US). community. last checked 2026-10.
- [ITU-T E.164, international public telecommunication numbering](https://www.itu.int/rec/T-REC-E.164). standard. last checked 2026-10.
- [Telephone Consumer Protection Act of 1991](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991). wikipedia. last checked 2026-10.
- [Interactive voice response](https://en.wikipedia.org/wiki/Interactive_voice_response). wikipedia. last checked 2026-10.
