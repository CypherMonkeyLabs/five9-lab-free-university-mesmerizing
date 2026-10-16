from curriculum_lib import ACD, APIS, DESK, SKILLS, WEM, WFM, lesson, compare, path, stack, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "The glossary is a contract with the page", "foundation", [
        "A glossary row in this lab is a term, a meaning, and the page that printed the meaning. Domain, skill group, campaign, and the rest already follow that rule. A new word with no page does not get a row.",
        "ACD is allowed because the Wikipedia article defines it. Skill group is allowed because the Five9 chapter defines it. A private acronym from a slide is not allowed until a public page says it.",
    ], [ACD, SKILLS], compare("In the glossary or not", "The test is a page.", "Has a page", ["ACD on Wikipedia", "Skill group on the admin chapter"], "No page", ["A slide acronym", "A guessed field name"]),
    "Test one word", ["Word", "Page"], [
        ("Word", "Hear", "Someone says a new acronym.", "hear"),
        ("Page", "Find", "Look for the public page.", "find"),
        ("Page", "Fail", "If the body did not open, there is no row.", "fail"),
        ("Word", "Keep", "The meaning stays shorter than the page.", "keep"),
        ("Reader", "Link", "The row points at the page.", "link"),
        ("Reader", "Drop", "No page, no row.", "drop"),
    ], [
        ("A glossary row needs", ["A confident tone", "A term, a meaning, and a page", "A package version", "An exam code"], 1, "That is the contract."),
        ("ACD is in bounds because", ["Every contact center uses it", "The Wikipedia page defines it", "Five9 printed a formula", "A badge says so"], 1, "The article opened."),
        ("A slide acronym with no public page", ["Gets a row anyway", "Does not get a row", "Becomes a skill", "Becomes a port"], 1, "No page, no row."),
        ("The meaning may", ["Add facts the page did not say", "Stay inside the page", "Include a customer quote as a spec", "Include an unread PDF number"], 1, "The page is the ceiling."),
        ("Skill group and ACD in one row would", ["Be precise", "Hide which page you mean", "Be required", "Fix the tab name"], 1, "They are different pages."),
    ], [("What does a row need?", "Term, meaning, page."), ("ACD allowed?", "Yes, from Wikipedia."), ("Slide acronym?", "No row."), ("Merge ACD and skill group?", "No.")],
    ("Accept or reject", "Take three words from a meeting and keep only the ones with a page.", ["One kept", "One rejected", "The page named"], "The rejected word has no row."),
    ("The glossary gains a row for a field nobody could open", "The row has a meaning and no page.", "ROW field SOURCE none", ["Delete the row", "Publish it", "Add a skill", "Change ANI"], 0, "The contract failed.", "Remove the row."),
    ["Keep the page on the row", "Reject words that have no page"]))
    R.append(L("l02", "The mind map only holds boxes you can cite", "foundation", [
        "A mind map of this floor can hold a domain, skill groups, the agent desktop, WFM, quality, and the API list, because each of those has a page this lab read. The lines between them are teaching lines. A line is not a protocol.",
        "The map fails when a box is a rumor. An unread admin dialog, an unreadable analytics PDF, and a marketplace this lab did not recount do not become boxes. They become a gap at the edge.",
    ], [SKILLS, DESK, WFM, APIS], path("Boxes this check can draw", "Each one has a page.", ["Skill groups", "Agent desktop", "WFM", "Quality pages", "API list", "A gap, not a box"]),
    "Add or refuse a box", ["Map", "Page"], [
        ("Map", "Ask", "Which page is this box?", "ask"),
        ("Page", "Open", "The page returned a body.", "open"),
        ("Map", "Draw", "The box uses the page's noun.", "draw"),
        ("Page", "Closed", "No body, no box.", "closed"),
        ("Map", "Gap", "The gap is labeled confirm.", "gap"),
        ("Reader", "Line", "The line is a teaching line, not a protocol.", "line"),
    ], [
        ("A box without a page is", ["Still useful", "Not allowed on this map", "A skill", "A port"], 1, "The map is a citation."),
        ("The line between desktop and CRM means", ["A specific socket this lab measured", "A teaching link to the page that named the integration", "A codec", "A badge"], 1, "Do not upgrade a line into a protocol."),
        ("An unreadable PDF becomes", ["A box with numbers", "A gap", "The service level", "The abandon rate"], 1, "No sentence, no box."),
        ("Skill groups can be a box because", ["Everyone knows them", "The admin chapter returned a body", "The marketplace said so", "A quote said so"], 1, "The chapter opened."),
        ("Confirm on the edge of the map means", ["The box is certified", "The page did not return a body", "The line is a trunk", "The count was audited"], 1, "Leave it off the drawing."),
    ], [("Box needs?", "A page."), ("Line is a protocol?", "No."), ("Unreadable PDF?", "A gap."), ("Skill groups box?", "Yes.")],
    ("Draw five boxes", "Use only pages this chapter cites. Add one gap.", ["Name each page", "Name the gap"], "No rumor became a box."),
    ("The map adds a screen-pop box with fields", "No page in this chapter printed those fields.", "BOX screen-pop", ["Turn it into a gap", "Keep the fields", "Delete skills", "Reset lists"], 0, "A box without a page breaks the map.", "Remove the box."),
    ["Draw only cited boxes", "Put unread pages on the edge as gaps"]))
    R.append(L("l03", "Sister technologies are the names on the neighboring pages", "practice", [
        "Sister technologies, in this lab, means products the Five9 pages name as living beside the domain. The WEM page names Verint as a partner example beside native WEM. The API page names Zoom Phone and Microsoft Teams. The CRM lists name Salesforce, ServiceNow, and the other CRMs on those lists.",
        "A sister is not a synonym. Verint is not native WEM. Teams is not Salesforce. The quality page's competency routing is not the skill-group chapter. Put the sister next to the domain and keep its own page.",
    ], [WEM, APIS], stack("Sisters this check can name", "Each stays on its page.", ["Verint, as a WEM partner example", "Zoom Phone and Microsoft Teams", "The CRM names on the API list"]),
    "Place a sister", ["Domain", "Sister"], [
        ("Domain", "Center", "Skills and campaigns stay in the domain.", "center"),
        ("Sister", "Verint", "Off to the side, with the WEM page.", "verint"),
        ("Sister", "Teams", "Off to the side, with the API page.", "teams"),
        ("Reader", "Refuse", "Do not merge the names.", "refuse"),
        ("Reader", "Ask", "Which one this floor bought.", "ask"),
        ("Reader", "Cite", "The caption names the page.", "cite"),
    ], [
        ("Verint is a sister because", ["It is the only WEM", "The WEM page names it as a partner example", "It is a codec", "It is a campaign type"], 1, "The page says both native and partner."),
        ("Teams belongs next to", ["The skill group", "The API page's UC list", "The forecast formula", "The badge"], 1, "That is the page that named it."),
        ("Calling Teams a CRM adapter is", ["Accurate", "A mix of two lists", "Required", "A prompt"], 1, "The page separates them."),
        ("A product the pages do not name", ["Can still be drawn as a sister", "Stays off the map", "Becomes a skill", "Becomes a port"], 1, "No name, no box."),
        ("Native WEM and Verint", ["Are synonyms", "Are two statements on one page", "Are both dialer modes", "Are both lists"], 1, "Ask which one is installed."),
    ], [("Why Verint?", "The WEM page names it."), ("Where does Teams go?", "On the API UC list."), ("Unnamed product?", "Off the map."), ("Synonym?", "No.")],
    ("Caption three sisters", "Name, page, and job.", ["Verint", "Teams or Zoom Phone", "One CRM"], "Each caption has a page."),
    ("The diagram labels Verint as native Five9 WFM", "The page said partner example.", "LABEL verint=native", ["Relabel it as the partner example", "Leave the label", "Delete forecasts", "Change ANI"], 0, "The word partner is the fact.", "Fix the label."),
    ["Caption each sister with its page", "Refuse unnamed products"]))
    R.append(L("l04", "The integration map is the API list, drawn", "practice", [
        "An integration map for this chapter is the API list turned sideways: CTI, Configuration, Reporting, Statistics, Web2Campaign, CRM SDK, and Web Connectors, plus the prebuilt CRM names and the UC names. REST is the access sentence for agents, administrators, supervisors, and reporting users.",
        "Web Connectors and the CRM SDK are both on that list and they are not the same row. A connector that opens a page and an SDK you build against are different objects. The map labels both. It does not invent payloads.",
    ], [APIS], path("One list, one map", "Labels only.", ["CTI Web Services API", "Reporting and Statistics, as two names", "CRM SDK", "Web Connectors", "Prebuilt CRM and UC names"]),
    "Place a label", ["List", "Map"], [
        ("List", "Read", "The seven API names are copied.", "read"),
        ("Map", "Split", "Reporting and Statistics stay apart.", "split"),
        ("Map", "SDK", "The SDK is its own box.", "sdk"),
        ("Map", "Web", "Web Connectors are their own box.", "web"),
        ("Map", "CRM", "Prebuilt names sit beside them.", "crm"),
        ("Reader", "Stop", "No payload is drawn.", "stop"),
    ], [
        ("Statistics and Reporting on the map are", ["One box", "Two names from the list", "Codecs", "Prompts"], 1, "The page prints both."),
        ("The CRM SDK is for", ["A named adapter you already have", "A CRM you bring, per the desktop and API pages", "A forecast", "A greeting"], 1, "That is the bring-your-own line."),
        ("Web Connectors are", ["The same box as the SDK", "A separate name on the list", "Skill groups", "Dispositions"], 1, "Do not merge them."),
        ("A payload field on this map is", ["Required", "Not drawn", "Always ANI", "Always the case number"], 1, "The list does not print payloads."),
        ("REST on the map is", ["A guess about every API", "The page's sentence about who the REST APIs serve", "A port", "A badge"], 1, "Agents, administrators, supervisors, and reporting users."),
    ], [("Reporting versus Statistics?", "Two names."), ("SDK versus connector?", "Two names."), ("Payloads?", "Not drawn."), ("Who does the REST sentence name?", "Agents, administrators, supervisors, reporting users.")],
    ("Draw the map", "Seven API labels and no fields.", ["CTI", "SDK", "Web Connectors"], "A reader can see they are different boxes."),
    ("The map shows Web Connectors and the SDK as one cloud", "The page printed two names.", "MAP merged", ["Split the boxes", "Leave the cloud", "Delete Salesforce", "Add a skill"], 0, "Two names, two boxes.", "Split them."),
    ["Draw the API list", "Do not draw payloads"]))
    R.append(L("l05", "A bridge is a teaching map, not an import", "advanced", [
        "A cross-platform bridge says how a person who knows another contact center might look for the same idea. Skill group is the Five9 queue the admin chapter describes. It is not a claim that another vendor's queue object imports.",
        "This chapter does not add gateway vendors, release names, or a migration wizard. Those sentences live on pages this chapter did not re-read. If you cannot open them, the bridge stops at the teaching sentence and the rest is confirm.",
    ], [SKILLS], compare("Bridge versus import", "Only one of these is claimed.", "Teaching bridge", ["A word in this lab for a word on a Five9 page"], "Import", ["Not described by the pages this chapter read"]),
    "Translate one word", ["Other", "Five9"], [
        ("Other", "Word", "Someone says queue.", "word"),
        ("Five9", "Page", "The chapter says skill group.", "page"),
        ("Reader", "Bridge", "The note says it is a teaching bridge.", "bridge"),
        ("Reader", "Stop", "No import button is drawn.", "stop"),
        ("Reader", "Gap", "Unread vendor pages stay confirm.", "gap"),
        ("Reader", "Cite", "The Five9 side has a URL.", "cite"),
    ], [
        ("A teaching bridge is", ["An import product", "A way to point a familiar word at a cited Five9 word", "A codec", "A badge"], 1, "It is a note, not a converter."),
        ("Skill group, on the Five9 side of the bridge, comes from", ["Memory", "The skill groups chapter", "A marketplace count", "A quote"], 1, "The chapter opened."),
        ("An import button in this chapter is", ["Documented", "Not documented", "On the WFM page", "On the API list"], 1, "These pages do not describe one."),
        ("A gateway vendor added from an unread PDF is", ["A bridge", "A confirm, with no box", "Required", "A prompt"], 1, "Unread stays off the bridge."),
        ("The other vendor's word can be", ["Used as if Five9 printed it", "The reader's word, labeled as theirs", "A disposition", "A forecast"], 1, "Label whose word it is."),
    ], [("What is a bridge?", "A teaching note."), ("Five9 queue word?", "Skill group."), ("Import button?", "Not in this chapter."), ("Unread vendor?", "Confirm, no box.")],
    ("Write one bridge", "Their word, Five9 word, page, and the word teaching.", ["No import", "No unread vendor"], "The note can be checked."),
    ("The bridge says a foreign queue object imports into a skill group", "No page in this chapter said that.", "IMPORT claimed", ["Reduce it to a teaching note", "Promise the import", "Delete the domain", "Change ANI"], 0, "A translation is not a converter.", "Remove the import."),
    ["Label the bridge as teaching", "Leave unread vendors off it"], uncertain=["This chapter does not re-quote gateway vendors or a migration wizard. Those pages were not the ones opened for these lessons."]))
    R.append(L("l06", "Future hooks stay unset until a page exists", "advanced", [
        "A future hook is a place the lab expects to grow and refuses to fake. The guide's cloud endpoint is unset. A product sentence that says often or up to is not a roadmap date. The API page's over 55 was not recounted.",
        "When a child page later returns a body, the hook can become a box. Until then it stays a hook: a named gap, last checked with the month, and no URL if the body did not open. That is how the map stays true while the catalog moves.",
    ], [APIS, WFM], path("A hook", "Not a feature.", ["Name the gap", "Say the body did not return", "No date", "No guessed field", "Replace the hook only when a page opens"]),
    "File one hook", ["Gap", "Later"], [
        ("Gap", "Name", "Skill Transfer priority, for example.", "name"),
        ("Gap", "Status", "Body did not return.", "status"),
        ("Later", "Wait", "No month is promised.", "wait"),
        ("Later", "Open", "A future reader opens the page.", "open"),
        ("Map", "Swap", "The hook becomes a box only then.", "swap"),
        ("Reader", "Keep", "Until then the hook stays blank.", "keep"),
    ], [
        ("A future hook may include", ["A made-up release date", "The name of a page that did not return a body", "A customer metric", "An exam code"], 1, "The name of the gap is the content."),
        ("The guide cloud endpoint is", ["A Five9 API", "Unset in this lab", "The CTI API", "The forecast engine"], 1, "Do not pretend it calls out."),
        ("Over 55 becomes a hook if", ["You recount and the number moves", "You want a rounder number", "Teams is removed", "Verint is native"], 1, "A recount would replace their sentence. Until then, quote them."),
        ("Turning a hook into a box requires", ["Confidence", "A page that returned a body", "A quote", "A theme"], 1, "The page is the gate."),
        ("A roadmap date this chapter adds is", ["January", "None", "Next quarter", "2027"], 1, "No date was on the pages."),
    ], [("What may a hook hold?", "The name of an unread page."), ("Guide endpoint?", "Unset."), ("When does a hook become a box?", "When a page returns a body."), ("Roadmap date?", "None added.")],
    ("Write two hooks", "Use gaps from the routing and CRM chapters.", ["No dates", "No fields"], "Both hooks are names, not features."),
    ("The hook is dated next spring", "No page said that.", "DATE next-spring", ["Remove the date", "Publish it", "Add a skill", "Reset a list"], 0, "A hook is not a calendar.", "Delete the date."),
    ["Name the gap", "Add a date only when a page prints one"], uncertain=["This lab's guide does not call a cloud endpoint. No product roadmap date is added in this chapter."]))
    R.append(L("l07", "Read the map before you add a box", "advanced", [
        "The review is the whole ecosystem section in one pass. Glossary: every new word has a page. Mind map: every box has a page and every line is teaching. Sisters: Verint, Zoom Phone, Teams, and the CRM names, each captioned. Integration map: the API list, unmerged. Bridges: teaching only. Hooks: named gaps, no dates.",
        "If a box fails the test, it comes off. The domain in the middle is still the skill groups, the campaigns, and the desktop the other chapters described. The neighbors do not leak into that box.",
    ], [SKILLS, DESK, APIS, WEM], path("The pass", "Six checks.", ["Glossary", "Mind map", "Sisters", "Integration map", "Bridges", "Hooks"]),
    "Review a crowded map", ["Box", "Test"], [
        ("Box", "Find", "One box has no caption.", "find"),
        ("Test", "Page", "Ask for the page.", "page"),
        ("Test", "Fail", "No page, the box leaves.", "fail"),
        ("Sister", "Check", "Verint is not labeled native.", "verint"),
        ("API", "Check", "SDK and connectors are split.", "api"),
        ("Hook", "Check", "No date was added.", "hook"),
    ], [
        ("A box with no page", ["Stays for color", "Comes off the map", "Becomes a skill", "Becomes a port"], 1, "The review removes it."),
        ("A sister caption must include", ["A quote", "The page that named it", "A package version", "An exam code"], 1, "The page is the caption."),
        ("An integration map that merges SDK and Web Connectors", ["Passes", "Fails", "Is the forecast", "Is adherence"], 1, "The list printed two names."),
        ("A bridge that promises an import", ["Passes", "Fails", "Is required", "Is a prompt"], 1, "Teaching is the only claim."),
        ("A hook with a season on it", ["Passes", "Fails", "Is the WFM card", "Is the CTI API"], 1, "No date was sourced."),
    ], [("No page?", "Remove the box."), ("Sister caption?", "Includes the page."), ("Merged SDK?", "Fails."), ("Dated hook?", "Fails.")],
    ("Run the pass", "Take a sketch and mark each box keep or cut.", ["One cut", "One keep", "The reason"], "The cut box had no page."),
    ("The center box says the CRM fields live inside the skill group", "The neighbors leaked.", "CENTER includes CRM fields", ["Put the fields back on the CRM gap", "Leave them in the center", "Delete WFM", "Change ANI"], 0, "The center is the domain objects the admin chapter described.", "Move the fields out."),
    ["Run the six checks", "Cut any box that has no page"]))
    return track(
        "t23",
        "Ecosystem",
        "Ecosystem",
        "Glossary, mind map, sister technologies, the integration list, teaching bridges, and hooks that stay blank.",
        "Ecosystem",
        "Practice",
        "A box needs a page. A line is teaching. A gap stays a gap until a body comes back.",
        R,
    )
