from curriculum_lib import MODULES, MENU, IFELSE, SKILLPAGE, SKILLMOD, PAUSE, QUERY, STUDIO, TECH, RFC4733, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "The module list is the vocabulary", "foundation", [
        "The IVR modules chapter names the blocks you may place. The list includes Play, Menu, Get Digits, Input, Voice Input, If/Else, Case, Set Variable, Lookup Contact Record, Query, Skill Transfer, IVA Transfer, Voicemail Transfer, Set DNC, Third Party Transfer, Foreign Script, Language, and others such as Conference, Iterator, and the Salesforce modules.",
        "This lab's builder uses those names. It does not contain a module called Hangup, because that name is not in the chapter list this lab read. A transfer that completes the script is the ending the skill article describes.",
    ], [MODULES, SKILLMOD], stack("A small legal vocabulary", "Use a name from the chapter.", ["Play", "Menu", "If/Else or Case", "Skill Transfer", "IVA Transfer", "Set DNC"]),
    "Open the script folder", ["Admin", "Script"], [
        ("Admin", "Folder", "IVR scripts live in the administrator tree.", "folder"),
        ("Script", "Edit", "Open the script.", "edit"),
        ("Script", "Add", "Add a module by its published name.", "add"),
        ("Script", "Connect", "Branches leave Menu, If/Else, or Case.", "branch"),
        ("Script", "End", "Skill Transfer completes when an agent answers.", "end"),
        ("Script", "Export", "This bench's JSON is not a VCC import file.", "json"),
    ], [
        ("Hangup, as a named module in the chapter this lab read, is", ["The first module", "Not in that list", "Required", "The same as Play"], 1, "The chapter list does not include a Hangup module."),
        ("Skill Transfer ends the script when", ["The prompt finishes", "An agent is connected", "The CSV uploads", "Java starts"], 1, "The skill article says the script is complete."),
        ("The bench export is", ["An official VCC script file", "A learning model, labeled as not importable", "A report", "A SIP trunk"], 1, "The builder says so on the page."),
        ("Menu is in the modules chapter. True or false?", ["False", "True", "Only in Studio", "Only in WEM"], 1, "Menu is named."),
        ("You should invent module names for local slang. True or false?", ["True", "False. Use the chapter names so the design matches the product", "True for TCPA", "True on UK domains"], 1, "Slang does not appear in the editor."),
    ], [("Is Hangup in the chapter list?", "Not in the list this lab read."), ("When does Skill Transfer finish the script?", "When an agent connects."), ("Bench JSON?", "Not a VCC import."), ("Menu exists?", "Yes.")],
    ("Place five blocks", "In the IVR builder, build Play, Menu, Skill Transfer.", ["Use published names", "Export the JSON", "Read the warning on the file"], "The file says it is a learning model."),
    ("The design says Hangup", "A diagram ends every branch with a box that does not exist in the editor.", "BOX Hangup", ["Replace the box with the module that actually ends the path", "Ship the diagram", "Add lines", "Disable TLS"], 0, "Agents will not find Hangup in the chapter list this lab read.", "End on Skill Transfer, Voicemail Transfer, or Third Party Transfer."),
    ["Use published module names", "Treat the bench file as a model"], uncertain=["Some third-party notes mention a hangup behavior. It is not in the modules chapter quoted here."], href="#/ivr"))

    R.append(L("l02", "Play, Menu, digits, and voice", "practice", [
        "Play speaks a prompt or TTS. Menu takes a choice and has an exit per option. Get Digits and Input collect what the caller types. Voice Input and the Natural Language Processing module are the speech-side blocks in the same chapter. Input is what the ZIP-code web-service example uses, storing ZIP as a variable.",
        "A menu that has no No Match path strands people who press the wrong key. Draw that exit before you draw option 1.",
    ], [MODULES, MENU, QUERY, RFC4733], path("A menu that fails cleanly", "The failure exit is part of the design.", ["Play greeting", "Menu", "Matched digit", "No match", "Get Digits or Input"]),
    "Press 2", ["Caller", "Menu", "Next"], [
        ("Caller", "Hear", "Play or the menu prompt speaks.", "hear"),
        ("Menu", "Wait", "The module waits for a digit or speech.", "wait"),
        ("Caller", "Press", "Digit 2 arrives.", "dtmf"),
        ("Menu", "Take", "Branch 2 runs.", "take"),
        ("Menu", "Miss", "Any other digit uses No Match.", "miss"),
        ("Next", "Store", "Input can keep a ZIP in a variable.", "zip"),
    ], [
        ("The ZIP example stores the code with", ["Skill Transfer", "The Input module", "Set DNC", "Conference"], 1, "The example chooses ZIP as an Input variable."),
        ("Menu needs a failure exit because", ["DTMF is illegal", "Wrong or missing input must go somewhere", "Profiles require it", "Java requires it"], 1, "Otherwise the caller is stuck."),
        ("Voice Input and NLP are", ["Not in the chapter", "Named modules in the chapter", "Report layouts", "Trunk types"], 1, "Both names are in the modules list."),
        ("Play can speak TTS. True or false?", ["False", "True, in the web-service example", "Only English legal text", "Only on SIP UDP"], 1, "The example adds a TTS prompt."),
        ("DTMF on a SIP gateway is specified by", ["A Five9 blog only", "RFC 4733 telephone events, when the gateway uses them", "The JRE", "WEM"], 1, "RFC 4733 is the telephone-event specification. A gateway may or may not offer it."),
    ], [("ZIP module?", "Input."), ("Why No Match?", "Wrong input needs an exit."), ("Speech modules?", "Voice Input and Natural Language Processing."), ("TTS?", "Yes, in the example.")],
    ("Build the hours menu", "Use the Hours preset in the builder and press a digit.", ["Play the greeting", "Take branch 2", "Land on Skill Transfer"], "You can narrate the path."),
    ("Callers who press 9 hear silence", "The menu has options 1 and 2 and no failure exit.", "MENU options=1,2 noMatch=unset", ["Add the No Match path", "Add a Hangup module from slang", "Raise abandon", "Change ANI"], 0, "9 is not a drawn branch.", "Send No Match to a replay or an agent."),
    ["Draw the failure exit", "Store digits in a named variable"], href="#/ivr"))

    R.append(L("l03", "If/Else is two ways. Case is more", "practice", [
        "If/Else has two branches. The modules chapter includes both If/Else and Case. When you need three or more outcomes, Case is the block that exists for that. Nesting If/Else until the drawing looks like a hedge is how scripts become unreviewable.",
        "The condition is your expression: open hours, a variable, a lookup result. The module does not know your business. It evaluates what you typed.",
    ], [IFELSE, MODULES], compare("Branch count", "Pick the module that matches the count.", "Two outcomes", ["If/Else"], "Three or more", ["Case", "Menu, if the caller chooses"]),
    "Open or closed", ["Clock", "If/Else", "Script"], [
        ("Clock", "Value", "A variable says whether you are open.", "var"),
        ("If/Else", "True", "The open path plays.", "true"),
        ("If/Else", "False", "The closed path plays.", "false"),
        ("Script", "Third", "A holiday path does not fit in two branches.", "third"),
        ("Script", "Case", "Case carries the third path.", "case"),
        ("Script", "Review", "Someone else can read it.", "review"),
    ], [
        ("Two branches means", ["Case only", "If/Else", "Set DNC", "Query"], 1, "If/Else is the two-way module."),
        ("A holiday, plus open, plus closed, means", ["One If/Else", "Case, or a structure you can still read", "Play only", "A trunk"], 1, "Three outcomes do not fit one If/Else."),
        ("The module invents your hours. True or false?", ["True", "False. You supply the expression or variable", "True in Studio only", "True for ANI"], 1, "The condition is yours."),
        ("Menu is still right when", ["The clock decides", "The caller decides", "The JRE decides", "The abandon cap decides"], 1, "Menu is a caller choice. If/Else is a test."),
        ("Deeply nested If/Else is", ["Required", "A review problem. Case or a cleaner test is usually kinder", "A codec", "A list mode"], 1, "Readability is part of running the floor."),
    ], [("Two ways?", "If/Else."), ("Three ways?", "Case."), ("Who writes the condition?", "You do."), ("Caller choice?", "Menu, not If/Else.")],
    ("Convert a nest", "Replace three nested If/Else blocks with one Case in the builder.", ["Add Case", "Name three labels", "Delete the nest"], "One block, three labels."),
    ("Holiday callers hear the open greeting", "Open and closed are an If/Else. Holiday was drawn as a comment.", "IF open/closed HOLIDAY comment-only", ["Add a Case that includes holiday", "Hope", "Stop the campaign", "Switch to power"], 0, "A comment is not a branch.", "Put holiday on a real branch."),
    ["Match branch count to the module", "Keep conditions readable"], href="#/ivr"))

    R.append(L("l04", "Skill Transfer has more than a skill name", "practice", [
        "The community article lists General, Skills, Announcement, Priority, Connectors, Queue Callback, and Disposition. It also says 'six tabs' and then names more than six. Count the tabs in your editor. Do not trust the word six.",
        "Multiple skills mean any agent who has one of them may get the call. The article says Five9 recommends one skill in the module if you want useful reports. No skill selected sends calls toward users with no skills, labeled Default. Pause Before Transfer defaults to 0 and is not On Hold in a report. The default disposition named in that article is Abandon.",
    ], [SKILLMOD, SKILLPAGE, PAUSE], stack("Skill Transfer tabs to verify", "Count them in the editor.", ["General", "Skills", "Announcement", "Priority", "Connectors", "Queue Callback", "Disposition"]),
    "One skill, on purpose", ["Script", "Queue", "Report"], [
        ("Script", "One", "Only Billing is selected.", "one"),
        ("Queue", "Offer", "Billing agents are eligible.", "offer"),
        ("Script", "Many", "Adding Sales means either skill can take it.", "many"),
        ("Report", "Blur", "The article says one skill keeps reports useful.", "blur"),
        ("Queue", "None", "No selection uses the Default queue.", "default"),
        ("Report", "Pause", "Pause seconds are not hold.", "pause"),
    ], [
        ("Two skills in one module means", ["Both are required on the agent", "An agent with either skill may receive the call", "The call fails", "TCPA typing starts"], 1, "The article says any agent who has one of the skills."),
        ("Recommended count for clean reports?", ["As many as possible", "One skill in the module", "Zero", "Seven"], 1, "That is the article's recommendation."),
        ("No skill selected routes toward", ["911", "The Default queue of users without skills", "The ITSP", "Studio only"], 1, "The article describes Default."),
        ("Default disposition named in the article?", ["Sale", "Abandon", "VIP", "Java"], 1, "Create real callback codes if you use callbacks. Do not leave Abandon as your only story."),
        ("The 'six tabs' sentence", ["Matches a careful count", "Does not match the list in the same article. Count the editor", "Is a codec", "Is the abandon window"], 1, "The list is longer than six."),
    ], [("Either skill or both?", "Either."), ("Report recommendation?", "One skill per module."), ("No skill?", "Default queue."), ("Article's default disposition?", "Abandon.")],
    ("One module, one skill", "Build two Skill Transfer modules instead of one module with two skills.", ["Billing module", "Sales module", "Say why reports prefer this"], "You can tell which queue the caller entered."),
    ("Everyone gets every call", "One Skill Transfer lists Billing, Sales, and Password.", "MODULE skills=Billing,Sales,Password", ["Split them if the queues mean different work", "Add a fourth skill", "Stop reports", "Enable paste"], 0, "Any of those skills can take the call.", "One skill per module unless you truly want a shared pool."),
    ["Count the tabs in the editor", "Prefer one skill when you need the report"], uncertain=["The article says six tabs and then lists seven names. The editor is the count that matters."]))

    R.append(L("l05", "Variables, lookup, and query", "advanced", [
        "Set Variable writes a value. Lookup Contact Record reads the contact. Query calls out, and the published example is an XML web service POST whose response groups are mapped with regular expressions into variables. That example uses script variables, not call variables, because the caller is not connected to an agent.",
        "Call variables are a different object, used when you need reporting later. Enabling them does not backfill history. A Query result you never store in a reporting call variable will not appear in a historical call log.",
    ], [QUERY, MODULES, cite_cav()], compare("Two variable families", "The example is careful about this.", "Script variable", ["IVR only", "Used in the ZIP example", "Caller may never reach an agent"], "Reporting call variable", ["Must be enabled", "New calls only", "Tied to dispositions"]),
    "ZIP in, weather out", ["Caller", "Query", "Play"], [
        ("Caller", "Digits", "Input stores ZIP.", "zip"),
        ("Query", "POST", "The module posts to the service.", "post"),
        ("Query", "Map", "A grouped regex fills variables.", "regex"),
        ("Play", "TTS", "The answer is spoken.", "tts"),
        ("Script", "Keep", "Script variables die with the script's needs.", "script"),
        ("Report", "Miss", "Nothing was marked as a reporting call variable.", "miss"),
    ], [
        ("The example's HTTP style is", ["A browser GET with cookies", "XML web service POST", "FTP", "Telnet"], 1, "The example says XML Web Service POST."),
        ("Why script variables in that example?", ["The caller is not connected to an agent", "Java requires it", "ANI requires it", "Ofcom requires it"], 1, "The example says so."),
        ("Regex groups in the response", ["Are ignored", "Can be mapped to IVR variables", "Set the abandon cap", "Replace skills"], 1, "The example describes RegExp groups."),
        ("Reporting call variables apply to", ["All history", "New calls after you enable them", "Only 911", "Only lists"], 1, "The call-variable article says data is not historical."),
        ("Lookup Contact Record is", ["A rumor", "A named module", "A trunk", "A theme"], 1, "It is in the modules chapter."),
    ], [("Example request?", "XML web service POST."), ("Why script variables?", "No agent on that call."), ("History backfill?", "No."), ("Lookup exists?", "Yes.")],
    ("Trace a ZIP", "In the builder, place Input then Query then Play and name the variable.", ["Name ZIP", "Say the variable is a script variable", "Say what you would enable if reports must show it"], "You did not assume history backfills."),
    ("Last month's ZIP is missing from reports", "The variable was enabled today.", "CAV enabled=today CALLS last-month=empty", ["Accept that old calls will not grow the column", "Reboot the SBC to backfill", "Switch to vertical", "Delete the script"], 0, "The article says the data is not historical.", "Report from the enable date forward."),
    ["Keep script variables and reporting variables apart", "Do not expect a backfill"]))

    R.append(L("l06", "IVA, foreign scripts, DNC, and leaving the platform", "advanced", [
        "IVA Transfer hands the call to a Studio task. Foreign Script jumps to another IVR script. Set DNC is the removal action. Third Party Transfer leaves your agents. Language switches prompt language. These are five different exits. A diagram that says 'send to bot' does not say which one.",
        "Digital IVA integration, in the March 2026 Studio article, needs a Studio API key with Build permission and a ChatBot task key pasted into the VCC side. Voice IVA Transfer is not automatically that digital article. Confirm which channel you are wiring.",
    ], [MODULES, STUDIO], path("Five exits", "Name the module.", ["IVA Transfer", "Foreign Script", "Set DNC", "Third Party Transfer", "Language"]),
    "A bot, then a person", ["IVR", "Studio", "Agent"], [
        ("IVR", "Language", "The language module sets the prompts.", "lang"),
        ("IVR", "IVA", "IVA Transfer calls the task.", "iva"),
        ("Studio", "Contain", "The bot finishes, or it does not.", "bot"),
        ("IVR", "Skill", "A later Skill Transfer is the human path.", "skill"),
        ("IVR", "DNC", "A removal uses Set DNC, not the bot.", "dnc"),
        ("IVR", "Leave", "Third party is a different exit.", "leave"),
    ], [
        ("A second script is called with", ["Set Variable only", "Foreign Script", "The JRE", "A list reset"], 1, "Foreign Script is the module."),
        ("Removal from calling uses", ["Language", "Set DNC", "Conference", "Iterator only"], 1, "Set DNC is the named module."),
        ("Digital IVA setup in the 2026 article needs", ["Only an ANI", "An API key with Build permission and a task key", "A matrix report", "IE 11"], 1, "Those are the article's ingredients."),
        ("That digital article is automatically the voice IVA Transfer screen. True or false?", ["True", "False. Confirm the channel", "True for all domains", "True if paste works"], 1, "ChatBot task and voice transfer are different write-ups."),
        ("Third Party Transfer keeps the call on your skill. True or false?", ["True", "False. It forwards outside", "True at night", "True for preview"], 1, "It is the leave-the-queue module."),
    ], [("Jump to another script?", "Foreign Script."), ("Opt out?", "Set DNC."), ("Digital keys?", "Build permission plus a task key."), ("Third party stays on your skill?", "No.")],
    ("Label five arrows", "On a sketch, name the module for each arrow.", ["Bot", "Other script", "Opt out", "Outside number", "Language"], "No arrow says 'stuff'."),
    ("Opt-out calls the bot", "The removal digit starts IVA Transfer.", "DIGIT 9 -> IVA Transfer", ["Point digit 9 at Set DNC", "Add more bots", "Raise power lines", "Stop the domain"], 0, "A bot is not the DNC list.", "Use Set DNC."),
    ["Name the exit module", "Keep digital IVA and voice IVA in their own notes"], uncertain=["Public pages describe IVA Transfer and a digital ChatBot integration separately. This lab does not claim they share one property sheet."]))

    R.append(L("l07", "Visual IVR and frames", "advanced", [
        "The technical requirements say administrators can apply web page security so a Visual IVR script is not embedded in a frame where the user can be hijacked. The mechanism named is the X-Frame-Options header. The browser table in that PDF lists old versions and tells you to test others.",
        "A visual script is still a script: prompts, branches, and a handoff. Framing is an extra threat. Do not treat a 2016-era browser row as the current support list. The PDF says to retest.",
    ], [TECH, MODULES], stack("Visual path plus a frame rule", "The script and the frame are both real.", ["Visual script", "X-Frame-Options", "Retest the browser", "Do not trust the old matrix"]),
    "A page embeds the IVR", ["Browser", "Five9", "Attacker"], [
        ("Browser", "Load", "Someone iframes the visual script.", "iframe"),
        ("Five9", "Header", "X-Frame-Options can refuse the frame.", "header"),
        ("Attacker", "Click", "Without the header, the user can be hijacked.", "click"),
        ("Admin", "Set", "Web page security is an administrator option.", "set"),
        ("Admin", "Test", "The PDF says to test browsers it does not list.", "test"),
        ("Caller", "Phone", "The voice script is a different surface.", "voice"),
    ], [
        ("The header named for visual IVR framing is", ["SIP-Route", "X-Frame-Options", "ANI", "STIR"], 1, "The PDF names X-Frame-Options."),
        ("The browser table in the PDF is", ["The 2026 support promise", "Old, and the PDF says to test other versions", "A dialer mode", "A skill list"], 1, "Chrome versions in the forties are not a current matrix."),
        ("Visual IVR security is", ["A carrier ticket", "An administrator control on the script", "A headset setting", "A list mode"], 1, "The PDF says VCC administrators apply it."),
        ("Voice IVR and visual IVR are", ["The same frame problem", "Related products with different surfaces", "Both illegal", "Both JRE updates"], 1, "Framing is a web problem."),
        ("You should copy the PDF's Chrome 46 row into a 2026 standard. True or false?", ["True", "False. Retest", "True for UK domains", "True for TCPA"], 1, "The PDF invites a test."),
    ], [("Which header?", "X-Frame-Options."), ("Trust the old browser table?", "No. Retest."), ("Who turns it on?", "A VCC administrator."), ("Voice versus visual?", "Different surfaces.")],
    ("Frame test", "Write the header you expect and the browser you would actually test.", ["Name X-Frame-Options", "Name a current browser", "Say you will not cite Chrome 46 as current"], "The note does not treat 2016 as now."),
    ("The visual script is embedded on a partner site", "Web page security is off. Users report the page 'moved' under them.", "XFO unset HOST partner-iframe", ["Turn on web page security and retest", "Add predictive lines", "Reset Sale", "Change list penetration"], 0, "The frame is allowed.", "Set the option and confirm the header."),
    ["Protect visual IVR from hostile frames", "Retest browsers"], uncertain=["The PDF's browser matrix is historical. Current browser behavior has to be tested."], href="#/ivr"))
    return track("t07", "IVR scripts", "IVR", "The module vocabulary, branches, Skill Transfer, queries, and visual framing.", "Voice", "Practice", "Scripts are named modules. The builder speaks that vocabulary and does not pretend to export a VCC file.", R)

def cite_cav():
    from curriculum_lib import CAV
    return CAV
