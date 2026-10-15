from curriculum_lib import INBOUND, PLAN, SKILLS, SKILLMOD, PAUSE, MODULES, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "A DNIS answers only while the campaign runs", "foundation", [
        "An inbound campaign receives calls for a DNIS and processes them with that campaign's IVR script. The inbound topic is blunt about state: if the campaign is not running, callers hear a busy signal.",
        "Greetings, skills, and hold music never get a chance to run in that state. The first check on a new number is the campaign state, not the carrier.",
    ], [INBOUND], path("Inbound answer", "State comes before treatment.", ["DNIS", "Campaign running", "IVR script", "Skill or treatment"]),
    "A call hits a DNIS", ["PSTN", "VCC", "Caller"], [
        ("PSTN", "INVITE", "The carrier delivers the DNIS.", "DNIS"),
        ("VCC", "State", "The campaign must be running.", "RUNNING"),
        ("VCC", "Busy", "If it is stopped, the caller hears busy.", "busy"),
        ("VCC", "IVR", "The script starts only after the campaign answers.", "script"),
        ("Caller", "Prompt", "Greetings and menus play from the script.", "prompt"),
        ("VCC", "Skill", "Skill Transfer queues to agents.", "skill"),
    ], [
        ("A stopped inbound campaign sounds like", ["Ringback forever", "A busy signal", "A Studio task", "Silence required by law"], 1, "The inbound topic says callers hear busy."),
        ("What processes the answered call?", ["The campaign IVR script", "The agent's notepad", "Only WEM", "Only the ANI"], 1, "Calls are processed according to the IVR script of the campaign."),
        ("DNIS means", ["The agent's skill level", "The number the caller dialed, as presented to the campaign", "The disposition", "The abandon window"], 1, "Inbound campaigns receive calls coming from a DNIS."),
        ("Hold music is configured where, relative to answer?", ["Before the campaign exists, on the carrier only", "In the treatment after the campaign has answered", "In the JRE", "In MyE911"], 1, "Prompts and hold are part of the running campaign's treatment."),
        ("First check when a new number is busy?", ["Rewrite the IVR", "Campaign run state", "Change G.711", "Reset dispositions"], 1, "State explains busy before the script does."),
    ], [("Stopped inbound?", "Busy."), ("What runs after answer?", "The campaign IVR."), ("What is DNIS?", "The called number presented to the campaign."), ("First busy check?", "Is the campaign running?")],
    ("State drill", "List three states you would check before a trunk ticket.", ["Campaign running", "DNIS attached", "Script assigned"], "Busy is explained or you have a real trunk symptom."),
    ("New store number is busy", "The DID was purchased this morning.", "DNIS 8005550148 CAMPAIGN Stores state=NOT_RUNNING", ["Start the campaign", "Enable TLS 1.1", "Turn on Efficiency Mode", "Delete the skill"], 0, "Not running means busy.", "Start Stores."),
    ["Tie DNIS, run state, and IVR together", "Check state before the carrier"]))

    R.append(L("l02", "The script is the inbound product", "practice", [
        "Once the campaign answers, the IVR script is the product the caller meets. The inbound topic lists custom greetings, loops and branching, collecting information, using contact data, voicemail when the queue is long, forward to a third party, and priority.",
        "Skill Transfer is how that script hands the caller to a queue. The community article says that after an agent is connected, the IVR script is complete. A module after Skill Transfer is not a second conversation with the same caller.",
    ], [INBOUND, SKILLMOD], stack("What an inbound script can do", "From the inbound campaign topic.", ["Greet and branch", "Collect digits", "Use contact data", "Queue with Skill Transfer", "Voicemail or third party"]),
    "From greeting to agent", ["Caller", "IVR", "Agent"], [
        ("Caller", "Hello", "The Play or Menu greeting runs.", "greet"),
        ("IVR", "Branch", "Digits or speech pick a path.", "branch"),
        ("IVR", "Data", "A lookup can read the contact.", "data"),
        ("IVR", "Queue", "Skill Transfer places the caller.", "queue"),
        ("Agent", "Answer", "The script is complete.", "done"),
        ("IVR", "Else", "Voicemail or a third-party forward is the other exit.", "else"),
    ], [
        ("After Skill Transfer connects an agent, the script", ["Keeps running forever", "Is complete", "Starts a second campaign", "Hangs the carrier"], 1, "The skill transfer article says the IVR script is complete."),
        ("Long queue options named in the inbound topic include", ["Deleting the domain", "Voicemail and third-party forward", "Changing the JRE", "Only a busy tone"], 1, "The topic lists voicemail and forward when agents are unavailable."),
        ("Priority of inbound traffic is", ["Impossible", "Something the inbound topic says you can set", "Only a WEM feature", "Only an ANI"], 1, "The topic says you can prioritize inbound call traffic."),
        ("Contact data in the IVR is", ["Forbidden", "Listed as something the inbound campaign can use", "Only for 911", "Only in CSV exports"], 1, "The topic says you can use contact data."),
        ("Loops and branching belong to", ["The headset", "The IVR script", "The bandwidth table", "The license PDF only"], 1, "The inbound topic says you can create loops and branching."),
    ], [("Script after agent connect?", "Complete."), ("Long queue options?", "Voicemail and third-party forward."), ("Priority?", "Supported in the inbound topic."), ("Branching?", "In the IVR script.")],
    ("One script, three exits", "Sketch greet, skill, and voicemail.", ["Name the greeting", "Name the skill", "Name the overflow"], "There is no module pretending to run after the agent is connected."),
    ("Callers reach agents and then hear the main menu again", "The designer placed Play after Skill Transfer and expected it to run for the connected caller.", "MODULE SkillTransfer then Play prompt=survey", ["The script already completed on connect", "DNIS was empty", "The profile had no ANI", "Efficiency Mode"], 0, "Post-connect treatment is not that later Play module.", "Put surveys in a path that is actually reached, such as a callback or a separate process you have verified."),
    ["List inbound script jobs", "Remember that connect ends the script"], uncertain=["A post-call survey exists as a campaign-admin topic title in the docs tree. This lesson does not describe its screens. Open that topic before you design one."]))

    R.append(L("l03", "Queue treatment is a choice, not a hope", "practice", [
        "The inbound topic allows custom prompts and hold music, a message when agents are unavailable, voicemail, and a forward to a third party. Those are different exits. Hold music is not voicemail. A forward leaves your agents entirely.",
        "Third Party Transfer is an IVR module in the modules list. Voicemail Transfer is another. Picking the wrong one is a routing bug, not a carrier bug.",
    ], [INBOUND, MODULES], compare("Overflow", "Name the exit before the queue melts.", "Stay in Five9", ["Hold prompt", "Voicemail Transfer", "Queue callback on Skill Transfer"], "Leave the queue", ["Third Party Transfer", "A stopped campaign's busy", "A DNIS with no campaign"]),
    "The queue is full", ["Caller", "IVR"], [
        ("Caller", "Wait", "Hold music and announcements play.", "hold"),
        ("IVR", "Time", "Max queue time can expire.", "timer"),
        ("IVR", "Voice", "Voicemail Transfer takes a message.", "vm"),
        ("IVR", "Out", "Third Party Transfer forwards away.", "3p"),
        ("IVR", "Back", "Queue callback is a Skill Transfer option.", "callback"),
        ("Caller", "Hear", "The path you drew is the path they hear.", "hear"),
    ], [
        ("Hold music and voicemail are", ["The same module", "Different treatments", "Both SIP trunks", "Both profiles"], 1, "The inbound topic lists them as separate options."),
        ("Third Party Transfer", ["Dials an agent skill", "Forwards to a third party", "Sets a disposition to Sale", "Edits the JRE"], 1, "The modules list names Third Party Transfer for that job."),
        ("Voicemail Transfer", ["Is the third-party module", "Sends the caller to voicemail", "Starts predictive dialing", "Opens Salesforce"], 1, "Voicemail Transfer is its own module."),
        ("A stopped campaign is a poor overflow because", ["It plays your branded prompt", "Callers hear busy instead of your treatment", "It sends Certified Caller", "It resets lists"], 1, "Busy is not a designed overflow."),
        ("Queue callback is discussed with", ["The JRE", "The Skill Transfer module", "Equinix Fabric", "Headset SKUs"], 1, "The skill transfer article includes a Queue Callback tab."),
    ], [("Hold vs voicemail?", "Different."), ("Third party module?", "Third Party Transfer."), ("Voicemail module?", "Voicemail Transfer."), ("Stopped campaign as overflow?", "No. Callers hear busy.")],
    ("Draw overflow", "Pick one branded exit for a 10-minute queue.", ["Choose voicemail or third party", "Name the module", "Say what busy would sound like instead"], "The exit is a module, not a stopped campaign."),
    ("After-hours callers hear busy", "The campaign is stopped at night instead of playing a closed message.", "SCHEDULE none CAMPAIGN state=NOT_RUNNING", ["The campaign is not running, so there is no script", "Skill level is too high", "ANI is local", "Matrix reports cannot export"], 0, "Stopped means busy, not your closed prompt.", "Keep a running campaign whose script plays the closed treatment, or use the IVR schedule the admin guide describes."),
    ["Choose an overflow module", "Do not use a stopped campaign as a prompt"]))

    R.append(L("l04", "Priority and service level", "practice", [
        "The inbound topic says you can prioritize inbound traffic. Skill Transfer has a Priority tab in the community write-up. Skill groups themselves have service-level settings in the basic admin topic.",
        "Priority is not the same number as a service-level target. One decides who gets the next agent when several calls wait. The other is how you measure whether the wait was acceptable. The public pages name both. They do not, in the text this lab read, give you a formula that mixes them.",
    ], [INBOUND, SKILLMOD, SKILLS], compare("Two different numbers", "Do not add them together.", "Priority", ["Who is offered first", "Skill Transfer priority tab", "Inbound topic says you can prioritize"], "Service level", ["How long is acceptable", "Set on the skill group", "A report, not a queue jump"]),
    "Two queues, one idle agent", ["Queue A", "Queue B", "VCC"], [
        ("Queue A", "Wait", "A caller has waited 30 seconds at low priority.", "low"),
        ("Queue B", "Wait", "A caller has waited 5 seconds at high priority.", "high"),
        ("VCC", "Offer", "Priority is the ordering input you configured.", "offer"),
        ("VCC", "SL", "Service level scores the wait afterward.", "score"),
        ("Queue A", "Report", "A missed service level does not by itself reorder the queue.", "report"),
        ("VCC", "Check", "Read both screens before you change either.", "check"),
    ], [
        ("Service level is configured with", ["The SIP cipher", "The skill group", "The JRE", "The call-log matrix"], 1, "The skill topic includes service levels."),
        ("Priority in an IVR queue is a", ["Skill Transfer concern", "Headset concern", "License PDF concern", "MAC address"], 1, "The skill transfer article lists a Priority tab."),
        ("A missed service level automatically jumps the queue. True or false?", ["True", "False. This lab did not find a page that says the service-level target reorders calls", "True at 30 days", "True for TCPA"], 1, "Treat them as different controls until a current page ties them together."),
        ("Inbound prioritization is", ["Undocumented", "Named in the inbound campaign topic", "Illegal", "Only for autodial"], 1, "The inbound topic says you can prioritize inbound traffic."),
        ("Changing priority without reading service level", ["Is the whole design", "Can make the report and the caller experience disagree", "Deletes recordings", "Fixes busy signals"], 1, "One orders calls. The other measures them."),
    ], [("Where is service level?", "On the skill group."), ("Where is IVR priority?", "Skill Transfer's priority tab."), ("Are they the same knob?", "No."), ("Who says inbound can be prioritized?", "The inbound campaign topic.")],
    ("Label the knobs", "Write one sentence for priority and one for service level.", ["Priority orders the offer", "Service level measures the wait", "You will not add the numbers"], "The sentences do not reuse the same verb."),
    ("VIP callers wait behind password resets", "Both skills share one small team and the VIP Skill Transfer priority was left at the default.", "SKILL VIP priority=default SKILL Reset priority=default", ["Set VIP higher on its Skill Transfer", "Stop the campaign", "Disable G.711", "Turn on cellular"], 0, "Nothing is ordering VIP first.", "Raise VIP priority and staff the skill."),
    ["Separate priority from service level", "Point at the screen for each"], uncertain=["The exact numeric interaction between skill service level and Skill Transfer priority is not stated in the pages this lab quoted."]))

    R.append(L("l05", "Schedules, not a stopped campaign", "practice", [
        "The campaign admin tree includes IVR script schedules for autodial and inbound campaigns. The planning topic tells you to set the campaign IVR schedule after the script exists. A schedule swaps treatment by time. Stopping the campaign does not. Stopping it returns busy.",
        "This lab does not reproduce the schedule dialog field by field. Use the schedule when you need a night path, and confirm the campaign stays running.",
    ], [PLAN, INBOUND], path("Day and night", "The campaign stays running.", ["Day script", "Schedule", "Night script", "Campaign still running"]),
    "Clock changes the script", ["Clock", "VCC", "Caller"], [
        ("Clock", "Open", "Day schedule selects the day script.", "day"),
        ("Caller", "Call", "The running campaign answers.", "answer"),
        ("Clock", "Close", "The schedule selects the closed script.", "night"),
        ("VCC", "Run", "State stays running.", "running"),
        ("Caller", "Hear", "The closed prompt plays.", "prompt"),
        ("VCC", "Avoid", "Nobody stops the campaign at 18:00.", "avoid"),
    ], [
        ("The planning topic says to set the IVR schedule", ["Before skills exist", "After the IVR scripts exist", "Instead of a DNIS", "Only for outbound preview"], 1, "The roadmap sets the campaign IVR schedule after scripts."),
        ("Stopping the campaign at night", ["Plays the closed prompt", "Makes callers hear busy", "Starts TCPA", "Exports a matrix report"], 1, "Busy is the stopped behavior."),
        ("Schedules apply to which types, by the admin tree label?", ["Outbound preview only", "Autodial and inbound", "E911 only", "WEM only"], 1, "The tree title is IVR script schedules for autodial and inbound."),
        ("A schedule is a reason to keep the campaign", ["Stopped", "Running", "Deleted", "In a JRE"], 1, "The script only runs if the campaign answers."),
        ("This lab's schedule screens are", ["A full copy of the dialog", "A pointer. Open the current admin topic for the fields", "Illegal to describe", "The dialer source"], 1, "Field-level schedule options were not quoted here."),
    ], [("When is the schedule set?", "After scripts exist."), ("Nightly stop?", "Causes busy, not a closed prompt."), ("Which types have the schedule topic?", "Autodial and inbound."), ("Campaign state at night?", "Running, with a different script.")],
    ("Write the night rule", "One sentence that forbids stopping the campaign at close of business.", ["Name the day script", "Name the night script", "State remains running"], "The sentence uses the word running."),
    ("17:55 change window", "Someone's runbook says to stop Inbound at 18:00.", "RUNBOOK 18:00 set NOT_RUNNING", ["Replace that step with a script schedule", "Also disable TLS", "Reset all dispositions", "Pin one SBC IP"], 0, "The runbook recreates the busy failure.", "Schedule the closed script and leave the campaign running."),
    ["Prefer a schedule to a stopped campaign", "Keep state running"]))

    R.append(L("l06", "Pause before the next call", "practice", [
        "Skill Transfer has Pause Before Transfer, in seconds, on the General tab. The default is 0. A value above 0 waits that long after an agent is selected before the call is delivered, so a queue does not slap the next call down instantly.",
        "The community article says those seconds do not show as On Hold in a report. On Plus applications the caller can sit in a Connecting state. Setting the pause to 0 removes that connecting bar. Do not 'fix' a report by deleting the pause if agents asked for the breath.",
    ], [PAUSE, SKILLMOD], stack("Pause before transfer", "A breath for the agent, not an On Hold statistic.", ["Agent selected", "Pause seconds", "Call delivered", "Report does not call it hold"]),
    "Back-to-back calls", ["Queue", "VCC", "Agent"], [
        ("Queue", "Next", "Another caller is already waiting.", "waiting"),
        ("VCC", "Select", "An agent becomes free and is selected.", "select"),
        ("VCC", "Pause", "The configured seconds elapse.", "pause"),
        ("Agent", "Offer", "The call arrives after the pause.", "offer"),
        ("VCC", "Report", "Those seconds are not On Hold.", "report"),
        ("Agent", "Zero", "A 0 value removes the connecting bar.", "zero"),
    ], [
        ("Where is Pause Before Transfer?", ["Campaign profile ANI", "Skill Transfer, General tab", "The JRE", "MyE911"], 1, "The article places it on the General tab."),
        ("Default value?", ["30 seconds", "0", "The abandon cap", "128 kbps"], 1, "The article says the default is 0."),
        ("Do the pause seconds appear as On Hold?", ["Yes", "No. The article says they do not", "Only in UK domains", "Only for matrix layouts"], 1, "The article is explicit."),
        ("A connecting bar on Plus apps can be removed by", ["Stopping the campaign", "Setting pause to 0", "Deleting the skill", "Using analog headsets"], 1, "The article says 0 removes the connecting bar."),
        ("The pause exists to", ["Increase abandon rate", "Give agents a gap before the next queued call", "Change ANI", "Disable TCPA"], 1, "The article describes a short pause when calls are queued."),
    ], [("Where?", "Skill Transfer General tab."), ("Default?", "0."), ("On Hold in reports?", "No."), ("Why set it above 0?", "A gap before the next call.")],
    ("Set a breath", "Choose a pause for a team that takes calls with no gap.", ["Open General", "Set a small number of seconds", "Tell the team it will not show as hold"], "The team knows why the report looks unchanged."),
    ("Agents say they have no wrap, reports say hold is zero", "Pause is 0 and the queue is deep.", "SKILL Support pause=0 queue=12", ["Set Pause Before Transfer above 0", "Stop the campaign at lunch", "Switch to analog headsets", "Delete call variables"], 0, "Zero pause delivers the next call immediately, and it was never going to show as hold.", "Set a few seconds of pause and give them a real disposition timer if they need wrap."),
    ["Set pause on purpose", "Do not expect it in the hold column"]))

    R.append(L("l07", "Inbound design review", "advanced", [
        "A review you can finish in one sitting: DNIS, running campaign, script, skill on the Outbound Skills tab, overflow module, schedule, and pause. Each one has a public page. None of them is a trunk setting.",
        "If all seven are right and the caller still hears silence or reorder, then you have a carrier or SBC symptom. The topology bench is the next tool, not another copy of the greeting.",
    ], [INBOUND, SKILLS, PLAN], path("Inbound review", "Seven checks before the carrier.", ["DNIS", "Running", "Script", "Skill tab", "Overflow", "Schedule", "Pause"]),
    "Review a new line", ["Reviewer", "VCC"], [
        ("Reviewer", "Number", "DNIS matches the number in the advertisement.", "dnis"),
        ("Reviewer", "State", "Campaign is running.", "run"),
        ("Reviewer", "Script", "The IVR assigned is the one you tested.", "script"),
        ("Reviewer", "Skill", "Outbound Skills lists the right group.", "skill"),
        ("Reviewer", "Exit", "Voicemail or third party is explicit.", "exit"),
        ("Reviewer", "Clock", "Night uses a schedule, and pause is intentional.", "clock"),
    ], [
        ("How many of these checks are trunk settings?", ["All seven", "None. They are campaign and script settings", "Three", "Only pause"], 1, "The carrier is what you check after these."),
        ("Wrong tab for inbound skills means", ["A busy signal always", "Agents never enter that queue", "TLS 1.3 fails", "Reports export as CSV"], 1, "The skill is on the wrong tab, so the queue is empty."),
        ("Night busy with a perfect daytime script usually means", ["G.711", "The campaign was stopped, or the night script was never scheduled", "Too many flashcards", "A matrix layout"], 1, "State or schedule."),
        ("Overflow should be", ["A stopped campaign", "A named module", "A JRE update", "A wireless headset"], 1, "Voicemail Transfer or Third Party Transfer."),
        ("After the seven checks pass, open", ["Another greeting file", "The topology and the trunk path", "The Credly badge", "Efficiency Mode"], 1, "The remaining failures are path failures."),
    ], [("Are the seven checks trunk settings?", "No."), ("Wrong skill tab?", "Empty queue."), ("Night busy?", "State or schedule."), ("Then what?", "Trunk and topology.")],
    ("Run the seven", "Use a real or sample campaign and tick the seven.", ["DNIS", "State", "Script", "Skill tab", "Overflow", "Schedule", "Pause"], "Each tick names a screen."),
    ("Ticket opened to the carrier first", "The DID is busy and nobody looked at campaign state.", "TICKET carrier CAMPAIGN state=NOT_RUNNING", ["Close the carrier ticket and start the campaign", "Order a new codec", "Enable IE", "Reset Sale dispositions"], 0, "The log already shows the cause.", "Start the campaign, then retest."),
    ["Run a seven-point inbound review", "Escalate to the trunk only after they pass"], href="#/topology"))
    return track("t03", "Inbound campaigns", "Inbound", "DNIS, run state, scripts, overflow, schedules, and the pause between calls.", "Voice", "Practice", "Inbound is a running campaign plus a script. Busy means the campaign is not in the call.", R)
