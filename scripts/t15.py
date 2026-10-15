from curriculum_lib import PLAN, SKILLS, INBOUND, MODULES, DIALER, OUTBOUND, SIP, TECH, E911, RETAIN, RFC3261, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "There is no import button", "foundation", [
        "This track is a teaching bridge. Five9's public pages name Cisco as a SIP gateway type. They do not publish a wizard that reads a UCCX script or a UCCE dial plan and emits a domain.",
        "The planning order still applies on the Five9 side: skills, users, lists, dispositions, profiles, then campaigns. A cutover that starts by 'moving the script' skips the objects the script will name.",
    ], [PLAN, SIP, TECH], compare("What you can cite", "Keep the bridge in its own column.", "Five9 documents", ["Planning order", "Cisco as a gateway type", "Campaign types: inbound, outbound, autodial"], "This lab's bridge", ["No official UCCX importer found", "Object names are a teaching map", "Marked uncertain on purpose"]),
    "A stakeholder wants a migration tool", ["Search", "Order", "Say"], [
        ("Search", "Docs", "You look for an official importer and do not find one to cite.", "search"),
        ("Order", "Plan", "The Five9 planning order is the build.", "plan"),
        ("Say", "Bridge", "You call the mapping a teaching bridge.", "bridge"),
        ("Say", "Gateway", "Cisco in the SIP chapter is a gateway.", "gw"),
        ("Admin", "Types", "Campaign types stay inbound, outbound, and autodial.", "types"),
        ("Admin", "No", "Blended is not introduced as a fourth campaign type.", "blend"),
    ], [
        ("This lab found an official UCCX-to-VCC importer. True or false?", ["True", "False", "True for IVR only", "True for lists only"], 1, "No such wizard is cited here."),
        ("Cisco in the technical requirements is", ["A script importer", "A gateway type, with Avaya and Asterisk", "A report layout", "A skill level"], 1, "Gateway type."),
        ("The first Five9 objects are", ["The old UCCX script file", "Skills, users, lists, dispositions, profiles", "Equinix edges", "Headsets"], 1, "The planning topic."),
        ("Blended is", ["A fourth campaign type", "Staffing language on the product pages", "A SIP port", "A retention clock"], 1, "Campaign types remain three."),
        ("You should label the object map as", ["A Five9 SKU", "A teaching bridge, uncertain where it is only ours", "An RFC", "A codec"], 1, "Honesty is the point of this track."),
    ], [("Official importer?", "None cited here."), ("Cisco in the PDF?", "A gateway type."), ("Build order?", "Skills through profiles, then campaigns."), ("Blended?", "Not a fourth campaign type.")],
    ("Say what the project is", "Write one sentence that refuses an importer and names the planning order.", ["No wizard", "Six layers", "Gateway versus script"], "The sentence would survive a documentation review."),
    ("The plan says 'export the .aef and import it Friday'", "There is no cited importer, and the domain has no skills yet.", "PLAN import=aef skills=0", ["Build the Five9 objects, then recreate the call flow", "Rename the file to .json", "Point the CUBE at a partition", "Skip dispositions"], 0, "The script names objects that do not exist yet.", "Follow the planning order."),
    ["Call this track a teaching bridge", "Start from the Five9 planning order"], uncertain=["Five9 publishes Cisco as a SIP gateway type. This lab did not find an official UCCX or UCCE migration wizard. Mappings below are instructional."]))
    R.append(L("l02", "CSQs, skills, and the partition you will not find", "practice", [
        "In this teaching map, a UCCX contact service queue is closest to a Five9 skill group: the people who can take that work. A UCCE skill group is a similar idea with a different name. Precision queues and attributes do not have a one-field equivalent you should invent.",
        "Five9 does not use CUCM partitions or calling search spaces. The boundary is the domain. If two businesses must not share lists, they are two domains, not two partitions.",
    ], [SKILLS, PLAN], stack("Teaching map, people and boundaries", "Left side is Cisco vocabulary. Right side is what you configure.", ["CSQ or skill group → Five9 skill group", "Agent team membership → user on that skill", "Partition → not present", "Separate tenants → separate domains"]),
    "An agent never gets the queue", ["UCCX", "Five9", "Boundary"], [
        ("UCCX", "CSQ", "The old queue name is written down.", "csq"),
        ("Five9", "Skill", "A skill group with the same job is created.", "skill"),
        ("Five9", "User", "The agent is on that skill.", "user"),
        ("Boundary", "Domain", "The user is in the right domain.", "dom"),
        ("Boundary", "No CSS", "Nobody hunts for a calling search space.", "nocss"),
        ("Admin", "Attributes", "Precision attributes are redesigned, not pasted.", "attr"),
    ], [
        ("The closest teaching map for a CSQ is", ["A campaign profile ANI", "A skill group", "A DID retention timer", "A matrix report"], 1, "People who can take the work."),
        ("CUCM partitions exist in Five9 admin as", ["A required tab", "They do not. The domain is the boundary", "Skill levels", "IVR modules"], 1, "Do not look for a partition table."),
        ("Two companies that must not share lists need", ["Two partitions in one domain", "Two domains", "Two ANIs only", "Two headsets"], 1, "Lists do not cross domains."),
        ("A precision-queue attribute string can be pasted into a skill name. True or false?", ["True", "False. Redesign it. Do not invent a field", "True for autodial", "True in Studio"], 1, "No one-field equivalent is cited."),
        ("A user may be on", ["Only one skill", "More than one skill group", "Skills only if they are reporting users", "No skills, ever"], 1, "The skill topic allows multiple skill groups."),
    ], [("CSQ maps toward?", "A skill group, as a teaching map."), ("Partitions?", "Not in Five9. Use domains."), ("Two tenants?", "Two domains."), ("Precision attributes?", "Redesign, do not invent a paste field.")],
    ("Map three queues", "Write three CSQ names and the skill groups you would create. Mark one attribute-based queue as a redesign.", ["Three skills", "One redesign", "The domain boundary"], "You did not draw a partition."),
    ("Calls hit Default because the CSQ name was typed into an ANI field", "The skill was never created.", "SKILL missing ANI=Billing", ["Create the skill and put the agents on it", "Add a partition", "Change G.711", "Extend DID retention"], 0, "The people were never attached.", "Create the skill group."),
    ["Map a CSQ to a skill group", "Drop partitions from the design"], uncertain=["The CSQ-to-skill mapping is a teaching bridge, not a Five9 migration utility."]))
    R.append(L("l03", "Scripts are rebuilt in modules", "practice", [
        "A UCCX script is a document in Cisco's editor. A Five9 IVR script is a chain of modules from the IVR Administrator's Guide: Menu, Get Digits, If/Else, Skill Transfer, Play, and the rest of that chapter. The lab's builder speaks those names and exports a learning JSON that VCC will not import.",
        "Time-of-day branches, a language prompt, and a transfer to a skill are the usual bones. Rebuild them. Do not hex-edit the old file.",
    ], [MODULES, INBOUND], path("Rebuild, do not convert", "Each Cisco step becomes a named module.", ["Greeting → Play", "Menu → Menu or Get Digits", "Decision → If/Else or Case", "Queue → Skill Transfer"]),
    "The old script has four boxes", ["Read", "Module", "Test"], [
        ("Read", "Boxes", "The Cisco flow is listed in plain language.", "read"),
        ("Module", "Play", "The greeting is a Play module.", "play"),
        ("Module", "Menu", "The menu is a Menu.", "menu"),
        ("Module", "If", "The hours check is If/Else or Case.", "if"),
        ("Module", "Skill", "The queue is a Skill Transfer with one skill.", "skill"),
        ("Test", "Export", "The learning export is labeled as not a VCC file.", "export"),
    ], [
        ("A UCCX .aef opens in the Five9 IVR editor. True or false?", ["True", "False", "True if renamed", "True for Menu only"], 1, "Rebuild it."),
        ("A spoken greeting becomes", ["A skill group", "A Play module", "An ANI", "A report layout"], 1, "Play is the module."),
        ("A queue handoff becomes", ["Skill Transfer", "Set DNC", "A partition", "Web2Campaign automatically"], 0, "Skill Transfer."),
        ("The lab builder's JSON is", ["A VCC import file", "A learning model", "A SIP trunk", "A retention export"], 1, "The builder says so."),
        ("Hours of operation belong in", ["The headset", "If/Else or Case, then the right branch", "The abandon percentage", "RFC 1918"], 1, "A decision module."),
    ], [("Import the .aef?", "No."), ("Greeting?", "Play."), ("Queue?", "Skill Transfer."), ("Builder JSON?", "Learning model only.")],
    ("Rewrite four boxes", "Turn a greeting, a menu, an hours check, and a queue into module names.", ["Play", "Menu", "If/Else", "Skill Transfer"], "You can point at each module in the builder."),
    ("Cutover morning, the script field is empty", "The file was copied and never rebuilt.", "IVR script=empty file=old.aef", ["Build the module chain and assign it", "Rename the extension", "Increase lines per agent", "Disable TLS"], 0, "The campaign has nothing to run.", "Assign a real script."),
    ["Rebuild flows as named modules", "Treat the builder export as a study file"], href="#/ivr", uncertain=["Module mapping from UCCX steps is instructional. Validate every script in a domain."]))
    R.append(L("l04", "Dialing modes do not survive the move by osmosis", "advanced", [
        "UCCE outbound has its own pacing words. Five9's product pages talk about Preview, Progressive, Power, Predictive, and Manual Touch. The simulator in this lab is a classroom clock, not either vendor's algorithm.",
        "Progressive on the outbound product page is one call per available agent. The dialer page also describes an adaptive pace and a smaller team. Quote the page you mean. Do not copy a Cisco lines-per-port number into Max Abandoned Call Percentage. This lab does not state a numeric default for that field.",
    ], [DIALER, OUTBOUND], compare("Leave Cisco's ratio behind", "Re-choose the mode in Five9's words.", "Do not copy", ["A UCCE port ratio", "A guessed abandon percent", "This lab's simulator as production"], "Do choose", ["A named Five9 mode", "The campaign dialog as the record", "TCPA manual touch when required"]),
    "The old campaign was 'predictive'", ["Name", "Size", "Record"], [
        ("Name", "Mode", "The Five9 mode is chosen by its product definition.", "mode"),
        ("Size", "Team", "The team size is compared with the guidance you are quoting.", "size"),
        ("Record", "Dialog", "The campaign dialog is the system of record.", "dialog"),
        ("Record", "Sim", "The simulator is labeled a classroom.", "sim"),
        ("Admin", "Abandon", "No numeric default is invented.", "abd"),
        ("Admin", "TCPA", "Manual touch is selected only where that control is required.", "tcpa"),
    ], [
        ("Five9 mode names on the product pages include", ["CSQ, precision, partition", "Preview, progressive, power, predictive, manual touch", "Only blended", "Only G.711"], 1, "Those are the product words."),
        ("This lab's pacing simulator is", ["The Five9 source code", "A teaching model", "A UCCE port calculator", "A report"], 1, "It is labeled as a classroom."),
        ("A Cisco lines-per-port figure should be typed into Max Abandoned Call Percentage. True or false?", ["True", "False", "True if the team is under 10", "True for preview"], 1, "Different fields."),
        ("This lab states Five9's numeric abandon default. True or false?", ["True", "False. It was not in the pages we quoted", "True, it is 3", "True, it is 0"], 1, "Do not invent it."),
        ("Progressive wording differs across two Five9 pages. You should", ["Average them", "Quote the page you mean and mark the tension", "Ignore both", "Use the simulator's math"], 1, "The outbound page and the dialer page are not identical."),
    ], [("Mode names?", "Preview, progressive, power, predictive, manual touch."), ("Simulator?", "A teaching model."), ("Copy the Cisco ratio into abandon %?", "No."), ("Numeric default?", "Not stated here.")],
    ("Re-choose a mode", "Pick a Five9 mode for a ten-agent team and write which page you are quoting.", ["Mode", "Page", "What you will not copy"], "You left the Cisco ratio out."),
    ("Abandon rate spikes because the old port ratio was pasted into lines per agent", "Power dialing is not a Cisco port group.", "MODE power lines=copied", ["Set the Five9 mode from its own definition and watch the abandon field", "Paste a second ratio", "Delete DNIS", "Turn off recording notice"], 0, "The fields do not mean the same thing.", "Reconfigure from the Five9 dialog."),
    ["Choose a Five9 mode by its own definition", "Keep the simulator in the classroom"], href="#/pacing", uncertain=["The dialer product page and the outbound product page describe progressive pacing in different words. Quote the page you use."]))
    R.append(L("l05", "Numbers, lists, and ANI are a data project", "practice", [
        "DNIS values, calling lists, dispositions, and do-not-call entries are domain data. They are not inside the Cisco script file. A cutover that moves only the IVR still has nothing to dial and nowhere legal to send a call.",
        "Campaign profiles hold the ANI override. Local ANI is not the Certified Caller program. If the old system presented a specific caller ID, create the profile and assign it in Advanced mode, then ask separately whether attestation is in scope.",
    ], [PLAN, INBOUND, RETAIN], path("Data that must exist on cutover morning", "The script cannot invent these.", ["DNIS on a running inbound campaign", "Lists actually loaded", "Dispositions and DNC", "One profile, assigned"]),
    "The first live hour", ["Voice", "Data", "ID"], [
        ("Voice", "Run", "The inbound campaign is running.", "run"),
        ("Data", "List", "The outbound list is loaded, not emailed.", "list"),
        ("Data", "DNC", "Do-not-call entries were loaded.", "dnc"),
        ("ID", "Profile", "The ANI profile is assigned.", "ani"),
        ("ID", "Attest", "Certified Caller is a separate question.", "attest"),
        ("Admin", "Clock", "Old domain DIDs follow the retention clock if a Five9 domain is closing.", "clock"),
    ], [
        ("A UCCX script file contains the Five9 list. True or false?", ["True", "False", "True for DNC", "True for ANI"], 1, "Lists are domain data."),
        ("ANI override lives on", ["The headset", "The campaign profile", "The matrix layout", "RFC 4733"], 1, "Profiles override defaults such as ANI."),
        ("Local ANI and Certified Caller are", ["The same project", "Different. Attestation is separate", "Both a CSQ", "Both a codec"], 1, "Do not conflate them."),
        ("An inbound campaign that is not running", ["Plays the new script anyway", "Does not answer. Callers can hear busy", "Uses the old CUCM partition", "Exports a CSV"], 1, "Start it."),
        ("DIDs after a Five9 domain closes are kept", ["Forever", "90 days, per the retention page", "Until the Cisco license expires", "60 days of agent data only"], 1, "90 days."),
    ], [("Lists in the script file?", "No."), ("ANI lives on?", "The campaign profile."), ("Certified Caller?", "A separate project."), ("Stopped inbound?", "Does not answer.")],
    ("Pack the data", "List the files you will load before the DNIS is pointed over.", ["Lists", "DNC", "Dispositions", "ANI profile"], "The IVR is not the only artifact."),
    ("Outbound dials and the caller ID is the platform default", "The profile was created and never assigned.", "PROFILE built assigned=no", ["Assign it in Advanced mode", "Import the .aef again", "Add a partition", "Change the report to matrix"], 0, "A profile that is not selected does nothing.", "Assign it."),
    ["Load lists, DNC, and dispositions as data", "Assign the ANI profile"]))
    R.append(L("l06", "The gateway cut, without pretending to be the CUBE guide", "advanced", [
        "When the third SIP story is a Cisco gateway, the technical requirements are still the Five9 side: DNS SRV preferred, G.711 as the default codec, TLS 1.2, no double NAT. What the gateway itself must rewrite — number format, a normalization script, early media — lives in Cisco's documentation.",
        "Practitioner notes often mention G.711 at 20 ms, NANP versus E.164, and 'do not send internal extensions.' Treat every one of those as uncertain until the trunk guide you and the carrier signed actually says them. RFC 3261 tells you what an INVITE is. It does not choose your dial plan.",
    ], [TECH, SIP, RFC3261], compare("Two vendors at the border", "Do not let one document speak for the other.", "Five9 requirements", ["SRV", "G.711 default", "TLS 1.2", "No double NAT"], "Confirm on the gateway", ["Number format", "Packet time", "Which numbers are allowed"]),
    "The first INVITE fails", ["Five9", "Gateway", "Plan"], [
        ("Five9", "Story", "The path is the Cisco gateway story, not the ITSP story.", "story"),
        ("Five9", "TLS", "TLS 1.2 is offered.", "tls"),
        ("Gateway", "Format", "The called number matches what the DNIS table expects.", "fmt"),
        ("Gateway", "Ext", "Internal extensions are not assumed to be public DNIS.", "ext"),
        ("Plan", "Uncertain", "20 ms and E.164 rules are marked until the guide says them.", "unc"),
        ("Admin", "RFC", "You can name RFC 3261 without pretending it is a dial plan.", "rfc"),
    ], [
        ("A failed INVITE is always a Five9 defect. True or false?", ["True", "False. The gateway and the number plan are in the path", "True if G.711 is on", "True for preview"], 1, "Both sides have a job."),
        ("Internal extensions should be assumed to be Five9 DNIS values. True or false?", ["True", "False. Confirm the numbering plan", "True for E911", "True in a matrix report"], 1, "That assumption is a common failure, and it is not a Five9 default this lab can cite."),
        ("20 ms ptime is", ["Quoted from the Five9 PDF here", "A practitioner note, uncertain", "The abandon window", "Required by RFC 3261"], 1, "Do not attribute it to the PDF."),
        ("DNS guidance on the Five9 side is", ["NetBIOS", "SRV preferred", "A hosts file on every phone", "Optional and discouraged"], 1, "SRV."),
        ("RFC 3261 replaces your dial plan. True or false?", ["True", "False", "True for UCCX", "True for skills"], 1, "It is the SIP specification."),
    ], [("INVITE failures?", "Check both sides."), ("Extensions as DNIS?", "Do not assume it."), ("20 ms?", "Uncertain practitioner note."), ("SRV?", "Preferred on the Five9 side.")],
    ("Write the border", "Two columns: what the Five9 PDF says, and what you still must confirm on the gateway.", ["Four PDF facts", "Three open gateway questions"], "The second column is labeled unconfirmed."),
    ("Calls fail with a number that still has a site code prefix", "The gateway is sending a private plan the DNIS table does not contain.", "INVITE to=8-8005550101 dnis=8005550101", ["Normalize to the DNIS that exists, after the guide says how", "Add the site code as a skill", "Switch to matrix reports", "Disable G.711"], 0, "The digits do not match.", "Fix the called number, with the gateway guide open."),
    ["Keep Five9 requirements and gateway chores in two columns", "Do not cite a Cisco example as a Five9 default"], uncertain=["NANP versus E.164, 20 ms ptime, and 'no internal extensions' are practitioner cautions. They are not quoted here as Five9 requirements."]))
    R.append(L("l07", "Cutover morning is a checklist, not a mood", "practice", [
        "The morning the numbers move, the domain should already contain skills, a script, a running inbound campaign, loaded lists, dispositions, DNC, an assigned profile, and a desktop the agent has signed into. E911 addresses have to be dispatchable for the place the agent actually is. A stale office address is not a courtesy.",
        "Keep a backout that does not depend on a disabled Five9 domain's DIDs surviving past their retention window. Test one DNIS, one outbound record, one pop, and one 911 procedure in the lab domain before the carrier repoints the range.",
    ], [PLAN, INBOUND, E911, RETAIN, TECH], stack("Before the carrier repoints", "Each line is a go or a stop.", ["Skills and users exist", "Script assigned", "Inbound campaign running", "Lists, DNC, dispositions loaded", "Profile assigned", "Desktop signed in", "E911 address is the real one"]),
    "Go or stop", ["Voice", "Data", "Safety"], [
        ("Voice", "DNIS", "One test DNIS answers.", "dnis"),
        ("Data", "List", "One outbound record dials under the chosen mode.", "list"),
        ("Data", "Pop", "The adapter or connector you promised actually opens.", "pop"),
        ("Safety", "E911", "The address is dispatchable for that agent.", "e911"),
        ("Safety", "Backout", "The old path still works if this test fails.", "back"),
        ("Admin", "Stop", "Any red line stops the repoint.", "stop"),
    ], [
        ("A busy test DNIS on cutover morning most often means", ["Certified Caller failed", "The inbound campaign is not running", "The matrix will not export", "Wireless headsets are ideal"], 1, "Start the campaign."),
        ("E911 addresses should describe", ["The data center you like", "The dispatchable location of the agent", "The Equinix code", "The ANI profile"], 1, "The data sheet is about dispatchable location."),
        ("You should repoint every number before one test call. True or false?", ["True", "False", "True if the .aef copied", "True at night only"], 1, "Test one path first."),
        ("A backout that depends on a closed domain's DIDs ignores", ["The retention clock", "RFC 4733 only", "The theme", "Skill tabs"], 0, "Numbers do not wait forever."),
        ("The desktop pop is in the cutover test because", ["Voice implies the screen", "Voice and the adapter fail separately", "It sets G.711", "It creates partitions"], 1, "Test the screen."),
    ], [("Busy DNIS?", "Campaign not running."), ("E911 address?", "Where the agent is."), ("Test one path first?", "Yes."), ("Why test the pop?", "It is a separate channel.")],
    ("Write the go/no-go", "Seven lines, each with a name who will check it.", ["Voice", "Data", "Screen", "E911"], "A failed line is a stop."),
    ("All numbers moved, then 911 would have shown the empty HQ", "Agents are at home and the location was never updated.", "E911 loc=HQ agents=home", ["Stop and register dispatchable locations", "Increase predictive lines", "Import the .aef", "Change the report layout"], 0, "The data sheet and the EULA both treat a wrong address as a failed emergency call.", "Fix locations before you call this done."),
    ["Run one DNIS, one dial, one pop, one location", "Stop the repoint when any line fails"], uncertain=["This checklist is a teaching bridge for cutover discipline. It is not an official Five9 UCCE runbook."]))
    return track("t15", "From UCCX and UCCE", "Migration", "A teaching bridge: skills, modules, modes, data, the gateway, and a go/no-go that can stop.", "Bridge", "Advanced", "There is no import button. Rebuild the domain, then move a number.", R)
