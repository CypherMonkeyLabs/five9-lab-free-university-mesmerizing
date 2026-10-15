from curriculum_lib import ADP, ENGAGE, TECH, ADAPTERS, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "One screen is the product", "foundation", [
        "Agent Desktop Plus is described as a single screen so the agent can stay with the customer. The Engage page adds real-time transcription, AI Agent Assist, and case context on that screen. The same underlying technology is what the desktop page says you get from Plus or from a pre-built CRM adapter.",
        "A design that needs five browser tabs is the problem Plus is published to remove. If your floor still alt-tabs, you have not deployed the product you named.",
    ], [ADP, ENGAGE], stack("What the pages put on the screen", "Product language, not a promise of every AI model.", ["Voice", "Digital", "Transcription", "Agent Assist", "CRM context"]),
    "A call arrives", ["Caller", "Desktop", "Agent"], [
        ("Caller", "Connect", "Voice is on the desktop.", "voice"),
        ("Desktop", "Text", "Transcription runs if that feature is on.", "text"),
        ("Desktop", "Assist", "Suggestions appear in the same place.", "assist"),
        ("Desktop", "CRM", "Context is the adapter or the SDK.", "crm"),
        ("Agent", "Stay", "No second product is required for the basic story.", "stay"),
        ("Agent", "Tab", "A leftover tab is a deployment gap.", "tab"),
    ], [
        ("Plus is published as", ["Five required apps", "One screen", "A report only", "A trunk"], 1, "The desktop page says a single screen."),
        ("Transcription is named on", ["The Engage page", "The JRE page only", "RFC 3261", "The list-mode article only"], 1, "Engage describes transcription and Agent Assist."),
        ("A pre-built CRM adapter, per the desktop page,", ["Uses a different voice stack", "Uses the same underlying technology", "Cannot pop a record", "Requires analog headsets"], 1, "The page says the same underlying technology."),
        ("Alt-tab as the daily path means", ["The design matches the page", "The deployment missed the point of Plus", "TCPA is on", "ANI is local"], 1, "One screen is the claim."),
        ("Agent Assist bandwidth in the PDF is", ["Included in nothing", "An extra 12 kbps on top of the desktop", "1 Mbps", "Zero"], 1, "The bandwidth table lists 12 kbps for Agent Assist."),
    ], [("Form factor?", "One screen."), ("Transcription source?", "Engage page."), ("Adapter voice stack?", "Same underlying technology, per the desktop page."), ("Assist bandwidth?", "12 kbps extra.")],
    ("Count the tabs", "Watch one real or role-played call and count windows.", ["Voice", "Context", "Anything that should have been inside Plus"], "You can say what is still outside."),
    ("Agents keep a CRM in another window", "Plus is installed and the adapter was never turned on.", "PLUS installed ADAPTER off", ["Turn on the adapter or the SDK pop", "Add a sixth window", "Stop inbound", "Change list mode"], 0, "The second window is the missed deployment.", "Use the published desktop path."),
    ["Describe Plus as one screen", "Count extra windows as a defect"]))
    R.append(L("l02", "Plus adapters speak HTTPS and WSS", "practice", [
        "The technical requirements say Plus adapters use HTTPS and Secure WebSocket. If a proxy is in the path, it must support WSS. The PDF also says Five9 does not support TLS 1.1, and that browsers need TLS 1.2. Unencrypted API connections are refused.",
        "A screen pop that fails while voice still works is often this path: the media is fine and the websocket is not. Do not replace the headset first.",
    ], [TECH, ADAPTERS], path("Two channels", "Voice can live while the pop dies.", ["HTTPS", "WSS", "Proxy must allow WSS", "TLS 1.2"]),
    "Pop fails, voice works", ["Phone", "Adapter", "Proxy"], [
        ("Phone", "Audio", "The caller is heard.", "audio"),
        ("Adapter", "WSS", "The pop channel tries to open.", "wss"),
        ("Proxy", "Block", "The proxy does not understand WSS.", "block"),
        ("Adapter", "Blank", "The CRM pane stays empty.", "blank"),
        ("Admin", "TLS", "TLS 1.1 will not be accepted.", "tls"),
        ("Admin", "Fix", "Allow WSS and TLS 1.2.", "fix"),
    ], [
        ("Plus adapter security is", ["HTTP", "HTTPS and Secure WebSocket", "Telnet", "FTP only"], 1, "The PDF says so."),
        ("A proxy in front of the desktop must", ["Strip TLS", "Support WSS", "Block 443", "Be double NAT"], 1, "The PDF requires WSS-capable proxies."),
        ("TLS 1.1", ["Is preferred", "Is not supported for inbound or outbound traffic", "Is required for IVR", "Is a codec"], 1, "The PDF says Five9 does not support TLS 1.1."),
        ("Voice up, pop down, first suspect", ["The abandon cap", "The websocket path", "List penetration", "A skill greeting"], 1, "They are different channels."),
        ("Cleartext API calls are", ["Encouraged", "Refused", "Required for SOAP nostalgia", "Fine on Saturday"], 1, "The PDF says Five9 does not accept unencrypted API connections."),
    ], [("Adapter transport?", "HTTPS and WSS."), ("Proxy?", "Must support WSS."), ("TLS 1.1?", "Not supported."), ("Pop down, voice up?", "Look at WSS.")],
    ("Draw the proxy", "Mark where WSS would be dropped.", ["Browser", "Proxy", "Five9", "A note that voice is a different path"], "The note does not say 'replace the headset'."),
    ("Monday pop outage", "A new proxy was installed over the weekend. Calls still connect.", "PROXY new WSS=blocked VOICE=up", ["Allow WSS on the proxy", "Replace every headset", "Switch to vertical dialing", "Disable recording"], 0, "The new proxy is the change.", "Permit Secure WebSocket and retest the pop."),
    ["Separate voice from the pop channel", "Require TLS 1.2 and WSS"]))
    R.append(L("l03", "Transcription and assist are features you turn on", "practice", [
        "The Engage page describes transcription, sentiment language, and Agent Assist suggestions on the desktop. GenAI Studio's page says it powers Five9 AI applications and initially focuses on Agent Assist summaries, with control over the output.",
        "None of those pages name a single model you can assume is the default in every domain. If a design says 'it uses model X,' mark that sentence uncertain until the domain's GenAI Studio screen says it.",
    ], [ENGAGE, cite_gen()], stack("What is public", "Features, not a secret model name.", ["Transcription", "Agent Assist", "Summaries via GenAI Studio", "Output control"]),
    "A summary after the call", ["Call", "Desktop", "Studio"], [
        ("Call", "Talk", "The conversation happens.", "talk"),
        ("Desktop", "Live", "Assist can suggest during the call.", "live"),
        ("Studio", "Prompt", "A managed prompt shapes the summary.", "prompt"),
        ("Studio", "Model", "The model is chosen in that hub, not guessed here.", "model"),
        ("Desktop", "Show", "The agent sees the result on the same screen.", "show"),
        ("Admin", "Check", "The domain screen is the source of the model name.", "check"),
    ], [
        ("Agent Assist is named on", ["The Engage page", "The list-penetration article only", "The E911 data sheet only", "RFC 4733"], 1, "Engage describes it."),
        ("GenAI Studio's initial focus, on its page, includes", ["Replacing SIP", "Agent Assist summaries", "Building PBXs", "Issuing DIDs"], 1, "The page says summaries first, with customizable output."),
        ("The model name in this lab is", ["Published as a universal default", "Not assumed. Read the domain", "Always a single vendor", "Illegal to ask"], 1, "The page says engine-agnostic."),
        ("Transcription without a readable screen", ["Still helps the agent in the moment", "Misses the point of putting it on the desktop", "Sets ANI", "Resets lists"], 1, "The agent has to see it."),
        ("Output control is", ["Absent", "Part of the GenAI Studio description", "A codec", "A skill tab"], 1, "The page talks about control and responsible AI."),
    ], [("Where is Assist named?", "Engage."), ("Studio's first named app?", "Summaries, among Agent Assist."), ("Universal model name?", "Do not assume one."), ("Why the same screen?", "So the agent sees it.")],
    ("Write the uncertain sentence", "Draft a design line that does not name a model.", ["Say Assist is on the desktop", "Say the model is whatever Studio is set to", "Refuse a fake default"], "The sentence has no invented model."),
    ("A slide says the floor runs a specific third-party model", "Nobody has opened GenAI Studio.", "SLIDE model=invented STUDIO unchecked", ["Open Studio and correct the slide", "Print the slide", "Change the dialer mode", "Delete skills"], 0, "The slide outran the product.", "Use the engine the hub is actually set to."),
    ["Keep Assist on the one screen", "Do not invent the model name"], uncertain=["GenAI Studio is described as engine-agnostic. This lab does not name the default model for a new domain."]))
    R.append(L("l04", "WEM lives in the same desktop", "practice", [
        "The desktop page says Plus can show schedules, adherence, time-off requests, and evaluations without another app. CRM connectors can surface the same WFO actions inside Salesforce and the other named CRMs.",
        "That is the staffing blend meeting the person: the agent can see that they are supposed to be on a break. A dialer that ignores the schedule will call it idle time.",
    ], [ADP, cite_wem()], path("Schedule on the desktop", "The person can see the plan.", ["WEM schedule", "Plus or CRM connector", "Adherence", "Dialer must not treat a break as idle"]),
    "Break starts", ["WEM", "Desktop", "Dialer"], [
        ("WEM", "Plan", "The schedule says break.", "plan"),
        ("Desktop", "Show", "Plus shows the schedule.", "show"),
        ("Agent", "Leave", "They go Not Ready or the schedule pulls them.", "leave"),
        ("Dialer", "Count", "They are not a free agent.", "count"),
        ("Supervisor", "Eval", "An evaluation can be reviewed in the same place.", "eval"),
        ("Admin", "CRM", "A connector can show the same actions in the CRM.", "crm"),
    ], [
        ("Schedules inside Plus are", ["Undocumented", "Named on the desktop page", "A SIP option", "A list mode"], 1, "The page lists schedules, adherence, time off, and evaluations."),
        ("A break is", ["Idle time to fill with predictive", "Not a free agent", "A DNIS", "A prompt"], 1, "Availability is the truth."),
        ("CRM connectors for WFO are", ["Absent", "Named on the desktop page", "Illegal", "Java-only"], 1, "The page lists them for the named CRMs."),
        ("Adherence is", ["A codec", "Whether the person followed the schedule", "An ANI", "A frame header"], 1, "That is the ordinary meaning, and the page uses the word."),
        ("Ignoring the schedule in the dialer", ["Improves service level honestly", "Dials against people who are supposed to be away", "Is required", "Signs calls"], 1, "The blend gets worse."),
    ], [("What does Plus show from WEM?", "Schedules, adherence, time off, evaluations."), ("Break equals idle?", "No."), ("CRM path?", "WFO connectors, per the desktop page."), ("Adherence?", "Plan versus actual.")],
    ("Subtract the break", "On a 20-person roster, remove the scheduled break before you set lines.", ["Read the schedule", "Count who is actually there", "Set the mode from that count"], "The line count uses the smaller number."),
    ("Predictive overdials every day at 10:15", "That is the scheduled break and the dialer still counts those logins.", "SCHEDULE break=10:15 MODE predictive uses=headcount", ["Remove break agents from the available count", "Add lines at 10:15", "Delete WEM", "Stop IVR"], 0, "The schedule already knew.", "Feed availability from the schedule, not from headcount."),
    ["Show the schedule on the desktop", "Do not dial a break"]))
    R.append(L("l05", "Digital text can be blocked", "practice", [
        "The technical requirements say some antivirus software, naming Avast as an example, can stop chat, social, or email text from loading. Voice can continue. The symptom is a blank digital pane, not a busy DNIS.",
        "Efficiency Mode can also sleep a background tab and drop a live call. Digital and voice fail differently. Write the symptom before you pick the cause.",
    ], [TECH], compare("Two desktop failures", "Match the symptom.", "Blank chat text", ["Antivirus is a documented suspect", "Voice may still work"], "Dropped live call", ["Efficiency Mode is a documented suspect", "A sleeping tab"]),
    "Blank chat", ["Agent", "AV", "Voice"], [
        ("Agent", "Open", "The digital pane is empty.", "empty"),
        ("Voice", "Fine", "The call audio still works.", "audio"),
        ("AV", "Block", "Text media never loads.", "block"),
        ("Admin", "Test", "A machine without that AV loads the text.", "test"),
        ("Admin", "Allow", "The AV exception is the fix.", "allow"),
        ("Admin", "Separate", "This is not the Efficiency Mode symptom.", "sep"),
    ], [
        ("Avast is named as", ["A supported headset", "An example of antivirus that can block text media", "A dialer mode", "A skill"], 1, "The PDF uses it as an example."),
        ("Voice works, chat text does not. First documented suspect?", ["List penetration", "Antivirus", "The 30-day abandon window", "A final disposition"], 1, "The PDF separates text media from the call."),
        ("Efficiency Mode's documented symptom is", ["Blank text only", "Interrupted apps and dropped calls", "A wrong ANI", "A CSV error"], 1, "Different symptom."),
        ("The fix for blocked text is", ["More predictive lines", "An exception or a different AV posture, then a retest", "Stopping the campaign", "Vertical dialing"], 1, "Restore the text path."),
        ("You should change both settings at once without a note. True or false?", ["True", "False. One change, one retest", "True on ARM Macs", "True for TCPA"], 1, "Otherwise you will not know which one mattered."),
    ], [("Avast example means?", "AV can block text."), ("Blank text suspect?", "Antivirus."), ("Dropped call suspect?", "Efficiency Mode, among others."), ("Change both at once?", "No.")],
    ("Write the symptom", "One sentence for blank text and one for a dropped call.", ["Name the suspect for each", "Name the retest"], "The sentences do not share a fix."),
    ("Chat has been blank since a security rollout", "A new AV suite landed on Monday. Voice is fine.", "AV deployed Monday TEXT empty", ["Pilot an exception on one PC", "Replace the SBC", "Reset all dispositions", "Enable TLS 1.1"], 0, "The rollout matches the documented failure.", "Get text loading on one PC, then widen the exception."),
    ["Match blank text to antivirus", "Match dropped calls to power management"]))
    R.append(L("l06", "Headsets and the path under the desk", "practice", [
        "USB noise-canceling headsets are the recommendation. Analog is not supported. Wireless is discouraged above about ten active agents because of delay. Wired LAN is preferred. Wi-Fi is tolerated only when bandwidth holds. Satellite and cellular, including 5G, are not supported.",
        "Agent Desktop Plus and the adapters are listed at 128 kbps for G.711, which the PDF says is the default codec. Agent Assist adds 12 kbps. CRM in the same session adds another 64 kbps in that table. A VPN adds 64 kbps. Latency to the data center should be under 150 ms one way.",
    ], [TECH], stack("Desk budget from the PDF", "Add the rows you actually use.", ["ADP 128 kbps", "Assist +12", "CRM +64", "VPN +64", "Under 150 ms one way"]),
    "A home agent", ["Desk", "Path", "Five9"], [
        ("Desk", "USB", "The headset is USB.", "usb"),
        ("Path", "Wire", "The LAN is wired, or Wi-Fi that meets the rate.", "lan"),
        ("Path", "No", "The path is not a phone hotspot.", "no"),
        ("Five9", "Rate", "The budget includes every extra row.", "rate"),
        ("Five9", "Time", "One-way delay is under 150 ms.", "rtt"),
        ("Desk", "Power", "Efficiency Mode is off.", "power"),
    ], [
        ("Analog headsets are", ["Preferred", "Not supported", "Required for preview", "Required for IVR"], 1, "The PDF says not supported."),
        ("Cellular or 5G as the agent path is", ["Supported", "Not supported", "Required", "Fine if G.711 is on"], 1, "The PDF excludes satellite and wireless internet such as 5G and cellular."),
        ("Default codec in the bandwidth section is", ["G.729", "G.711", "Opus only", "GSM required"], 1, "G.711 is the default in that section. GSM and iLBC are mentioned elsewhere as untested options on iPad supervisor."),
        ("150 ms is", ["A round trip suggestion", "The one-way latency limit in the PDF", "An abandon window", "A pause timer"], 1, "One way, to the data center."),
        ("CRM's extra row in the table is", ["0", "64 kbps", "320 kbps", "12 kbps"], 1, "64 kbps additional for business apps such as CRM. Assist is the 12 kbps row."),
    ], [("Analog?", "Not supported."), ("5G agent path?", "Not supported."), ("Default codec in that table?", "G.711."), ("One-way latency?", "Under 150 ms.")],
    ("Add the budget", "Sum the rows for Plus, Assist, CRM, and VPN.", ["128", "12", "64", "64"], "You did not forget Assist."),
    ("Agents on hotspots sound broken", "The office Wi-Fi died and everyone tethered.", "PATH cellular", ["Move them back to a supported path", "Lower the bitrate in a myth", "Switch to analog", "Disable WSS"], 0, "Cellular is outside the published support list.", "Restore wired or a Wi-Fi path that meets the table."),
    ["Budget the kilobits", "Refuse a cellular agent path"], uncertain=["The iPad supervisor section says G711U and G711A are primary and that GSM or iLBC may be used but have not been tested. That sentence is about that app, not a blanket codec menu."]))
    R.append(L("l07", "The desktop review", "advanced", [
        "A desktop review is short: one screen, WSS through the proxy, TLS 1.2, the schedule visible, text not blocked, USB headset, supported path, Efficiency Mode off, and the bandwidth rows added up. Each line is from the product page or the PDF.",
        "If those pass and audio is still one-way, you are in NAT and firewall territory, which is the SIP track. The desktop is no longer the prime suspect.",
    ], [ADP, TECH], path("Desktop review", "Then hand the ticket to the network track.", ["One screen", "WSS", "TLS 1.2", "Schedule", "Text loads", "USB and path", "Budget"]),
    "Close or escalate", ["Desk", "Network"], [
        ("Desk", "Screen", "Plus holds the work.", "screen"),
        ("Desk", "Socket", "WSS opens.", "wss"),
        ("Desk", "Text", "Chat text loads.", "text"),
        ("Desk", "Path", "Not cellular. Efficiency Mode off.", "path"),
        ("Network", "One way", "Audio fails in one direction.", "oneway"),
        ("Network", "NAT", "The SIP track owns double NAT and UDP timeouts.", "nat"),
    ], [
        ("One-way audio after the desk checks pass belongs to", ["Another greeting file", "The network and NAT notes", "A flashcard", "Credly"], 1, "The PDF's NAT section is the next page."),
        ("Efficiency Mode belongs in", ["The dialer ratio", "The desktop review", "The list filter", "The ANI"], 1, "It drops calls."),
        ("WSS belongs in", ["The desktop review", "The skill greeting", "The disposition", "The Credly exam"], 1, "Pops depend on it."),
        ("A review that skips the schedule will", ["Still pace honestly", "Count people who are on break", "Fix 911", "Sign calls"], 1, "Breaks are on the desktop for a reason."),
        ("The PDF is", ["Optional folklore", "The source for the bandwidth and TLS lines", "A dialer mode", "A campaign type"], 1, "Re-read it. It moves."),
    ], [("One-way audio next stop?", "NAT and SIP."), ("Efficiency Mode?", "Desktop review."), ("WSS?", "Desktop review."), ("Skip the schedule?", "You will mis-count people.")],
    ("Tick the review", "Seven checks on one workstation.", ["Screen", "WSS", "TLS", "Schedule", "Text", "Headset and path", "Budget"], "Either the desk is clean or you have a named defect."),
    ("The ticket says headset, the log says proxy", "Voice is fine, pop is empty, a proxy changed.", "WSS blocked HEADSET new", ["Fix the proxy. Leave the new headset", "Buy another headset", "Enable TLS 1.1", "Stop the domain"], 0, "The symptom matches WSS, not the transducer.", "Open WSS and retest the pop."),
    ["Run the desktop review", "Escalate one-way audio to the network track"], href="#/topology"))
    return track("t09", "Agent Desktop Plus", "Desktop", "One screen, WSS, assist, WEM on the desktop, and the desk the PDF will support.", "People", "Practice", "Plus is the agent's instrument. Voice, pop, text, and the schedule fail in different ways.", R)

def cite_gen():
    from curriculum_lib import GENAI
    return GENAI

def cite_wem():
    from curriculum_lib import WEM
    return WEM
