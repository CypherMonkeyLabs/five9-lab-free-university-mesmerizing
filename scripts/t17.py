from curriculum_lib import WEM, WEMDS, ADP, ENGAGE, GENAI, APIS, E911, STIR, TECH, REPORTS, cite, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "The domain has neighbors", "foundation", [
        "A Five9 domain does not live alone. Voice arrives on a SIP story. Agents sit in a desktop. WEM or a partner workforce suite watches the roster. A CRM pops. GenAI Studio may draft a summary. E911 carries a location. Reports leave through a role and an API.",
        "The ecosystem page in this lab is a map of those neighbors with the same citations as the lessons. If a box has no link, it does not belong on the map.",
    ], [ADP, WEM, APIS, E911], stack("Neighbors you should be able to name", "Each one fails differently.", ["SIP path", "IVR and skills", "Agent desktop", "WEM", "CRM", "GenAI Studio", "E911", "Reports and APIs"]),
    "A call crosses the map", ["Edge", "Domain", "After"], [
        ("Edge", "SIP", "The trunk story is named.", "sip"),
        ("Domain", "IVR", "A script runs, or the campaign is direct to a skill.", "ivr"),
        ("Domain", "Skill", "A skill has people.", "skill"),
        ("After", "Desk", "The desktop shows the contact.", "desk"),
        ("After", "CRM", "The adapter or connector is named.", "crm"),
        ("After", "Record", "A report and a recording follow their own clocks.", "rec"),
    ], [
        ("WEM is inside the dialer algorithm. True or false?", ["True", "False. It is a neighbor that should feed who is supposed to be ready", "True for predictive", "True for TLS"], 1, "Scheduling and dialing are different products."),
        ("E911 sits", ["In the campaign profile as ANI", "Beside the domain, with its own location data", "In the matrix layout", "In a partition"], 1, "Location is its own service."),
        ("A CRM pop is", ["Proof the SIP trunk is up", "A separate neighbor", "A codec", "A retention clock"], 1, "Voice can work while the pop does not."),
        ("GenAI Studio, on its product page, is", ["The dialer", "The place prompts and knowledge are managed", "A headset", "An Equinix edge"], 1, "It is its own product."),
        ("The map in this lab is allowed to include an uncited box. True or false?", ["True", "False", "True if it looks official", "True for Cisco"], 1, "No link, no box."),
    ], [("WEM equals the dialer?", "No."), ("E911?", "Its own location service."), ("Pop equals trunk?", "No."), ("Uncited boxes?", "Leave them off.")],
    ("Draw eight boxes", "Name the neighbor and one failure that does not indict the others.", ["SIP", "Desktop", "E911"], "You gave each a separate failure."),
    ("The bridge is blamed for a blank CRM card", "Voice is up. The adapter is down.", "SIP ok CRM timeout", ["Open the adapter path", "Add SIP trunks", "Change list penetration", "Rewrite Kari's Law"], 0, "The neighbor that failed is the CRM.", "Debug the adapter."),
    ["Name the neighbors", "Give each one its own failure"], href="#/ecosystem"))
    R.append(L("l02", "Workforce, quality, and the recording shelf", "practice", [
        "The WEM product page describes workforce management, quality, analytics, surveys, and recording, and it also describes a Verint partnership. Five9 says it manages install and upgrades for the solution it delivers. The data sheet is the short version of that claim.",
        "Native WEM and a Verint deployment are not interchangeable words. Ask which one is in the contract. Quality scores do not change a skill assignment unless a process says they do.",
    ], [WEM, WEMDS], compare("Say which WEM", "The page describes both a native suite and a partnership.", "Ask", ["Native or Verint?", "Who upgrades it?", "Does a score move a skill?"], "Do not assume", ["Scores reroute calls", "Surveys are the IVR", "Recording retention is 120 days"]),
    "A low score", ["Who", "Where", "Effect"], [
        ("Who", "Product", "Native or Verint is named.", "who"),
        ("Where", "Eval", "The evaluation lives in WEM.", "eval"),
        ("Effect", "Coach", "Coaching is the default effect.", "coach"),
        ("Effect", "Skill", "A skill change is a separate admin act.", "skill"),
        ("Shelf", "Audio", "Recording retention is the retention page, not the WEM slogan.", "audio"),
        ("Admin", "Upgrade", "Five9's upgrade claim is limited to the solution they deliver.", "up"),
    ], [
        ("The WEM page mentions", ["Only a dialer", "WFM, quality, analytics, surveys, recording, and Verint", "Only E911", "Only SOAP"], 1, "That is the product scope."),
        ("A quality score automatically removes a skill. True or false?", ["True", "False. Not unless your process does it in admin", "True at night", "True for TCPA"], 1, "The products are neighbors."),
        ("Install and upgrades for the delivered solution are", ["Always the customer's Java admin", "Described as managed by Five9", "A Cisco gateway task", "Optional and undocumented"], 1, "The product page says Five9 manages them."),
        ("Recording shelf life is decided by", ["The WEM marketing sentence alone", "The retention terms", "The theme", "RFC 3261"], 1, "Use the retention page."),
        ("You should say Verint when the contract is native WEM. True or false?", ["True", "False", "True in the UK", "True for surveys"], 1, "Name the one you bought."),
    ], [("What does the page include?", "WFM, QM, analytics, surveys, recording, Verint."), ("Scores move skills by themselves?", "No."), ("Who upgrades the delivered solution?", "Five9, per the page."), ("Which retention text?", "The retention page.")],
    ("Name the suite", "Write native or Verint, and what a bad evaluation will not do by itself.", ["The product", "The non-effect", "The audio clock"], "You did not let a score edit a skill."),
    ("Agents lose a skill overnight and nobody filed a change", "Someone treated a score as a router.", "SKILL removed source=score", ["Restore the skill and separate coaching from routing", "Add predictive lines", "Delete recordings", "Change ANI"], 0, "WEM did not get a silent write into the skill.", "Put the skill back and fix the process."),
    ["Name native WEM or Verint", "Keep quality scores out of the router unless an admin change says so"]))
    R.append(L("l03", "Analytics and the report that is not a dashboard rumor", "practice", [
        "Analytics shows up on the WEM page and inside reporting. They are not one button. Standard reports need the Reporting role. Categories include ACD Queue, Campaign, Call Log, and the rest of that list. Layouts are tabular, summary, and matrix.",
        "A wallboard that refreshes from Statistics Web Services is an integration. A scheduled summary email is a report. Say which one broke.",
    ], [WEM, REPORTS, APIS], path("Three ways a number reaches a screen", "Name the pipe.", ["A standard report", "A WEM analytics view", "Statistics Web Services into a wallboard"]),
    "The number disagrees", ["Source", "Role", "Layout"], [
        ("Source", "Which", "Report, WEM, or statistics feed?", "which"),
        ("Role", "Reporting", "The report user has the role.", "role"),
        ("Layout", "Kind", "Tabular, summary, or matrix.", "lay"),
        ("Feed", "Name", "Statistics Web Services is named if that is the pipe.", "api"),
        ("Admin", "Window", "The call log window is not used for a queue snapshot.", "win"),
        ("Admin", "Stop", "You do not 'average' two products into a third number.", "stop"),
    ], [
        ("A wallboard feed and a standard report are", ["Always the same query", "Different pipes. Name them", "Both the IVR", "Both E911"], 1, "Say which one."),
        ("Statistics Web Services is", ["A headset", "A named API family", "A skill", "A codec"], 1, "The API page lists it."),
        ("The Reporting role gates", ["SIP", "Standard reports", "RedSky", "G.711"], 1, "Reports."),
        ("A matrix is the best CSV. True or false?", ["True", "False", "True for wallboards", "True for WEM"], 1, "Matrix is not a direct CSV."),
        ("WEM analytics replaces the Reporting role. True or false?", ["True", "False", "True for supervisors", "True after offload"], 1, "Different products."),
    ], [("Wallboard versus report?", "Different pipes."), ("Statistics API?", "A named family."), ("Reporting role?", "Gates standard reports."), ("Matrix as CSV?", "No.")],
    ("Label three numbers", "For service level, a survey score, and a wallboard, name the product.", ["Report", "WEM", "Statistics feed"], "You used three labels."),
    ("Leadership averages the wallboard and the summary into a bonus", "The pipes were never the same query.", "SL wall=40 report=55", ["Pick the system of record and stop averaging", "Change the abandon window", "Reboot phones", "Delete the skill"], 0, "Two products, two numbers.", "Choose one source."),
    ["Name the pipe that produced the number", "Do not average a wallboard and a report"]))
    R.append(L("l04", "AI agents are a handoff with a name", "advanced", [
        "Five9 Engage talks about self-service and the agent desktop together. Studio holds a digital IVA task. GenAI Studio is where knowledge and prompts are tested, and the product page says it powers Five9 AI applications, starting with Agent Assist summaries. This lab does not name a default model.",
        "An AI agent that cannot transfer to a real skill is a dead end. The IVR module list includes IVA Transfer. Digital IVA uses a Studio task key placed into VCC. Those are the handoffs you can cite.",
    ], [ENGAGE, GENAI, ADP], stack("A bot that can leave", "Cite the handoff you mean.", ["Studio task in the right region", "Task key in VCC", "IVA Transfer or a skill", "GenAI prompt tested before it is live"]),
    "The bot keeps the caller", ["Task", "Key", "Exit"], [
        ("Task", "Region", "The Studio region matches the domain.", "region"),
        ("Key", "VCC", "The task key is in VCC.", "key"),
        ("Exit", "Module", "IVA Transfer or Skill Transfer exists.", "exit"),
        ("Exit", "Skill", "The destination skill has people.", "skill"),
        ("Prompt", "Test", "A GenAI prompt was tested before production.", "test"),
        ("Prompt", "Model", "No model name is invented.", "model"),
    ], [
        ("This lab names GenAI Studio's default model. True or false?", ["True", "False", "True, it is a public rumor", "True for Agent Assist only"], 1, "The page does not give this lab a default to repeat."),
        ("IVA Transfer is", ["A rumor", "An IVR module", "A retention clock", "A gateway"], 1, "It is in the modules chapter."),
        ("A digital IVA reaches VCC with", ["A CUCM partition", "A Studio task key", "An ANI profile", "A matrix"], 1, "The Studio article."),
        ("Agent Assist summaries are", ["The dialer mode", "Named as an early GenAI Studio consumer", "A SIP port", "E911"], 1, "The GenAI page."),
        ("A bot with no transfer target is", ["A complete design", "A dead end", "Certified Caller", "A report layout"], 1, "Give it a skill."),
    ], [("Default model named here?", "No."), ("IVA Transfer?", "A real module."), ("Digital handoff?", "A Studio task key."), ("No exit?", "A dead end.")],
    ("Draw the exit", "Name the task, the key, and the skill a bot must be able to reach.", ["Region", "Key", "Skill"], "You did not name a model."),
    ("The bot apologizes forever", "IVA Transfer was never added.", "BOT exit=none", ["Add a transfer to a staffed skill", "Add lines per agent", "Change the abandon percent", "Register a fake HQ address"], 0, "The caller cannot leave.", "Add the handoff."),
    ["Give every bot a named exit", "Do not invent a model name"], uncertain=["GenAI Studio's product page describes an engine-agnostic studio and names Agent Assist summaries as an initial consumer. It does not name a default model for this lab to repeat."]))
    R.append(L("l05", "CRM, UC, and the desktop are three contracts", "practice", [
        "Plus adapters named in the technical requirements include Salesforce, ServiceNow, Dynamics 365, Zendesk, Oracle, NetSuite, Epic, and the Agent Desktop Toolkit. Zoom Phone and Teams show up as prebuilt paths on the API page. A UC app on the PC is also a bandwidth line, about 320 kbps.",
        "The agent's screen can show a CRM card, a UC window, and Agent Assist at once. When one is blank, name which contract failed.",
    ], [TECH, APIS, ADP], stack("Three contracts on one desk", "Blank is not one disease.", ["Plus adapter or CRM SDK", "Prebuilt UC, if purchased", "UC app bandwidth, if installed", "Assist, if enabled"]),
    "One pane is blank", ["Voice", "Card", "UC"], [
        ("Voice", "Ok", "The caller is heard.", "voice"),
        ("Card", "Adapter", "The adapter process is checked.", "ad"),
        ("UC", "App", "The UC client is checked separately.", "uc"),
        ("UC", "Bw", "320 kbps is in the budget if the app is local.", "bw"),
        ("Assist", "On", "Assist is either enabled or it is not.", "as"),
        ("Admin", "Word", "The ticket uses one product name.", "word"),
    ], [
        ("Epic is in the Plus adapter list. True or false?", ["False", "True", "Only as a codec", "Only in the EULA"], 1, "The PDF lists Epic."),
        ("A local Teams client is about", ["12 kbps", "320 kbps", "Zero", "88 kbps"], 1, "The workstation note."),
        ("Voice up and CRM blank means", ["G.711 failed", "The adapter is its own incident", "E911 failed", "The list is vertical"], 1, "Separate channels."),
        ("The CRM SDK is for", ["Replacing TLS", "A CRM that is not a named adapter", "Setting abandon rate", "Headsets"], 1, "Bring your own CRM."),
        ("Agent Assist bandwidth in the PDF is about", ["+12 kbps", "+320 kbps", "A trunk", "A domain"], 0, "About 12."),
    ], [("Epic listed?", "Yes."), ("Local Teams?", "About 320 kbps."), ("Blank card, live voice?", "Adapter incident."), ("SDK?", "Unlisted CRMs.")],
    ("Split a desk ticket", "Write the three contracts and which one is failing.", ["Adapter", "UC", "Assist"], "Voice is marked up so you do not reboot the trunk."),
    ("Someone adds Teams 'because the integration was purchased' and the floor slows", "The app's bandwidth was never added.", "BW budget=voice teams=on", ["Budget 320 kbps or remove the client", "Lower the abandon window", "Change skills to Default", "Disable SRV"], 0, "The client is traffic.", "Fix the budget."),
    ["Treat adapter, UC integration, and local UC app as three lines", "Budget Assist and Teams separately"]))
    R.append(L("l06", "The glossary is the contract with yourself", "foundation", [
        "Teams lose hours to words that Five9 uses narrowly: domain, skill, campaign profile, DNIS, disposition, list penetration, vertical dialing, campaign, autodial, blended, manual touch. The ecosystem glossary in this lab defines the ones we could cite and marks the rest.",
        "If you cannot point at a page, say 'we use this word locally' and keep it out of a design that claims to be vendor language.",
    ], [REPORTS, TECH], path("A word earns its place", "Citation or a local label.", ["Say the word", "Open the page", "Quote it", "Or mark it local"]),
    "A design review", ["Word", "Page", "Label"], [
        ("Word", "Hear", "Someone says 'partition' or 'CSQ'.", "hear"),
        ("Page", "Find", "You look for the Five9 page.", "find"),
        ("Label", "Local", "If there is no page, the word is marked local.", "local"),
        ("Label", "Teach", "The teaching bridge is named as a bridge.", "bridge"),
        ("Admin", "Profile", "Profile is not used to mean user profile and campaign profile at once.", "prof"),
        ("Admin", "Blend", "Blended is not written as a campaign type.", "blend"),
    ], [
        ("A word with no Five9 page should be", ["Put in the admin guide as official", "Marked local", "Used as a cert code", "Used as a port"], 1, "Citation or a local label."),
        ("Campaign profile and user profile are", ["Synonyms", "Different objects", "Both ANIs", "Both reports"], 1, "Do not merge them."),
        ("Blended, on the product pages, is", ["A fourth campaign type", "Staffing language", "A SIP port", "A retention row"], 1, "Inbound, outbound, and autodial are the types."),
        ("'Partition' in a Five9 design is", ["Required", "A visiting Cisco word. Mark it", "A skill level", "A layout"], 1, "Five9's boundary is the domain."),
        ("The glossary on the ecosystem page is", ["Decorative", "The same discipline as the lessons", "A dialer", "Optional fiction"], 1, "It is cited."),
    ], [("No page?", "Mark the word local."), ("Two profiles?", "Different objects."), ("Blended?", "Not a campaign type."), ("Partition?", "A visiting word.")],
    ("Audit ten words", "Mark each cited or local. Include blended, profile, and DNIS.", ["Cited", "Local", "One you almost misused"], "The local ones are labeled."),
    ("A diagram says 'partition = skill'", "That erases both products.", "MAP partition-as-skill", ["Redraw domain and skill, and mark the old word as Cisco", "Ship it", "Add the word to a cert exam", "Change the codec"], 0, "The map lied.", "Separate the vocabularies."),
    ["Cite a word or mark it local", "Keep campaign profile and user profile apart"], href="#/ecosystem"))
    R.append(L("l07", "Read the map before you add a box", "practice", [
        "Integration maps fail when a logo is enough. Salesforce in the IVR is a module. Salesforce on the desktop is an adapter. Certified Caller is not the ANI. RedSky is not the ITSP. Verint is not automatically your WEM. Studio regions are not Equinix edges.",
        "Open the ecosystem page, filter the glossary, and check the integration table against whatever you are about to buy. If the row is missing, you do not yet have a citation.",
    ], [APIS, E911, STIR, WEM, TECH], compare("Logos that get confused", "The row says how they meet.", "Often merged", ["IVR module and adapter", "ANI and attestation", "ITSP and RedSky"], "Keep split", ["Native WEM and Verint", "Studio region and Equinix edge", "Report and statistics feed"]),
    "A vendor slide arrives", ["Logo", "Row", "Gap"], [
        ("Logo", "See", "The slide has a logo and a verb.", "logo"),
        ("Row", "Find", "You find the row in the map, or you do not.", "row"),
        ("Gap", "Write", "A missing row is a question, not a yes.", "gap"),
        ("Split", "Two", "If two products share a brand, you name both.", "two"),
        ("Admin", "Cite", "The link is the one from the lesson.", "cite"),
        ("Admin", "Buy", "The purchase waits on the row.", "buy"),
    ], [
        ("A missing integration row means", ["Buy it", "You do not have a citation yet", "It is included in G.711", "It is a skill"], 1, "No row, no claim."),
        ("RedSky and the ITSP are", ["Always the same company", "Different roles", "Both report layouts", "Both headsets"], 1, "Location partner versus call path."),
        ("Studio region and an Equinix edge are", ["The same code", "Different lists", "Both DNIS", "Both dispositions"], 1, "Do not mix the lists."),
        ("Two uses of Salesforce should be", ["One SKU in the diagram", "Module versus adapter", "Both Certified Caller", "Both partitions"], 1, "Name which one."),
        ("The filter on the glossary is there so you can", ["Hide uncertainty", "Find a term before you misuse it", "Edit Five9's site", "Change TLS"], 1, "Use it."),
    ], [("Missing row?", "No citation yet."), ("RedSky versus ITSP?", "Different roles."), ("Studio versus Equinix?", "Different lists."), ("Two Salesforces?", "Module versus adapter.")],
    ("Check a slide", "Take three logos and write the row, or write 'no citation'.", ["Open the ecosystem page", "Filter one term", "Reject one merged logo"], "You left with fewer boxes than you started."),
    ("A slide connects RedSky to the SIP trunk as if it were the carrier", "The data sheet names an emergency partner.", "SLIDE redsky=itsp", ["Split emergency calling from the SIP story", "Order the edge as RedSky", "Delete E911", "Paste TCPA numbers"], 0, "The roles differ.", "Redraw the two boxes."),
    ["Check the integration row before you buy", "Split logos that hide two products"], href="#/ecosystem"))
    return track("t17", "Ecosystem", "Ecosystem", "Neighbors, WEM, analytics pipes, AI handoffs, and a glossary that refuses uncited words.", "Ecosystem", "Practice", "Every box needs a link. Every word needs a page or a local label.", R)
