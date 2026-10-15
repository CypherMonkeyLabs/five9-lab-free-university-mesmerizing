from curriculum_lib import DIALER, OUTBOUND, DEFAULTS, TCPA, DIALTEST, lesson, compare, stack, path, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "Preview lets the agent read first", "foundation", [
        "Preview delivers the contact and, on the product page, CRM history before the call is placed. It is the mode for conversations that need context. It does not overdial, so abandon from extra ringing lines is not the design.",
        "The product page's Manual Touch mode goes further and removes automated dialing. Preview itself can still place the call after the agent has seen the record. Do not describe preview and TCPA manual touch as the same switch.",
    ], [DIALER, OUTBOUND, TCPA], path("Preview", "See the record, then one call.", ["Record pops", "Agent reads", "One dial", "Talk or disposition"]),
    "One preview cycle", ["Dialer", "Agent"], [
        ("Dialer", "Offer", "The next record is delivered.", "record"),
        ("Agent", "Read", "History is on screen before dial.", "read"),
        ("Agent", "Dial", "One call goes out for that agent.", "one"),
        ("Dialer", "Connect", "A live answer reaches that agent.", "live"),
        ("Agent", "Code", "A disposition decides the next try.", "code"),
        ("Dialer", "Next", "Another record waits until an agent is free.", "next"),
    ], [
        ("Preview is aimed at", ["Maximum overdial", "Reading the relationship before the call", "911 location", "Matrix exports"], 1, "The product page says agents get customer history before dialing."),
        ("Preview and TCPA manual touch are", ["Identical", "Related, but manual touch removes automatic dialing", "Both inbound types", "Both codecs"], 1, "Manual touch is the stricter mode."),
        ("Abandon caused by extra lines is", ["The point of preview", "Not the preview design, because you do not stack lines per agent", "Required by the FTC page in this lab", "A skill setting"], 1, "Preview is one record in front of an agent."),
        ("CRM history on the product page is", ["Hidden until wrap", "Part of why you pick preview", "Illegal", "A JRE feature"], 1, "The dialer page says preview provides CRM history before dialing."),
        ("A preview campaign still needs", ["No list", "A list, a running campaign, and agents", "Only a DNIS", "Only WEM"], 1, "It is an outbound mode."),
    ], [("Why preview?", "Context before the dial."), ("Same as TCPA?", "No. TCPA removes automatic dialing."), ("Overdial?", "Not the design."), ("Still needs a list?", "Yes.")],
    ("When to pick it", "Name two campaigns that should be preview and one that should not.", ["A retention save", "A complaint callback", "A huge identical reminder"], "The reminder is not preview."),
    ("Agents dial blind", "The mode is power and the CRM pop never arrives before the beep.", "MODE power POP after-connect", ["Move that book to preview if they must read first", "Raise lines per agent", "Stop inbound", "Disable reports"], 0, "Power will not wait for a reading.", "Use preview for that book."),
    ["Choose preview for context", "Separate it from TCPA"], href="#/pacing"))

    R.append(L("l02", "Progressive keeps one call per free agent", "practice", [
        "The outbound product page says progressive dialing automatically dials one customer per available agent and is what centers use when they want to avoid dropped outbound calls. The dialer product page also says progressive is appropriate when fewer than 10 agents are active, and that it adapts pace to campaign performance.",
        "Those two sentences are both public and they are not the same sentence. One says one call per available agent. The other says the pace adapts. Reconcile them in the admin UI of your domain. This lab's simulator uses the one-call reservation so you can see abandon stay near zero.",
    ], [OUTBOUND, DIALER], compare("Two public sentences", "Read both before you argue.", "Outbound page", ["One customer per available agent", "Used to avoid dropped calls"], "Dialer page", ["Adapts pace", "Fewer than 10 active agents as guidance"]),
    "A free agent", ["Agent", "Dialer"], [
        ("Agent", "Free", "The agent is available.", "free"),
        ("Dialer", "One", "One number is placed for that agent.", "one"),
        ("Dialer", "Reserve", "The agent is not offered a second line.", "reserve"),
        ("Dialer", "Miss", "No answer releases the agent.", "miss"),
        ("Dialer", "Hit", "A live person is connected.", "hit"),
        ("Agent", "Talk", "Occupancy rises without an abandon pile.", "talk"),
    ], [
        ("The outbound page's progressive rule of thumb is", ["As many lines as possible", "One customer per available agent", "TCPA typing", "A stopped campaign"], 1, "That page says one customer per available agent."),
        ("The dialer page's staffing hint is", ["More than 100 agents", "Fewer than 10 active agents", "Zero agents", "Only supervisors"], 1, "It says progressive is appropriate when fewer than 10 are active. Treat it as guidance, not a hard block."),
        ("Why abandon stays low in the one-call design", ["Lines are stacked", "A live answer has the agent who was reserved", "Calls are inbound", "ANI is local"], 1, "You do not create an extra live answer with nobody to take it."),
        ("The two product sentences", ["Contradict in a way you should notice and then check in the UI", "Are a SIP spec", "Replace the admin guide", "Set the JRE"], 1, "One-call and adaptive pace need a look in the domain."),
        ("This lab's pacing chart for progressive is", ["Five9 source code", "A teaching model of the one-call description", "A legal opinion", "A report export"], 1, "The simulator is labeled as a lab model."),
    ], [("One per agent?", "That is the outbound page."), ("Ten-agent hint?", "Dialer page guidance, not a proven hard limit."), ("Why low abandon?", "The agent is reserved."), ("Simulator?", "Teaching model.")],
    ("Run progressive", "Open the pacing bench, pick Progressive, and watch abandon.", ["Set 8 agents", "Set a 30 percent live rate", "Note abandon versus predictive"], "Abandon stays near zero while predictive can climb."),
    ("Dropped calls on a 'progressive' campaign", "The campaign is actually power with three lines per agent.", "MODE power lines=3 LABEL on-whiteboard=progressive", ["Change the campaign mode. The whiteboard was wrong", "Add more lines", "Stop all inbound forever", "Delete ANI"], 0, "The mode in the campaign is the mode that dials.", "Set progressive if one call per agent is the requirement."),
    ["Quote the one-call sentence", "Check the other sentence in the UI"], uncertain=["Five9 publishes both 'one customer per available agent' and 'adaptively control dialing pace' for progressive. This lab does not know which sentence the current build implements."], href="#/pacing"))

    R.append(L("l03", "Power dials a ratio you chose", "practice", [
        "The dialer page says power dials a user-configured number of calls per available agent and adjusts from abandon rates. It points that mode at a small group with a large list. The outbound page says the same shape: a small sales team and a large prospect list.",
        "Because you choose the lines, you can create live answers with no agent. The abandon cap and the warning on the default-settings page are the brakes. The simulator lets you move lines per agent and watch the amber abandon line.",
    ], [DIALER, OUTBOUND, DEFAULTS], stack("Power", "You set the ratio. The abandon monitor is the brake.", ["Lines per free agent", "Live answers", "Idle agents", "Abandon versus cap"]),
    "Three lines, two agents", ["Dialer", "Caller", "Agent"], [
        ("Dialer", "Place", "Several calls go out per free agent.", "place"),
        ("Caller", "Live", "Two people answer.", "live"),
        ("Agent", "One", "Only one agent is free.", "one"),
        ("Caller", "Drop", "The extra live answer is an abandon.", "drop"),
        ("Dialer", "Brake", "The abandon monitor pulls the ratio down.", "brake"),
        ("Admin", "Cap", "The cap is a campaign default with a warning if you move it.", "cap"),
    ], [
        ("Who configures the power ratio?", ["The carrier", "The administrator, as calls per available agent", "The IVR Menu", "RedSky"], 1, "The dialer page says user-configured."),
        ("Power is marketed for", ["A hundred agents and a tiny list", "A small team and a large list", "Inbound only", "E911 only"], 1, "Both product pages describe a small team and a large volume."),
        ("An extra live answer with no agent is", ["A connect", "An abandon", "A skill greeting", "A profile filter"], 1, "That is the drop you are trading for speed."),
        ("The abandon brake is documented as", ["A secret", "Monitor and max abandoned call percentage, with a warning if you change the max", "A JRE flag", "A headset button"], 1, "Default settings name those fields."),
        ("This lab prints the vendor's numeric default cap as", ["3 percent", "It does not. Read your domain", "0 percent", "50 percent"], 1, "The preset is real and it can differ. Do not copy a number from memory."),
    ], [("Who sets the ratio?", "The administrator."), ("Who is it for?", "Small team, large list."), ("Extra live answer?", "An abandon."), ("Where is the brake?", "Abandon monitor and max percent.")],
    ("Move the ratio", "In the simulator, compare 1.0 and 3.0 lines.", ["Watch abandon", "Watch occupancy", "Write which one you would sign"], "You can explain the trade."),
    ("Abandon alarm on a five-person sales pod", "Power is set to four lines and the cap warning was clicked through.", "MODE power lines=4 WARN=dismissed", ["Lower the lines and read the warning", "Add lines", "Switch the list to inbound", "Disable call analysis by habit"], 0, "The ratio is above what the pod can answer.", "Drop the lines or move to progressive."),
    ["Set a power ratio on purpose", "Treat the abandon warning as a brake"], href="#/pacing"))

    R.append(L("l04", "Predictive fills idle time, and it can drop calls", "advanced", [
        "The dialer page says predictive mode uses algorithms to predict agent availability and is suited to more than 10 active agents. The outbound page says it increases time spent talking to people instead of dialing. Both are marketing descriptions of an overdial.",
        "The default-settings topic is the control room: monitor abandoned call percentage, a max percentage, a warning if you change the max, 30 rolling days on US domains, and 24 hours on UK domains. A community test article says predictive throttles and does not necessarily lock to one-to-one, while other lines in that same article talk about dropping to one-to-one. Use the settings page as the control. Treat the test article as a field note with mixed wording.",
    ], [DIALER, OUTBOUND, DEFAULTS, DIALTEST], stack("Predictive controls you can cite", "The algorithm itself is not public source.", ["More than 10 agents, as guidance", "Abandon monitor", "Max percent with a warning", "30 days US or 24 hours UK"]),
    "The pacer overdials", ["Dialer", "Agent", "Caller"], [
        ("Dialer", "Predict", "It estimates who will be free.", "predict"),
        ("Dialer", "Extra", "It places more calls than idle agents.", "extra"),
        ("Caller", "Answer", "A live answer arrives.", "answer"),
        ("Agent", "Busy", "Nobody is free.", "busy"),
        ("Caller", "Drop", "That answer counts as an abandon.", "drop"),
        ("Dialer", "Window", "The US window is 30 days, not this chart's minute.", "window"),
    ], [
        ("Predictive staffing guidance on the dialer page is", ["Fewer than 2 agents", "More than 10 active agents", "Zero agents", "Only TCPA"], 1, "The page says best when more than 10 are active. It reads as guidance."),
        ("US abandon window in the admin topic is", ["24 hours", "Rolling 30 days", "1 hour", "A single call"], 1, "UK domains use 24 hours."),
        ("The community test article is", ["The source code", "A field note whose own wording is not uniform about one-to-one", "The E911 guide", "A Credly exam"], 1, "Do not treat one sentence in it as the algorithm."),
        ("This simulator's short window", ["Is the US legal window", "Is a classroom clock so you can see a throttle. Five9's US window is 30 days", "Replaces the warning", "Disables preview"], 1, "The bench says so on the page."),
        ("Changing the max abandon percent", ["Cannot warn you", "Can warn that you may leave compliance", "Deletes recordings", "Changes DNIS"], 1, "The default-settings topic shows that warning."),
    ], [("Ten-agent line?", "Dialer page guidance."), ("US window?", "30 days."), ("Test article?", "Mixed field note."), ("Simulator window?", "Not Five9's 30 days.")],
    ("Watch a throttle", "Run Predictive in the bench with 12 agents and a low live rate, then a high one.", ["Note abandon", "Note pace falling when abandon is high", "Write the real window next to the chart"], "You wrote 30 days, not the chart's minute."),
    ("A 12-person pod is in predictive and inbound at once", "Abandon climbs whenever inbound takes the same agents.", "MODE predictive SKILLS also=inbound ABANDON rising", ["Give predictive its own agents or expect the drops", "Ignore the 30-day window", "Type numbers faster", "Stop call recording"], 0, "The dialer page wants agents available to predict. Shared inbound steals them.", "Dedicate agents or move the book to progressive."),
    ["Explain predictive without claiming the source code", "Quote the 30-day and 24-hour windows"], uncertain=["The exact throttle curve is not specified on the default-settings page. The community test article disagrees with itself about an instant drop to 1:1."], href="#/pacing"))

    R.append(L("l05", "TCPA manual touch is a typed number", "advanced", [
        "TCPA manual touch exists only on domains enabled for it. The community article says those domains are generally for telemarketing to cell phones without express consent, and that no other dialing mode is available. Contacts are shown and not dialed. The agent must type the external number. Paste and drag-and-drop are not allowed. The Dial button enables when the typed number matches.",
        "Preview time still exists. If it expires, the agent goes Not Ready and nothing auto-dials. Dial Immediately and Dial Number are removed. The rule also covers click-to-dial, previews, and queue or voicemail callbacks. Internal speed dial and a third-party transfer do not make you retype. There is a permission to skip records.",
    ], [TCPA], stack("What the agent must do", "From the TCPA manual-touch article.", ["See the record", "Type the external number", "No paste", "Dial enables", "Timeout means Not Ready"]),
    "A cell number without consent", ["Record", "Agent", "Dialer"], [
        ("Record", "Show", "The number is visible and not dialed.", "show"),
        ("Agent", "Type", "Every digit is entered.", "type"),
        ("Agent", "Paste", "Paste is refused.", "paste"),
        ("Dialer", "Arm", "Dial enables on a match.", "arm"),
        ("Agent", "Wait", "Timeout sets Not Ready.", "timeout"),
        ("Dialer", "Still", "No external auto-dial on that timeout.", "still"),
    ], [
        ("TCPA manual touch is available", ["On every domain", "Only on domains enabled for it", "Only for inbound DNIS", "Only in Studio"], 1, "The article says the domain must be enabled, and other modes are not offered there."),
        ("Paste into the number field?", ["Allowed", "Not allowed", "Allowed for internal numbers only on external fields", "Allowed if the ANI is local"], 1, "The article forbids cut, paste, and drag-and-drop for the external number."),
        ("When does Dial enable?", ["Immediately", "After the external number is typed correctly", "After 30 days", "After a skill change"], 1, "The article says the button activates after a correct entry."),
        ("Preview timeout does what?", ["Auto-dials", "Sets Not Ready and does not auto-dial the external number", "Deletes the list", "Starts predictive"], 1, "That is the published timeout behavior."),
        ("Queue callbacks in this mode", ["Auto-dial", "Do not auto-dial", "Skip TCPA", "Require a JRE"], 1, "The article includes queue callbacks."),
    ], [("Where does the mode exist?", "Domains enabled for it, with no other mode."), ("Paste?", "Blocked."), ("Dial enables when?", "The typed number matches."), ("Timeout?", "Not Ready, no auto-dial.")],
    ("Type it", "On the pacing bench, type 8005550142. Try to paste.", ["Paste is blocked", "Dial stays disabled until the digits match", "You can say why"], "Dial armed only after typing."),
    ("Dial stays grey", "The agent pasted the number from the CRM screen.", "EVENT paste blocked BUTTON dial=disabled", ["Type the digits. Paste will not arm Dial", "Switch the domain to predictive quietly", "Lower abandon to zero", "Delete the skill"], 0, "Paste is refused on purpose.", "Type the number."),
    ["Enforce typed external dials", "Include callbacks in the rule"], href="#/pacing"))

    R.append(L("l06", "The defaults are the compliance posture", "advanced", [
        "For every dialing mode, the default-settings topic says options start at values Five9 recommends for FCC, FTC, and UK Ofcom telemarketing rules. If you change them you can see a warning. The example field is Max Abandoned Call Percentage.",
        "Other defaulted fields on that page include max queue time, the out-of-numbers alert, whether abandon percentage is monitored, call analysis, voice detection level, and the action when max queue time expires. Calculations differ for US and European domains. The topic tells you to refer to the current agency rules.",
    ], [DEFAULTS], stack("Defaulted fields you can name", "From the default campaign settings topic.", ["Max queue time", "Out-of-numbers alert", "Abandon monitor and max", "Call analysis", "Voice detection", "Queue-time action"]),
    "A warning appears", ["Admin", "Campaign"], [
        ("Admin", "Open", "Dialing options show the presets.", "open"),
        ("Admin", "Edit", "Max abandon is changed.", "edit"),
        ("Campaign", "Warn", "A compliance warning appears.", "warn"),
        ("Admin", "Read", "The warning is the point, not a nuisance dialog.", "read"),
        ("Admin", "Rule", "The agency text is outside the dialog.", "rule"),
        ("Admin", "Domain", "US 30 days versus UK 24 hours still applies.", "window"),
    ], [
        ("Defaults are there for", ["Headset color", "FCC, FTC, and Ofcom posture, per the topic", "Faster IVR", "Equinix SLAs"], 1, "The topic names those regulators."),
        ("The example warning field is", ["ANI", "Max Abandoned Call Percentage", "Skill name", "Prompt file"], 1, "That is the example in the topic."),
        ("Out of numbers alert is", ["Not a setting", "One of the defaulted fields", "A codec", "A Credly item"], 1, "It is in the list."),
        ("European versus US math", ["Is identical", "Differs. The topic says so, and names 30 days versus 24 hours for abandon", "Is illegal to mention", "Depends on the headset"], 1, "Do not assume one window worldwide."),
        ("This lab's job when you want a new cap is", ["Invent 3 percent", "Send you to the live default and the current rule", "Disable monitoring", "Switch to TCPA without a reason"], 1, "The number in the domain wins."),
    ], [("Why defaults?", "A stated compliance posture."), ("Example warning?", "Max abandon percent."), ("US vs UK?", "30 days vs 24 hours."), ("Where is the legal text?", "The agency rule, not this lab.")],
    ("Screenshot the warning", "In a lab domain, start to change the max and read the dialog. Cancel.", ["Open dialing options", "Invoke the warning", "Cancel"], "Production is unchanged."),
    ("The warning was clicked through on every campaign", "Abandon monitor is off and nobody wrote down the rule they think they are meeting.", "MONITOR off MAX changed NOTE none", ["Turn monitoring back on and write the rule you rely on", "Hide the dialog in CSS", "Delete lists", "Use 5G agents"], 0, "The warning is the control.", "Restore the preset or document the current legal basis."),
    ["Name the defaulted fields", "Treat the warning as part of the design"]))

    R.append(L("l07", "Pick a mode in one page", "advanced", [
        "Use the person's job, not the logo. Context before the call is preview. A promise of no dropped calls and a small team is progressive. A small team and a huge list, with eyes on abandon, is power. A large team whose idle time is the enemy is predictive, with dedicated agents. A cell book without consent is TCPA manual touch, and only if the domain is enabled.",
        "The ten-agent lines on the dialer page are guidance from a product page. The abandon windows are admin-guide facts. The simulator is a classroom. Your domain's dialog is the system of record.",
    ], [DIALER, OUTBOUND, DEFAULTS, TCPA], compare("Mode picker", "Match the constraint.", "Constraint", ["Must read first", "Must not drop", "Small team, huge list", "Large team, fill idle", "No consent on cells"], "Mode", ["Preview", "Progressive", "Power", "Predictive", "TCPA manual touch"]),
    "Five requests", ["Request", "Mode"], [
        ("Request", "Save", "A banker must read the note.", "preview"),
        ("Request", "Careful", "Eight agents, no drops.", "progressive"),
        ("Request", "Blitz", "Four sellers, fifty thousand rows, watch abandon.", "power"),
        ("Request", "Floor", "Forty agents, outbound only.", "predictive"),
        ("Request", "Cell", "No express consent.", "tcpa"),
        ("Mode", "Write", "The abandon window goes in the design note.", "window"),
    ], [
        ("No express consent on cell phones points to", ["Predictive", "TCPA manual touch, on an enabled domain", "Inbound DNIS", "Vertical list mode"], 1, "That is the article's setting."),
        ("Forty dedicated agents and a goal of talk time point to", ["Preview for every row", "Predictive, with the abandon window understood", "A stopped campaign", "Voicemail Transfer"], 1, "That matches the product description, as guidance."),
        ("Eight agents who must not drop calls point to", ["Power at four lines", "Progressive", "TCPA paste", "Inbound busy"], 1, "The outbound page ties progressive to avoiding drops."),
        ("The system of record for the cap is", ["This simulator", "The campaign dialog in the domain", "A whiteboard", "A flashcard"], 1, "The bench is a teaching clock."),
        ("Dedicated agents matter for predictive because", ["Skills are optional", "The product story assumes it can predict their availability", "ANI changes", "Java requires it"], 1, "If inbound steals them, the prediction is wrong."),
    ], [("No consent?", "TCPA manual touch on an enabled domain."), ("Forty agents?", "Predictive, eyes open."), ("No drops, small team?", "Progressive."), ("System of record?", "The domain dialog.")],
    ("Five sticky notes", "Write the mode next to five real books your floor might run.", ["One preview", "One progressive", "One power or predictive with a reason"], "Each note names a constraint."),
    ("One mode for the whole domain", "A TCPA domain was asked to run predictive on a second campaign.", "DOMAIN tcpa MODES available=manual-touch only", ["Keep predictive off that domain", "Paste harder", "Rename the skill", "Stop reports"], 0, "The article says no other mode is available there.", "Use a domain that is allowed to predict, or stay on manual touch."),
    ["Match five constraints to five modes", "Keep TCPA domains pure"], href="#/pacing"))
    return track("t05", "Dialer modes and pacing", "Dialer", "Preview, progressive, power, predictive, and TCPA manual touch, with the abandon window kept honest.", "Voice", "Advanced", "Five modes. The simulator is a classroom. The campaign dialog is the system of record.", R)
