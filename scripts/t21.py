from curriculum_lib import DESK, QM, WEM, WEMDS, lesson, compare, path, stack, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "Quality management scores the work on purpose", "foundation", [
        "The workforce engagement page describes quality management as multi-channel evaluations, real-time agent desktop monitoring and assistance, and automated scoring and evaluation selection. The quality page says manual review covers a small share of interactions and frames that as a problem the product is aimed at. It does not give this lab a measured percent.",
        "A score without a recording and a form is a mood. The WEM data-sheet page says the suite is about integrating recording with quality management, interaction analytics, workforce management, recording data protection, customer surveys, and CRM connectors. Those are the pieces. They are not one button.",
    ], [WEM, QM, WEMDS], stack("Pieces named beside quality", "From the data-sheet page.", ["Recording", "Quality management", "Interaction analytics", "Surveys", "CRM connectors"]),
    "Separate the pieces", ["QM", "Survey"], [
        ("QM", "Form", "An evaluation has a form.", "form"),
        ("Record", "Exist", "Recording is a different piece.", "rec"),
        ("Analytics", "Pattern", "Analytics looks across interactions.", "an"),
        ("Survey", "One", "A survey is the customer's score of a contact.", "sv"),
        ("Reader", "Small", "Small share is the page's phrase, not a lab measurement.", "small"),
        ("Reader", "Stop", "No percent is added.", "stop"),
    ], [
        ("Multi-channel evaluations are named under", ["The codec list", "Quality management on the WEM page", "The dialer modes", "The badge"], 1, "The WEM page puts them there."),
        ("Automated scoring is", ["Absent", "Named with evaluation selection", "Illegal on the page", "A list mode"], 1, "The WEM line includes it."),
        ("A customer survey and a QM score are", ["The same object", "Both named, and not the same sentence", "Both ANI", "Both prompts"], 1, "The data-sheet list keeps them separate."),
        ("The phrase small share is", ["A percent this lab measured", "The quality page's own wording", "A port number", "An exam code"], 1, "Do not turn it into a number."),
        ("Recording data protection is", ["On the data-sheet list", "Denied", "A campaign type", "A skill tab"], 1, "The page includes it."),
    ], [("Evaluations?", "Named under QM."), ("Automated scoring?", "Named."), ("Survey equals QM?", "No."), ("Small share?", "The page's phrase, not a measured percent.")],
    ("Name four pieces", "Recording, QM, analytics, surveys.", ["Do not average them into one health number"], "Each piece keeps its name."),
    ("A dashboard averages abandon, a survey, and a QM score into one percent", "The pages list them as separate tools.", "HEALTH blended", ["Split the numbers", "Publish the blend", "Delete recordings", "Change ANI"], 0, "A blend hides which tool moved.", "Show the pieces."),
    ["Keep QM, surveys, and analytics apart", "Do not invent the small-share percent"]))
    R.append(L("l02", "The evaluation list is forms, queries, coaching, and assignment", "practice", [
        "The WEM quality list names call, screen, and digital-channel transcription capture, real-time call and desktop monitoring, flexible evaluation form creation, query, coaching packages, and automated evaluation assignment.",
        "The same list ends with pre-built CRM integration for Salesforce, Zendesk, Oracle, and ServiceNow. That is a quality-page list. It is not a promise that every floor bought every name.",
    ], [WEM], stack("Quality list that opened", "Copy the nouns. Skip the contract you have not seen.", ["Transcription capture", "Live monitoring", "Flexible forms", "Coaching packages", "Automated assignment"]),
    "Build one form", ["QM", "CRM"], [
        ("QM", "Form", "The form matches the work.", "form"),
        ("QM", "Query", "The page says you can query.", "query"),
        ("QM", "Assign", "Assignment can be automated.", "assign"),
        ("QM", "Coach", "Coaching packages are named.", "coach"),
        ("CRM", "Names", "Four CRM names are on this list.", "names"),
        ("Contract", "Check", "The purchase is still a question.", "check"),
    ], [
        ("Flexible evaluation forms are", ["Absent", "On the quality list", "A dialer mode", "A codec"], 1, "The list includes form creation."),
        ("Transcription capture on that list includes", ["Only the first second of voice", "Call, screen, and digital channel", "Only 911", "Only chat"], 1, "Those three are named."),
        ("Automated evaluation assignment is", ["Named", "Forbidden", "A list reset", "A badge"], 1, "The list includes it."),
        ("The CRM names on this quality list are", ["None", "Salesforce, Zendesk, Oracle, and ServiceNow", "Only Epic", "Only a URL pop"], 1, "That is the list."),
        ("Naming a CRM here means the floor bought it. True or false?", ["True", "False. It means the page names the integration", "True if the agent is Ready", "True for UK domains only"], 1, "A catalog is not a contract."),
    ], [("Forms?", "Flexible creation is listed."), ("Transcription?", "Call, screen, and digital."), ("Assignment?", "Can be automated."), ("CRM names?", "Salesforce, Zendesk, Oracle, ServiceNow.")],
    ("One form line", "Write a behavior a stranger could score from a recording.", ["Name the behavior", "Name the evidence", "Do not call it a vibe"], "The line points at something the recording could hold."),
    ("Agents are scored on a sales form for a complaint queue", "The form was copied from another campaign.", "FORM sales QUEUE complaints", ["Use a form that matches the work", "Keep the sales form for speed", "Delete recordings", "Enable an old browser"], 0, "The form is the definition of good.", "Score the work they were asked to do."),
    ["Match the form to the queue", "Treat the CRM names as a catalog"]))
    R.append(L("l03", "Monitoring and coaching are on the quality pages", "practice", [
        "The WEM list includes real-time call and desktop monitoring. The quality page adds real-time monitoring and coaching, and a line that says supervisors can be flagged for immediate coaching with dynamic guidance. It also says agent assistance can be personalized from agent competency.",
        "The page says competency is infused into routing decisions. That sentence is on the quality page. It is not a field on the skill groups chapter this lab read. Do not paste it into the skill tab as if the admin guide had printed it.",
    ], [WEM, QM], compare("Two quality sentences", "Both opened. They are not the skill chapter.", "WEM list", ["Real-time call and desktop monitoring"], "Quality page", ["Coaching flags", "Competency in routing and assistance"]),
    "A live call", ["Monitor", "Coach"], [
        ("Monitor", "Watch", "Call and desktop monitoring are named.", "watch"),
        ("Coach", "Flag", "The quality page says supervisors can be flagged.", "flag"),
        ("Assist", "Guide", "Assistance can use competency.", "guide"),
        ("Route", "Separate", "The routing sentence stays on the quality page.", "route"),
        ("Skill", "Closed", "The skill chapter did not print that field.", "skill"),
        ("Reader", "Cite", "The note names which page.", "cite"),
    ], [
        ("Real-time desktop monitoring is", ["Absent", "On the WEM quality list", "A trunk feature", "A list mode"], 1, "The list includes it."),
        ("Flagging a supervisor for coaching is", ["Named on the quality page", "Forbidden", "A disposition", "A codec"], 1, "The page says it."),
        ("Competency-based routing is a sentence on", ["The skill groups chapter this lab read", "The quality page", "The Wikipedia ACD page only", "The badge"], 1, "Keep it on the quality page."),
        ("Personalized assistance is", ["Named", "Denied", "A SIP header", "An exam code"], 1, "The quality page says guidance based on competency."),
        ("Pasting that routing sentence into the skill tab is", ["Required", "A way to invent a field", "How service level is calculated", "How ANI works"], 1, "The skill chapter did not print it."),
    ], [("Desktop monitoring?", "On the WEM list."), ("Coaching flag?", "On the quality page."), ("Which page owns competency routing?", "The quality page."), ("Paste it into skills?", "No.")],
    ("Place the sentence", "Write the competency line and the page title above it.", ["Quality page", "Not the skill tab"], "A reader can see which page you mean."),
    ("A skill design says competency routing because the quality page exists", "The skill chapter did not print the field.", "SKILL competency SOURCE quality-page", ["Keep the sentence on the quality note", "Add a fake skill field", "Delete the queue", "Change ANI"], 0, "The pages are neighbors, not the same dialog.", "Leave the skill tab alone."),
    ["Cite the page that printed the sentence", "Do not move it onto the skill tab"]))
    R.append(L("l04", "Analytics is a sweep across interactions", "practice", [
        "The WEM page says interaction analytics analyzes 100 percent of captured interactions to find trends, automate the quality process, and see where service went well or badly. The feature list names voice, chat, and email, 100 percent call transcription, automated QM scoring, statistical group comparison, ad hoc word or phrase search, automatic categorization, and emotion and sentiment analysis.",
        "The quality page's conversational-intelligence line says analyze up to 100 percent of interactions. Up to 100 percent and 100 percent are not the same sentence. Quote the page you mean. This lesson does not average them into a single guarantee.",
    ], [WEM, QM], compare("Read the percent you cite", "The pages do not match word for word.", "WEM analytics list", ["100 percent of captured interactions", "100 percent call transcription"], "Quality page", ["Up to 100 percent of interactions"]),
    "A phrase spikes", ["Calls", "Analytics"], [
        ("Calls", "Happen", "Many contacts mention a fee.", "fee"),
        ("Analytics", "Search", "Ad hoc word search is on the list.", "search"),
        ("Analytics", "Bucket", "Automatic categorization is on the list.", "bucket"),
        ("Analytics", "Feel", "Emotion and sentiment are named.", "feel"),
        ("Reader", "Percent", "The percent stays attached to its page.", "percent"),
        ("Action", "Separate", "A survey is still a different piece.", "survey"),
    ], [
        ("Channels named on the analytics list are", ["Voice only", "Voice, chat, and email", "Only SMS", "Only video"], 1, "The list names those three."),
        ("Ad hoc word or phrase search is", ["Absent", "On the list", "A dialer mode", "A port"], 1, "The list includes it."),
        ("Emotion and sentiment analysis is", ["Named", "Denied", "A codec", "A badge"], 1, "The list includes it."),
        ("100 percent call transcription is a sentence on", ["The quality page's up-to line", "The WEM analytics list", "The skill tab", "The badge"], 1, "Quote that list if you say 100 percent transcription."),
        ("Up to 100 percent and 100 percent should be", ["Averaged", "Quoted from the page that printed each one", "Ignored", "Treated as a port"], 1, "They are different sentences."),
    ], [("Channels?", "Voice, chat, email."), ("Word search?", "Yes."), ("Sentiment?", "Named."), ("Which percent?", "Quote the page.")],
    ("Quote one percent", "Copy one sentence and the page title.", ["Do not merge the two percents"], "The title matches the sentence."),
    ("A slide says every interaction is transcribed because one page said up to 100 percent", "Up to is not a guarantee, and the other page is about captured interactions and calls.", "SLIDE every-interaction", ["Quote the page you mean", "Upgrade up-to into always", "Delete recordings", "Change ANI"], 0, "The wording is the fact.", "Use the page's words."),
    ["Quote the percent with its page", "Keep surveys and analytics apart"], uncertain=["The WEM page says 100 percent of captured interactions and 100 percent call transcription. The quality page says up to 100 percent. This lesson does not merge them."]))
    R.append(L("l05", "Performance views are dashboards, wallboards, and KPIs", "advanced", [
        "The WEM page lists performance management separately from quality and from analytics: role-based customizable dashboards, customizable KPIs and metrics, real-time performance visibility, data from external sources, wallboards, and gamification.",
        "A wallboard is not a standard report, and gamification is not a disposition. The page names them. It does not define a formula for a KPI. The analytics PDF downloaded in this check did not yield readable sentences, so no retention month and no chart-count is taken from it.",
    ], [WEM], stack("Performance list", "Names only.", ["Role-based dashboards", "Custom KPIs", "Real-time visibility", "External data", "Wallboards", "Gamification"]),
    "Hang a board", ["Page", "Floor"], [
        ("Page", "List", "Wallboards are named.", "list"),
        ("Page", "Role", "Dashboards can be role-based.", "role"),
        ("Page", "Out", "External sources are named.", "out"),
        ("Floor", "Ask", "Which KPI is still a local choice.", "ask"),
        ("Reader", "PDF", "The analytics PDF did not yield sentences.", "pdf"),
        ("Reader", "Stop", "No chart count is copied.", "stop"),
    ], [
        ("Wallboards are", ["Absent", "On the performance list", "A dialing mode", "A skill tab"], 1, "The list includes them."),
        ("Gamification is", ["Named on that list", "A disposition", "A codec", "Forbidden"], 1, "The list includes it."),
        ("External data sources are", ["Denied", "Named", "Only SIP", "Only the IVR"], 1, "The list says data aggregation from external sources."),
        ("A KPI formula in this lesson is", ["Fully derived", "Not stated. The page says KPIs can be customized", "Always service level", "Always abandon"], 1, "Customizable is not a formula."),
        ("The analytics PDF in this check", ["Supplied a retention month", "Downloaded and did not yield readable sentences", "Replaced the WEM page", "Named an exam code"], 1, "Unreadable text is not a citation."),
    ], [("Wallboards?", "Named."), ("Gamification?", "Named, not a disposition."), ("External data?", "Named."), ("PDF sentences?", "Did not yield.")],
    ("Pick a view", "Say dashboard, wallboard, or KPI, and say the formula is not in this lesson.", ["One view", "No invented formula"], "The note matches the list."),
    ("A wallboard is exported as the call-log archive", "The performance list and the call log are different tools.", "BOARD called call-log", ["Call the board a board", "Replace the call log with it", "Delete recordings", "Reset lists"], 0, "Names matter.", "Keep the board on the performance list."),
    ["Use the performance nouns the page printed", "Leave unread PDF claims out"], uncertain=["A Five9 Analytics PDF downloaded in this check did not yield readable sentences. No retention period or visualization count is taken from it."]))
    R.append(L("l06", "Agents can read evaluations without a second story", "advanced", [
        "The desktop page says Plus can show schedules, adherence, time-off requests, and evaluations without leaving the desktop. The same page says WFO connectors can show schedules, adherence, time off, shift bidding, and evaluation review inside the CRM.",
        "Recording on the WEM page is described as full-time capture of customer interactions and agent screens, kept in encrypted storage. That is the page's sentence. Notice and consent laws are not restated here, because this check did not re-open the license. Do not skip them. Confirm them on the license before you record.",
    ], [DESK, WEM], path("Where an evaluation can be read", "From the desktop page.", ["Agent Desktop Plus", "A WFO connector inside the CRM", "The recording the WEM page describes", "The license, still to be confirmed"]),
    "Close the loop", ["Record", "Agent"], [
        ("Record", "Store", "The WEM page says encrypted storage.", "store"),
        ("QM", "Score", "The evaluation exists.", "score"),
        ("Agent", "Plus", "Plus can show it.", "plus"),
        ("CRM", "Connector", "The connector path is also named.", "crm"),
        ("Law", "Open", "The license is not re-quoted here.", "law"),
        ("Reader", "Say", "The note says which path is installed.", "say"),
    ], [
        ("Evaluations in Plus are", ["Hidden", "Named on the desktop page", "A trunk feature", "A list mode"], 1, "The page lists them."),
        ("Shift bidding inside the CRM is", ["On the WFO connector line", "A dialer mode", "Absent", "A codec"], 1, "The desktop page includes it."),
        ("Encrypted storage of recordings and screens is", ["Named on the WEM page", "Denied", "Only for 911", "A badge"], 1, "The page says encrypted storage."),
        ("This lesson restates notice and consent law. True or false?", ["True, with a statute number", "False. The license was not re-opened for this chapter", "True for every country", "True if ANI is local"], 1, "Confirm the license. Do not invent the statute."),
        ("A second system of record for the same evaluation is", ["Required by the page", "Something to question if Plus or the connector was the design", "A codec", "A list reset"], 1, "The page's point is that the evaluation can live where the agent already works."),
    ], [("Plus shows evaluations?", "Yes, per the desktop page."), ("CRM path?", "WFO connector, including evaluation review."), ("Encrypted storage?", "Named on the WEM page."), ("Consent law quoted here?", "No. Confirm the license.")],
    ("Name the path", "Plus or the CRM connector, and say the license is still to be read.", ["One path", "License marked confirm"], "You did not invent a consent rule."),
    ("Agents are sent to a third site for scores the desktop page already names", "The extra login was never justified.", "LOGIN extra PATH plus", ["Use the path the page names", "Keep the extra site", "Delete evaluations", "Change ANI"], 0, "The page offers Plus and the connector.", "Start with the path you bought."),
    ["Show the evaluation where the page says it can live", "Confirm consent on the license"], uncertain=["Notice and consent are not re-quoted in this chapter. The license page was not the source opened for these lessons."]))
    R.append(L("l07", "A quality review you can finish", "advanced", [
        "Finish a quality note with the lists that opened. Name the form, the monitoring, the analytics sentence with its percent attached to a page, and the place the agent reads the score. Say whether you mean the WEM list or the quality page when the words differ.",
        "The quality page also says routing, assistance, and coaching can be refined with zero human involvement. That is the page's claim. This lab did not run that cycle. Treat it as a product sentence, not as a result you measured.",
    ], [QM, WEM], path("The review", "Page, then claim, then gap.", ["Which list", "Which percent", "Where the agent reads it", "The zero-human sentence, labeled as theirs", "The unread license and the unread PDF"]),
    "Sign the note", ["Note", "Gap"], [
        ("Note", "List", "WEM list or quality page, named.", "list"),
        ("Note", "Percent", "One percent, one page.", "percent"),
        ("Note", "Reader", "Plus or the connector.", "reader"),
        ("Note", "Claim", "Zero human involvement stays in quotes.", "claim"),
        ("Gap", "Law", "Consent is confirm.", "law"),
        ("Gap", "PDF", "The analytics PDF stays out.", "pdf"),
    ], [
        ("A finished note names", ["An invented KPI formula", "The list, the percent's page, and where the agent reads the score", "A package version", "An exam code"], 1, "Those are the opened facts."),
        ("Zero human involvement is", ["A result this lab measured", "A sentence on the quality page", "A skill-tab field", "A port"], 1, "Quote it as their sentence."),
        ("Merging the two 100 percent lines is", ["Required", "A mistake", "How transcription works", "How adherence works"], 1, "Keep the pages apart."),
        ("The unread analytics PDF belongs", ["In the note as a number", "Outside the note", "As the service level", "As the abandon rate"], 1, "No sentence was read from it."),
        ("Signing a note that adds a consent statute from memory is", ["Complete", "Ahead of the source", "Required", "A codec choice"], 1, "Confirm the license."),
    ], [("What must the note name?", "List, percent page, where the score is read."), ("Zero human involvement?", "Their sentence, not a lab result."), ("Merge the percents?", "No."), ("PDF numbers?", "Leave them out.")],
    ("Finish one note", "Use the lists and mark the gaps.", ["One percent with its page", "Consent marked confirm", "PDF left out"], "Nothing unread was filled in."),
    ("The review adds a 13-month analytics retention from a PDF this check could not read", "The number has no sentence behind it.", "RETAIN 13 SOURCE unreadable", ["Remove the number", "Publish it", "Add a wallboard", "Reset lists"], 0, "Unreadable text is not a fact.", "Delete the number."),
    ["Finish the note", "Label product claims as product claims"], uncertain=["The quality page says routing, assistance, and coaching can be refined with zero human involvement. This lab did not test that claim."]))
    return track(
        "t21",
        "Quality management and analytics",
        "Quality",
        "Evaluations, monitoring, analytics wording, and the claims this check would not upgrade.",
        "Quality",
        "Practice",
        "Quality scores a recording against a form. Analytics sweeps interactions. The percents stay on the page that printed them.",
        R,
    )
