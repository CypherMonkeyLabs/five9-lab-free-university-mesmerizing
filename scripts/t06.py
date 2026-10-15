from curriculum_lib import OUTBOUND, PLAN, INBOUND, SKILLS, DIALER, DIALTEST, DISP, TCPA, DEFAULTS, lesson, compare, stack, path, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "Blended is a staffing plan", "foundation", [
        "The outbound product page says outbound works with inbound digital channels and that blended behavior lets agents move between inbound and outbound as inbound rises and falls. It does not add a campaign type named Blended to the planning roadmap.",
        "You blend by which skills an agent holds and which campaigns are running, not by a secret fourth object. If inbound and a predictive book share the same people, the dialer is predicting availability it does not have.",
    ], [OUTBOUND, PLAN, DIALER], compare("Words", "Use the page that defines the word.", "Product page", ["Agents move between inbound and outbound"], "Planning roadmap", ["Inbound, outbound, and autodial campaigns"]),
    "Inbound rises", ["Inbound", "Agent", "Outbound"], [
        ("Inbound", "Spike", "The queue grows.", "spike"),
        ("Agent", "Skill", "The same person holds the inbound skill.", "skill"),
        ("Agent", "Take", "They take the inbound call.", "take"),
        ("Outbound", "Miss", "A predictive book loses the agent it counted on.", "miss"),
        ("Outbound", "Drop", "A live answer can abandon.", "drop"),
        ("Agent", "Plan", "Dedicated pods avoid that surprise.", "plan"),
    ], [
        ("Blended, on the outbound product page, means", ["A campaign type", "Agents moving between inbound and outbound", "A codec", "A report layout"], 1, "That is the sentence on the page."),
        ("The planning roadmap's campaign types are", ["Blended only", "Inbound, outbound, autodial", "Preview and power", "WEM and QM"], 1, "Blended is not in that list."),
        ("Sharing agents with predictive is risky because", ["Skills are illegal", "The dialer is guessing availability those agents may not have", "ANI breaks", "IVR cannot play"], 1, "Prediction assumes the agents stay available to that book."),
        ("You implement a blend with", ["A new campaign type", "Skill membership and running campaigns", "A JRE flag", "A matrix CSV"], 1, "Skills and campaigns are the objects that exist."),
        ("Digital channels are mentioned with blend on", ["The outbound product page", "RFC 4733 only", "The headset section only", "The Credly badge"], 1, "The page ties outbound to inbound digital engagement."),
    ], [("What is blended?", "Agents moving across inbound and outbound."), ("Is it a campaign type?", "Not in the planning list."), ("Predictive plus shared agents?", "Availability gets stolen."), ("How do you build it?", "Skills and running campaigns.")],
    ("Staff a blend", "Name who may take inbound during a spike and who stays on the dialer.", ["A shared pod", "A dedicated predictive pod", "The reason they are split"], "Predictive people are not also the inbound overflow."),
    ("Abandon spikes at lunch", "The outbound book is predictive and the same skill takes the noon inbound rush.", "SKILL shared campaigns=[inbound,predictive]", ["Split the skills or change the mode", "Add lines", "Stop the inbound campaign as a habit", "Disable monitoring"], 0, "Inbound is consuming the predicted agents.", "Dedicate agents or move the book to progressive."),
    ["Define blended from the product page", "Keep predictive agents dedicated"], uncertain=["A community test note says predictive agents should not also be skilled for inbound. That is consistent with the product story and is still a field note, not a settings screenshot."]))

    R.append(L("l02", "Autodial is the IVR's outbound", "practice", [
        "Autodial is the third campaign type. The planning topic groups it with inbound when it tells you to record prompts and build IVR scripts. It still uses lists, like outbound. Think of it as the dialer reaching a person and then handing them a script, not an agent, unless the script transfers.",
        "Skill assignment for autodial uses the same oddly named tab as inbound: Outbound Skills. An autodial campaign that is not running will not place those calls.",
    ], [PLAN, SKILLS, INBOUND], path("Autodial", "List, then script, then maybe a skill.", ["List", "Running autodial", "IVR", "Optional skill transfer"]),
    "A reminder call", ["Dialer", "IVR", "Person"], [
        ("Dialer", "List", "The next reminder row is dialed.", "list"),
        ("Dialer", "Run", "The autodial campaign is running.", "run"),
        ("IVR", "Play", "The prompt speaks the reminder.", "play"),
        ("Person", "Digit", "A menu can offer an agent.", "digit"),
        ("IVR", "Skill", "Skill Transfer uses the Outbound Skills list.", "skill"),
        ("Person", "Done", "A final disposition or the script ends the row.", "done"),
    ], [
        ("Autodial is grouped with which build extras?", ["Headsets", "Prompts and IVR scripts", "STIR only", "Java only"], 1, "The planning topic says so."),
        ("Autodial still needs", ["No list", "A list", "Only a DNIS", "Only a profile ANI"], 1, "It dials contacts."),
        ("Its skill tab is named", ["Autodial Skills", "Outbound Skills", "ANI", "JRE"], 1, "The skill topic groups inbound and autodial on that tab."),
        ("A reminder with no agent is a fair autodial use. True or false?", ["False", "True. The script can complete without a transfer", "Only on TCPA domains", "Only if paste works"], 1, "The script can play and end."),
        ("If you wanted an agent to read the account first, you would pick", ["Autodial", "Outbound preview", "A stopped inbound", "Set DNC"], 1, "Preview is the read-first mode."),
    ], [("Planning extras?", "Prompts and IVR."), ("Needs a list?", "Yes."), ("Skill tab?", "Outbound Skills."), ("Read-first alternative?", "Outbound preview.")],
    ("Reminder or conversation", "Label three call types as autodial or preview.", ["Appointment reminder", "Collections with a note to read", "Outage notification"], "The collections call is preview."),
    ("Autodial queue is empty", "The skill was added on the Skills tab used by agent outbound campaigns.", "CAMPAIGN type=AUTODIAL tab=Skills empty outboundSkills=empty", ["Put the skill on Outbound Skills", "Enable paste", "Change G.711", "Delete the prompt"], 0, "Autodial does not read the outbound campaign's Skills tab.", "Use Outbound Skills."),
    ["Choose autodial for scripted outbound", "Use the inbound-style skill tab"]))

    R.append(L("l03", "Priority and ratio are campaign settings", "advanced", [
        "The campaign admin tree includes a topic for campaign priority and ratio settings. This lab has not quoted that topic's fields, so it will not invent the numbers. What is safe to say is that inbound priority, Skill Transfer priority, and any campaign ratio are different screens until you have read them.",
        "A blend fails when every campaign is 'the important one.' Write the order down: which campaign may steal an agent, and which may not.",
    ], [INBOUND, SKILLS], stack("Write the steal rules", "Priority without a sentence is a guess.", ["Who may interrupt", "Who is dedicated", "Which screen you changed", "What the report will show"]),
    "Two campaigns want the same agent", ["Inbound", "Outbound", "Admin"], [
        ("Admin", "Write", "Inbound may interrupt the shared pod.", "rule"),
        ("Admin", "Protect", "Predictive agents are not in that pod.", "protect"),
        ("Inbound", "Priority", "The Skill Transfer priority is set on purpose.", "pri"),
        ("Outbound", "Mode", "The shared pod is progressive, not predictive.", "mode"),
        ("Admin", "Read", "Open the priority and ratio topic before typing a number.", "read"),
        ("Admin", "Watch", "Abandon and service level the next day.", "watch"),
    ], [
        ("This lesson's numeric ratio is", ["2.5", "Not stated. The ratio topic was not quoted field by field", "10", "0"], 1, "Do not invent the dialog."),
        ("Skill Transfer priority and a campaign ratio are", ["Proven to be one field", "Different names. Confirm in the guide before you treat them as one", "Both headsets", "Both ANIs"], 1, "They come from different parts of the docs tree."),
        ("A blend needs a written steal rule because", ["Skills are optional", "Otherwise every campaign is the important one", "TCPA requires it", "Java requires it"], 1, "Someone has to lose the agent."),
        ("Predictive on the shared pod is", ["The safest blend", "The mode most exposed to stolen availability", "Required", "Illegal"], 1, "It plans on agents who may leave."),
        ("Service level tells you", ["Who to dial next", "Whether the wait you allowed was acceptable", "The ANI", "The JRE"], 1, "It is a measure, on the skill."),
    ], [("Numeric ratio in this lesson?", "None."), ("Steal rule?", "Write who may take the agent."), ("Predictive on a shared pod?", "Exposed."), ("Service level?", "A measure, not the dialer.")],
    ("Write three lines", "Who may steal, who is dedicated, which mode the shared pod uses.", ["Shared pod is progressive", "Predictive pod is dedicated", "Inbound may interrupt only the shared pod"], "A stranger could staff from the note."),
    ("Every campaign priority is maxed", "Inbound, autodial, and outbound all claim the same agents.", "PRIORITY all=max AGENTS shared=20", ["Pick an order and dedicate the predictive book", "Max them higher", "Disable abandon monitoring", "Use cellular"], 0, "Maximum on every campaign is no order.", "Write a real order."),
    ["Leave undocumented ratio fields unread-by-you", "Write a steal rule anyway"], uncertain=["The numeric behavior of campaign priority and ratio settings is in a guide topic this lab did not quote. Do not copy a ratio from the simulator into that dialog."]))

    R.append(L("l04", "Not Ready is a real state", "practice", [
        "Agents are not always available. TCPA manual touch forces Not Ready when preview time runs out, and it does not dial. A blend that assumes every login is a dialer resource will over-predict.",
        "Reason codes and Not Ready are how you explain the gap. They are not a carrier outage. Reports in the agent category are where you see the pattern before you add lines.",
    ], [TCPA, cite_rep()], path("Unavailable on purpose", "The dialer must not count these people.", ["Preview timeout", "Not Ready", "Reason", "Agent report"]),
    "Timeout", ["Agent", "Dialer", "Report"], [
        ("Agent", "Read", "The TCPA record sits on screen.", "read"),
        ("Agent", "Stall", "The preview timer ends.", "stall"),
        ("Dialer", "State", "The agent becomes Not Ready.", "nr"),
        ("Dialer", "No", "The external number is not auto-dialed.", "no"),
        ("Report", "See", "Agent reports show the state.", "report"),
        ("Admin", "Staff", "Do not count that login as a predictive resource.", "staff"),
    ], [
        ("TCPA preview timeout sets", ["Ready and dials", "Not Ready and does not dial", "A new DNIS", "A skill greeting"], 1, "Published TCPA behavior."),
        ("Not Ready during a blend", ["Still counts as a free predictive agent", "Should not be treated as available", "Deletes the list", "Signs STIR"], 1, "Unavailable is unavailable."),
        ("Agent reports are a standard category. True or false?", ["False", "True", "Only in Studio", "Only for 911"], 1, "The reporting article lists Agent Reports."),
        ("A reason code explains", ["The codec", "Why the agent is not taking contacts", "The ANI", "The JRE build"], 1, "It is an agent state, not a trunk state."),
        ("Adding lines because people are Not Ready", ["Fixes the book", "Dials more calls into fewer real agents", "Is required by RFC 3261", "Resets dispositions"], 1, "You would raise abandon, not coverage."),
    ], [("TCPA timeout?", "Not Ready, no dial."), ("Count them as free?", "No."), ("Which report category?", "Agent reports."), ("Adding lines?", "Makes abandon worse.")],
    ("Count the floor", "From a sample of 20 logins, subtract Not Ready before you pick a mode.", ["Count Ready", "Count Not Ready", "Pick the mode from Ready"], "The mode uses the Ready number."),
    ("Predictive ratio was set from headcount", "Half the logins are in a meeting.", "LOGINS 40 READY 18 MODE predictive lines~40", ["Rebuild the ratio from Ready, or stop the mode", "Use headcount anyway", "Paste numbers", "Stop recording"], 0, "Headcount is not availability.", "Use the Ready count."),
    ["Subtract Not Ready before you pace", "Use agent reports"]))

    R.append(L("l05", "After-call work feeds the next dial", "practice", [
        "A disposition is what the dialer remembers. A final code stops the record. A retryable code brings it back after the redial rules. Wrap time, in the simulator, is the gap before the agent is free again. Five9's pause-before-transfer is a different gap, on the next inbound delivery, and it is not reported as hold.",
        "If wrap is fiction and pause is zero, a blended agent finishes one call and is instantly eligible. That is how a progressive book and an inbound queue trade the same person every few seconds.",
    ], [DISP, cite_pause()], compare("Two gaps", "Do not add them into one number.", "Disposition and wrap", ["Ends the outbound attempt", "Decides if the row returns"], "Pause before transfer", ["Delays the next inbound delivery", "Not shown as On Hold"]),
    "The call ends", ["Agent", "Dialer", "Queue"], [
        ("Agent", "Code", "A disposition is set.", "code"),
        ("Dialer", "Remember", "Final or retry is now stored.", "store"),
        ("Agent", "Wrap", "The agent is not free yet.", "wrap"),
        ("Queue", "Wait", "Inbound pause may add a breath.", "pause"),
        ("Agent", "Free", "Only then is the person predictable.", "free"),
        ("Dialer", "Next", "The next outbound uses the stored code.", "next"),
    ], [
        ("A final disposition", ["Dials number2 immediately", "Stops the record for that campaign", "Starts IVR", "Changes ANI"], 1, "List and disposition topics agree on this."),
        ("Pause before transfer is", ["Wrap time", "A Skill Transfer delay, not an On Hold statistic", "The abandon window", "A profile filter"], 1, "The pause article separates it from hold."),
        ("Zero pause and zero wrap on a blend", ["Is restful", "Hands the agent back instantly", "Is required", "Signs the call"], 1, "Both queues can grab them."),
        ("Redial count for many system codes, by default, is", ["Zero", "Five, if the default count remains", "Fifty", "One hundred"], 1, "The disposition topic says five."),
        ("The simulator's wrap slider is", ["Five9 source", "A teaching delay", "The 30-day window", "A DNIS"], 1, "It is labeled on the bench."),
    ], [("Final code?", "Stops the record."), ("Pause vs wrap?", "Different gaps."), ("Default system redials?", "Often five."), ("Simulator wrap?", "Teaching delay.")],
    ("Time the gap", "In the bench, set wrap to 45 seconds and watch idle fall.", ["Run progressive", "Add wrap", "Say what pause would do on the inbound side"], "You did not call wrap 'hold'."),
    ("Agents plead for a breath and the hold report is empty", "Inbound pause is 0. Outbound wrap is a disposition timer of 0.", "PAUSE 0 WRAP 0", ["Set pause and a real wrap or disposition timer", "Stare at the hold column", "Add predictive lines", "Delete the profile"], 0, "The breath was never configured, and pause would not have shown as hold anyway.", "Set the controls that exist."),
    ["Separate wrap, pause, and hold", "Let dispositions decide the next dial"], href="#/pacing"))

    R.append(L("l06", "Digital and voice share the person", "advanced", [
        "The outbound page says the dialer works with inbound digital engagement, and Agent Desktop Plus is the screen where voice, digital, and context are meant to meet. A blend that is only a voice story misses chat and email sitting on the same login.",
        "Antivirus products can block digital text from loading. The technical requirements name that failure. A 'blend' that cannot show the chat is a desktop failure, not a skill failure.",
    ], [OUTBOUND, cite_adp(), cite_tech()], path("One login, more than voice", "Digital still consumes the agent.", ["Voice skill", "Digital item", "Same desktop", "Not available to the dialer"]),
    "A chat arrives mid-dial", ["Chat", "Desktop", "Dialer"], [
        ("Chat", "Arrive", "A digital item is offered.", "chat"),
        ("Desktop", "Show", "Plus is supposed to show it with the voice context.", "show"),
        ("Desktop", "Block", "An antivirus product can stop the text.", "av"),
        ("Agent", "Busy", "The person is not a free voice resource.", "busy"),
        ("Dialer", "Wait", "Predictive should not count them.", "wait"),
        ("Admin", "Skill", "Digital and voice skills are an explicit choice.", "skill"),
    ], [
        ("The outbound page ties blend to", ["Only PRI circuits", "Inbound digital engagement as well as voice", "Only 911", "Only Java"], 1, "Digital is part of the sentence."),
        ("Agent Desktop Plus is described as", ["Five separate products the agent alt-tabs", "One screen for the job", "A report layout", "A trunk"], 1, "The agent desktop page says one screen."),
        ("Chat text fails to load and voice still works. A named cause is", ["List penetration", "Antivirus interfering with text media", "A final disposition", "Pause set to 2"], 1, "The technical requirements name antivirus products such as Avast for this."),
        ("While the agent handles chat they are", ["A free predictive agent", "Busy", "A DNIS", "A profile"], 1, "Digital consumes the person."),
        ("Alt-tab as the design", ["Matches the Plus story", "Is what Plus is trying to remove", "Is required by Ofcom", "Is a codec"], 1, "The product page argues for one screen."),
    ], [("Blend includes digital?", "The outbound page says so."), ("Plus promise?", "One screen."), ("Text blocked?", "Antivirus is a documented suspect."), ("Chat and predictive?", "The agent is busy.")],
    ("Count digital", "Add chat to the steal rule you wrote earlier.", ["Who takes chat", "Whether they are also predictive", "What you check if text does not load"], "Antivirus is on the list."),
    ("Agents keep a second browser for chat", "Plus is licensed and unused. The dialer sees them as voice-idle while they type.", "DESKTOP plus=unused CHAT other-browser", ["Move the work into Plus and stop counting them as idle voice", "Add power lines", "Delete IVR", "Enable IE for everyone"], 0, "The blend is happening off to the side.", "Use the desktop that was supposed to hold both, and staff from real availability."),
    ["Include digital in the blend", "Check antivirus when text disappears"]))

    R.append(L("l07", "A blend you can defend", "advanced", [
        "A defensible blend is a paragraph: which campaigns run, which skills overlap, which mode each outbound book uses, who may be stolen, what Not Ready does to the count, and which abandon window the domain uses. Every noun in that paragraph is a screen you can open.",
        "If you cannot point at the screen, it is not a design. The simulator can illustrate it. It cannot be attached to the domain.",
    ], [OUTBOUND, DIALER, DEFAULTS, PLAN], path("The paragraph", "Six nouns, six screens.", ["Campaigns", "Skills", "Modes", "Steal rule", "Not Ready", "Abandon window"]),
    "Read it aloud", ["Design", "Floor"], [
        ("Design", "Types", "Inbound, one autodial, one outbound.", "types"),
        ("Design", "Skills", "Overlap is only on the shared pod.", "skills"),
        ("Design", "Modes", "Shared pod is progressive. The other book is preview.", "modes"),
        ("Design", "Steal", "Inbound may take the shared pod.", "steal"),
        ("Floor", "Ready", "Not Ready is subtracted.", "ready"),
        ("Floor", "Window", "The domain is US, so 30 days.", "window"),
    ], [
        ("A blend paragraph that names no screen is", ["Complete", "Not a design", "A report layout", "A JRE"], 1, "Each noun should be a screen."),
        ("The simulator attaches to the domain. True or false?", ["True", "False. It is a classroom", "True for TCPA paste", "True on UK domains"], 1, "The dialog in the domain is the system of record."),
        ("US abandon window to write in the paragraph is", ["24 hours", "30 days", "One chart minute", "Seven years"], 1, "That is the admin topic."),
        ("Autodial belongs in the paragraph when", ["You want a scripted outbound", "You want preview reading", "You want a DNIS", "You want a headset"], 1, "It is the scripted outbound type."),
        ("Dedicated predictive agents appear as", ["Also the inbound overflow", "A pod the steal rule does not touch", "A profile ANI", "A prompt"], 1, "Otherwise they are not dedicated."),
    ], [("No screen, no design?", "Correct."), ("Simulator equals domain?", "No."), ("US window?", "30 days."), ("Dedicated pod?", "Outside the steal rule.")],
    ("Write the paragraph", "Six sentences, one screen each.", ["Campaigns", "Skills", "Modes", "Steal rule", "Not Ready", "Window"], "Someone else could configure Tuesday from it."),
    ("The design is a logo slide", "No skills, no modes, no window.", "SLIDE title=Blended AI", ["Reject it until the six nouns exist", "Add more adjectives", "Raise lines to 8", "Stop the domain"], 0, "A logo is not a staffing plan.", "Write the paragraph."),
    ["Defend a blend with six screens", "Keep the simulator in the classroom"], href="#/pacing"))
    return track("t06", "Blended operations and autodial", "Blended", "How agents move between inbound, autodial, and outbound without lying to the dialer.", "Voice", "Advanced", "Blended is a staffing plan. Autodial is the scripted outbound. Predictive people should stay dedicated.", R)

def cite_rep():
    from curriculum_lib import REPORTS
    return REPORTS

def cite_pause():
    from curriculum_lib import PAUSE
    return PAUSE

def cite_adp():
    from curriculum_lib import ADP
    return ADP

def cite_tech():
    from curriculum_lib import TECH
    return TECH
