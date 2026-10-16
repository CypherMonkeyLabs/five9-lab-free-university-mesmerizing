# After-call work feeds the next dial · Learn it in 5 minutes

- A disposition is what the dialer remembers. A final code stops the record. A retryable code brings it back after the redial rules. Wrap time, in the simulator, is the gap before the agent is free again. Five9's pause-before-transfer is a different gap, on the next inbound delivery, and it is not reported as hold.
- If wrap is fiction and pause is zero, a blended agent finishes one call and is instantly eligible. That is how a progressive book and an inbound queue trade the same person every few seconds.

## Sources and go deeper

- [Managing campaign dispositions](https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-dispositions/managing-dispositions.htm). vendor. last checked 2026-10.
- [Pause before transfer](https://community.five9.com/s/article/Administrator-Pause-Before-Transfer?language=en_US). community. last checked 2026-10.
