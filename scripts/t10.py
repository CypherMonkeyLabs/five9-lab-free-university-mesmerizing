from curriculum_lib import WEM, WEMDS, ADP, RETAIN, EULA, lesson, stack, compare, path, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "Five9 WEM and a Verint path both exist", "foundation", [
        "The workforce page says Five9 offers WEM natively and also partners with vendors such as Verint so a customer can fit the suite they already run. It says Five9 manages installation, configuration, maintenance, and upgrades for the WEM solution they deliver.",
        "Do not tell a floor they are 'on Verint' or 'on native WEM' without looking. The page says both exist. Recording, QM, analytics, WFM, surveys, and CRM connectors are the pieces the data sheet says you integrate.",
    ], [WEM, WEMDS], compare("Two public statements", "Ask which one this domain uses.", "Native Five9 WEM", ["Offered on the product page"], "Partner suite", ["Verint is named as an example"]),
    "Ask which suite", ["Admin", "Suite"], [
        ("Admin", "Ask", "Which WEM is in the contract?", "ask"),
        ("Suite", "Native", "Schedules may be the Five9 suite.", "native"),
        ("Suite", "Partner", "Or a named partner suite.", "partner"),
        ("Suite", "Pieces", "QM, WFM, analytics, surveys, recording.", "pieces"),
        ("Desktop", "Show", "Plus can surface schedules either way the page describes.", "show"),
        ("Admin", "Own", "Five9 says they run the maintenance.", "own"),
    ], [
        ("Verint is", ["The only WEM Five9 allows", "Named as a partner path beside native WEM", "A codec", "A campaign type"], 1, "The product page says both."),
        ("The data sheet pieces include", ["Only dialer modes", "Recording, QM, analytics, WFM, surveys, CRM connectors", "Only SIP", "Only Java"], 1, "That is the data sheet's list of integrations."),
        ("Who does the WEM upgrades, per the product page?", ["The agent's headset vendor", "Five9, for the solution they deliver", "The caller", "The ITSP only"], 1, "The page says Five9 manages upgrades."),
        ("You should guess native versus Verint. True or false?", ["True", "False. Look at the contract or the app", "True in UK domains", "True for TCPA"], 1, "The page refuses a single answer."),
        ("Plus showing a schedule proves which vendor. True or false?", ["True", "False. The desktop page says the function can appear there either way", "True if ANI is local", "True if Java is gone"], 1, "The screen is not the vendor name."),
    ], [("Verint?", "A named partner path, not the only path."), ("Data sheet pieces?", "Recording, QM, WFM, analytics, surveys, connectors."), ("Who upgrades?", "Five9, per the page."), ("Guess the vendor?", "No.")],
    ("Write the question", "The first WEM question on a new floor.", ["Which suite", "Which pieces are in the contract", "Where the agent sees the schedule"], "You did not assume Verint."),
    ("A runbook says to open Verint. The floor is native.", "Agents cannot find the URL.", "RUNBOOK verint APP native", ["Open the suite that is actually installed", "Keep the wrong URL", "Delete skills", "Enable TLS 1.1"], 0, "The runbook guessed.", "Point it at the native app."),
    ["Ask which WEM", "List the pieces in the contract"], uncertain=["This lab does not know which suite a given customer bought. The product page says both native WEM and partners such as Verint are offered."]))
    R.append(L("l02", "Workforce management is the roster", "practice", [
        "WFM, in the product language, is how you staff to the work: schedules, intraday changes, adherence. It is not the dialer mode and not the service level target, though it exists so those can be met.",
        "A predictive book that uses headcount instead of the schedule will overdial at every planned break. The roster is an input to the mode you already chose.",
    ], [WEM, ADP], path("From forecast to Ready", "The dialer should see the second number.", ["Forecast", "Schedule", "Who is Ready", "Mode uses that count"]),
    "Tuesday at 10", ["WFM", "Floor", "Dialer"], [
        ("WFM", "Forecast", "The expected inbound volume is written.", "fcst"),
        ("WFM", "Schedule", "People are placed against it.", "sched"),
        ("Floor", "Break", "A break removes people.", "break"),
        ("Floor", "Ready", "The remainder can take contacts.", "ready"),
        ("Dialer", "Use", "Lines are based on Ready.", "use"),
        ("Report", "Adhere", "Adherence says who ignored the plan.", "adh"),
    ], [
        ("WFM replaces the dialing mode. True or false?", ["True", "False. It supplies the people the mode needs", "True for autodial only", "True for ANI"], 1, "Modes and rosters are different objects."),
        ("A scheduled break is", ["Idle opportunity", "A person the dialer should not count", "A DNIS", "A prompt"], 1, "They are not available."),
        ("Adherence measures", ["Codec quality", "Whether people followed the schedule", "STIR attestation", "Frame headers"], 1, "Plan versus actual."),
        ("Service level is met by", ["Renaming the target only", "Having the people the schedule promised", "A louder greeting", "Paste"], 1, "The roster is the supply."),
        ("Intraday change is", ["Forbidden", "Part of a living schedule when volume moves", "A JRE flag", "A list mode"], 1, "The product page discusses intraday adjustment in its WFM description."),
    ], [("Does WFM pick preview vs power?", "No. It staffs."), ("Break?", "Not available."), ("Adherence?", "Plan versus actual."), ("Service level needs?", "The people.")],
    ("Staff from the schedule", "Given 30 scheduled and 6 on break, set the agent count in the simulator.", ["Subtract 6", "Run progressive", "Note occupancy"], "You did not type 30."),
    ("The dialer was built from the org chart", "Breaks are real and abandon alarms fire on the hour.", "COUNT orgchart=80 schedule=54", ["Use the schedule", "Use the org chart harder", "Disable monitoring", "Stop IVR"], 0, "The org chart is not the roster.", "Pace from the schedule."),
    ["Feed the dialer from the schedule", "Treat adherence as evidence"], href="#/pacing"))
    R.append(L("l03", "Quality management listens on purpose", "practice", [
        "The product page describes multi-channel evaluations, desktop monitoring, and automated scoring. The desktop page says agents can review evaluations without leaving Plus. That is QM: a sample of work, a score, a conversation with the person.",
        "A 100 percent score on a form nobody respects is not quality. The form has to match the call the customer had. Recording is the evidence. The EULA says recordings include hold and what happens after a transfer, and that the customer must meet notice and consent laws.",
    ], [WEM, ADP, EULA], stack("A fair evaluation", "Evidence, form, conversation.", ["Recording", "Form that matches the work", "Score", "Review on the desktop"]),
    "One evaluation", ["Record", "Form", "Agent"], [
        ("Record", "Exist", "The call was recorded, including hold, per the EULA.", "rec"),
        ("Form", "Fit", "The form matches that kind of call.", "form"),
        ("QM", "Score", "A person or a rule scores it.", "score"),
        ("Agent", "See", "Plus can show the evaluation.", "see"),
        ("Law", "Notice", "Consent and notice are the customer's duty.", "law"),
        ("QM", "Coach", "The score starts a conversation.", "coach"),
    ], [
        ("Evaluations in Plus are", ["Hidden from agents", "Named on the desktop page", "A trunk feature", "A list mode"], 1, "Agents can review them there."),
        ("The EULA says recordings include", ["Only the first second", "Hold and the call after transfer", "Only IVR", "Only 911"], 1, "Hold and post-transfer are in the EULA."),
        ("Notice and consent are", ["Five9's problem alone, in the EULA", "The customer's duty when they use recording", "Optional", "A codec"], 1, "The EULA assigns that compliance to the customer."),
        ("A form that scores the wrong behavior", ["Is efficient", "Teaches the wrong call", "Sets ANI", "Fixes abandon"], 1, "The form is the definition of good."),
        ("Automated scoring, on the product page, is", ["Absent", "Part of the QM description", "Illegal", "A JRE feature"], 1, "The page mentions automated scoring and evaluation selection."),
    ], [("Where do agents read evaluations?", "Plus, per the desktop page."), ("Hold recorded?", "Yes, per the EULA."), ("Who handles consent?", "The customer, per the EULA."), ("Wrong form?", "Teaches the wrong work.")],
    ("Score one behavior", "Write a single evaluation line a stranger could apply to a recording.", ["Name the behavior", "Name the evidence", "Say it is not a vibe"], "The line points at something audible."),
    ("Agents are scored on a sales form for a complaint queue", "The form was copied from another campaign.", "FORM sales QUEUE complaints", ["Use a form that matches complaints", "Keep the sales form for speed", "Delete recordings", "Enable TLS 1.1"], 0, "The form is the wrong definition.", "Score the work they were asked to do."),
    ["Match the form to the queue", "Remember hold is in the recording"]))
    R.append(L("l04", "Analytics and surveys sit beside the call", "practice", [
        "The data sheet and the product page put interaction analytics and customer surveys next to QM and WFM. Analytics is how you see topics across many calls. A survey is how the customer scores the one call. They are not the abandon rate and they are not a disposition, unless you deliberately map them.",
        "This lab does not claim a specific analytics vendor screen. Native WEM and a partner suite will not look identical. The question to ask is which topics you will act on.",
    ], [WEM, WEMDS], compare("Three scores", "Do not average them into one vanity number.", "Abandon", ["A dialer outcome", "Not a survey"], "Survey and analytics", ["The customer's score", "A pattern across calls"]),
    "A topic spikes", ["Calls", "Analytics", "Action"], [
        ("Calls", "Happen", "Many contacts mention a fee.", "fee"),
        ("Analytics", "Cluster", "The topic is visible.", "topic"),
        ("Survey", "Drop", "Scores fall on those calls.", "score"),
        ("Action", "Script", "The IVR or the agent form changes.", "change"),
        ("Action", "Avoid", "Nobody averages this with abandon and calls it 'health'.", "avoid"),
        ("Admin", "Suite", "The screen depends on which WEM you bought.", "suite"),
    ], [
        ("A survey and an abandon rate are", ["The same metric", "Different", "Both codecs", "Both ANIs"], 1, "One is the customer. One is the dialer."),
        ("Analytics is useful when", ["It changes a script or a coach plan", "It is a slide with no owner", "It replaces TLS", "It replaces skills"], 1, "A topic without an action is a poster."),
        ("Partner and native analytics screens are", ["Guaranteed identical", "Not assumed identical here", "Illegal", "Both Java"], 1, "Ask which suite."),
        ("Mapping a survey onto a disposition is", ["Automatic in every domain", "A design you must choose", "A SIP header", "A JRE update"], 1, "Do not assume the map."),
        ("The data sheet includes surveys among", ["Headset SKUs", "The WEM pieces to integrate", "Dialer modes only", "Equinix cities"], 1, "Surveys are in that list."),
    ], [("Survey versus abandon?", "Different."), ("A topic without an owner?", "A poster."), ("Screens identical?", "Do not assume."), ("Surveys in the data sheet?", "Yes.")],
    ("Name one topic", "Pick a topic you would change a prompt for.", ["Name the topic", "Name the prompt", "Say you will not average it with abandon"], "The prompt change is specific."),
    ("Leadership wants one health number", "They add abandon, survey, and handle time with equal weight.", "INDEX made-up", ["Refuse the index. Show the three series", "Publish the index", "Delete QM", "Stop recording"], 0, "The series mean different things.", "Show them separately."),
    ["Keep survey, abandon, and topics apart", "Give every topic an owner"], uncertain=["Screen names inside a partner analytics tool are not copied here."]))
    R.append(L("l05", "Recordings expire", "advanced", [
        "The retention page says VCC audio recordings are kept for the sooner of 30 days or a successful SFTP or FTP offload, or as the contract says. E911 call recordings are listed at 30 days. Agent data is 60 days. Campaign state is 120 days. Disabled domains are listed at 120 days after closure. DIDs and toll-free numbers are listed at 90 days after closure.",
        "If you need a call from last quarter, the offload had to succeed. A failed SFTP job is a silent deletion clock. QM cannot score what is already gone.",
    ], [RETAIN], stack("Clocks from the retention page", "Confirm the live page. Contracts can override.", ["VCC audio: 30 days or offload", "E911 audio: 30 days", "Agent data: 60 days", "Campaign state: 120 days"]),
    "The offload fails", ["Recorder", "SFTP", "Clock"], [
        ("Recorder", "Store", "The audio exists today.", "store"),
        ("SFTP", "Fail", "The nightly copy fails.", "fail"),
        ("Clock", "Run", "The retention clock is still running.", "clock"),
        ("QM", "Miss", "Next month the file is gone.", "miss"),
        ("Admin", "Alarm", "A failed copy needs a human.", "alarm"),
        ("Contract", "Read", "The contract can say something else.", "contract"),
    ], [
        ("VCC audio, on the retention page, lasts", ["Forever", "The sooner of 30 days or a successful offload, unless the contract says otherwise", "7 years always", "1 day"], 1, "That is the published line."),
        ("A failed SFTP job", ["Extends retention automatically", "Leaves you with the clock", "Deletes the domain today", "Changes ANI"], 1, "Success is the offload condition."),
        ("E911 recordings on that page are", ["10 years", "30 days", "The same as campaign state", "Not listed"], 1, "30 days."),
        ("Agent data on that page is", ["30 days", "60 days", "120 days", "90 days"], 1, "60 days. Campaign state is 120. DIDs after closure are 90."),
        ("QM next quarter", ["Can always replay", "Needs the offload to have worked", "Needs TLS 1.1", "Needs vertical dialing"], 1, "You cannot score a deleted file."),
    ], [("VCC audio rule?", "30 days or successful offload, or the contract."), ("Failed copy?", "The clock continues."), ("E911 audio?", "30 days on that page."), ("Agent data?", "60 days on that page.")],
    ("Name the clock", "For one complaint you may need in 45 days, say where the file must be.", ["Not only in VCC", "On the offload", "Checked for success"], "The plan does not say 'it will still be there'."),
    ("Legal asks for a call from March in June", "Offload has been failing since February.", "SFTP fail since=Feb REQUEST June", ["The file is likely gone. Fix the copy for the next one", "Reboot to restore it", "Change the dialer", "Edit the retention page"], 0, "The clock won.", "Restore the offload and tell legal the truth."),
    ["Plan the offload", "Do not promise a recording past the clock"], uncertain=["Contracts can override the published table. Read the agreement for the domain you are in."]))
    R.append(L("l06", "The agent should not need a second login", "practice", [
        "The desktop page's point is that schedules, adherence, time off, shift bidding, and evaluations are reachable in Plus and, through connectors, in the CRM. A second password for WEM is a design smell if the connector was in the contract.",
        "Shift bidding is named on that page. This lab does not reproduce the bidding rules. If bidding exists, the result still has to become the schedule the dialer respects.",
    ], [ADP, WEM], path("One place to look", "Then the schedule has to be real.", ["Plus or CRM", "Schedule", "Bid result", "Dialer count"]),
    "Time off", ["Agent", "WEM", "Dialer"], [
        ("Agent", "Request", "Time off is requested in Plus.", "req"),
        ("WEM", "Approve", "The schedule changes.", "ok"),
        ("Dialer", "See", "Tomorrow's count drops.", "count"),
        ("Agent", "Eval", "An evaluation opens in the same desktop.", "eval"),
        ("CRM", "Same", "A connector can show the same actions.", "crm"),
        ("Admin", "Gap", "A second URL means the connector is unused.", "gap"),
    ], [
        ("Time off in Plus is", ["Undocumented", "Named on the desktop page", "A codec", "A list mode"], 1, "The page lists it."),
        ("Shift bidding is", ["Invented here", "Named on the desktop page", "A SIP verb", "A JRE"], 1, "The page lists shift bidding among WFO actions."),
        ("A bid that does not change the schedule", ["Still staffs the dialer", "Does not", "Sets ANI", "Records hold"], 1, "The dialer needs the resulting roster."),
        ("A second WEM login for every agent means", ["The connector story is in use", "The connector story is probably not", "TCPA is on", "IVR is done"], 1, "Plus was supposed to hold it."),
        ("This lab's bidding rules are", ["Complete", "Not reproduced. Read the suite you own", "The abandon window", "The module list"], 1, "Rules differ by suite."),
    ], [("Time off in Plus?", "Named."), ("Shift bidding?", "Named, rules not copied here."), ("Bid without a schedule change?", "The dialer never sees it."), ("Second login?", "Connector probably unused.")],
    ("One path", "Say where an agent requests time off on your paper floor.", ["Plus or the CRM", "The schedule updates", "The dialer count updates"], "There is no mystery URL."),
    ("Bids are a spreadsheet", "Plus can do it. The spreadsheet is the real roster and it is wrong by Thursday.", "BID sheet PLUS unused", ["Move bidding into the suite and publish one schedule", "Keep both forever", "Delete QM", "Stop SFTP"], 0, "Two rosters is how you overdial.", "One schedule."),
    ["Put WEM actions where the agent already works", "Make the result a schedule"], uncertain=["Bidding rules are suite-specific and were not copied from a manual."]))
    R.append(L("l07", "What this lab will not pretend to run", "advanced", [
        "This lab has no live WEM tenant. You cannot approve a real time-off request here. You can say which product page promised the button, which retention clock will delete the evidence, and which dialer mistake a bad roster causes.",
        "That is the useful line between a simulator and a system of record. The pacing bench is a classroom. The schedule in the customer's suite is the roster. The campaign dialog is the mode.",
    ], [WEM, RETAIN, ADP], compare("Classroom versus record", "Say which one you are touching.", "This lab", ["Pacing model", "IVR learning JSON", "Cited explanations"], "The customer", ["WEM suite", "Campaign dialog", "Offload server"]),
    "A question arrives", ["Person", "Lab", "Suite"], [
        ("Person", "Ask", "How many people are on break?", "ask"),
        ("Lab", "Refuse", "This lab does not know.", "no"),
        ("Suite", "Answer", "The schedule knows.", "yes"),
        ("Lab", "Teach", "The lab can say what to subtract.", "teach"),
        ("Suite", "Offload", "Recordings live or die on the copy job.", "copy"),
        ("Person", "Write", "The answer names the system.", "write"),
    ], [
        ("This lab can approve time off. True or false?", ["True", "False", "True on Tuesdays", "True if you export JSON"], 1, "There is no tenant."),
        ("The pacing bench is", ["The dialer", "A classroom model", "The schedule", "The offload"], 1, "It is labeled that way."),
        ("The roster of record is", ["A flashcard", "The WEM schedule in the suite you bought", "The hero animation", "Chrome 46"], 1, "Look there."),
        ("A recording of record after 30 days is", ["Always in VCC", "Wherever the offload put it, if the job worked", "In the quiz", "In the theme"], 1, "The retention page."),
        ("Saying 'the AI will staff it' is", ["A design", "Not a screen", "A module", "A codec"], 1, "Name the suite."),
    ], [("Approve time off here?", "No."), ("Pacing bench?", "A model."), ("Roster of record?", "The suite."), ("Recording after the clock?", "The offload.")],
    ("Name the system", "For schedule, mode, and recording, name the system of record.", ["WEM suite", "Campaign dialog", "Offload"], "None of the three is this website."),
    ("Someone configured production inside the simulator", "They set lines per agent here and told the floor it was live.", "BENCH saved as production", ["Redo it in the campaign dialog", "Trust the browser", "Delete the schedule", "Disable TLS"], 0, "The bench does not dial.", "Set the mode in the domain."),
    ["Keep the lab and the tenant apart", "Name the system of record"], href="#/pacing"))
    return track("t10", "Workforce engagement", "WEM", "Native WEM and Verint, the roster, quality, surveys, and the recording clock.", "People", "Practice", "WEM tells you who should be there. The dialer should believe the schedule. Recordings do not last by hope.", R)
