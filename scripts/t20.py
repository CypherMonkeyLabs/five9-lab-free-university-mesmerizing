from curriculum_lib import ADP, DESK, WEM, WFM, lesson, compare, path, stack, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "Workforce management staffs the work", "foundation", [
        "The Five9 workforce management page says WFM aligns agent resources with contact volumes through the day, so the right number of agents with the right skills are available. It describes volumes that sometimes exceed the people on hand, and times when more agents are on hand than the work needs.",
        "The workforce engagement page puts the same idea in one line: accurate multi-skill, multi-channel forecasts and schedules, real-time adherence, intraday management, and more. WFM is that staffing layer. It is not a dialing mode and not a skill group.",
    ], [WFM, WEM], stack("What the pages put under WFM", "Staffing, not the dialer.", ["Forecasts", "Schedules", "Real-time adherence", "Intraday management"]),
    "Name the layer", ["WFM", "Dialer"], [
        ("WFM", "Aim", "Match people to the volume.", "aim"),
        ("WFM", "Skills", "The page says the right skills.", "skills"),
        ("Dialer", "Separate", "A mode is a different object.", "mode"),
        ("WEM", "Line", "Forecasts, schedules, adherence, intraday.", "line"),
        ("Reader", "Stop", "Do not rename WFM as a campaign type.", "stop"),
        ("Reader", "Cite", "The sentence keeps the WFM page.", "cite"),
    ], [
        ("The WFM page says the tool aligns", ["Codecs with trunks", "Agent resources with contact volumes", "ANI with STIR", "Badges with exams"], 1, "That is the page's sentence."),
        ("Right skills are", ["Ignored", "Part of the same sentence", "A SIP option", "A list reset"], 1, "The page says the right skills."),
        ("WFM replaces the dialing mode. True or false?", ["True", "False. It is the staffing layer", "True for autodial only", "True for TLS"], 1, "Modes and rosters are different objects."),
        ("The WEM page includes intraday management under", ["Quality only", "The workforce management description", "The codec list", "The badge"], 1, "The WEM line names it."),
        ("A skill group and a schedule are", ["The same object", "Different. One is the queue, one is the roster", "Both ANI", "Both prompts"], 1, "Do not collapse them."),
    ], [("What does WFM align?", "People with volume."), ("Right skills?", "Named on the page."), ("Is it a dialing mode?", "No."), ("Intraday?", "On the WEM line.")],
    ("One sentence", "Say what WFM is for, without naming a dialing mode.", ["Volumes", "People", "Skills"], "The sentence matches the page."),
    ("A plan calls WFM a fourth campaign type", "The pages describe staffing.", "PLAN type=wfm", ["Call it staffing", "Add the type in admin", "Change the codec", "Reset lists"], 0, "There is no such campaign type on these pages.", "Rename the plan."),
    ["Call WFM the roster layer", "Keep it off the campaign-type list"]))
    R.append(L("l02", "Forecasts are multiskill and multichannel", "foundation", [
        "The WFM page says accurate contact-volume forecasts are the base for staffing, and that you create multiskill, multichannel forecasts. The feature list names multiple forecasting algorithms, inbound, outbound, and blended environments, and what-if analysis.",
        "The page says multiple algorithms. It does not name them. This lab will not label one of them Erlang C, and it will not invent an accuracy percent. What-if is on the list. The inputs to a what-if are not printed here.",
    ], [WFM], stack("Forecast list on the page", "Names, not formulas.", ["Multiple forecasting algorithms", "Multiskill and multichannel", "Inbound, outbound, and blended", "What-if analysis"]),
    "Read the list", ["Page", "Model"], [
        ("Page", "List", "The four forecast lines are copied.", "list"),
        ("Model", "Ask", "Which algorithm is not named.", "ask"),
        ("Model", "Refuse", "No formula is added.", "refuse"),
        ("Page", "Blend", "Blended is an environment on this list.", "blend"),
        ("Reader", "Skill", "Multiskill means the forecast can see more than one skill.", "skill"),
        ("Reader", "Stop", "The percent stays off the slide.", "stop"),
    ], [
        ("The page says forecasts can cover", ["Voice only, always", "Multiple skills and multiple channels", "Only SIP", "Only 911"], 1, "Multiskill and multichannel are the words."),
        ("How many algorithms does this lesson name?", ["Six, with formulas", "None. The page says multiple and does not name them", "One, Erlang C", "Zero, forecasting is absent"], 1, "Do not invent the names."),
        ("Inbound, outbound, and blended appear as", ["Campaign objects you create here", "Environments on the forecast list", "Codecs", "Badges"], 1, "That is the feature line."),
        ("What-if analysis is", ["Absent", "On the forecast list", "A dialer mode", "A retention clock"], 1, "The page lists it."),
        ("An accuracy percent in this lesson is", ["Quoted", "Not quoted", "93", "100"], 1, "The page did not give this lesson a percent to repeat."),
    ], [("Multiskill?", "Yes."), ("Algorithm names?", "Not printed."), ("Blended on this list?", "Yes, as an environment."), ("What-if?", "Listed.")],
    ("Copy the list", "Write the four forecast lines and stop.", ["Algorithms unnamed", "Multiskill", "Channels", "What-if"], "No formula was added."),
    ("A worksheet says the Five9 forecast is Erlang C at 80 percent", "The page does not say that.", "MODEL erlang TARGET 80 SOURCE none", ["Remove the formula and the percent", "Publish the worksheet", "Add lines", "Change ANI"], 0, "Unnamed algorithms stay unnamed.", "Delete the formula."),
    ["Copy the forecast list", "Leave the algorithm unnamed"], uncertain=["The WFM page says multiple forecasting algorithms and does not name them. This lesson does not call the engine Erlang C."]))
    R.append(L("l03", "Schedules can be built or bid", "practice", [
        "The WFM page says you can schedule agents automatically based on preferences, or let them bid on schedules, and that the plans are there to meet service goals and limit labor cost. The feature list adds flexible start and stop times, and optimization of lunch, break, meeting, and coaching.",
        "Those are the schedule facts. The page does not print a maximum shift length or a break rule in minutes. Service goals are named. The numeric target still lives on the skill, and that child page did not open in the routing chapter.",
    ], [WFM], compare("Two ways onto a schedule", "The page allows both.", "Automatic from preferences", ["The system builds the plan"], "Bidding", ["Agents bid on schedules"]),
    "Pick a method", ["Planner", "Agent"], [
        ("Planner", "Choose", "Preferences or bidding.", "choose"),
        ("Planner", "Times", "Start and stop can flex.", "times"),
        ("Planner", "Blocks", "Lunch, break, meeting, and coaching are on the list.", "blocks"),
        ("Agent", "Bid", "Bidding is a published option.", "bid"),
        ("Planner", "Goal", "Service goals are the aim, not a number copied here.", "goal"),
        ("Planner", "Stop", "No minute value is invented.", "stop"),
    ], [
        ("Schedule bidding is", ["Forbidden", "Named on the WFM page", "A dialer mode", "A codec"], 1, "The page offers bidding."),
        ("Preference scheduling is", ["The only method", "The other method the page names", "Absent", "A list reset"], 1, "Automatic scheduling from preferences is the pair."),
        ("Lunch, break, meeting, and coaching are", ["Ignored by the scheduler, per the page", "On the optimization list", "SIP headers", "Exam codes"], 1, "The feature list includes them."),
        ("A break length in minutes in this lesson is", ["15", "Not stated", "30", "60"], 1, "The page does not give the number."),
        ("Flexible start and stop times are", ["Named", "Denied", "A TLS setting", "A prompt"], 1, "The list includes them."),
    ], [("Bid or assign?", "The page allows both."), ("Breaks on the list?", "Yes, without a minute count."), ("Start and stop?", "Flexible, as stated."), ("Numeric service goal here?", "Not copied.")],
    ("Choose one method", "Say preference scheduling or bidding, and name one block the optimizer is told about.", ["Method", "Lunch or break or meeting or coaching", "No invented minutes"], "The choice is one of the two the page names."),
    ("The schedule ignores breaks because they are not work", "The page lists break optimization.", "SCHEDULE breaks=ignored", ["Put breaks on the plan", "Leave them off", "Add power lines", "Delete the skill"], 0, "A break is one of the blocks the page names.", "Include it."),
    ["Pick preference or bidding on purpose", "Include the blocks the page lists"]))
    R.append(L("l04", "Intraday is a comparison, a reforecast, and a notice", "practice", [
        "The WEM page says intraday management and automated adjustment sit with workforce management. The WFM page's change card says you compare interval by interval to the plan, reforecast automatically, flex the schedule, and notify agents in a few clicks.",
        "That card is titled for multiple change notification channels and says there are six. It does not name the six. This lesson will not invent email, SMS, or a chat product as the list.",
    ], [WFM, WEM], path("When the day moves", "From the change card.", ["Compare each interval to the plan", "Reforecast", "Flex the schedule", "Notify", "Six channels, unnamed"]),
    "A volume spike", ["Plan", "Floor"], [
        ("Plan", "Compare", "The interval is off the plan.", "cmp"),
        ("Plan", "Reforecast", "The page lists automatic reforecasting.", "re"),
        ("Plan", "Flex", "The schedule can flex.", "flex"),
        ("Floor", "Notify", "Agents are told.", "notify"),
        ("Plan", "Count", "Six channels are claimed and not named.", "six"),
        ("Reader", "Stop", "No channel brand is added.", "stop"),
    ], [
        ("Intraday management is named on", ["The dialer page only", "The WEM workforce line and the WFM change card", "The badge", "The codec page"], 1, "Both pages speak to it."),
        ("Interval-by-interval comparison is", ["Absent", "On the change card", "A list mode", "A prompt"], 1, "The card lists it."),
        ("The six notification channels are", ["Named in this lesson", "Counted on the page and not named", "Only email", "Only the softphone"], 1, "Do not invent the six."),
        ("Automatic reforecasting is", ["Forbidden", "On the card", "A SIP option", "A retention rule"], 1, "The card lists it."),
        ("Flex schedules means", ["The plan can change when the day moves", "The plan is frozen at midnight", "ANI changes", "The domain closes"], 1, "The card says flex schedules."),
    ], [("Intraday named?", "Yes."), ("Interval compare?", "Yes."), ("Six channels named?", "No."), ("Reforecast?", "Listed.")],
    ("Write the reaction", "Four steps from the card, then the unnamed six.", ["Compare", "Reforecast", "Flex", "Notify"], "The channel brands are blank."),
    ("A runbook names six channels from a different vendor", "The Five9 page did not name them.", "CHANNELS guessed", ["Leave the six unnamed", "Publish the other vendor's list as Five9", "Add lines", "Reset lists"], 0, "A count is not a catalog.", "Delete the guessed names."),
    ["Use the intraday steps the card lists", "Leave the six channels unnamed"], uncertain=["The WFM page says six change notification channels and does not name them."]))
    R.append(L("l05", "Adherence is plan versus what the person did", "practice", [
        "The WFM page says adherence can be tracked over time or in real time. The feature list adds historical adherence, real-time monitoring, out-of-adherence alerts, and both an agent view and a supervisor view.",
        "The same page's portal list says agents can see schedules and adherence. Adherence is evidence about the plan. It is not the service-level formula, and it is not a disposition.",
    ], [WFM], stack("Adherence on the page", "Plan versus actual.", ["Historical", "Real time", "Out-of-adherence alerts", "Agent view and supervisor view"]),
    "Someone leaves the plan", ["Schedule", "Alert"], [
        ("Schedule", "Exist", "The person had a plan.", "plan"),
        ("Floor", "Leave", "They are not on the planned activity.", "leave"),
        ("Alert", "Fire", "The page lists an out-of-adherence alert.", "alert"),
        ("Agent", "See", "The agent view is named.", "agent"),
        ("Supervisor", "See", "The supervisor view is named.", "sup"),
        ("Reader", "Stop", "No threshold minute is copied.", "stop"),
    ], [
        ("Real-time adherence is", ["Absent", "Named", "A codec", "A campaign type"], 1, "The page lists it."),
        ("Historical adherence is", ["The only view", "Also named", "Forbidden", "A list mode"], 1, "The list includes historical."),
        ("Who has a view, per the list?", ["Nobody", "Agents and supervisors", "Only the carrier", "Only the IVR"], 1, "Both views are named."),
        ("An out-of-adherence alert is", ["Named", "Denied", "A SIP 911 header", "A badge"], 1, "The list includes alerts."),
        ("A minute threshold for the alert in this lesson is", ["Stated as 5", "Not stated", "Stated as 15", "Stated as 0"], 1, "The page does not give the number."),
    ], [("Real time?", "Yes."), ("History?", "Yes."), ("Who can look?", "Agent and supervisor views."), ("Threshold minutes?", "Not stated.")],
    ("Define adherence", "One sentence: plan versus actual, plus who can see it.", ["No minute threshold", "Name both views"], "The sentence matches the list."),
    ("Adherence is graded as a call disposition", "The page describes a staffing view, not a disposition.", "ADHERENCE stored-as disposition", ["Keep it as a staffing view", "Add a disposition named Adherence", "Reset the list", "Change ANI"], 0, "Different objects.", "Leave dispositions alone."),
    ["Treat adherence as plan versus actual", "Do not invent the alert threshold"]))
    R.append(L("l06", "The agent can see the plan, including on a phone", "advanced", [
        "The agent portal on the WFM page lists viewing schedules and adherence, bidding on shifts, requesting schedule changes, vacation, and voluntary overtime, plus notifications and alerts. The mobile card lists Android and iOS, self-service away from the desk, absentee and late check-in, and alerts.",
        "The desktop page says Plus can show schedules and adherence, time-off requests, and evaluations without leaving the desktop. A second login is a design smell only if that connector was what you bought. The page does not say every contract includes it.",
    ], [WFM, DESK, ADP], compare("Two places the plan can show up", "Both pages name a view.", "WFM portal and mobile", ["Schedules, bids, requests", "Android and iOS"], "Agent Desktop Plus", ["Schedules and adherence", "Time off", "Evaluations"]),
    "Where will they look", ["Portal", "Desktop"], [
        ("Portal", "List", "Schedules, bids, and requests.", "list"),
        ("Mobile", "OS", "Android and iOS are named.", "os"),
        ("Desktop", "Plus", "Plus can show the plan.", "plus"),
        ("Contract", "Ask", "The connector is not assumed.", "ask"),
        ("Agent", "Late", "Late check-in is on the mobile card.", "late"),
        ("Reader", "Stop", "No app-store version is copied.", "stop"),
    ], [
        ("Shift bidding on the portal is", ["Absent", "Listed", "A dialer mode", "A prompt"], 1, "The portal list includes it."),
        ("Voluntary overtime requests are", ["Named on the portal list", "Forbidden", "A codec", "A badge"], 1, "The list says voluntary overtime."),
        ("Mobile operating systems named are", ["None", "Android and iOS", "Only a desk phone", "Only Java"], 1, "The mobile card names them."),
        ("Plus shows schedules", ["On the desktop page", "Never", "Only in a PDF this lesson could not read", "Only for supervisors"], 1, "The desktop page says so."),
        ("Every customer already has the WFO connector. True or false?", ["True", "False. The page describes the capability. The contract still matters", "True in one country only", "True if ANI is local"], 1, "Do not assume the purchase."),
    ], [("Portal includes bidding?", "Yes."), ("Mobile OS?", "Android and iOS."), ("Plus?", "Schedules, adherence, time off, evaluations."), ("Assume the connector?", "No.")],
    ("Pick the surface", "Say portal, mobile, or Plus, and one action from that list.", ["One surface", "One action", "No assumed contract"], "The action is on the page you named."),
    ("Agents are told to install a desktop app the page does not name", "The mobile card names Android and iOS, not a third-party brand.", "APP guessed", ["Stay with the named surfaces", "Mandate the extra app", "Delete skills", "Change TLS"], 0, "An extra brand is not the page.", "Use the named surfaces."),
    ["Offer the portal, the phone, or Plus", "Do not assume the connector is installed"]))
    R.append(L("l07", "Native WEM and a partner path both exist", "advanced", [
        "The workforce engagement page says Five9 offers WEM natively and also partners with vendors such as Verint. It says Five9 manages installation, configuration, maintenance, and upgrades for the WEM solution they deliver.",
        "The WFM page is the native product story this chapter read. It does not say a given floor is native rather than Verint. Ask. The WFM card for pre-built CRM integrations names Oracle and ServiceNow on that page. A longer CRM list lives on the desktop and API pages, in the CRM chapter, and should not be pasted back as if the WFM card printed it.",
    ], [WEM, WFM], compare("Two public statements", "Ask which one this floor bought.", "Native WFM page", ["Forecast, schedule, adhere, intraday"], "Partner path", ["Verint is the example the WEM page names"]),
    "Ask before you document", ["Contract", "Page"], [
        ("Contract", "Ask", "Native or a named partner.", "ask"),
        ("Page", "Native", "The WFM page is the native story.", "native"),
        ("Page", "Verint", "Verint is an example, not a synonym.", "verint"),
        ("Page", "CRM", "The WFM card names Oracle and ServiceNow.", "crm"),
        ("Reader", "Split", "The longer CRM list stays in the CRM chapter.", "split"),
        ("Reader", "Own", "Upgrades, per the WEM page, are managed by Five9 for the solution they deliver.", "own"),
    ], [
        ("Verint is", ["The only WEM Five9 allows", "Named as a partner example beside native WEM", "A codec", "A campaign type"], 1, "The WEM page says both."),
        ("Who manages upgrades, per the WEM page?", ["The headset vendor", "Five9, for the solution they deliver", "The caller", "The ITSP only"], 1, "The page says Five9 manages them."),
        ("The WFM pre-built CRM card, as read here, names", ["Every CRM on earth", "Oracle and ServiceNow", "Only Zoom", "Only a badge"], 1, "Those are the two items on that card."),
        ("You should guess native versus Verint. True or false?", ["True", "False. Look at the contract or the app", "True for TCPA", "True if Java is gone"], 1, "The page refuses a single answer."),
        ("A longer adapter list belongs", ["Pasted onto the WFM card", "On the pages that actually print it", "In a rumor", "On the codec page"], 1, "Keep each list on its page."),
    ], [("Verint?", "A named partner example."), ("Who upgrades?", "Five9, for the solution they deliver."), ("WFM CRM card?", "Oracle and ServiceNow."), ("Guess the suite?", "No.")],
    ("Write the question", "The first WFM question on a new floor.", ["Which suite", "Which cards you actually read", "Where the agent sees the schedule"], "You did not assume Verint, and you did not borrow the other CRM list."),
    ("A runbook says to open Verint. The floor is native.", "Agents cannot find the URL.", "RUNBOOK verint APP native", ["Open the suite that is installed", "Keep the wrong URL", "Delete skills", "Enable an old TLS"], 0, "The runbook guessed.", "Point it at the installed suite."),
    ["Ask which suite", "Keep each CRM list on its own page"], uncertain=["This lab does not know which WEM suite a given customer bought. The WFM CRM card read here names Oracle and ServiceNow, not the longer adapter list."]))
    return track(
        "t20",
        "Workforce management",
        "Workforce",
        "Forecasts, schedules, intraday changes, and adherence from the public WFM and WEM pages.",
        "Workforce",
        "Practice",
        "WFM is the roster. The pages name the tools and leave the formulas unnamed.",
        R,
    )
