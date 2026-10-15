from curriculum_lib import PLAN, SKILLS, PROFILES, PROFILEHOW, TECH, ADP, MODULES, OUTBOUND, REPORTS, lesson, stack, path, compare, track

def build():
    L = lesson
    rows = []
    rows.append(L("l01", "Two administrator applications", "foundation", [
        "The technical requirements still describe a Java VCC Administrator and a web Administrator Console. Java is not supported on Mac workstations with ARM processors. On those machines the document says to use VCC Administrator via Web in Admin Console.",
        "Because web applications do not need a Java SE subscription, the same document strongly recommends moving to the Five9 Plus applications. The Java client is still documented, with named JRE 8 update builds. Treat that list as dated and re-read the PDF before you image a PC.",
    ], [TECH], compare("Admin clients", "Pick the client the workstation can actually run.", "Java VCC Administrator", ["Windows and supported Mac", "Not on Mac ARM", "Needs a JRE"], "Web admin and Plus", ["No Java SE requirement", "Recommended path", "HTTPS and WSS"]),
    "Choose a client", ["Admin", "Workstation"], [
        ("Admin", "Java", "Opens the classic administrator.", "java"),
        ("Workstation", "ARM Mac", "Java admin is not supported.", "arm"),
        ("Admin", "Web", "Use VCC Administrator via Web.", "web"),
        ("Admin", "Plus", "Web apps avoid the Java subscription.", "plus"),
        ("Workstation", "JRE", "The PDF names specific JRE 8 updates.", "jre"),
        ("Admin", "Recheck", "Version lists move. Open the current PDF.", "pdf"),
    ], [
        ("Java VCC Administrator on a Mac with an ARM chip?", ["Supported", "Not supported. Use the web administrator", "Supported only for TCPA", "Supported only for IVR"], 1, "The technical requirements say Java admin is not supported on Mac ARM. Use the web administrator."),
        ("Why does Five9 recommend Plus applications in that PDF?", ["They use more Java", "Web applications do not require Java SE", "They remove skills", "They disable recording"], 1, "The PDF says web applications do not require Java SE and recommends Plus."),
        ("The JRE line in the PDF is", ["A permanent promise", "A time-specific list you must re-read", "Optional for browsers", "The dialer algorithm"], 1, "Update numbers change. The lab marks them as time-specific."),
        ("Plus adapters talk to Five9 with", ["Cleartext SIP only", "HTTPS and Secure WebSocket", "FTP only", "RMI without TLS"], 1, "The PDF says Plus adapters use HTTPS and Secure WebSocket."),
        ("Internet Explorer is", ["The primary browser", "Ended, except IE 11 for the Oracle Service Cloud adapter only", "Required for ADP", "Required for IVR"], 1, "The PDF says IE support ended, with that one adapter exception."),
    ], [("Mac ARM and Java admin?", "Not supported. Use the web administrator."), ("Why Plus?", "Web apps do not need Java SE."), ("Plus transport?", "HTTPS and WSS."), ("IE exception?", "IE 11 for Oracle Service Cloud only.")],
    ("Pick the client", "For a Windows PC and an ARM Mac, name the administrator you would open.", ["Windows: Java or web", "ARM Mac: web", "Write down that the JRE list must be rechecked"], "You did not install Java on the ARM Mac."),
    ("Admin will not launch", "A new Mac laptop shows a Java error before the domain tree appears.", "HOST chip=ARM APP=VCC-Administrator-Java", ["Use VCC Administrator via Web", "Lower the abandon cap", "Switch the list to vertical", "Disable WSS"], 0, "Java admin is unsupported on Mac ARM.", "Open the web administrator."),
    ["Choose Java or web admin", "Remember the ARM exception"], uncertain=["The fetched PDF names JRE 8 updates 421, 451, and 461, and macOS 15 Sequoia, 26 Tahoe, and 27 Golden Gate. Those lines are time-specific."], callout=("Re-read", "Do not copy a JRE or macOS version out of this lab into a purchase order.")))

    rows.append(L("l02", "User profiles before user accounts", "foundation", [
        "The planning roadmap says to define user profiles before you add user accounts. A profile is the permission bundle. An account is the person. Creating people first and hoping the default permissions match the job is how reporting and call-variable edits go missing.",
        "Skill groups then take users who already have the agent or supervisor role. An administrator account is not automatically a member of a queue.",
    ], [PLAN, SKILLS], path("Permission, then person, then queue", "The roadmap order is the point.", ["User profile", "User account", "Role", "Skill group"]),
    "Add a billing agent", ["Admin", "Domain"], [
        ("Admin", "Profile", "Define the agent permission bundle.", "profile"),
        ("Admin", "Account", "Create the person and attach the profile.", "account"),
        ("Domain", "Role", "The role must include agent.", "role"),
        ("Domain", "Skill", "Add that user to Billing.", "skill"),
        ("Domain", "Ready", "The agent can now be offered Billing calls.", "ready"),
        ("Admin", "Audit", "A second user reuses the profile.", "reuse"),
    ], [
        ("What is created first, the person or the profile?", ["The person", "The user profile", "The SIP trunk", "The call log"], 1, "The planning roadmap defines user profiles before accounts."),
        ("Does an administrator login receive queue calls?", ["Yes, always", "No. Queue membership is a skill assignment on an agent or supervisor", "Yes in predictive mode", "Yes if ANI matches"], 1, "Skill groups take agent or supervisor users."),
        ("A missing report permission looks like", ["A carrier outage", "A feature that was never granted", "A bad G.711 ptime", "A final disposition"], 1, "Check the profile before you open a trunk ticket."),
        ("One profile can be reused for many accounts. True or false?", ["False", "True. That is why the profile exists before the accounts", "Only for TCPA", "Only for one day"], 1, "The profile is the bundle. Accounts attach to it."),
        ("Where do you look when an admin cannot edit call variables?", ["The ITSP", "The administrator role permission", "The headset mute", "The Equinix SLA"], 1, "User Can Edit Call Variables is a role permission."),
    ], [("Profile or account first?", "Profile, then account."), ("Who joins a skill?", "Agent or supervisor users."), ("Missing permission symptom?", "It looks like a missing feature."), ("Call variable edits?", "A named permission on the administrator role.")],
    ("Write a profile", "List the permissions for one agent profile and one admin profile.", ["Agent: no IVR folder", "Admin: call variables if they need them", "Neither profile includes every right"], "The two profiles are different."),
    ("New hire cannot change Ready state reason codes", "The account exists and the skill is correct.", "USER nia profile=blank role=Agent", ["The account was created without the intended user profile", "SBC B failed", "The Menu module is full", "ANI is empty"], 0, "A blank or wrong profile omits permissions.", "Attach the agent profile the design named."),
    ["Create a profile before accounts", "Keep admin rights off the agent profile"]))

    rows.append(L("l03", "Skill groups are the queues", "practice", [
        "Skill groups organize agent and supervisor users into the queues that belong to campaigns. A user can be in several groups. A campaign can list several groups.",
        "The same help topic uses two different places for the assignment. Outbound campaigns take skills on the Skills tab. Inbound and autodial campaigns take them on a tab named Outbound Skills. Read that name twice before you decide the tab is missing.",
    ], [SKILLS], compare("Where the skill is attached", "The tab name is easy to misread.", "Outbound campaign", ["Skills tab"], "Inbound and autodial", ["Outbound Skills tab"]),
    "Attach Billing", ["Admin", "Campaign"], [
        ("Admin", "Create", "Add a skill group named Billing.", "create"),
        ("Admin", "Members", "Add agents who should take those calls.", "members"),
        ("Campaign", "Outbound", "Open the Skills tab.", "skills tab"),
        ("Campaign", "Inbound", "Open Outbound Skills instead.", "outbound skills"),
        ("Campaign", "Run", "A running inbound campaign can now queue.", "run"),
        ("Admin", "Voicemail", "Skill groups can also take voicemail.", "vm"),
    ], [
        ("Inbound skill assignment is on a tab named", ["Inbound Skills", "Outbound Skills", "TLS", "ANI"], 1, "The skill topic says inbound and autodial use the Outbound Skills tab."),
        ("Outbound skill assignment is on", ["The Skills tab", "The IVR Menu", "MyE911", "The JRE"], 1, "Outbound campaigns use the Skills tab."),
        ("A campaign may list", ["Only one skill", "Multiple skill groups", "No users ever", "Only Default"], 1, "Campaigns can have multiple skill groups."),
        ("An agent may belong to", ["One skill only", "Multiple skill groups", "Only the domain admin role", "Only WEM"], 1, "Users can be assigned to multiple skill groups."),
        ("Skill voicemail is", ["Undocumented", "Part of the skill group topic, including greetings and messages", "A SIP trunk feature only", "Removed in Plus"], 1, "The skill topic covers voicemail messages and greetings for the group."),
    ], [("Inbound tab name?", "Outbound Skills."), ("Outbound tab name?", "Skills."), ("Multiple skills per campaign?", "Yes."), ("Multiple skills per user?", "Yes.")],
    ("Name the tab", "For one inbound and one outbound campaign, write the tab you would open.", ["Inbound: Outbound Skills", "Outbound: Skills", "Add the same agent to both groups"], "You did not hunt for a tab called Inbound Skills."),
    ("Inbound queue with no agents", "The skill exists and the agents are Ready. The inbound campaign never offers the call.", "CAMPAIGN inbound tab=Skills EMPTY otherTab=OutboundSkills has=Billing", ["The skill was added on the wrong tab", "Predictive ratio is 1", "The ANI is local", "Java is current"], 0, "Inbound uses the Outbound Skills tab.", "Move Billing onto Outbound Skills."),
    ["Use the correct skills tab", "Put one agent in two groups"]))

    rows.append(L("l04", "Prompts before the script", "practice", [
        "The inbound and autodial roadmaps tell you to define and record prompts before you build the IVR. A Play or Menu module can only speak what the prompt library already holds, or what a text-to-speech entry supplies in that module.",
        "Skill groups have their own audio: voicemail greetings and other skill audio. A campaign prompt and a skill greeting are different objects. Replacing one does not replace the other.",
    ], [PLAN, SKILLS], path("Audio objects", "Record the file before the module names it.", ["Record prompt", "Prompt library", "Play or Menu", "Skill greeting"]),
    "A greeting reaches the caller", ["Admin", "IVR"], [
        ("Admin", "Record", "Add the prompt in the library.", "library"),
        ("IVR", "Play", "The Play module points at it.", "play"),
        ("IVR", "Menu", "The Menu module plays its own prompt.", "menu"),
        ("Admin", "Skill", "A separate greeting can live on the skill.", "skill audio"),
        ("IVR", "Run", "The campaign must be running or inbound callers hear busy.", "run"),
        ("Admin", "Check", "Listen in the script, not only in the file list.", "listen"),
    ], [
        ("When does the roadmap say to record prompts?", ["After the first live day", "Before you create the IVR scripts", "After you delete skills", "Never"], 1, "Planning says to define and record prompts, then create scripts."),
        ("A skill voicemail greeting is", ["The same object as a campaign Play prompt", "A skill-group audio object", "A SIP codec", "A disposition"], 1, "The skill topic has its own greeting and audio tasks."),
        ("If the inbound campaign is stopped, a perfect prompt", ["Still answers", "Is never heard, because callers get busy", "Plays twice", "Becomes a list"], 1, "The campaign must be running."),
        ("Play can use TTS in the web-service example. True or false?", ["False", "True. The example adds a TTS prompt on the Play module", "Only for Spanish", "Only on Saturday"], 1, "The XML query example plays a TTS prompt."),
        ("You should test the prompt", ["Only on the file's duration field", "Inside the script path the caller will hit", "By emailing it", "In MyE911"], 1, "A file that is not referenced is silent."),
    ], [("Prompts before scripts?", "Yes, on the inbound and autodial roadmap."), ("Skill greeting vs Play prompt?", "Different objects."), ("Stopped campaign?", "Busy, prompt unheard."), ("TTS?", "The query example uses a TTS prompt on Play.")],
    ("Library check", "Name one campaign prompt and one skill greeting.", ["Record or import the campaign prompt", "Point a Play module at it", "Leave the skill greeting alone"], "You can point at which object the caller hears."),
    ("Silence after the greeting file was replaced", "The new WAV is in the library. Callers still hear the old sentence.", "IVR Play prompt=greeting-v1 FILE greeting-v2 unused", ["The script still points at version 1", "TLS 1.1 is on", "The list is empty", "ANI changed"], 0, "Replacing a file does not retarget the module.", "Point Play at greeting-v2."),
    ["Record prompts before scripts", "Keep skill audio separate"]))

    rows.append(L("l05", "Do-not-call is a list, and a module", "practice", [
        "Outbound product material lists DNC list management with time-zone rules and Certified Caller as compliance tools. Inside the IVR, Set DNC is a real module in the modules chapter. A spoken 'remove me' path should hit that module, not a note in a disposition comment.",
        "A disposition called DNC is not the same object as the Set DNC module. Use both only if you know which system each one updates. This lab does not pretend they are automatically the same switch.",
    ], [MODULES, OUTBOUND, REPORTS], stack("Two different DNC actions", "Do not assume a comment field updates the DNC list.", ["Set DNC module", "DNC list management", "A disposition named DNC", "A report of DNC"]),
    "Caller says do not call", ["Caller", "IVR", "List"], [
        ("Caller", "Request", "The caller asks to be removed.", "speech"),
        ("IVR", "Menu", "A digit or speech branch catches it.", "branch"),
        ("IVR", "Set DNC", "The module is the documented action.", "module"),
        ("List", "Stop", "Further dialer attempts must honor the list.", "list"),
        ("IVR", "Disposition", "A code alone is a label unless you know it writes the list.", "code"),
        ("List", "Report", "Do Not Call is a standard report category.", "report"),
    ], [
        ("Which IVR module is named for this job?", ["Play", "Set DNC", "Language", "Conference"], 1, "Set DNC is in the modules chapter."),
        ("A disposition comment that says DNC", ["Always updates the DNC list", "Is not documented as the same thing as Set DNC", "Deletes the domain", "Starts predictive mode"], 1, "Treat them as separate until a current guide says otherwise."),
        ("Do Not Call reports are", ["Missing from the standard catalog", "A named standard report category", "Only in Studio", "Only on paper"], 1, "The reporting article lists Do Not Call Reports."),
        ("Product material groups DNC with", ["Headset SKUs", "Time-zone rules and Certified Caller", "Java updates", "Equinix cities"], 1, "The outbound product page lists those compliance tools together."),
        ("The safe design is", ["A free-text note", "An explicit Set DNC step on the spoken path", "A faster abandon cap", "A second ANI"], 1, "The module exists so the request is an action."),
    ], [("IVR module?", "Set DNC."), ("Is a disposition the same?", "Not documented as the same object."), ("Report category?", "Do Not Call Reports."), ("Product grouping?", "With time-zone rules and Certified Caller.")],
    ("Draw the path", "Sketch Menu to Set DNC for a removal request.", ["Add the branch", "Name the module", "Say what you will not trust a comment to do"], "The path hits Set DNC."),
    ("Removals keep dialing", "Agents type DNC in a note. The list still dials those numbers.", "DISPOSITION note=DNC MODULE SetDNC count=0", ["The script never called Set DNC", "G.711 failed", "The profile had two ANIs", "SBC A rebooted"], 0, "A note is not the module.", "Add Set DNC on that branch."),
    ["Use the Set DNC module", "Do not confuse it with a disposition label"], uncertain=["Public pages do not spell out, in one paragraph, whether a custom disposition named DNC writes the same list as the Set DNC module. Confirm in your domain."]))

    rows.append(L("l06", "Workstations that drop live calls", "practice", [
        "The technical requirements tell you to turn off Windows 11 Efficiency Mode on PCs that take live calls. Efficiency Mode can limit CPU and sleep inactive tabs, and the PDF says that can drop active Five9 calls. If you leave it on, use a high-performance power plan.",
        "Headsets should be USB with noise canceling. Analog headsets are not supported. Wireless is discouraged when more than 10 agents are active, because of delay and quality. Wired LAN is recommended. Wi-Fi is allowed only if each user still meets the bandwidth numbers. Satellite and cellular, including 5G, are not supported.",
    ], [TECH], stack("Workstation rules from the PDF", "These are support boundaries, not suggestions from a blog.", ["Efficiency Mode off", "USB headset", "Wired LAN preferred", "No satellite or cellular"]),
    "A call survives the PC", ["PC", "Five9"], [
        ("PC", "Power", "Efficiency Mode is unchecked.", "efficiency"),
        ("PC", "Headset", "USB, not analog.", "usb"),
        ("PC", "LAN", "Wired link, or Wi-Fi that meets the rate.", "lan"),
        ("Five9", "Media", "G.711 is the default codec in the bandwidth section.", "g711"),
        ("Five9", "Rate", "Agent Desktop Plus and adapters are listed at 128 kbps.", "128"),
        ("PC", "Refuse", "A 5G hotspot is outside the supported list.", "cellular"),
    ], [
        ("Windows 11 Efficiency Mode on a live agent PC?", ["Required", "Turn it off. It can drop calls", "Only for supervisors", "Only in UK domains"], 1, "The PDF says it can interrupt Five9 apps and drop active calls."),
        ("Analog headsets are", ["Preferred", "Not supported", "Required for TCPA", "Required for IVR"], 1, "The PDF says analog headsets are not supported."),
        ("Wireless headsets above about 10 active agents?", ["Recommended", "Not recommended, because of delay and quality", "Required", "Illegal"], 1, "The PDF does not recommend wireless when more than 10 agents are active."),
        ("Satellite or 5G as the agent path?", ["Supported", "Not supported", "Supported for inbound only", "Supported if G.711 is on"], 1, "Satellite and wireless internet such as 5G and cellular are not supported."),
        ("Listed bandwidth for Agent Desktop Plus and Plus adapters?", ["12 kbps", "128 kbps minimum and recommended", "1 Mbps required by law", "320 kbps for every adapter"], 1, "The bandwidth table lists 128 kbps for ADP and Plus adapters. Agent Assist is an extra 12 kbps."),
    ], [("Efficiency Mode?", "Off for live calls."), ("Analog headsets?", "Not supported."), ("5G?", "Not supported."), ("ADP bandwidth?", "128 kbps in the table, G.711 default.")],
    ("Desk audit", "Check one agent PC against the PDF.", ["Efficiency Mode", "USB headset", "Path is not cellular"], "The desk matches the support boundary."),
    ("Calls drop when the agent opens a second tab", "The softphone falls over only on Windows 11.", "TASK efficiency=on SYMPTOM drop-on-background-tab", ["Turn Efficiency Mode off", "Raise the abandon cap", "Change list penetration", "Delete the skill"], 0, "The PDF names this failure mode.", "Disable Efficiency Mode and keep a high-performance power plan if you cannot."),
    ["Apply the workstation rules", "Quote the bandwidth table, not a guess"], uncertain=["Headset model numbers are not listed in the section this lab read. The PDF points at a separate recommended-headsets note."]))

    rows.append(L("l07", "Reason codes, voicemail, and what admin is not", "practice", [
        "Not every silence is a carrier failure. Agents have Not Ready states. TCPA manual touch even forces Not Ready when preview time expires. Skill groups can hold voicemail, greetings, and messages. Those are administrator objects with their own reports.",
        "Admin work does not include inventing a dialer ratio in a spreadsheet and calling it the Five9 algorithm. The dialer has documented modes and a documented abandon window. Configuration belongs in the campaign, not in a side file.",
    ], [SKILLS, TCPA()], compare("Admin objects vs guesses", "Configure the object that exists.", "Real objects", ["Skill voicemail", "Not Ready", "Profiles", "Scripts"], "Not an admin object", ["A homemade abandon formula", "A CUCM partition", "A pasted TCPA number"]),
    "A message lands on a skill", ["Caller", "Skill", "Supervisor"], [
        ("Caller", "Queue", "The caller chooses voicemail or times out.", "queue"),
        ("Skill", "Mailbox", "The skill group receives the message.", "box"),
        ("Skill", "Greeting", "The greeting is the skill audio, not the campaign prompt.", "greeting"),
        ("Supervisor", "Listen", "Someone with access works the message.", "listen"),
        ("Agent", "Not Ready", "A preview timeout can force this state.", "not ready"),
        ("Admin", "Report", "Look at skill and agent reports before the trunk.", "report"),
    ], [
        ("Skill groups can receive", ["Only live calls", "Voicemail as well, with greetings", "Only emails", "Only 911"], 1, "The skill topic covers voicemail routing, messages, and greetings."),
        ("TCPA preview timeout sets the agent to", ["Ready", "Not Ready, and does not auto-dial", "On a SIP trunk", "In a report only"], 1, "The TCPA article says the status becomes Not Ready and no external number is auto-dialed."),
        ("A homemade pacing spreadsheet is", ["The Five9 dialer", "Not the product. Modes and abandon windows are campaign settings", "Required by RFC 3261", "The campaign profile"], 1, "Keep the dialer settings in the campaign."),
        ("Campaign profiles control pop-up windows. True or false?", ["False", "True. The profile topic includes pop-up control", "Only for Java", "Only for 911"], 1, "Profiles control pop-ups, list filter and sort, and disposition counts."),
        ("Service level targets for a skill are", ["Absent", "Part of the skill group topic", "A codec setting", "A JRE setting"], 1, "The skill topic includes service levels."),
    ], [("Skill voicemail?", "Yes, with its own greeting."), ("TCPA timeout state?", "Not Ready, no auto-dial."), ("Where do dialer settings live?", "On the campaign, not in a side spreadsheet."), ("Profiles and pop-ups?", "Profiles can control them.")],
    ("Separate the piles", "List one voicemail task, one Not Ready cause, and one setting you will not fake.", ["Skill greeting", "TCPA timeout", "Abandon cap stays in the campaign"], "Three different piles."),
    ("Voicemail greeting is the campaign prompt", "After hours, callers hear the daytime IVR prompt on the skill mailbox.", "SKILL Billing greeting=unset PLAY prompt=daytime", ["The skill greeting was never recorded", "The abandon window is 30 days", "WSS failed", "The list is vertical"], 0, "Skill audio is separate.", "Record the skill greeting."),
    ["Treat voicemail as a skill object", "Keep dialer math in the campaign"], href="#/pacing"))
    return track("t02", "VCC administration", "VCC admin", "Clients, permissions, skills, prompts, DNC, and the PCs that drop calls.", "Platform", "Foundation", "The administrator console is where the domain becomes a floor people can work.", rows)

def TCPA():
    from curriculum_lib import TCPA as SRC
    return SRC
