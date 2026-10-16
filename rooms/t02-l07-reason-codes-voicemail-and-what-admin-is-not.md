# Reason codes, voicemail, and what admin is not

- Not every silence is a carrier failure. Agents have Not Ready states. TCPA manual touch even forces Not Ready when preview time expires. Skill groups can hold voicemail, greetings, and messages. Those are administrator objects with their own reports.
- Admin work does not include inventing a dialer ratio in a spreadsheet and calling it the Five9 algorithm. The dialer has documented modes and a documented abandon window. Configuration belongs in the campaign, not in a side file.
- Treat voicemail as a skill object
- Keep dialer math in the campaign

## Sources and go deeper

- [Skill groups](https://documentation.five9.com/bundle/basic-admin/page/basic-admin/skill-groups/_ch-skill-groups.htm). vendor. last checked 2026-10.
- [TCPA manual touch](https://community.five9.com/s/article/Administrator-TCPA-Manual-Touch-Dialing-Mode?language=en_US). community. last checked 2026-10.
- [Telephone Consumer Protection Act of 1991](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991). wikipedia. last checked 2026-10.
