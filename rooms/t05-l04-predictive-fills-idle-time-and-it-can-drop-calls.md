# Predictive fills idle time, and it can drop calls

- The dialer page says predictive mode uses algorithms to predict agent availability and is suited to more than 10 active agents. The outbound page says it increases time spent talking to people instead of dialing. Both are marketing descriptions of an overdial.
- The default-settings topic is the control room: monitor abandoned call percentage, a max percentage, a warning if you change the max, 30 rolling days on US domains, and 24 hours on UK domains. A community test article says predictive throttles and does not necessarily lock to one-to-one, while other lines in that same article talk about dropping to one-to-one. Use the settings page as the control. Treat the test article as a field note with mixed wording.
- Explain predictive without claiming the source code
- Quote the 30-day and 24-hour windows

## Sources and go deeper

- [Dialer product page](https://www.five9.com/products/capabilities/dialer-system). vendor. last checked 2026-10.
- [Outbound product page](https://www.five9.com/products/capabilities/outbound-contact-center). vendor. last checked 2026-10.
- [Default campaign settings](https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-dialing-modes/default-campaign-settings.htm). vendor. last checked 2026-10.
- [Dialing modes live testing](https://community.five9.com/s/article/Administrator-Campaign-Dialing-Modes-and-Live-Testing-Results). community. last checked 2026-10. Community test notes. Wording inside the article is not uniform.
- confirm. The exact throttle curve is not specified on the default-settings page. The community test article disagrees with itself about an instant drop to 1:1.. last checked 2026-10.
