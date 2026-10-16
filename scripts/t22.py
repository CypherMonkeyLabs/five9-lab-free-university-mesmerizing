from curriculum_lib import APIS, DESK, WEM, WFM, lesson, compare, path, stack, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "CTI is a named API, not a vibe", "foundation", [
        "The APIs and SDKs page lists a Computer Telephony Integration (CTI) Web Services API next to Configuration, Reporting, Statistics, Web2Campaign, the CRM SDK, and Web Connectors. CTI, on that page, is one of those names.",
        "Wikipedia's ACD article says an advanced distributor may use computer telephony integration as an input to the route. That is the general word. Five9's page is the product name. A screen pop, a click-to-dial button, and a package version were not on the pages this chapter read.",
    ], [APIS], compare("Two uses of the letters", "Do not mix them.", "Wikipedia", ["CTI as an input an advanced ACD may use"], "Five9 API page", ["A web services API named CTI"]),
    "Point at the name", ["Page", "Design"], [
        ("Page", "List", "CTI Web Services API is on the list.", "list"),
        ("Page", "Neighbors", "Configuration, Reporting, and Statistics are different names.", "near"),
        ("Design", "Ask", "Which API the integration actually calls.", "ask"),
        ("Design", "Refuse", "No screen-pop field is invented.", "refuse"),
        ("Reader", "Wiki", "The general word stays on Wikipedia.", "wiki"),
        ("Reader", "Cite", "The note names the API page.", "cite"),
    ], [
        ("The Five9 page names CTI as", ["A dialing mode", "A web services API", "A skill group", "A badge"], 1, "It is on the API list."),
        ("Reporting Web Services and CTI Web Services are", ["The same name", "Both on the list, as different names", "Both codecs", "Both prompts"], 1, "The list prints both."),
        ("Web2Campaign is", ["Absent", "On the same list", "A campaign type", "A disposition"], 1, "The list includes it."),
        ("A screen-pop field in this lesson is", ["Fully specified", "Not specified. Those admin pages did not return a body", "Always ANI", "Always the case id"], 1, "Do not invent the pop."),
        ("The Wikipedia sentence about CTI is", ["A Five9 dialog", "A general definition", "A package version", "A port"], 1, "Keep it on that article."),
    ], [("Five9's CTI name?", "CTI Web Services API."), ("Same as Reporting?", "No."), ("Web2Campaign?", "On the list."), ("Screen pop specified?", "No.")],
    ("Name three APIs", "Pick three from the list and do not describe their payloads.", ["CTI", "One neighbor", "No invented field"], "The names match the page."),
    ("A diagram shows the CTI API pushing a Salesforce field list", "The API page names the API. It does not print that field list.", "FIELDS guessed", ["Stop at the API name", "Publish the fields", "Add lines", "Change ANI"], 0, "A name is not a schema.", "Delete the fields."),
    ["Use the API name the page printed", "Leave screen pop unspecified"], uncertain=["Salesforce screen pop, click-to-dial, and package versions were not on the pages this chapter could read."]))
    R.append(L("l02", "The prebuilt CRM names are a list", "foundation", [
        "The APIs page says it has pre-built integrations with Salesforce, ServiceNow, Microsoft Dynamics 365, Oracle Service Cloud, Oracle NetSuite, and Zendesk. A later line says robust pre-built integrations with Salesforce, ServiceNow, Microsoft, Oracle, and Zendesk.",
        "The desktop page's out-of-the-box line is Salesforce, ServiceNow, Microsoft, Oracle, and Zendesk, and it adds bring-your-own with the CRM SDK. Microsoft on that line is not spelled Dynamics. Dynamics 365 is spelled on the API list. Quote the line you mean.",
    ], [APIS, DESK], stack("Names on the API list", "Copy the spelling.", ["Salesforce", "ServiceNow", "Microsoft Dynamics 365", "Oracle Service Cloud", "Oracle NetSuite", "Zendesk"]),
    "Spell the CRM", ["API list", "Desktop line"], [
        ("API", "Read", "Dynamics 365 is spelled out.", "dyn"),
        ("Desktop", "Read", "The shorter line says Microsoft.", "ms"),
        ("Reader", "Keep", "Both lines are real.", "keep"),
        ("Reader", "SDK", "Anything off the list starts at the CRM SDK.", "sdk"),
        ("Reader", "Stop", "No package number is added.", "stop"),
        ("Reader", "Cite", "The note says which line.", "cite"),
    ], [
        ("Dynamics 365 is spelled on", ["The short desktop line", "The API pre-built list", "The skill tab", "The badge"], 1, "The API list uses that name."),
        ("Zendesk is", ["Absent", "On both the API list and the desktop line", "A dialer mode", "A codec"], 1, "Both pages name it."),
        ("Oracle NetSuite and Oracle Service Cloud are", ["One product name", "Two names on the API list", "SIP trunks", "Prompts"], 1, "The list prints both."),
        ("A CRM that is not on the list uses", ["A fictional adapter", "The CRM SDK, per the desktop page", "Only FTP", "Only a skill group"], 1, "Bring your own CRM is the SDK line."),
        ("A package version in this lesson is", ["2.46, restated", "Not stated. That PDF was not the page read for this chapter", "Always 1.0", "Always current"], 1, "Do not copy a number from a file this chapter did not quote."),
    ], [("Dynamics spelling?", "On the API list."), ("Zendesk?", "Named."), ("Two Oracle names?", "Service Cloud and NetSuite."), ("Unlisted CRM?", "CRM SDK.")],
    ("Sort three systems", "Adapter list, or SDK.", ["Salesforce", "An internal CRM", "Zendesk"], "The internal CRM is the SDK case."),
    ("The design says Microsoft and Dynamics are different products because the lines differ", "They might be the same family. The pages use different words.", "NAMES microsoft dynamics", ["Quote each line as printed", "Declare them unrelated", "Delete Salesforce", "Change ANI"], 0, "Different words are not proof of two products.", "Cite the line."),
    ["Spell the name the page spelled", "Send unlisted CRMs to the SDK"], uncertain=["This chapter does not restate Salesforce package numbers. The technical-requirements PDF was not the page quoted here."]))
    R.append(L("l03", "Plus and a prebuilt adapter share a technology story", "practice", [
        "The desktop page says that whether you deploy Agent Desktop Plus or a pre-built CRM integration, you get the same underlying technology. It also describes the Agent Desktop Toolkit as REST APIs, reference UIs, and other tools to embed agent functionality in a custom CRM or another CRM.",
        "Same technology is not the same screen. Plus is the Five9 screen. A prebuilt integration is the CRM screen. The toolkit is how you embed. Say which of the three you are looking at.",
    ], [DESK], compare("Three ways the desktop page talks", "Pick one.", "Plus", ["The Five9 screen"], "Prebuilt or toolkit", ["The CRM screen", "REST APIs and reference UIs to embed"]),
    "Name the surface", ["Agent", "Builder"], [
        ("Agent", "Plus", "One Five9 screen.", "plus"),
        ("Agent", "CRM", "Or the CRM's own screen.", "crm"),
        ("Builder", "Toolkit", "REST APIs and reference UIs.", "kit"),
        ("Reader", "Same", "The page says the underlying technology matches.", "same"),
        ("Reader", "Split", "The screens are still different objects.", "split"),
        ("Reader", "Say", "The design names which one.", "say"),
    ], [
        ("Plus and a prebuilt integration, per the desktop page,", ["Use unrelated technology", "Share the same underlying technology", "Are both dialer modes", "Are both codecs"], 1, "That is the page's sentence."),
        ("The toolkit includes", ["Only a wallpaper", "REST APIs and reference UIs", "Only SIP", "Only a badge"], 1, "The page says so."),
        ("Embedding into a custom CRM is", ["Named", "Forbidden", "A list mode", "A prompt"], 1, "The toolkit sentence includes custom or other CRM systems."),
        ("Same technology means the screens are identical. True or false?", ["True", "False. The page says the technology. The screens are still different products", "True if ANI matches", "True for Zendesk only"], 1, "Do not collapse the screens."),
        ("A URL bookmark is", ["Automatically the toolkit", "Not what the toolkit sentence describes", "A skill", "A forecast"], 1, "Name the object you actually deployed."),
    ], [("Same technology?", "Yes, per the page."), ("Toolkit contents?", "REST APIs and reference UIs."), ("Custom CRM?", "Named."), ("Screens identical?", "Not claimed.")],
    ("Label the desk", "Write Plus, prebuilt, or toolkit under the picture.", ["One label", "No bookmark called an adapter"], "The label matches the page's three stories."),
    ("Leadership calls a bookmark the Salesforce adapter", "Agents are clicking a saved URL.", "ADAPTER absent BOOKMARK yes", ["Say bookmark until an adapter is installed", "Rename the bookmark", "Add lines", "Delete the IVR"], 0, "The object in production is not the slide.", "Use the true name."),
    ["Name Plus, the prebuilt integration, or the toolkit", "Do not call a bookmark an adapter"]))
    R.append(L("l04", "Workforce tools can show up inside the CRM", "practice", [
        "The desktop page says WFO connectors reach schedules, adherence, time-off requests, shift bidding, and evaluation review from inside the CRM. The WFM page says you can embed WFM in the CRM and extend it to CRM digital channels, and its pre-built CRM card names Oracle and ServiceNow.",
        "The WEM quality list names Salesforce, Zendesk, Oracle, and ServiceNow for that quality integration. Three lists, three pages. A floor can have the voice adapter and not the WFO connector. Ask which list you implemented.",
    ], [DESK, WFM, WEM], stack("Three lists", "Do not merge them.", ["Desktop WFO connector actions", "WFM card: Oracle and ServiceNow", "Quality list: Salesforce, Zendesk, Oracle, ServiceNow"]),
    "Ask which connector", ["Voice", "WFO"], [
        ("Voice", "Adapter", "The CRM adapter is one purchase.", "voice"),
        ("WFO", "Connector", "Schedules and evaluations are another line.", "wfo"),
        ("WFM", "Card", "Oracle and ServiceNow on that card.", "card"),
        ("QM", "List", "Four names on the quality list.", "qm"),
        ("Reader", "Ask", "Which of these is in the contract.", "ask"),
        ("Reader", "Stop", "Do not assume all three.", "stop"),
    ], [
        ("Shift bidding inside the CRM is named on", ["The skill tab", "The desktop WFO connector line", "The codec page", "The badge"], 1, "The desktop page includes it."),
        ("The WFM pre-built card read for this lesson names", ["Oracle and ServiceNow", "Every CRM", "Only Zoom", "Only a bookmark"], 1, "Those two items were on the card."),
        ("The quality CRM list adds", ["No names", "Salesforce and Zendesk beside Oracle and ServiceNow", "Only Epic", "Only a gateway"], 1, "That is the quality list."),
        ("Voice adapter present means the WFO connector is present. True or false?", ["True", "False. They are different lines", "True if the agent is Ready", "True for one edition"], 1, "Ask."),
        ("Embedding WFM in the CRM is", ["Named on the WFM page", "Denied", "A dialer mode", "A prompt"], 1, "The page says embed WFM in the CRM interface."),
    ], [("WFO actions?", "Schedules, adherence, time off, bidding, evaluations."), ("WFM card?", "Oracle and ServiceNow."), ("Quality list?", "Salesforce, Zendesk, Oracle, ServiceNow."), ("One purchase covers all?", "Not claimed.")],
    ("Tick the lists", "Mark voice, WFO, and the WFM card as bought or unknown.", ["Unknown is allowed"], "Nothing was assumed."),
    ("Agents have the voice adapter and no schedule inside the CRM", "Someone assumed the WFO connector came with it.", "VOICE yes WFO no", ["Treat the schedule path as not installed", "Tell them to look harder in the CRM", "Delete the adapter", "Change ANI"], 0, "Different lines.", "Document the missing connector or install it."),
    ["Ask which connector was bought", "Keep the three lists apart"]))
    R.append(L("l05", "Zoom Phone and Teams are on the same API page", "advanced", [
        "The APIs page also lists pre-built integrations with Zoom Phone and Microsoft Teams. It says those connections are so agents can reach someone to resolve a question or consult an expert. That is a UC story, not a CRM adapter.",
        "The same page says the partner app marketplace has over 55 partner solutions. Over 55 is the page's count. This lab did not open the marketplace and did not recount it. REST, on the same page, is how it describes access for agents, administrators, supervisors, and reporting users.",
    ], [APIS], compare("CRM list versus UC list", "Both are prebuilt. They are not the same job.", "CRM names", ["Salesforce through Zendesk"], "UC names", ["Zoom Phone", "Microsoft Teams"]),
    "Classify the icon", ["Page", "Design"], [
        ("Page", "CRM", "A CRM name stays on the CRM list.", "crm"),
        ("Page", "UC", "Zoom Phone or Teams stays on the UC list.", "uc"),
        ("Page", "Count", "Over 55 is quoted as their count.", "count"),
        ("Reader", "Recount", "This lab did not recount the marketplace.", "recount"),
        ("Page", "REST", "REST is the access sentence.", "rest"),
        ("Design", "Say", "The design says CRM or UC.", "say"),
    ], [
        ("Zoom Phone is listed as", ["A CRM adapter", "A pre-built integration on the API page", "A skill group", "A forecast"], 1, "The page puts it with Teams."),
        ("Microsoft Teams on that page is", ["A CRM", "A pre-built integration for consult and resolve", "A dialer mode", "A codec"], 1, "The page describes that use."),
        ("Over 55 partner solutions is", ["A count this lab audited", "The API page's own sentence", "A port", "An exam score"], 1, "Quote it as their sentence."),
        ("REST on that page is described for", ["Nobody", "Agents, administrators, supervisors, and reporting users", "Only trunks", "Only the IVR"], 1, "That is the sentence."),
        ("A Teams integration replaces a Salesforce adapter. True or false?", ["True", "False. The page lists them for different jobs", "True if WFM is native", "True in one region"], 1, "Do not swap the lists."),
    ], [("Zoom Phone?", "A prebuilt UC integration."), ("Teams?", "Same kind of line."), ("Over 55?", "Their count, not a recount."), ("REST users?", "Agents, administrators, supervisors, reporting users.")],
    ("Sort four icons", "CRM or UC.", ["Salesforce", "Zoom Phone", "Teams", "Zendesk"], "The UC pair is Zoom Phone and Teams."),
    ("The design replaces Salesforce with Teams", "The page did not say they do the same job.", "SWAP teams salesforce", ["Put each name back on its list", "Ship the swap", "Delete IVR", "Change ANI"], 0, "Different jobs.", "Undo the swap."),
    ["Keep UC names off the CRM list", "Quote over 55 as their count"], uncertain=["This lab did not open the partner marketplace, so over 55 is the API page's sentence and not a fresh count."]))
    R.append(L("l06", "Salesforce and ServiceNow are names until the admin page opens", "advanced", [
        "Salesforce and ServiceNow are on the API list, the desktop line, and the quality list. ServiceNow is also on the WFM CRM card with Oracle. That is what this chapter can say about them.",
        "The ServiceNow admin guide, the Salesforce install guide, and the community feature article did not return a feature body in this check. Workspace names, Lightning CTI editions, screen pop, click-to-dial, and campaign sync are confirm. Describe them only after you read the page.",
    ], [APIS, DESK, WFM], path("How far the name goes", "Then stop.", ["The name is on a list", "The list is cited", "The admin body did not return", "Features of that body stay blank"]),
    "Stop at the name", ["List", "Guide"], [
        ("List", "See", "ServiceNow is on the API list.", "see"),
        ("List", "See2", "Salesforce is on the API list.", "sf"),
        ("Guide", "Closed", "The admin body did not return.", "closed"),
        ("Reader", "Blank", "No workspace name is copied.", "blank"),
        ("Reader", "Blank2", "No screen-pop rule is copied.", "pop"),
        ("Reader", "Mark", "The gap is confirm.", "mark"),
    ], [
        ("This chapter can say ServiceNow is", ["Configured in a named workspace", "On the public lists that opened", "A codec", "A skill"], 1, "The lists opened. The admin body did not."),
        ("Lightning CTI editions in this chapter are", ["Quoted", "Not quoted", "Professional only", "Unlimited only"], 1, "That page was not the source read here."),
        ("Click-to-dial is", ["Specified step by step", "Confirm. The feature article body did not return", "A forecast", "A disposition"], 1, "Do not invent the button."),
        ("Campaign sync from the CRM is", ["Described", "Confirm, for the same reason", "A list mode", "A prompt"], 1, "The body did not return."),
        ("Repeating a feature from memory is", ["Helpful", "How this chapter gets a fact wrong", "Required", "A codec choice"], 1, "Memory is not the page."),
    ], [("ServiceNow on a list?", "Yes."), ("Admin body read?", "No."), ("Screen pop?", "Confirm."), ("Click-to-dial?", "Confirm.")],
    ("Write the Salesforce sentence you are allowed", "It is a named pre-built integration. Stop.", ["No edition", "No package number", "No pop rule"], "The sentence matches the list."),
    ("A worksheet lists ServiceNow Zurich as the supported release", "This chapter did not read that release table.", "RELEASE zurich SOURCE unread", ["Remove the release name", "Publish it", "Add a skill", "Reset lists"], 0, "An unread table is not a source.", "Delete the name."),
    ["Stop at the published name", "Mark unread admin pages confirm"], uncertain=["ServiceNow workspace names, Salesforce Lightning editions, screen pop, and click-to-dial did not return a body in this check."]))
    R.append(L("l07", "A CRM note you can defend", "advanced", [
        "A defendable note names the surface, the list, and the gap. Surface: Plus, prebuilt, toolkit, or bookmark. List: the API CRM names, the UC names, or the WFO actions. Gap: anything from an admin guide that did not open, marked confirm, with no URL and no guessed field.",
        "The API page says integrations can often be done with minimal coding. Often and minimal are the page's words. They are not a project estimate. The desktop page's single screen is the agent experience it describes, not a count of browser tabs this lab measured.",
    ], [APIS, DESK], path("The note", "Three lines.", ["Surface", "List you copied", "Confirm, with the feature left blank"]),
    "Sign it", ["Note", "Gap"], [
        ("Note", "Surface", "Plus, prebuilt, toolkit, or bookmark.", "surface"),
        ("Note", "List", "Names copied from one page.", "list"),
        ("Note", "Often", "Minimal coding stays in their words.", "often"),
        ("Gap", "Pop", "Screen pop is blank.", "pop"),
        ("Gap", "Release", "Release names are blank.", "rel"),
        ("Note", "Sign", "A stranger can see what was not read.", "sign"),
    ], [
        ("A defendable note includes", ["A guessed screen-pop field", "The surface, the copied list, and the blank gap", "A package version", "An exam code"], 1, "That is the review."),
        ("Minimal coding is", ["This lab's estimate", "The API page's wording", "A port", "A skill level"], 1, "Do not turn it into a schedule."),
        ("A bookmark labeled as an adapter fails the note because", ["Bookmarks are illegal", "The surface name is wrong", "Zendesk is absent", "Teams is a CRM"], 1, "Say what is actually installed."),
        ("Leaving screen pop blank is", ["Incomplete in a bad way", "The honest end of this chapter", "A codec choice", "A forecast"], 1, "The body did not return."),
        ("Mixing the WFM CRM card into the API list without saying so is", ["Fine", "How a reader loses the source", "Required", "A prompt"], 1, "Name the page."),
    ], [("Three parts of the note?", "Surface, list, gap."), ("Minimal coding?", "Their words."), ("Wrong surface name?", "Fails the note."), ("Blank screen pop?", "Honest.")],
    ("Write the note", "One CRM, one surface, one confirm.", ["No guessed field"], "The gap has no URL and no invented feature."),
    ("The note says minimal coding so the project is two days", "The page did not say two days.", "ESTIMATE 2d SOURCE often", ["Delete the estimate", "Keep two days", "Add agents", "Change ANI"], 0, "Often is not a schedule.", "Remove the date."),
    ["Name the surface and the list", "Leave unread features blank"], uncertain=["Project size is not on the API page. Minimal coding is their phrase, not an estimate."]))
    return track(
        "t22",
        "CRM and CTI integrations",
        "CRM and CTI",
        "Named adapters, the CTI API, and the Salesforce and ServiceNow details this check would not guess.",
        "Integrations",
        "Practice",
        "Public pages name the CRMs and the CTI API. Admin feature lists that did not open stay blank.",
        R,
    )
