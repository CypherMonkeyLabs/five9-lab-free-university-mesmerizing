from curriculum_lib import STUDIO, TECH, MODULES, GENAI, ENGAGE, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "Studio has regions", "foundation", [
        "The technical requirements publish Studio portal hosts by region: five9.us, five9.au, five9.ca, five9.uk, and five9.br studioportal.io, plus older inferencecommunications.com names. A task built in the wrong region will not be the task your VCC domain can call.",
        "SIP notes in that same part of the PDF, including UDP 5060 and a beta TCP 5061, are labeled next to Studio SBC material. Do not paste those ports onto every VCC trunk without checking which SBC family the domain uses. DNS SRV is the preferred way to find Five9 SIP resources.",
    ], [TECH], stack("Studio portals in the PDF", "Pick the region that matches the domain.", ["US", "Australia", "Canada", "UK", "Brazil"]),
    "Open the right portal", ["Admin", "Studio"], [
        ("Admin", "Region", "The VCC domain's region is known.", "region"),
        ("Studio", "Host", "The matching studioportal host is opened.", "host"),
        ("Studio", "Task", "The task is created there.", "task"),
        ("VCC", "Point", "IVA Transfer or the digital key points at that task.", "point"),
        ("Net", "SRV", "SIP targets prefer DNS SRV.", "srv"),
        ("Net", "Avoid", "A copied IP from the PDF is not a forever allow-list.", "ip"),
    ], [
        ("A US Studio task belongs on", ["Any portal", "The US portal published for that region", "The Brazil portal by default", "A local HTML file"], 1, "The PDF splits portals by region."),
        ("Old inferencecommunications.com hosts are", ["Invented", "Also listed in that PDF table", "Illegal", "Codecs"], 1, "They appear beside the studioportal names."),
        ("DNS SRV is", ["Discouraged", "The preferred way to reach Five9 SIP resources, in that PDF", "A dialer mode", "A skill"], 1, "The PDF says so, and tells you IPs can change."),
        ("Studio SIP ports in the PDF apply automatically to every VCC trunk. True or false?", ["True", "False. Confirm the SBC family", "True for analog headsets", "True for lists"], 1, "The notes sit with the Studio SBC section."),
        ("Pinning one IP forever is", ["The PDF's advice", "The opposite of the DNS SRV note", "Required for QM", "Required for ANI"], 1, "Addresses change."),
    ], [("Region matters?", "Yes. Use the matching portal."), ("Legacy hosts listed?", "Yes."), ("How to find SIP?", "DNS SRV."), ("Paste Studio ports onto every trunk?", "No. Confirm the family.")],
    ("Pick a host", "For a Canadian domain, name the portal host from the PDF.", ["five9.ca.studioportal.io", "Not the US host", "SRV instead of a pinned IP"], "The host matches Canada."),
    ("The bot works in test and fails in production", "The task was built in the US portal and the domain is in the UK.", "TASK us DOMAIN uk", ["Rebuild or reference the task in the UK portal", "Add predictive lines", "Change ANI", "Disable WSS"], 0, "The regions do not match.", "Use the UK Studio portal."),
    ["Match Studio region to the domain", "Prefer DNS SRV over a pinned IP"], uncertain=["Studio signaling ports in the PDF are easy to misread as universal VCC trunk ports. Confirm which SBC your domain uses."]))
    R.append(L("l02", "A task key is not a vibe", "practice", [
        "IVA Transfer is a module. It needs a task to transfer to. The digital integration article, dated in the community as 26 March 2026, says you copy a ChatBot task key into the VCC IVA transfer side after the Studio task exists.",
        "Voice and digital write-ups are separate. Use the article that matches the channel. A key with no Build permission, in that digital article, is not enough: the key is created with Build selected.",
    ], [STUDIO, MODULES], path("Digital path from the 2026 article", "Key, then task, then VCC.", ["API key with Build", "ChatBot task", "Copy task key", "VCC side"]),
    "Wire a digital bot", ["Studio", "VCC"], [
        ("Studio", "Key", "Create an API key.", "key"),
        ("Studio", "Build", "Grant Build on that key.", "build"),
        ("Studio", "Task", "Create a ChatBot task.", "task"),
        ("Studio", "Copy", "Copy the task key.", "copy"),
        ("VCC", "Paste", "The VCC authentication and transfer use those values.", "paste"),
        ("VCC", "Test", "A digital contact reaches the bot.", "test"),
    ], [
        ("The March 2026 article requires which permission on the API key?", ["Reporting only", "Build", "Headset", "ANI"], 1, "It says select Build."),
        ("The task type in that article is", ["Predictive", "ChatBot", "Skill group", "Campaign profile"], 1, "Create ChatBot task."),
        ("The task key goes", ["Into a disposition comment", "Into the VCC IVA transfer side", "Into the JRE", "Into MyE911"], 1, "The article says to paste it there."),
        ("A voice IVA design can ignore that article. True or false?", ["Always true", "You need the voice write-up. Do not assume the ChatBot steps are the voice screen", "False, they are identical", "True if you paste"], 1, "Channel matters."),
        ("IVA Transfer without a task", ["Still contains the caller", "Has nowhere real to send them", "Sets DNC", "Changes list mode"], 1, "The module needs a target."),
    ], [("Digital key permission?", "Build."), ("Task type in that article?", "ChatBot."), ("Where does the key go?", "The VCC side."), ("Same as voice?", "Do not assume.")],
    ("Checklist", "Order the four digital steps.", ["API key", "Build permission", "ChatBot task", "Paste into VCC"], "The order matches the article."),
    ("The bot returns 401", "The key exists and Build was never selected.", "KEY build=false", ["Edit the key and grant Build", "Add skills", "Lower abandon", "Change codec"], 0, "The article makes Build required.", "Grant Build and retest."),
    ["Follow the digital key steps", "Keep voice steps in their own note"], uncertain=["Voice IVA Transfer property names are not copied key-for-key from the digital article."]))
    R.append(L("l03", "Contain, or hand back with context", "practice", [
        "A useful bot either finishes the job or returns the caller to a skill with the reason intact. IVA Transfer that dead-ends, or a Skill Transfer with no skill, is how you manufacture the Default queue.",
        "The Engage page describes sentiment and a handoff to a human with context. Treat that as the product story. The variables you actually pass are the ones you stored. A script variable the reporting side never enabled will not be in the historical report.",
    ], [ENGAGE, MODULES, cite_cav()], path("Contain or return", "Both endings are designed.", ["IVA", "Contained", "Or skill", "With a variable the agent can see"]),
    "The bot cannot refund", ["Bot", "IVR", "Agent"], [
        ("Bot", "Fail", "The refund is out of scope.", "fail"),
        ("IVR", "Branch", "The failure branch is drawn.", "branch"),
        ("IVR", "Set", "A variable records the reason.", "var"),
        ("IVR", "Skill", "Skill Transfer names Billing.", "skill"),
        ("Agent", "See", "The desktop shows the reason.", "see"),
        ("Report", "Later", "A reporting call variable was enabled if history matters.", "cav"),
    ], [
        ("A bot with no failure branch", ["Is complete", "Drops the caller when it cannot finish", "Sets ANI", "Is required"], 1, "Draw the return path."),
        ("Default queue is what you get if", ["The skill is named", "Skill Transfer has no skill", "TLS 1.2 is on", "The schedule is right"], 1, "Select the skill."),
        ("Context the agent sees is", ["Automatic from any variable", "What you passed and what the desktop integration shows", "Always in last year's call log", "A codec"], 1, "Store it on purpose."),
        ("Historical reports of that variable require", ["Nothing", "A reporting call variable, and only for new calls", "A JRE", "Paste"], 1, "No backfill."),
        ("Engage's handoff story includes", ["Context to the human", "Deleting the skill", "Stopping recording", "Analog headsets"], 1, "The page describes a handoff with context."),
    ], [("No failure branch?", "The caller is stranded."), ("No skill selected?", "Default."), ("History?", "Enable a reporting call variable. New calls only."), ("Engage handoff?", "With context.")],
    ("Draw both endings", "Contained, and returned to Billing with a reason variable.", ["Name the variable", "Name the skill", "Say what Default would mean"], "Both endings are real modules."),
    ("Refund callers reach new hires", "The failure branch uses Skill Transfer with no skill, and new hires have none.", "SKILLS empty", ["Select Billing", "Add more bots", "Raise power", "Disable reports"], 0, "Default caught them.", "Name the skill."),
    ["Design both endings", "Pass a reason the agent can see"], href="#/ivr"))
    R.append(L("l04", "GenAI Studio is a hub, not a slogan", "advanced", [
        "The GenAI Studio page describes a low-code hub: choose among models, attach knowledge and customer data, test on real call data, keep a prompt library, and control output. It says the hub powers Five9 AI applications and initially focuses on Agent Assist summaries.",
        "Engine-agnostic means you do not get to write a single model name into an architecture slide until the hub shows it. Responsible AI, on that page, is part of the claim. A prompt you cannot test is not a control.",
    ], [GENAI], stack("Studio controls you can ask to see", "From the GenAI Studio page.", ["Model choice", "Knowledge", "Prompt library", "Tests on call data", "Output control"]),
    "A summary prompt changes", ["Author", "Hub", "Call"], [
        ("Author", "Write", "The prompt is in the library.", "prompt"),
        ("Hub", "Model", "A model is selected there.", "model"),
        ("Hub", "Test", "Real call data is used to test.", "test"),
        ("Hub", "Bound", "Output controls limit the shape.", "bound"),
        ("Call", "Summary", "Agent Assist shows the result.", "sum"),
        ("Author", "Revise", "A bad test changes the prompt, not the slide.", "revise"),
    ], [
        ("GenAI Studio is described as", ["A single fixed model", "Engine-agnostic", "A dialer", "A trunk"], 1, "The page says you can choose models."),
        ("Initial application focus on that page includes", ["SIP trunks", "Agent Assist summaries", "Headset SKUs", "Equinix"], 1, "Summaries are the named start."),
        ("Testing is described with", ["Synthetic hopes only", "Real call data", "A JRE", "A list reset"], 1, "The page says real call data."),
        ("A prompt that was never tested", ["Is a control", "Is not the testing story the page tells", "Sets DNC", "Is TLS"], 1, "Test is part of the hub."),
        ("Knowledge and customer data are", ["Forbidden", "Part of the page's personalization claim", "A codec", "A skill tab"], 1, "The page includes them."),
    ], [("Engine-agnostic?", "Yes."), ("First named app?", "Agent Assist summaries."), ("Test data?", "Real calls, per the page."), ("Untested prompt?", "Not the control the page describes.")],
    ("Name the screen", "List the five controls you would ask an admin to show you.", ["Model", "Prompt", "Knowledge", "Test", "Output control"], "You did not accept 'we use AI'."),
    ("Summaries invent a refund policy", "The prompt was edited in a slide and never tested on calls.", "PROMPT untested OUTPUT refunds-for-all", ["Test on real calls and constrain the output", "Ship it", "Delete QM", "Change list mode"], 0, "The hub's own page says to test and control output.", "Run the test before the prompt is live."),
    ["Ask to see model, prompt, and test", "Do not ship an untested summary"]))
    R.append(L("l05", "NLP in the IVR is not the same as Studio", "advanced", [
        "The modules chapter includes a Natural Language Processing module and Voice Input, and it also includes IVA Transfer. They are different blocks. NLP inside a script is not automatically a Studio task, and a Studio task is not automatically the NLP module.",
        "Pick the block that matches the design. If the work is a Studio bot with a task key, use IVA Transfer and the Studio article. If the work is a grammar in the IVR, use the IVR module and its own properties.",
    ], [MODULES, STUDIO], compare("Two language tools", "Do not swap the names.", "IVR NLP or Voice Input", ["A module in the script"], "Studio via IVA Transfer", ["A task, a key, a region"]),
    "Choose the block", ["Need", "Module"], [
        ("Need", "Grammar", "A small speech choice inside the script.", "grammar"),
        ("Module", "Voice", "Voice Input or NLP.", "voice"),
        ("Need", "Bot", "A Studio conversation.", "bot"),
        ("Module", "IVA", "IVA Transfer plus a task.", "iva"),
        ("Admin", "Region", "The task's portal matches the domain.", "region"),
        ("Admin", "Write", "The design names the block.", "write"),
    ], [
        ("NLP module and IVA Transfer are", ["The same block", "Different modules", "Both dialer modes", "Both profiles"], 1, "Both names are in the chapter, separately."),
        ("A Studio task is attached with", ["Set DNC", "IVA Transfer and the task identity", "List penetration", "A headset"], 1, "That is the handoff."),
        ("A short speech menu can stay", ["Only in Studio", "In the IVR module", "Only in WEM", "Only in a CSV"], 1, "Voice Input exists for that."),
        ("Region still matters for", ["A local If/Else", "A Studio task", "A disposition", "A pause of zero"], 1, "The portal is regional."),
        ("Naming the wrong block", ["Is fine if the slide is pretty", "Sends the builder to the wrong system", "Sets ANI", "Fixes abandon"], 1, "The editor will not guess."),
    ], [("Same block?", "No."), ("Studio handoff?", "IVA Transfer."), ("Short speech menu?", "An IVR module can do it."), ("Wrong name?", "Wrong system.")],
    ("Label the box", "On two designs, write the module name.", ["A yes-or-no speech check", "A Studio billing bot"], "The labels differ."),
    ("The team built a grammar and called it Studio", "No task key exists. The module is Voice Input.", "MODULE VoiceInput DOC says Studio", ["Rename the design to the module you used", "Invent a task key", "Stop inbound", "Enable IE"], 0, "The document lies.", "Say Voice Input unless a Studio task is really there."),
    ["Use the module name you configured", "Keep Studio for tasks with keys"]))
    R.append(L("l06", "Prompts are a production change", "advanced", [
        "A prompt library in GenAI Studio is production configuration. Changing a summary prompt changes what agents and customers are told. The page says you can test with call data and control output. A change without a test is how a policy you do not have gets spoken.",
        "IVR prompts are a different library. The planning topic has you record those before the script. Swapping a WAV and swapping a GenAI prompt are both releases. Neither belongs in an unreviewed chat message.",
    ], [GENAI, cite_plan()], compare("Two prompt libraries", "Both are releases.", "IVR prompt", ["WAV or TTS in the script", "Recorded before the script, per planning"], "GenAI prompt", ["In the hub", "Tested on calls"]),
    "A one-line edit", ["Author", "Test", "Release"], [
        ("Author", "Edit", "The summary prompt changes.", "edit"),
        ("Test", "Calls", "Real calls are run through it.", "test"),
        ("Test", "Fail", "It invents a policy.", "fail"),
        ("Author", "Revert", "The prompt goes back.", "revert"),
        ("Release", "Note", "Someone writes what changed.", "note"),
        ("IVR", "Separate", "The WAV library is a different change.", "wav"),
    ], [
        ("A GenAI prompt change is", ["Cosmetic", "A production change", "A codec", "A skill tab"], 1, "It changes what is said."),
        ("The page's test material is", ["Optional folklore", "Real call data", "A JRE", "A DNIS"], 1, "Test on calls."),
        ("IVR WAV changes are", ["The same object as the GenAI prompt", "A separate library", "Automatic", "A list mode"], 1, "Do not confuse the two releases."),
        ("An invented refund in a summary means", ["The test failed and the prompt is not ready", "Ship faster", "Raise lines", "Delete skills"], 1, "Output control exists for this."),
        ("Planning says IVR prompts are recorded", ["After go-live", "Before the scripts are built", "Never", "Only in Studio"], 1, "That is the roadmap."),
    ], [("Prompt edit?", "A release."), ("Test on?", "Call data."), ("Same as a WAV?", "No."), ("Invented policy?", "Not ready.")],
    ("Write the release note", "One GenAI prompt change, in three lines.", ["What changed", "What the test showed", "Who can roll it back"], "The note would stop a bad prompt."),
    ("The summary started offering credits", "A prompt edit went out from a chat thread with no test.", "PROMPT live test=none", ["Roll back and test", "Add more credit language", "Switch to power dialing", "Disable WSS"], 0, "There was no test.", "Restore the last tested prompt."),
    ["Treat prompt edits as releases", "Test on calls before they go live"]))
    R.append(L("l07", "A bot review you can finish", "advanced", [
        "Region, key permission, task type, failure branch, named skill, variable the agent sees, prompt test, and the recording clock. Eight checks. Each one has a page. A bot project that cannot pass them is a slide.",
        "The pacing bench and the IVR builder can illustrate the return path. They do not host Studio.",
    ], [STUDIO, GENAI, TECH, cite_ret()], path("Eight checks", "Then the bot can be discussed.", ["Region", "Build key", "Task", "Failure branch", "Skill", "Variable", "Prompt test", "Recording clock"]),
    "Review", ["Reviewer", "Studio", "VCC"], [
        ("Reviewer", "Region", "Portal matches the domain.", "region"),
        ("Reviewer", "Key", "Build is on.", "key"),
        ("Reviewer", "Fail", "The failure branch names a skill.", "fail"),
        ("Reviewer", "Var", "The agent can see the reason.", "var"),
        ("Reviewer", "Test", "The prompt has a call-data test.", "test"),
        ("Reviewer", "Tape", "The offload would keep the audio.", "tape"),
    ], [
        ("A bot review without a region is", ["Fine", "Incomplete", "A codec", "A list mode"], 1, "The portal is regional."),
        ("Build permission is from", ["The March 2026 digital article", "The headset page", "RFC 3261", "The retention page"], 1, "That article requires it for the digital key."),
        ("The recording clock matters because", ["Bots are not recorded", "You may need the audio after 30 days", "ANI changes", "Java changes"], 1, "Retention still applies."),
        ("The IVR builder hosts Studio. True or false?", ["True", "False", "True if you export JSON", "True on UK domains"], 1, "The builder is a learning model."),
        ("Default as the failure skill is", ["A good VIP path", "The catch-all you were warned about", "STIR", "A profile"], 1, "Name a real skill."),
    ], [("Skip region?", "The review is incomplete."), ("Build permission source?", "The digital IVA article."), ("Why the clock?", "Audio expires."), ("Does this lab host Studio?", "No.")],
    ("Run the eight", "Tick them on a paper bot.", ["Region", "Key", "Task", "Branch", "Skill", "Variable", "Test", "Offload"], "Any blank tick stops the review."),
    ("The bot is 'done' with no failure skill", "Contained calls work. Everyone else hears Default.", "FAIL branch skill=empty", ["Name the skill before go-live", "Call it done", "Add lines", "Disable recording"], 0, "The return path is the catch-all.", "Select the skill."),
    ["Finish the eight checks", "Refuse a slide that skips them"], href="#/ivr"))
    return track("t11", "IVA and GenAI", "IVA", "Studio regions, task keys, handoffs, and prompts that are production changes.", "Intelligence", "Advanced", "A bot is a task in the right region, with a way back to a named skill, and a prompt that was tested.", R)

def cite_cav():
    from curriculum_lib import CAV
    return CAV

def cite_plan():
    from curriculum_lib import PLAN
    return PLAN

def cite_ret():
    from curriculum_lib import RETAIN
    return RETAIN
