# What an extract is allowed to remember

- Reporting Web Services can move numbers out of the domain. Retention still applies to what Five9 keeps, not to the warehouse you built. Once a row is in your bucket, your policy owns it.
- Disabled domains, campaign state, agent data, and numbers have their own retention lines: agent data 60 days, campaign state 120 days, a disabled domain 120 days after closure, DIDs and toll-free numbers 90 days after closure. Do not design a 'temporary' domain and expect the DIDs to wait forever.
- Export before the clocks run out
- Keep DID retention separate from domain retention

## Sources and go deeper

- [Data retention](https://www.five9.com/legal/dataretention). vendor. last checked 2026-10.
- [APIs and SDKs](https://www.five9.com/platform/integrations-and-ecosystem/apis-and-sdks). vendor. last checked 2026-10.
- [Generating standard reports](https://community.five9.com/s/article/Reporting-I-Generating-Standard-Reports). community. last checked 2026-10.
