# Do-not-call is a list, and a module

- Outbound product material lists DNC list management with time-zone rules and Certified Caller as compliance tools. Inside the IVR, Set DNC is a real module in the modules chapter. A spoken 'remove me' path should hit that module, not a note in a disposition comment.
- A disposition called DNC is not the same object as the Set DNC module. Use both only if you know which system each one updates. This lab does not pretend they are automatically the same switch.
- Use the Set DNC module
- Do not confuse it with a disposition label

## Sources and go deeper

- [IVR modules](https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/_ch-modules.htm). vendor. last checked 2026-10.
- [Outbound product page](https://www.five9.com/products/capabilities/outbound-contact-center). vendor. last checked 2026-10.
- [Generating standard reports](https://community.five9.com/s/article/Reporting-I-Generating-Standard-Reports). community. last checked 2026-10.
- [Interactive voice response](https://en.wikipedia.org/wiki/Interactive_voice_response). wikipedia. last checked 2026-10.
- confirm. Public pages do not spell out, in one paragraph, whether a custom disposition named DNC writes the same list as the Set DNC module. Confirm in your domain.. last checked 2026-10.
