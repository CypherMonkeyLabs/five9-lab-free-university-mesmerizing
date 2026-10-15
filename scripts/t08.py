from curriculum_lib import SKILLS, SKILLMOD, INBOUND, lesson, compare, stack, path, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "A skill is a queue with people in it", "foundation", [
        "A skill group holds users who have the agent or supervisor role. Campaigns point at one or more groups. The people, not the name, determine who can receive the contact.",
        "Service level, voicemail, greetings, and a message to the group are all on the skill topic. A skill with no members is a label.",
    ], [SKILLS], stack("Skill contents", "From the skill group topic.", ["Agent or supervisor users", "Campaign assignment", "Service level", "Voicemail and greeting"]),
    "Build Billing", ["Admin", "Agent"], [
        ("Admin", "Create", "The group exists.", "create"),
        ("Admin", "Add", "Agents are members.", "add"),
        ("Admin", "Level", "A service level is set.", "sl"),
        ("Admin", "Audio", "A greeting is recorded.", "audio"),
        ("Agent", "Ready", "A member is available.", "ready"),
        ("Admin", "Empty", "A group with no members never answers.", "empty"),
    ], [
        ("Who can be in a skill group?", ["Reporting-only users", "Agent or supervisor users", "SIP trunks", "Profiles by themselves"], 1, "The topic names those roles."),
        ("A skill with no members", ["Answers faster", "Cannot deliver a call", "Sets ANI", "Exports CSV"], 1, "There is nobody to offer."),
        ("Service level lives", ["On the skill", "On the codec", "On the JRE", "On the badge"], 1, "The topic includes service levels."),
        ("One user, several skills?", ["Forbidden", "Allowed", "Only in UK domains", "Only for IVA"], 1, "Users can be in multiple groups."),
        ("Voicemail on a skill is", ["Undocumented", "In the skill topic", "A list mode", "A dialer mode"], 1, "Messages and greetings are part of the topic."),
    ], [("Membership?", "Agent or supervisor."), ("Empty skill?", "No delivery."), ("Service level?", "On the skill."), ("Several skills per user?", "Yes.")],
    ("Roster", "Write a skill and three members.", ["Name the skill", "Name who is excluded", "Name the service level as a target, not a priority"], "The roster is not the campaign."),
    ("The queue name exists and never rings", "Billing has zero users.", "SKILL Billing members=0", ["Add members", "Change the codec", "Enable paste", "Reset Sale"], 0, "A name is not a person.", "Add the agents."),
    ["Staff the skill", "Set a service level you can explain"]))
    R.append(L("l02", "The tab is named backwards on inbound", "practice", [
        "Outbound campaigns take skills on the Skills tab. Inbound and autodial take them on a tab named Outbound Skills. The skill topic says this in one paragraph. People miss it because the word outbound sits on an inbound campaign.",
        "If the right people are Ready and the queue is still empty, look at the tab before you look at the carrier.",
    ], [SKILLS], compare("Tab names", "Read the words on the screen.", "Outbound campaign", ["Skills"], "Inbound and autodial", ["Outbound Skills"]),
    "Attach the same group twice", ["Admin", "Campaign"], [
        ("Admin", "Group", "Support exists and has members.", "group"),
        ("Campaign", "Out", "The outbound campaign uses Skills.", "skills"),
        ("Campaign", "In", "The inbound campaign uses Outbound Skills.", "outskills"),
        ("Campaign", "Wrong", "Using Skills on inbound leaves the queue empty.", "wrong"),
        ("Agent", "Ready", "Ready does not fix the wrong tab.", "ready"),
        ("Admin", "Retest", "A test call hits a member.", "test"),
    ], [
        ("Inbound skills tab is named", ["Inbound Skills", "Outbound Skills", "ANI", "Pause"], 1, "That is the published name."),
        ("Ready agents on the wrong tab", ["Still get the call", "Do not", "Get 911 instead", "Change the list mode"], 1, "The campaign is not pointing at them."),
        ("Autodial uses", ["The outbound campaign Skills tab", "Outbound Skills", "No skills ever", "Only Default always"], 1, "The topic groups autodial with inbound."),
        ("The fix is", ["A new codec", "The other tab", "A JRE update", "A frame header"], 1, "Move the assignment."),
        ("This is documented in", ["A rumor", "The skill groups topic", "RFC 3261", "The Credly badge"], 1, "It is one of the first facts on that page."),
    ], [("Inbound tab?", "Outbound Skills."), ("Ready but wrong tab?", "No offer."), ("Autodial?", "Same tab as inbound."), ("Where documented?", "Skill groups topic.")],
    ("Two campaigns", "Write the tab name under each.", ["Inbound", "Outbound", "Autodial"], "Inbound and autodial match."),
    ("Support never rings on the new inbound line", "The skill is on the Skills tab.", "INBOUND tab=Skills outboundSkills=empty", ["Move Support to Outbound Skills", "Add power lines", "Delete the prompt", "Enable IE"], 0, "Wrong tab.", "Use Outbound Skills."),
    ["Memorize the awkward tab name", "Check it before the trunk"]))
    R.append(L("l03", "One module, one skill, when you need the truth", "practice", [
        "Skill Transfer may list several skills, and any agent who has one of them can take the call. The same article recommends a single skill in the module when you want reports that mean something.",
        "A shared pool is a valid design. An accidental shared pool is how billing calls show up as a blob. Split modules if the work is different. Keep one module if the pool is the point.",
    ], [SKILLMOD], compare("Pool or precision", "Both are configurations. Only one is an accident.", "One skill in the module", ["Clearer reports", "A specific queue"], "Several skills", ["Any matching agent", "A deliberate pool"]),
    "Choose", ["Designer", "Report"], [
        ("Designer", "Ask", "Is this one kind of work?", "ask"),
        ("Designer", "One", "Then one skill.", "one"),
        ("Designer", "Pool", "If any of three teams may take it, list them on purpose.", "pool"),
        ("Report", "Read", "One skill keeps the column meaningful.", "read"),
        ("Designer", "Write", "The design note says pool or not.", "note"),
        ("Report", "Check", "A week later the report matches the note.", "check"),
    ], [
        ("Several skills in one module means", ["The agent must have all of them", "Any one of them qualifies", "The call fails", "ANI changes"], 1, "The article says any agent with one of the skills."),
        ("The report recommendation is", ["As many skills as possible", "One", "Zero", "Default only"], 1, "One skill per module for useful reports."),
        ("A deliberate pool is", ["Forbidden", "Fine, if you meant it", "A codec", "A JRE"], 1, "The software allows it. The accident is the problem."),
        ("Splitting modules means", ["Two queues you can see", "One blob", "No IVR", "No agents"], 1, "Each module names its skill."),
        ("Default queue is what you get when", ["You pick one skill", "You select none", "You set pause to 0", "You upload a list"], 1, "No selection routes to users without skills."),
    ], [("Any or all?", "Any one skill."), ("Report tip?", "One skill."), ("Deliberate pool?", "Allowed if intended."), ("No selection?", "Default.")],
    ("Split or pool", "Take three call reasons and decide.", ["Billing alone", "Sales alone", "A true overflow pool"], "The pool is labeled on purpose."),
    ("Billing reports include password resets", "One module lists both skills.", "SKILLS Billing+Reset", ["Split the modules", "Add a third skill", "Stop the campaign nightly", "Change ANI"], 0, "Either skill can take the call, so the report blends them.", "One skill per module."),
    ["Choose pool or precision out loud", "Match the report to that choice"]))
    R.append(L("l04", "Skill level versus list order", "advanced", [
        "The skill transfer article describes an option to ignore the order of skills in the module and distribute by the agent's skill level instead. Order and level are different ideas. Order is the list you typed. Level is a property of the agent.",
        "This lab does not quote the click-path for editing an agent's level. If you use the option, confirm in the editor which number wins. Do not assume the top of the list is the highest level.",
    ], [SKILLMOD], compare("Two orderings", "The article gives you a switch.", "List order", ["The sequence in the module"], "Agent skill level", ["A property of the person", "Used when you ignore list order"]),
    "Two agents, one call", ["Module", "Agent A", "Agent B"], [
        ("Module", "Order", "Billing is listed before Sales.", "order"),
        ("Agent A", "Level", "A is a high level on Sales only.", "a"),
        ("Agent B", "Level", "B is a low level on Billing.", "b"),
        ("Module", "Switch", "Ignore-order is off, so the list matters.", "off"),
        ("Module", "On", "Ignore-order uses level instead.", "on"),
        ("Admin", "Confirm", "The editor is checked before go-live.", "confirm"),
    ], [
        ("List order and skill level are", ["The same number", "Different. The article describes a switch between them", "Both ANIs", "Both codecs"], 1, "The option exists so they are not the same."),
        ("Ignore skills order means", ["Delete skills", "Prefer agent skill level over the typed list", "Stop the campaign", "Enable paste"], 1, "That is the article's description."),
        ("This lab's click-path for editing a level is", ["Fully quoted", "Not quoted. Confirm in the editor", "A SIP header", "A Credly rule"], 1, "Do not invent the dialog."),
        ("Leaving the switch off means", ["Level always wins", "The list order is what you configured", "911 fails", "Java fails"], 1, "The default behavior follows the list unless you enable the option."),
        ("A design note should say", ["Nothing", "Which ordering is on", "Only the logo", "The JRE update"], 1, "Otherwise the next admin flips it."),
    ], [("Same number?", "No."), ("What does ignore-order do?", "Uses agent skill level."), ("Click-path quoted here?", "No."), ("Switch off?", "List order stands.")],
    ("Write the rule", "One sentence: list order or agent level.", ["Name the switch", "Name who would receive a test call", "Say what you did not assume"], "The sentence matches the switch."),
    ("Senior agents never get the call", "They are high level and the module is set to list order, which prefers a junior skill listed first.", "IGNORE_ORDER off LIST junior-first", ["Turn the option on, or reorder the list to match the intent", "Delete seniors", "Add predictive lines", "Frame the visual IVR"], 0, "The switch does not match the intent.", "Change the switch or the list, on purpose."),
    ["Pick list order or agent level", "Do not assume they match"], uncertain=["The article names the option. The exact screen where an agent's skill level is edited was not quoted in this lab."]))
    R.append(L("l05", "Default is a queue, not a compliment", "practice", [
        "If Skill Transfer has no skill selected, the article says calls go to users who are not assigned skills. That queue is labeled Default in the softphone. It is a catch-all, not a place you want billing calls.",
        "Supervisors and agents with empty skill lists become the Default pool. An empty list is easy to create when a user profile is cloned and skills are forgotten.",
    ], [SKILLMOD, SKILLS], path("The catch-all", "No selection does not mean no route.", ["No skill selected", "Default queue", "Users with no skills", "A report you did not expect"]),
    "A cloned user", ["Admin", "VCC"], [
        ("Admin", "Clone", "A new user copies a login and no skills.", "clone"),
        ("VCC", "Default", "They sit in Default.", "def"),
        ("Script", "Empty", "A module with no skill selected finds them.", "empty"),
        ("Caller", "Reach", "The caller gets whoever has no skill.", "reach"),
        ("Admin", "See", "The softphone label is Default.", "label"),
        ("Admin", "Fix", "Select a real skill. Give the user a real membership.", "fix"),
    ], [
        ("No skill selected routes to", ["911", "Default, users without skills", "The ITSP only", "Studio only"], 1, "The article says so."),
        ("The softphone label is", ["Any", "Default", "ANI", "TCPA"], 1, "The article names Default."),
        ("A user with no skills is", ["Invisible", "Eligible for that catch-all", "A trunk", "A prompt"], 1, "Empty membership is membership in the catch-all story."),
        ("The safe module is", ["Skill list empty", "A named skill", "Hangup slang", "A comment"], 1, "Name the skill."),
        ("Cloning users without checking skills", ["Is the design", "Creates Default agents by accident", "Sets STIR", "Sets pause"], 1, "Check membership after every clone."),
    ], [("No selection?", "Default queue."), ("Label?", "Default."), ("User with no skills?", "Catch-all eligible."), ("Safe pattern?", "Name the skill.")],
    ("Find Default", "List who on your paper floor has no skill.", ["Clone a user on paper", "Leave skills empty", "Say which module would reach them"], "You would rather see a named skill."),
    ("New hires answer VIP calls", "Their Skill Transfer for VIP has no skill selected, and the new hires have no skills yet.", "MODULE skills=[] USERS new skills=[]", ["Select VIP and add the real VIP agents", "Add the new hires to nothing and hope", "Enable cellular", "Reset all dispositions"], 0, "Default is doing what it says.", "Name VIP and staff it."),
    ["Treat Default as a catch-all", "Name a skill on every transfer"]))
    R.append(L("l06", "Service level is the scoreboard", "practice", [
        "The skill topic includes service levels. A service level answers 'how fast is acceptable,' usually as a percent of contacts answered inside a number of seconds. It does not, by itself, reorder the queue. Priority does the ordering. The scoreboard tells you if the ordering and the staffing worked.",
        "A blend that steals agents will miss the inbound service level even when the skill is configured perfectly. The scoreboard is how you prove the steal rule.",
    ], [SKILLS, INBOUND], compare("Scoreboard versus steering", "Do not turn the scoreboard to steer.", "Service level", ["Target", "Measured later"], "Priority", ["Who is offered first", "Set before the call waits"]),
    "End of day", ["Calls", "Skill", "Report"], [
        ("Calls", "Arrive", "Inbound hits the skill.", "in"),
        ("Skill", "Target", "Eighty in twenty, or whatever you set.", "target"),
        ("Report", "Score", "The day made it or it did not.", "score"),
        ("Report", "Cause", "A missed score sends you to staffing or priority.", "cause"),
        ("Admin", "Avoid", "Raising the target does not add agents.", "avoid"),
        ("Admin", "Staff", "The steal rule changes, or the roster grows.", "staff"),
    ], [
        ("Service level without staff", ["Answers faster", "Still misses", "Changes ANI", "Signs calls"], 1, "A target is not a person."),
        ("Priority is", ["The scoreboard", "The steering", "The JRE", "The frame header"], 1, "It orders offers."),
        ("Where is service level configured?", ["On the skill group", "On the headset", "In Credly", "In the CSV only"], 1, "The skill topic."),
        ("A missed level after a blend change means", ["Look at who was stolen", "Rewrite G.711", "Enable IE", "Delete prompts"], 1, "The scoreboard is evidence."),
        ("Changing the target to be easier", ["Adds agents", "Changes the definition of success, not the roster", "Fixes busy", "Fixes paste"], 1, "Be honest about which one you did."),
    ], [("Target without people?", "Still misses."), ("What steers?", "Priority."), ("Where is the target?", "The skill."), ("Easier target?", "A new definition, not new staff.")],
    ("Pick a target", "Write a service level and the staffing sentence that could meet it.", ["Name the seconds", "Name the people", "Name what you will not change to hide a miss"], "The sentence includes people."),
    ("The target was edited from 20 seconds to 120 after a bad week", "No staff changed.", "SL was=20 now=120 ROSTER same", ["Report both definitions. Do not call it an improvement", "Delete the old number", "Add lines on predictive", "Stop recording"], 0, "The scoreboard was moved.", "Keep the original target or add people."),
    ["Set a service level you mean", "Do not move it to hide a miss"]))
    R.append(L("l07", "Skill voicemail is its own mailbox", "practice", [
        "The skill topic covers routing voicemail to the group, greetings, messages, and audio files. That mailbox is not the campaign Play prompt and not an agent's personal phone mailbox unless you have built it that way.",
        "Queue callback, on Skill Transfer, is yet another path, with its own disposition advice: the article says the default disposition is Abandon and tells you to create callback-specific codes.",
    ], [SKILLS, SKILLMOD], path("Message, callback, or agent", "Three endings.", ["Live agent", "Skill voicemail", "Queue callback"]),
    "After hours message", ["Caller", "Skill"], [
        ("Caller", "Choose", "The script offers voicemail.", "choose"),
        ("Skill", "Greet", "The skill greeting plays.", "greet"),
        ("Skill", "Store", "The message sits on the group.", "store"),
        ("Admin", "Work", "Someone with access reviews it.", "work"),
        ("Script", "Callback", "A callback path uses its own disposition.", "cb"),
        ("Admin", "Code", "Abandon is a poor name for a promised callback.", "code"),
    ], [
        ("Skill voicemail greeting is", ["Always the campaign Play file", "A skill audio object", "A codec", "A list"], 1, "The skill topic has greetings."),
        ("Default callback disposition in the article is", ["Sale", "Abandon", "VIP", "Java"], 1, "Create a specific code."),
        ("A promised callback coded as Abandon", ["Is honest", "Hides the promise in a drop statistic", "Signs STIR", "Sets ANI"], 1, "The article warns you to create specific codes."),
        ("Reviewing skill messages is", ["A carrier task", "An administrator or supervisor task on that object", "Automatic IVA", "A JRE task"], 1, "The topic includes managing the messages."),
        ("Personal mobile voicemail is", ["The same object", "Not what this topic is describing", "Required", "The Default queue"], 1, "Do not assume the cell phone mailbox."),
    ], [("Greeting object?", "Skill audio."), ("Default callback code?", "Abandon. Replace it."), ("Why a specific code?", "So the promise is visible."), ("Cell mailbox?", "Not this object.")],
    ("Three endings", "Label live, voicemail, and callback with the object and the disposition.", ["Live skill", "Skill greeting", "Callback code that is not Abandon"], "Abandon is not the callback code."),
    ("Callbacks look like abandons", "Queue callback is on and the disposition was left at the default.", "CALLBACK on DISP=Abandon", ["Create a callback disposition and use it", "Turn off reports", "Add skills at random", "Use 5G"], 0, "The article predicted this.", "Add a callback-specific code."),
    ["Give skill voicemail its own greeting", "Give callbacks their own disposition"]))
    return track("t08", "Skills routing", "Skills", "Queues, the awkward tab name, pools, levels, Default, and the scoreboard.", "Voice", "Practice", "A skill is people plus a place on the campaign. Default is what you get when you forget.", R)
