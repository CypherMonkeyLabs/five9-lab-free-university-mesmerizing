from curriculum_lib import ADP, ADAPTERS, TECH, APIS, MODULES, SNOW, lesson, stack, compare, path, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "The adapter family", "foundation", [
        "The technical requirements list Plus adapters for Agent Desktop Toolkit, Epic, Microsoft Dynamics 365, NetSuite, Oracle, Salesforce, ServiceNow, and Zendesk. They use HTTPS and Secure WebSocket. The desktop page says a pre-built adapter and Plus share the same underlying technology, and that a CRM SDK exists when you bring your own CRM.",
        "The product API page also names Web Connectors. A connector that pops a URL is not the same object as a full Plus adapter. Say which one you deployed.",
    ], [ADAPTERS, ADP, APIS, TECH], stack("Named Plus adapters", "From the technical requirements list.", ["Salesforce", "ServiceNow", "Dynamics 365", "Zendesk", "Oracle", "NetSuite", "Epic", "Desktop Toolkit"]),
    "Pick the integration", ["CRM", "Five9"], [
        ("CRM", "Known", "The CRM is one of the named products.", "known"),
        ("Five9", "Adapter", "The matching Plus adapter is the first choice.", "adapter"),
        ("CRM", "Other", "Anything else starts with the CRM SDK.", "sdk"),
        ("Five9", "Pop", "A web connector can open a URL.", "url"),
        ("Five9", "WSS", "The proxy must pass Secure WebSocket.", "wss"),
        ("Admin", "Say", "The design names adapter, SDK, or connector.", "say"),
    ], [
        ("ServiceNow is in the adapter list. True or false?", ["False", "True", "Only as a connector rumor", "Only in Studio"], 1, "The PDF lists the ServiceNow Plus adapter."),
        ("An unlisted homegrown CRM uses", ["A fictional adapter", "The CRM SDK, per the product pages", "Only FTP", "Only Java admin"], 1, "Bring your own CRM is the SDK line."),
        ("A URL pop is", ["Always a Plus adapter", "Often a web connector. Say which", "A skill", "A list mode"], 1, "Connectors and adapters are both real and different."),
        ("Proxy requirement is", ["Optional HTTP", "WSS support", "Double NAT", "TLS 1.1"], 1, "Plus adapters need a WSS-capable proxy if you have one."),
        ("Epic is", ["Not listed", "In the Plus adapter list", "A dialer mode", "A codec"], 1, "The PDF names Epic."),
    ], [("ServiceNow listed?", "Yes."), ("Homegrown CRM?", "CRM SDK."), ("URL pop versus adapter?", "Name which one."), ("Proxy?", "Must support WSS.")],
    ("Name it", "For three systems, write adapter, SDK, or connector.", ["Salesforce", "An internal CRM", "A simple URL pop"], "The three words are not interchangeable."),
    ("The pop is a bookmark", "Leadership thinks they bought the Salesforce adapter. Agents click a bookmark.", "ADAPTER absent BOOKMARK yes", ["Deploy the adapter or call the bookmark a connector, honestly", "Rename the bookmark", "Add lines", "Delete IVR"], 0, "The object in production is not the object in the slide.", "Install the adapter or document the connector."),
    ["Name the adapter, the SDK, or the connector", "Keep WSS in the design"]))
    R.append(L("l02", "Salesforce versions move", "practice", [
        "The technical requirements fetched for this lab say the Salesforce managed package is 2.46, SAML 2.0 is supported, and Lightning CTI is supported on Sales Cloud and Service Cloud for Professional, Enterprise, Unlimited, and Performance. Lightning Experience is supported for the Plus adapter.",
        "2.46 is a line in a PDF, not a law. The next PDF can move it. Write 'as of the PDF we read' on any design that copies the number. Internet Explorer is ended except IE 11 for the Oracle Service Cloud adapter only, which is a different CRM.",
    ], [TECH, ADAPTERS], stack("Salesforce lines that age", "Re-read before you freeze a standard.", ["Package version in the PDF", "SAML 2.0", "Lightning CTI", "Those four editions"]),
    "Check the package", ["PDF", "Org"], [
        ("PDF", "Read", "The current technical requirements are opened.", "pdf"),
        ("PDF", "Version", "The package number is copied with a date.", "ver"),
        ("Org", "Installed", "The org's installed package is compared.", "org"),
        ("Org", "CTI", "Lightning CTI is the mode in the note.", "cti"),
        ("Org", "Edition", "The edition is one of the supported names, or it is not.", "ed"),
        ("Admin", "Stop", "IE is not the Salesforce browser story.", "ie"),
    ], [
        ("This lab treats package 2.46 as", ["Eternal", "The number in the PDF it read. Recheck", "A dialer mode", "A skill"], 1, "Versions move."),
        ("SAML version named for that adapter is", ["1.1", "2.0", "3.0", "None"], 1, "The PDF says 2.0."),
        ("Lightning CTI is", ["Unsupported", "Supported, including Lightning Experience for the Plus adapter", "Voice-only", "Removed"], 1, "The PDF says so."),
        ("Editions named include", ["Essentials only", "Professional, Enterprise, Unlimited, and Performance", "Free", "Trial only"], 1, "That is the list in the PDF."),
        ("IE 11 remains for", ["Salesforce", "The Oracle Service Cloud adapter only", "All adapters", "Studio"], 1, "The PDF carves out that one exception."),
    ], [("Is 2.46 forever?", "No. Recheck the PDF."), ("SAML?", "2.0 in that PDF."), ("Lightning?", "Supported."), ("IE 11 remains for Salesforce?", "No. The exception is Oracle Service Cloud.")],
    ("Date the number", "Write the package version with the phrase 'as of'.", ["Open the current PDF", "Write the number and the date", "Compare to the org"], "The sentence includes a date."),
    ("A standard says IE for Salesforce", "The PDF ended IE except for Oracle Service Cloud.", "STD browser=IE CRM=Salesforce", ["Change the standard to a supported browser", "Keep IE", "Disable WSS", "Use analog headsets"], 0, "The standard contradicts the PDF.", "Pick a supported browser."),
    ["Date every Salesforce version you copy", "Do not keep IE for Salesforce"], uncertain=["Managed package 2.46 and the edition list came from the technical requirements read in October 2026. They will move."]))
    R.append(L("l03", "ServiceNow releases are named", "practice", [
        "The same PDF says the ServiceNow Plus adapter supports the Service Operations and Configurable workspaces, and names the Australia, Zurich, and Yokohama releases. Those names are a support list with a date on it, like the Salesforce package.",
        "There is a portal chapter for configuring the Plus adapter for ServiceNow. Use it for the steps. Use the PDF for which release you are allowed to be on, and re-read both.",
    ], [TECH, SNOW], stack("ServiceNow lines from the PDF", "Re-read before an upgrade.", ["Service Operations workspace", "Configurable workspace", "Australia", "Zurich", "Yokohama"]),
    "An upgrade is proposed", ["Now", "Five9", "Change"], [
        ("Now", "Release", "The instance is on a named release.", "rel"),
        ("Five9", "List", "The PDF list is checked.", "list"),
        ("Change", "Match", "The target is on the list, or the upgrade waits.", "match"),
        ("Change", "Workspace", "The workspace is one of the two named.", "ws"),
        ("Admin", "Guide", "The portal chapter is the click path.", "guide"),
        ("Admin", "Date", "The decision records the PDF date.", "date"),
    ], [
        ("Workspaces named in the PDF are", ["Any", "Service Operations and Configurable", "Classic only", "None"], 1, "Those two."),
        ("Australia, Zurich, and Yokohama are", ["Cities you must dial", "Release names in that PDF", "Skill groups", "Codecs"], 1, "They are ServiceNow release names in the support list."),
        ("A release that is not on the current PDF is", ["Automatically supported", "Not something this lab will call supported", "Required", "A list mode"], 1, "The list is the boundary."),
        ("The click path lives", ["Only in this lesson", "In the ServiceNow adapter chapter", "In the dialer", "In MyE911"], 1, "Use the portal chapter."),
        ("You should freeze Yokohama as forever. True or false?", ["True", "False. The next PDF can change the list", "True for US domains", "True for TCPA"], 1, "Date the list."),
    ], [("Workspaces?", "Service Operations and Configurable."), ("Those three names?", "Releases in the PDF."), ("Off-list release?", "Do not call it supported."), ("Forever?", "No.")],
    ("Gate an upgrade", "Write pass or wait for a fictional upgrade to a release not on the list.", ["Find the name", "Compare", "Wait if it is absent"], "You waited."),
    ("The instance moved to a brand-new release overnight", "The PDF on the desk does not list it. Pops fail.", "RELEASE unlisted POP fail", ["Open the current PDF before you debug the skill", "Add predictive lines", "Reset lists", "Change ANI"], 0, "Supportability is the first question.", "Confirm the release, then the adapter."),
    ["Check the ServiceNow release list", "Date it"], uncertain=["Australia, Zurich, and Yokohama were the names in the PDF read for this lab. Confirm the current list before an upgrade."]))
    R.append(L("l04", "The rest of the named CRMs", "practice", [
        "Dynamics 365, Zendesk, Oracle, NetSuite, and Epic are in the same Plus adapter list as Salesforce and ServiceNow. The PDF does not give this lab a package number for each of them. Absence of a number here is not absence of an adapter.",
        "Treat each one as its own guide chapter. A Zendesk pop that fails is not fixed by a Salesforce package upgrade.",
    ], [TECH, ADAPTERS], path("One chapter each", "Do not share a package number across CRMs.", ["Dynamics 365", "Zendesk", "Oracle", "NetSuite", "Epic"]),
    "A Zendesk ticket", ["Agent", "Adapter", "Guide"], [
        ("Agent", "Pop", "The ticket should appear.", "pop"),
        ("Adapter", "Zendesk", "The Zendesk adapter is the one installed.", "ad"),
        ("Guide", "Chapter", "The Zendesk chapter is the one opened.", "ch"),
        ("Admin", "Avoid", "The Salesforce package number is irrelevant.", "no"),
        ("Proxy", "WSS", "The socket still has to pass.", "wss"),
        ("Agent", "Voice", "Voice can work while the ticket does not.", "voice"),
    ], [
        ("Epic is listed as a Plus adapter. True or false?", ["False", "True", "Only in WEM", "Only as a codec"], 1, "The PDF includes Epic."),
        ("A Salesforce package number fixes Zendesk. True or false?", ["True", "False", "True if SAML matches", "True on ARM Macs"], 1, "Different adapters."),
        ("This lab's package number for NetSuite is", ["2.46", "Not stated. 2.46 was the Salesforce line", "1.0", "10"], 1, "Do not reuse the Salesforce number."),
        ("Oracle Service Cloud's IE exception applies to Zendesk. True or false?", ["True", "False. The PDF limits that exception to Oracle Service Cloud", "True for all Plus adapters", "True for Studio"], 1, "Keep the exception narrow."),
        ("Voice up, ticket down, still starts with", ["The skill greeting", "Whether the adapter channel is up", "List penetration", "The abandon window"], 1, "Same split as any pop."),
    ], [("Epic listed?", "Yes."), ("Salesforce package fixes Zendesk?", "No."), ("NetSuite package in this lab?", "Not stated."), ("IE exception scope?", "Oracle Service Cloud only.")],
    ("Separate the chapters", "Write the guide you would open for Epic and for Zendesk.", ["Epic chapter", "Zendesk chapter", "Not the Salesforce package"], "Two chapters."),
    ("NetSuite was upgraded using the Salesforce notes", "The pop broke and the notes never mentioned NetSuite.", "NOTES salesforce CRM netsuite", ["Open the NetSuite adapter chapter", "Reinstall Salesforce", "Change the dialer", "Delete skills"], 0, "Wrong chapter.", "Use the NetSuite guide."),
    ["Give each CRM its own chapter", "Do not reuse another product's version"]))
    R.append(L("l05", "SDK and connectors when there is no adapter", "advanced", [
        "The API product page lists a CRM SDK and web connectors beside the CTI, configuration, reporting, and statistics web services, plus Web2Campaign. The desktop page says bring your own CRM with the SDK.",
        "A connector is a lighter pop. An SDK integration is code. Neither is maintained as a managed package by the Salesforce story. You own the tests when Five9 or the CRM moves.",
    ], [APIS, ADP], compare("Build versus buy", "Say who patches it.", "Plus adapter", ["Named CRM", "Vendor guide"], "SDK or connector", ["Your code or your URL", "You retest on change"]),
    "A homegrown pop", ["App", "Five9", "Test"], [
        ("App", "Need", "The CRM is not in the adapter list.", "need"),
        ("Five9", "SDK", "The SDK is the documented extension point.", "sdk"),
        ("Five9", "URL", "Or a connector opens a URL with call data.", "url"),
        ("Test", "Call", "A test call pops the right record.", "test"),
        ("Test", "Fail", "Voice still works. The pop is yours to fix.", "fail"),
        ("Change", "Retest", "A platform upgrade reruns the test.", "re"),
    ], [
        ("The CRM SDK is named on", ["The API product page and the desktop page", "The headset page only", "RFC 4733 only", "The retention page only"], 1, "Both pages mention it."),
        ("Web connectors are", ["Absent", "Named on the API page", "A dialer mode", "A skill tab"], 1, "The API page lists them."),
        ("You own retesting a homegrown pop. True or false?", ["False", "True", "Only if ANI is local", "Only in UK domains"], 1, "There is no managed package for it."),
        ("Web2Campaign is", ["A headset", "One of the named APIs on that page", "A skill", "A theme"], 1, "The API page lists it."),
        ("A connector that only opens a URL", ["Is a full adapter", "Does less than a full adapter. Say so", "Sets DNC", "Schedules WEM"], 1, "Scope the claim."),
    ], [("SDK named?", "Yes."), ("Connectors named?", "Yes."), ("Who retests custom code?", "You."), ("URL pop scope?", "Smaller than a full adapter.")],
    ("Scope the pop", "Write what the connector will and will not do.", ["Open the record", "Not replicate every adapter button", "Name the retest"], "The scope is short."),
    ("The custom pop broke after a Five9 change", "Nobody owned a retest.", "SDK last-test=never", ["Add a retest to the change process", "Blame the skill", "Switch to analog", "Disable TLS"], 0, "Custom code has an owner.", "Retest and fix the SDK pop."),
    ["Use the SDK or a connector on purpose", "Own the retest"]))
    R.append(L("l06", "Screen pop down, voice up", "practice", [
        "This is the signature adapter incident. The caller is heard. The record is not on screen. Causes you can cite: WSS blocked, TLS 1.1, the wrong CRM chapter, an unassigned campaign profile that was supposed to control pop-up behavior, or a connector pointed at a dead URL.",
        "Campaign profiles can control pop-up windows. That is a second place, besides the adapter, where a pop is configured. Check both.",
    ], [TECH, cite_prof(), ADAPTERS], path("Voice up, screen down", "Split the paths.", ["Audio works", "WSS or URL fails", "Profile pop-up setting", "Right adapter chapter"]),
    "Isolate", ["Voice", "Pop", "Fix"], [
        ("Voice", "Ok", "The agent hears the caller.", "ok"),
        ("Pop", "Blank", "No record.", "blank"),
        ("Net", "WSS", "The socket is tested.", "wss"),
        ("CRM", "Chapter", "The right guide is open.", "ch"),
        ("Profile", "Popup", "The profile's pop-up control is checked.", "prof"),
        ("Fix", "One", "One change, then a test call.", "one"),
    ], [
        ("Voice working proves the pop path. True or false?", ["True", "False", "True for Salesforce only", "True if G.711"], 1, "They are different channels."),
        ("Profiles can control", ["Only ANI", "Pop-up windows too", "Only skills", "Only JRE"], 1, "The profile topic includes pop-ups."),
        ("TLS 1.1", ["Fixes pops", "Is unsupported", "Is required", "Is a skill"], 1, "The PDF rejects it."),
        ("One change at a time matters because", ["It is slower and therefore better evidence", "It is a codec", "It sets DNC", "It is a list mode"], 0, "You need to know what fixed it."),
        ("A dead connector URL", ["Still pops", "Blanks the screen", "Dials predictive", "Changes region"], 1, "The URL has to resolve."),
    ], [("Voice proves the pop?", "No."), ("Profiles and pop-ups?", "Yes, they can control them."), ("TLS 1.1?", "Unsupported."), ("Dead URL?", "Blank screen.")],
    ("Order the checks", "Write WSS, TLS, chapter, profile, URL in the order you would test.", ["WSS", "Right chapter", "Profile pop-up", "URL"], "Voice is not in the fix list."),
    ("Three changes were made at once", "The pop returned and nobody knows why.", "CHANGED proxy, profile, url", ["Back out to one change and retest", "Celebrate", "Delete recordings", "Add lines"], 0, "The evidence was destroyed.", "Retest one change at a time in a lab domain."),
    ["Split voice from the pop", "Check the profile's pop-up control"]))
    R.append(L("l07", "Salesforce modules inside the IVR", "advanced", [
        "The IVR modules chapter includes a Salesforce module and an SFDC Einstein module, plus Contact Update and Lookup Contact Record. Those run in the script, before an agent exists. They are not the Plus adapter the agent uses after connect.",
        "A design that 'integrates Salesforce' must say which of those it means. The ZIP example used a generic Query, not the Salesforce module. Use the Salesforce module when the target is Salesforce. Use Query when the target is some other service.",
    ], [MODULES, cite_query(), ADP], compare("Script versus desktop", "Both can say Salesforce.", "IVR Salesforce or Einstein module", ["During the script", "Before an agent"], "Plus adapter", ["On the agent screen", "After connect"]),
    "Look up a balance before the agent", ["Caller", "IVR", "Agent"], [
        ("Caller", "ID", "Digits identify the account.", "id"),
        ("IVR", "SF", "The Salesforce module queries.", "sf"),
        ("IVR", "Var", "A variable holds the result.", "var"),
        ("IVR", "Skill", "Then the agent is offered.", "skill"),
        ("Agent", "Adapter", "The Plus adapter shows the record again, live.", "ad"),
        ("Admin", "Two", "Both were tested. They are not one config.", "two"),
    ], [
        ("The Salesforce IVR module is", ["The Plus adapter", "A script module", "A dialer mode", "A codec"], 1, "It is in the modules chapter."),
        ("Einstein in the IVR is", ["A rumor", "SFDC Einstein, a named module", "A trunk", "A theme"], 1, "The chapter lists it."),
        ("The ZIP web-service example uses", ["The Salesforce module", "Query", "Set DNC", "Conference"], 1, "It is a generic XML web service."),
        ("After connect, the agent's screen is", ["Still the IVR module", "The adapter or SDK", "A WAV file", "A list"], 1, "The script has completed on Skill Transfer."),
        ("One sentence that says 'we integrate Salesforce' is", ["Enough", "Not enough. Say script module or adapter", "A service level", "A roster"], 1, "They are different projects."),
    ], [("IVR Salesforce module?", "A script block."), ("Einstein module?", "Named in the chapter."), ("ZIP example?", "Query, not the Salesforce module."), ("After connect?", "The adapter.")],
    ("Two projects", "Label a before-agent lookup and an after-connect screen.", ["Salesforce module", "Plus adapter", "A variable that connects the story"], "You used both names."),
    ("The IVR lookup works and the agent sees a blank screen", "Only the script module was built.", "IVR sf=yes ADAPTER=no", ["Build the adapter too", "Add another IVR module and call it done", "Change list mode", "Disable recording"], 0, "The script already ended.", "Deploy the adapter for the agent."),
    ["Say whether you mean the IVR module or the adapter", "Test both"], href="#/ivr"))
    return track("t12", "CRM integrations", "CRM", "Plus adapters, version lists that age, the SDK, and Salesforce inside the IVR.", "Systems", "Practice", "Name the adapter. Date the version. A blank screen with live voice is a different channel.", R)

def cite_prof():
    from curriculum_lib import PROFILES
    return PROFILES

def cite_query():
    from curriculum_lib import QUERY
    return QUERY
