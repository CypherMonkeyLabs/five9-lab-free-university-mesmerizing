from curriculum_lib import UNIV, UNIVADMIN, UNIVPDF, BADGE, IVABLOG, PLAN, DEFAULTS, MODULES, cite, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "University is a catalog, not a secret exam code", "foundation", [
        "Five9 University is the public training front door: online classes, webinars, instructor-led classes, train-the-trainer, and custom programs. The curriculum brief this lab read is dated April 2023. Treat the mix of courses as a dated brochure.",
        "Administrator classes exist, and the community article says administrator assessments exist. It does not publish an exam code this lab can repeat. If a study guide invents Five9-CA-100 or any cousin, close it.",
    ], [UNIV, UNIVADMIN, UNIVPDF], stack("Formats named in the 2023 brief", "Re-check the live catalog.", ["Online", "Webinars", "Instructor-led", "Train-the-trainer", "Custom"]),
    "Someone quotes an exam code", ["Ask", "Page", "Refuse"], [
        ("Ask", "Code", "They name a code.", "code"),
        ("Page", "Search", "You look for it on the University pages.", "search"),
        ("Refuse", "Blank", "If it is not there, you do not memorize it.", "blank"),
        ("Refuse", "Assess", "You can say assessments exist without a code.", "assess"),
        ("Admin", "Date", "The April 2023 brief is dated when you cite it.", "date"),
        ("Admin", "Live", "The live catalog wins over the PDF.", "live"),
    ], [
        ("This lab publishes a Five9 administrator exam code. True or false?", ["True", "False", "True, Five9-CA-100", "True for partners only"], 1, "No public code was found to cite."),
        ("Formats in the April 2023 brief include", ["Only videos", "Online, webinars, ILT, train-the-trainer, and custom", "Only a lab", "Only Credly"], 1, "Those formats."),
        ("Administrator assessments", ["Do not exist", "Are mentioned, without a code this lab can quote", "Are RFC 3261", "Are the abandon default"], 1, "Mentioned, not coded."),
        ("A third-party code should be", ["Memorized", "Ignored unless Five9 publishes it", "Used as a skill name", "Typed into ANI"], 1, "Do not launder it."),
        ("The curriculum brief is", ["Eternal", "Dated April 2023. Re-check", "A SIP guide", "The EULA"], 1, "Date it."),
    ], [("Exam code in this lab?", "None."), ("Formats?", "Online, webinars, ILT, train-the-trainer, custom."), ("Assessments?", "Mentioned, no code quoted."), ("Invented codes?", "Ignore them.")],
    ("Refuse a fake code", "Write what you can say about administrator training and what you will not say.", ["Assessments exist", "No code", "The brief's date"], "The fake code is absent."),
    ("A flashcard deck uses Five9-CA-240 as the goal", "That code is not on the pages this lab cites.", "CARD code=invented", ["Delete the code and use the University catalog", "Add it to the domain", "Put it on a campaign", "Print it on badges"], 0, "Invented credentials waste people's months.", "Study the published catalog."),
    ["Say that assessments exist without inventing a code", "Date the curriculum brief"], uncertain=["The curriculum brief is from April 2023. Course lists move. This lab found no public administrator exam code to quote."]))
    R.append(L("l02", "The badge we could verify is a sales badge", "practice", [
        "Five9 IVA Sales Certified is a Credly badge. The public badge says five modules and a 20-question final, with a passing mark of 80 percent. The partner blog describes it as a sales certification for partners.",
        "It is not an engineering credential for VCC administration, IVR build, or dialer design. Passing it does not make someone the person who should change Max Abandoned Call Percentage.",
    ], [BADGE, IVABLOG, UNIV], compare("What the badge is", "Read the badge before you put it on a job description.", "Public badge", ["IVA Sales Certified", "5 modules", "20 questions", "80 percent"], "What it is not", ["A VCC admin exam", "An IVR engineer cert", "A dialer license"]),
    "A résumé arrives", ["Read", "Scope", "Job"], [
        ("Read", "Badge", "The Credly page is opened.", "badge"),
        ("Scope", "Sales", "The scope is partner sales.", "sales"),
        ("Job", "Match", "The job is compared with that scope.", "job"),
        ("Job", "Admin", "Admin work still needs the admin curriculum.", "admin"),
        ("Admin", "80", "80 percent is the published passing mark, not a trunk setting.", "80"),
        ("Admin", "No", "You do not promote the badge into an engineer cert.", "no"),
    ], [
        ("IVA Sales Certified is", ["A public sales badge", "The VCC administrator exam", "A SIP certification", "Required to dial"], 0, "Sales, via Credly and the partner blog."),
        ("The final, as published, is", ["100 questions", "20 questions", "A lab only", "Unstated"], 1, "20 questions."),
        ("The published passing mark is", ["70 percent", "80 percent", "100 percent", "A Five9 representative sets it per domain"], 1, "80 percent."),
        ("Modules published for that badge", ["5", "18", "The whole University", "None"], 0, "Five."),
        ("You should require this badge for a dialer administrator. True or false?", ["True", "False. It is a sales cert", "True for TCPA", "True for E911"], 1, "Wrong scope."),
    ], [("What is the badge?", "IVA sales, for partners."), ("Questions?", "20."), ("Pass mark?", "80 percent."), ("Admin substitute?", "No.")],
    ("Read a badge", "Write the audience and one job it does not qualify.", ["Audience", "Passing mark", "The job you will not assign from it"], "You kept the word sales."),
    ("A posting requires IVA Sales Certified for IVR engineers", "The badge does not say that.", "JOB req=sales-badge role=ivr", ["Rewrite the posting around the work and the admin curriculum", "Keep it", "Invent an engineer code", "Remove IVR from the product"], 0, "The credential and the job disagree.", "Fix the posting."),
    ["Describe the sales badge accurately", "Do not use it as an admin license"], uncertain=["Badge details were read from the public Credly page and the partner blog. Confirm the current attempt rules before you depend on them."]))
    R.append(L("l03", "Practice is the domain, not the badge", "practice", [
        "The objects you must be able to touch are the ones in the planning topic and the IVR chapter: skill groups, users, lists, dispositions, profiles, campaigns, and modules. A certification that never had you start a stopped inbound campaign did not finish the job.",
        "Use this lab's lessons as the drill. Each one ends in a lab and a fault. The fault log is synthetic. The failure mode is the one the cited page describes.",
    ], [PLAN, MODULES, UNIVADMIN], path("A drill that matches the job", "Touch the object the page names.", ["Build in the planning order", "Assign a script", "Start the campaign", "Read one report with the right role"]),
    "An interview claims admin skill", ["Ask", "Watch", "Stop"], [
        ("Ask", "Order", "They say what is built before a campaign.", "order"),
        ("Watch", "Start", "They know a stopped inbound campaign does not answer.", "start"),
        ("Watch", "Module", "They name a module from the chapter.", "mod"),
        ("Stop", "Code", "They do not recite an invented exam code.", "code"),
        ("Stop", "Default", "They do not invent an abandon percent.", "abd"),
        ("Admin", "Role", "They know Reporting is its own role.", "role"),
    ], [
        ("A finished admin practice includes", ["Only slides", "Creating the objects and starting a campaign", "Memorizing a fake code", "Buying headsets only"], 1, "The planning order is the practice."),
        ("A busy DNIS with a stopped campaign is", ["A carrier mystery first", "The expected symptom", "A Credly failure", "A matrix bug"], 1, "Start the campaign."),
        ("Naming Menu and Skill Transfer shows", ["They read the module chapter", "They passed the sales badge", "They configured BGP", "They set retention"], 0, "Those names are in the chapter."),
        ("Inventing an abandon percent in an interview is", ["A sign of confidence", "A miss. The page warns, it does not give this lab a default", "Required", "The sales exam"], 1, "Do not invent it."),
        ("The Reporting role is", ["Implied by admin", "Separate", "The sales badge", "Optional for every user"], 1, "Separate."),
    ], [("Practice equals the planning order?", "Yes."), ("Stopped campaign?", "Busy DNIS."), ("Invent a percent?", "No."), ("Reporting role?", "Separate.")],
    ("Run one drill", "Say the build order, name two modules, and say why you will not guess the abandon default.", ["Order", "Modules", "The refusal"], "You sounded like the documents."),
    ("A candidate's only evidence is the sales badge and a fake exam code", "Neither one is admin practice.", "RESUME badge=sales code=fake", ["Ask them to walk the planning order instead", "Hire on the code", "Skip skills", "Hand them production"], 0, "The evidence does not match the job.", "Interview the work."),
    ["Practice the objects", "Treat invented codes as a negative signal"]))
    R.append(L("l04", "Version timelines go stale on purpose", "advanced", [
        "Numbers you copy from a PDF are dates, not laws. The technical requirements this lab read named Salesforce managed package 2.46, ServiceNow releases Australia, Zurich, and Yokohama, JRE 8 updates 421, 451, and 461, and macOS 15 Sequoia, 26 Tahoe, and 27 Golden Gate. All of that is an October 2026 reading.",
        "A study plan that memorizes those numbers without a date will be wrong. Write 'as of' or do not write them.",
    ], [cite("Technical requirements PDF", "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf", "October 2026 reading."), UNIVPDF], stack("Numbers that need a date", "From the PDF this lab opened.", ["Salesforce package 2.46", "ServiceNow Australia, Zurich, Yokohama", "JRE 8 updates 421, 451, 461", "macOS Sequoia 15, Tahoe 26, Golden Gate 27"]),
    "A standard is being written", ["Copy", "Date", "Recheck"], [
        ("Copy", "PDF", "The number comes from the current PDF.", "pdf"),
        ("Date", "As of", "The sentence includes a date.", "date"),
        ("Recheck", "Next", "Someone owns the next read.", "next"),
        ("Recheck", "Brief", "The 2023 curriculum brief is not the version list.", "brief"),
        ("Admin", "Mac", "Java admin is not the Mac ARM answer in that PDF.", "mac"),
        ("Admin", "JRE", "The JRE updates are a list, not a vibe.", "jre"),
    ], [
        ("Package 2.46 should be taught as", ["Forever", "The package in the PDF read in October 2026", "A cert code", "A skill"], 1, "Date it."),
        ("ServiceNow release names in that reading were", ["London only", "Australia, Zurich, and Yokohama", "Any", "None"], 1, "Those three."),
        ("JRE 8 updates named were", ["421, 451, and 461", "Any Java", "Java 21 only", "None"], 0, "That list."),
        ("macOS names in that reading included", ["Only Catalina", "Sequoia 15, Tahoe 26, Golden Gate 27", "No Mac support at all", "Windows only"], 1, "Three latest non-beta, as that PDF listed them."),
        ("The April 2023 curriculum brief sets the JRE list. True or false?", ["True", "False. Different documents", "True for Mac", "True for Salesforce"], 1, "Do not cross the wires."),
    ], [("2.46?", "Dated PDF fact."), ("ServiceNow names?", "Australia, Zurich, Yokohama, in that reading."), ("JRE updates?", "421, 451, 461."), ("Curriculum brief equals the JRE list?", "No.")],
    ("Date a standard", "Copy one version number and the sentence you will put around it.", ["The number", "The date", "Who re-reads it"], "The sentence contains 'as of'."),
    ("A runbook says Golden Gate is unsupported because the author remembers Catalina", "The PDF this lab read already moved on, and the next one might too.", "STD macos=old", ["Open the current PDF and date the line", "Freeze Catalina", "Disable web admin", "Invent a cert code"], 0, "Memory is not the requirements.", "Re-read and date it."),
    ["Date every version you copy", "Re-read the PDF before you freeze a standard"], uncertain=["Salesforce 2.46, ServiceNow Australia/Zurich/Yokohama, JRE 8 updates 421/451/461, and macOS Sequoia 15, Tahoe 26, and Golden Gate 27 are from the technical requirements read in October 2026."]))
    R.append(L("l05", "How to answer without inventing", "practice", [
        "An interview answer in this lab has four beats: the object, the behavior, the page, and the gap. 'A stopped inbound campaign does not answer. The inbound topic says callers hear busy. I have not memorized a numeric abandon default.' That is a complete answer.",
        "The interview deck on this site uses the same links as the lessons. If you cannot say the page, say you do not know. Guessing a port, a percent, or a cert code is a worse answer than silence.",
    ], [PLAN, DEFAULTS, MODULES], path("Four beats", "Then stop talking.", ["Object", "Behavior", "Page", "Gap"]),
    "A panel asks a sharp question", ["Object", "Page", "Gap"], [
        ("Object", "Name", "You name the Five9 object.", "obj"),
        ("Page", "Cite", "You name the page a reviewer can open.", "page"),
        ("Gap", "Unknown", "You say what you will not invent.", "gap"),
        ("Gap", "Date", "Version numbers get a date.", "date"),
        ("Admin", "Bridge", "Cisco mappings are called a teaching bridge.", "bridge"),
        ("Admin", "Stop", "You stop. You do not fill the silence with a rumor.", "stop"),
    ], [
        ("A strong answer includes", ["Only a product logo", "Object, behavior, page, and the gap", "A fake exam code", "A 20 ms claim as fact"], 1, "Four beats."),
        ("Silence is better than", ["A cited fact", "An invented percent or port", "Naming a skill", "Saying you will look it up"], 1, "Inventions are worse than gaps."),
        ("A Cisco comparison should be labeled", ["An official wizard", "A teaching bridge", "A cert", "A codec"], 1, "We did not find a wizard."),
        ("Version numbers in an answer need", ["Nothing", "A date", "A badge", "A headset"], 1, "They go stale."),
        ("The interview deck is allowed to disagree with the lessons. True or false?", ["True", "False. Same citations", "True for sales", "True for ports"], 1, "One set of sources."),
    ], [("Four beats?", "Object, behavior, page, gap."), ("Invent a port?", "No. Stop."), ("Cisco map?", "A teaching bridge."), ("Versions?", "Dated.")],
    ("Answer one question", "Use the four beats on 'why is the DNIS busy?'", ["Object", "Page", "Gap"], "You did not blame the carrier first."),
    ("A candidate fills every gap with a precise fake number", "Precision is not evidence.", "ANSWER abandon=3 source=none", ["Ask which page says 3", "Hire them for confidence", "Add 3 to the domain", "Print the number in the glossary"], 0, "The page was the missing beat.", "Keep the gap visible."),
    ["Use object, behavior, page, and gap", "Prefer a marked unknown to a fake precision"], href="#/interview"))
    R.append(L("l06", "A study week that stays inside the documents", "practice", [
        "Six sessions cover the floor without a fake exam. One: planning order and skills. Two: inbound, lists, and the three campaign types. Three: dial modes and the abandon warning, plus the pacing lab. Four: IVR modules and the builder. Five: desktop, CRM, and WEM as neighbors. Six: SIP stories, E911, retention, and one boss incident.",
        "Each session ends by opening the page, not by highlighting this lab. The lab is a door.",
    ], [UNIV, PLAN, DEFAULTS], stack("Six sessions", "Open the page at the end of each.", ["Planning and skills", "Campaign types and lists", "Modes and the warning", "IVR modules", "Desktop, CRM, WEM", "SIP, E911, retention"]),
    "A study block", ["Read", "Touch", "Cite"], [
        ("Read", "Lesson", "One lesson, including the fault.", "lesson"),
        ("Touch", "Tool", "The builder, the simulator, or the topology, when the lesson names it.", "tool"),
        ("Cite", "Page", "The cited page is opened.", "page"),
        ("Cite", "Gap", "Uncertain notes are read, not skipped.", "gap"),
        ("Admin", "Card", "Four flashcards are answered aloud.", "card"),
        ("Admin", "Stop", "The session stops before a fake practice test.", "stop"),
    ], [
        ("The point of a session is", ["To finish a fake exam", "To touch the object and open the page", "To memorize Equinix codes forever", "To learn a prefix for 911"], 1, "The page is the authority."),
        ("Uncertain notes are", ["Errors to ignore", "Part of the lesson", "Only for lawyers", "Hidden"], 1, "Read them."),
        ("Campaign types to practice are", ["Four, including blended", "Inbound, outbound, autodial", "Only predictive", "Only skills"], 1, "Three types."),
        ("A session that never opens a Five9 page", ["Is complete", "Stopped early", "Counts as the sales badge", "Sets TLS"], 1, "Open the page."),
        ("Boss incidents use", ["Live customer data", "Synthetic logs of real failure modes", "Exam codes", "Analog headsets"], 1, "Synthetic logs."),
    ], [("Session goal?", "Object plus the page."), ("Skip uncertain notes?", "No."), ("Campaign types?", "Three."), ("Boss logs?", "Synthetic.")],
    ("Plan six sittings", "Assign one track group to each sitting and the page you will open.", ["Six titles", "Six URLs", "One tool"], "No sitting ends on this lab alone."),
    ("A study group highlights the lab and never opens the inbound topic", "They can recite the lab and still mis-state the product.", "GROUP pages=0", ["Open the cited page before the next card", "Add more highlights", "Invent an exam", "Skip faults"], 0, "The lab is not the source.", "Open the page."),
    ["End each session on the cited page", "Read the uncertain notes"], href="#/boss"))
    R.append(L("l07", "What this lab will not pretend to be", "foundation", [
        "Five9 Lab is an independent study floor. It is not Five9, not a partner portal, and not a place that can change your domain. The builder's JSON is not an import. The pacing chart is not the dialer. The 3D topology is a picture of failure, not a network map of your tenant.",
        "When a fact might have moved, the lesson says uncertain. Your next step is the linked page, then Five9 University if you want an official class. That is the whole honesty policy.",
    ], [UNIV, PLAN], compare("Use the lab for this", "Then leave it.", "Here", ["Drills", "Citations", "Marked gaps", "Three tools"], "Not here", ["A live domain", "An official exam", "Vendor support", "A file VCC imports"]),
    "You are about to cite the lab in a design", ["Check", "Link", "Vendor"], [
        ("Check", "Page", "The Five9 page is the citation.", "page"),
        ("Link", "Lab", "The lab is optional further reading.", "lab"),
        ("Vendor", "Open", "A production change goes through your administrator and Five9's own guides.", "prod"),
        ("Vendor", "Support", "An outage goes to Five9 support, not to a lesson.", "sup"),
        ("Admin", "Tool", "You can still use the tools to think.", "tool"),
        ("Admin", "Mark", "Anything you are unsure of stays marked.", "mark"),
    ], [
        ("This lab can change a production domain. True or false?", ["True", "False", "True if you export JSON", "True on the topology page"], 1, "It is a study floor."),
        ("The IVR export is", ["Importable to VCC", "A learning file", "A SIP trunk", "A badge"], 1, "Not an import."),
        ("An outage should be reported to", ["This lesson", "Five9 through your support path", "The theme picker", "A flashcard"], 1, "The vendor."),
        ("Uncertain means", ["The sentence is decorative", "Confirm it before you depend on it", "Ignore the citation", "The feature is illegal"], 1, "Go check."),
        ("Official classes live at", ["A code we invented", "Five9 University", "The pacing simulator", "Equinix"], 1, "The University page."),
    ], [("Can the lab edit your domain?", "No."), ("IVR export?", "Learning file."), ("Outage?", "Five9 support."), ("Uncertain?", "Confirm before you depend on it.")],
    ("Write the disclaimer you will actually use", "Three sentences: what the lab is, what the citation is, where an outage goes.", ["Independent study", "The vendor page", "Support"], "You did not call the lab official."),
    ("A design's only footnote is this website", "The vendor page was skipped.", "DESIGN cite=lab-only", ["Add the Five9 or RFC link, and mark the lab as study notes", "Ship it", "Add a fake exam code", "Remove the uncertain notes"], 0, "The lab is not the authority.", "Cite the source."),
    ["Cite the vendor page", "Keep this lab in the study column"], href="#/certs"))
    return track("t18", "Certifications and practice", "Practice", "University formats, the one badge we could verify, dated versions, and answers that keep their gaps.", "Practice", "Foundation", "No invented exam codes. The sales badge is a sales badge. Date every number.", R)
