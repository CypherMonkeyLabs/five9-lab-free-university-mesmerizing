from curriculum_lib import ACD, SKILLS, lesson, compare, path, stack, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "An ACD distributes. A skill group is the Five9 queue", "foundation", [
        "Wikipedia describes an automatic call distributor as a telephony device that answers and distributes incoming calls to a group of terminals or agents. It says the route can depend on the caller's number, the number dialed, the time of day, or an answer to a voice prompt, and that an advanced system may take input from CTI, CSTA, or an IVR.",
        "The Five9 skill groups chapter is the queue this lab could read. It says skill groups organize users who have the agent or supervisor role into groups assigned to the call queues that are part of campaigns. That is the Five9 object. The Wikipedia article is the general word ACD. Do not treat them as the same paragraph.",
    ], [ACD, SKILLS], compare("Two pages", "Read both. Quote the one you mean.", "Wikipedia ACD", ["Distributes incoming calls", "May use number, time, or a prompt"], "Five9 skill group", ["Agent or supervisor users", "A queue inside a campaign"]),
    "Name the object", ["Reader", "Page"], [
        ("Reader", "Ask", "Is this the general word or the Five9 object?", "ask"),
        ("Page", "Wiki", "The general word is on Wikipedia.", "wiki"),
        ("Page", "Skill", "The Five9 queue is the skill group.", "skill"),
        ("Reader", "Role", "Only agent or supervisor users are named.", "role"),
        ("Reader", "Stop", "Do not paste a vendor algorithm the page did not print.", "stop"),
        ("Reader", "Cite", "The sentence keeps its page.", "cite"),
    ], [
        ("An ACD, on the Wikipedia page, distributes calls to", ["A single voicemail box only", "A group of terminals or agents", "A campaign profile", "A Credly badge"], 1, "That is the article's definition."),
        ("Who can be in a Five9 skill group, per the chapter that opened?", ["Any login", "Users with the agent or supervisor role", "SIP trunks", "Campaign profiles by themselves"], 1, "The chapter names those roles."),
        ("CTI, on the Wikipedia page, is", ["A Five9 package version", "One input an advanced ACD may use", "A dialing mode", "A list reset"], 1, "The article lists CTI, CSTA, or IVR as possible inputs."),
        ("The skill group and the Wikipedia ACD are", ["One sentence you can merge", "Two pages. Quote the one you mean", "Both codecs", "Both exam codes"], 1, "They answer different questions."),
        ("A route based on the number dialed is described on", ["The Wikipedia ACD page", "A package number", "The Credly badge", "A theme swatch"], 1, "The article includes the number dialed."),
    ], [("General word?", "ACD, on Wikipedia."), ("Five9 queue?", "A skill group."), ("Who is in it?", "Agent or supervisor users."), ("Merge the pages?", "No.")],
    ("Two sentences", "Write one Wikipedia sentence and one Five9 sentence.", ["Name the ACD idea", "Name the skill group", "Do not invent a routing algorithm"], "Each sentence has its own page."),
    ("A design says Five9 always routes longest-idle", "No opened page in this chapter says that.", "CLAIM longest-idle SOURCE none", ["Delete the claim until a page prints it", "Keep it because other ACDs do it", "Change the codec", "Add a badge"], 0, "A general ACD idea is not a Five9 setting.", "Cite the page or drop the sentence."),
    ["Separate the general word from the Five9 object", "Quote the page that opened"]))
    R.append(L("l02", "One person, several skills. One campaign, several groups", "foundation", [
        "The same chapter says users can be assigned to multiple skill groups, and campaigns can have multiple skill groups. Membership is not a single label for life.",
        "A campaign with several groups is a pool you chose. A user in several groups can be offered work from more than one queue. This page does not say which queue wins when both are ringing. That tie-break did not come back in this check.",
    ], [SKILLS], stack("What the chapter allows", "Both directions are written.", ["A user in more than one skill group", "A campaign with more than one skill group", "A tie-break that this check did not read"]),
    "Count memberships", ["Admin", "User"], [
        ("Admin", "Groups", "Billing and Sales both exist.", "groups"),
        ("User", "Both", "One agent is in both.", "both"),
        ("Campaign", "Pool", "The campaign lists both groups.", "pool"),
        ("Admin", "Ask", "Which call should win is still a question.", "ask"),
        ("Admin", "Gap", "The tie-break is not copied from this page.", "gap"),
        ("Admin", "Note", "The design says pool, and says the tie-break is unread.", "note"),
    ], [
        ("A user may belong to", ["Only one skill group", "Multiple skill groups", "No role at all", "Only a profile"], 1, "The chapter says multiple."),
        ("A campaign may have", ["Only one skill group", "Multiple skill groups", "No queues", "Only ANI"], 1, "The chapter says campaigns can have multiple."),
        ("The tie-break when two skills can take the call is", ["Printed as longest idle on this page", "Not in the chapter this lab read", "Always the codec", "Always Default"], 1, "Do not invent it."),
        ("A pool is", ["Forbidden", "What you get when the campaign lists more than one group", "A SIP header", "A badge"], 1, "Multiple groups on a campaign are allowed."),
        ("Supervisor users are", ["Excluded", "Named alongside agents", "Trunks", "Lists"], 1, "The chapter names the supervisor role."),
    ], [("Several skills per user?", "Yes."), ("Several groups per campaign?", "Yes."), ("Tie-break quoted?", "No."), ("Pool allowed?", "Yes.")],
    ("Draw the pool", "Name two groups and one person who is in both.", ["Billing", "Sales", "The shared person", "The unread tie-break"], "The drawing matches the chapter, and the gap is labeled."),
    ("The runbook says a person can have only one skill", "The chapter says otherwise.", "RUNBOOK one-skill PAGE multiple", ["Correct the runbook", "Delete the extra membership to match the runbook", "Change ANI", "Stop the domain"], 0, "The public chapter allows multiple memberships.", "Fix the runbook."),
    ["Allow multiple memberships", "Label the tie-break as unread"], uncertain=["Which skill wins when one agent is eligible for two ringing queues was not on the skill groups chapter this lab read."]))
    R.append(L("l03", "Outbound uses Skills. Inbound and autodial use Outbound Skills", "practice", [
        "The chapter splits the tabs. Outbound campaigns route dialer calls by the skill groups on the Skills tab of the campaign properties. Inbound and autodial campaigns route to the skill groups listed on the Outbound Skills tab of the inbound campaign properties.",
        "The word outbound sits on an inbound campaign. That is the published name. Ready agents on the other tab are not the queue the page describes.",
    ], [SKILLS], compare("Read the tab", "The chapter names both.", "Outbound campaign", ["Skills tab"], "Inbound and autodial", ["Outbound Skills tab"]),
    "Attach one group twice", ["Admin", "Campaign"], [
        ("Admin", "Group", "Support exists and has members.", "group"),
        ("Campaign", "Out", "The outbound campaign uses Skills.", "skills"),
        ("Campaign", "In", "The inbound campaign uses Outbound Skills.", "out"),
        ("Campaign", "Wrong", "Skills on an inbound campaign is the other tab.", "wrong"),
        ("Agent", "Ready", "Ready does not repair the tab.", "ready"),
        ("Admin", "Retest", "A test call is the check.", "test"),
    ], [
        ("Inbound skill assignment lives on a tab named", ["Inbound Skills", "Outbound Skills", "ANI", "Pause"], 1, "That is the published name."),
        ("Outbound campaigns use", ["Outbound Skills", "The Skills tab", "No skills", "Only Default"], 1, "The chapter says the Skills tab."),
        ("Autodial is grouped with", ["Outbound's Skills tab", "Inbound, on Outbound Skills", "No queue", "A badge"], 1, "The chapter names inbound and autodial together."),
        ("Ready agents on the wrong tab", ["Still receive the call the page describes", "Are not the assignment the page describes", "Change the codec", "Export a matrix"], 1, "The campaign is pointing at the other list."),
        ("The awkward name is", ["A rumor", "Printed on the skill groups chapter", "An exam code", "A JRE flag"], 1, "It is in the chapter."),
    ], [("Inbound tab?", "Outbound Skills."), ("Outbound tab?", "Skills."), ("Autodial?", "With inbound."), ("Ready on the wrong tab?", "Not the assignment the page describes.")],
    ("Label two campaigns", "Write the tab name under inbound and under outbound.", ["Inbound", "Outbound", "Autodial"], "Inbound and autodial match."),
    ("Support never rings on the new inbound line", "The group was saved on Skills.", "INBOUND tab=Skills", ["Move it to Outbound Skills", "Add power lines", "Delete the prompt", "Enable an old browser"], 0, "Wrong tab.", "Use the tab the chapter names."),
    ["Memorize the tab names", "Check the tab before the carrier"]))
    R.append(L("l04", "You can add, change, remove, and message the group", "practice", [
        "The chapter says you can add, modify, and remove skill groups. It also says you can send a message to all the agents in a skill group.",
        "Those four verbs are the administration the page states. The click-path inside each verb is a child topic. This check read the chapter, not a screenshot of every dialog.",
    ], [SKILLS], path("Four verbs", "Stay inside the sentence.", ["Add", "Modify", "Remove", "Message every agent in the group"]),
    "A new queue", ["Admin", "Agents"], [
        ("Admin", "Add", "The group is created.", "add"),
        ("Admin", "Modify", "The name or the membership changes.", "mod"),
        ("Admin", "Message", "One note goes to the members.", "msg"),
        ("Admin", "Remove", "Removal is allowed, and it is not casual.", "rem"),
        ("Agents", "See", "The message is for the people in the group.", "see"),
        ("Admin", "Stop", "Do not invent extra buttons.", "stop"),
    ], [
        ("Removing a skill group is", ["Forbidden", "One of the actions the chapter names", "A dialer mode", "A codec"], 1, "The chapter says you can remove them."),
        ("A message from the skill group goes to", ["The carrier", "All the agents in that skill group", "Only supervisors outside the group", "The IVR prompt library"], 1, "The chapter says all the agents in the group."),
        ("Modify means", ["The group can be changed", "The group is frozen", "ANI changes by itself", "The domain closes"], 1, "The chapter includes modify."),
        ("The dialog screenshots for each verb were", ["Quoted click by click in this lesson", "Not the page this lesson read. The chapter states the verbs", "A SIP trace", "A badge"], 1, "Do not invent the dialog."),
        ("Add is", ["Unsupported", "Named", "A list mode", "A retention clock"], 1, "The chapter says you can add skill groups."),
    ], [("Remove allowed?", "Yes, the chapter says so."), ("Who gets the message?", "Agents in the group."), ("Click-path quoted?", "No."), ("Modify?", "Named.")],
    ("Write the four verbs", "Add, modify, remove, message.", ["Do not add a fifth verb", "Say who receives the message"], "The list matches the chapter."),
    ("A runbook says skill groups cannot be removed", "The chapter says they can.", "RUNBOOK remove=no PAGE remove=yes", ["Correct the runbook and treat removal as a real change", "Keep the runbook", "Reset a list", "Change TLS"], 0, "The public chapter includes remove.", "Update the runbook."),
    ["Use the four verbs the chapter names", "Do not invent the dialogs"]))
    R.append(L("l05", "Service level and voicemail are topics on the same chapter", "practice", [
        "The skill groups table of contents that opened lists Managing Skill Group Service Levels, Routing Voicemail Messages to Skill Groups, Managing Skill Voicemail Messages, Managing Skill Voicemail Greetings, and Managing Audio Files for Skill Groups.",
        "Those titles say the work exists on the chapter. The child pages did not return a body in this check, so this lesson does not describe the service-level math or the voicemail click-path. The titles are the fact. The procedure is confirm.",
    ], [SKILLS], stack("Titles this check could read", "Procedures under them did not open.", ["Service levels", "Routing voicemail to skill groups", "Voicemail messages and greetings", "Audio files"]),
    "Stop at the title", ["Reader", "Child page"], [
        ("Reader", "See", "The contents list names service level.", "see"),
        ("Reader", "See2", "It also names skill voicemail.", "vm"),
        ("Child", "Closed", "The child page did not return a body.", "closed"),
        ("Reader", "Refuse", "No percent and no click-path is copied.", "refuse"),
        ("Reader", "Say", "The design says the topic exists.", "say"),
        ("Reader", "Mark", "The procedure is marked confirm.", "mark"),
    ], [
        ("Service level appears as", ["An invented percent", "A topic title on the skill groups chapter", "A dialer mode", "A badge"], 1, "The contents list names it."),
        ("Skill voicemail routing appears as", ["Absent", "A topic title on the same chapter", "A list penetration mode", "A codec"], 1, "The contents list names it."),
        ("This lesson's service-level formula is", ["Fully quoted", "Not quoted. The child page did not return a body", "Always 80/20", "A JRE flag"], 1, "Do not invent the math."),
        ("Greetings are", ["Named as a topic title", "Denied by the chapter", "A campaign type", "An exam code"], 1, "Managing Skill Voicemail Greetings is on the contents list."),
        ("A page that did not return a body is", ["Still linked as if it were read", "Marked confirm, with no procedure copied", "Treated as a law", "Ignored"], 1, "Confirm means the body was not read."),
    ], [("Service level on the contents?", "Yes."), ("Formula quoted?", "No."), ("Voicemail topic?", "Yes."), ("Child page body?", "Did not return.")],
    ("List the titles", "Write the topic names you are allowed to say.", ["Service level", "Voicemail routing", "Greetings", "The missing procedure"], "The missing procedure is labeled confirm."),
    ("A slide prints 80 percent in 20 seconds as the Five9 default", "The child page did not open, so the number has no source here.", "SL 80/20 SOURCE unread", ["Remove the number", "Keep it as industry habit", "Add lines", "Change ANI"], 0, "A habit is not the chapter.", "Delete the number until the child page is read."),
    ["Name the topic", "Refuse the unread procedure"], uncertain=["The service-level and skill-voicemail child pages did not return a body in this check. No threshold and no click-path is stated."]))
    R.append(L("l06", "Adding skills to a campaign points at another guide", "advanced", [
        "The skill groups chapter says that adding skill groups to campaigns is covered in Configuring Skills in the Campaign Administrator's Guide. It does not paste that guide into the chapter.",
        "The Configuring Skills page and the Skill Transfer module page did not return a body in this check. Priority numbers, an ignore-order switch, and a Default queue label are not copied here. If you need them, open those pages yourself and mark anything you cannot read as confirm.",
    ], [SKILLS], path("Where the sentence stops", "The pointer is not the other guide.", ["Skill groups chapter", "Pointer to Configuring Skills", "That page did not return a body", "No priority number is copied"]),
    "Follow the pointer", ["Chapter", "Guide"], [
        ("Chapter", "Point", "It names Configuring Skills.", "point"),
        ("Guide", "Closed", "The page did not return a body.", "closed"),
        ("Reader", "Wait", "No priority value is typed from memory.", "wait"),
        ("Reader", "IVR", "Skill Transfer's own page also did not return a body.", "ivr"),
        ("Reader", "Say", "The design says the pointer exists.", "say"),
        ("Reader", "Confirm", "The unread page is confirm.", "confirm"),
    ], [
        ("Where does the chapter send you to add skills to a campaign?", ["The Credly badge", "Configuring Skills in the Campaign Administrator's Guide", "The codec page", "A community rumor only"], 1, "That is the pointer."),
        ("Did this check read the Configuring Skills body?", ["Yes, every field", "No. The page did not return a body", "Yes, as a PDF appendix", "It is the same page as skill groups"], 1, "A pointer is not the other page."),
        ("A priority number for Skill Transfer in this lesson is", ["Quoted", "Not quoted", "Always 20", "Always 100"], 1, "That page did not return a body."),
        ("Default queue behavior in this lesson is", ["Fully specified", "Not copied, because that article body did not return", "Always abandon", "A list mode"], 1, "Do not reuse an unread article as if this page printed it."),
        ("The safe sentence is", ["The chapter points at another guide", "The other guide's fields, from memory", "Longest idle is the default", "Level 1 is defined here"], 1, "Stay on the sentence you read."),
    ], [("Pointer name?", "Configuring Skills."), ("Body read?", "No."), ("Priority number?", "Not in this lesson."), ("Safe sentence?", "The chapter points elsewhere.")],
    ("Write the pointer", "One sentence that names the guide and stops.", ["Configuring Skills", "Campaign Administrator's Guide", "No extra field"], "The sentence does not invent a field."),
    ("A diagram shows Skill Transfer priority 20 as the Five9 default", "This check did not read that module page.", "PRIORITY 20 SOURCE unread", ["Remove the number", "Publish the diagram", "Add predictive lines", "Change the greeting"], 0, "An unread page is not a default.", "Delete the number."),
    ["Follow the pointer", "Do not fill the gap from memory"], uncertain=["Configuring Skills and the Skill Transfer module page did not return a body in this check. No priority value is stated."]))
    R.append(L("l07", "A routing review you can finish", "advanced", [
        "A routing note can be finished with the pages that opened. Say that a skill group is agent or supervisor users on a campaign queue. Say whether the user and the campaign have one group or several. Say which tab the campaign type uses. Say that service level and voicemail are topic titles.",
        "Then stop. Availability, caller ID, ANI, IVR, and DNIS are routing inputs on the Wikipedia page, not a Five9 field list. Competency-based routing is a sentence on the quality page, in the quality chapter, not a skill-group setting this page printed.",
    ], [SKILLS, ACD], path("The review", "Five lines, then a gap list.", ["Who is in the group", "How many groups", "Which tab", "Which topic titles exist", "Which pages did not open"]),
    "Review one queue", ["Note", "Gap"], [
        ("Note", "Who", "Agents or supervisors.", "who"),
        ("Note", "Count", "One group or several, on purpose.", "count"),
        ("Note", "Tab", "Skills, or Outbound Skills.", "tab"),
        ("Note", "Titles", "Service level and voicemail are titles.", "titles"),
        ("Gap", "Unread", "Tie-break, formula, and priority stay blank.", "gap"),
        ("Note", "Sign", "The note matches the opened pages.", "sign"),
    ], [
        ("A finished routing note includes", ["A guessed longest-idle rule", "Roles, membership, the tab, and the topic titles", "A package version", "An exam code"], 1, "Those are the sentences this chapter read."),
        ("Wikipedia routing inputs such as ANI and DNIS are", ["Five9 field names by themselves", "On the Wikipedia page, not a Five9 dialog this chapter read", "Codecs", "Badges"], 1, "Keep the page attached to the sentence."),
        ("The tie-break belongs in the note as", ["A number", "A blank marked confirm", "Level 1", "Priority 20"], 1, "It was not read."),
        ("The tab for inbound is", ["Skills", "Outbound Skills", "Either, it does not matter", "Absent"], 1, "The chapter names Outbound Skills."),
        ("Signing a note that adds an unread default is", ["Thorough", "A failure of the review", "Required", "A codec choice"], 1, "The review stops at the opened pages."),
    ], [("What must the note name?", "Roles, membership, tab, topic titles."), ("Wikipedia inputs?", "Not Five9 fields by themselves."), ("Unread tie-break?", "Leave it blank."), ("Inbound tab?", "Outbound Skills.")],
    ("Finish one note", "Use a real or sample queue and stop at the gaps.", ["Name the group", "Name the tab", "List the confirms"], "Nothing unread was filled in."),
    ("The review adds a skill level of 1 as the highest priority", "That sentence was not on the page this chapter read.", "LEVEL 1 SOURCE unread", ["Remove it", "Keep it as a common ACD habit", "Add a third skill", "Reset the list"], 0, "A habit is not the chapter.", "Delete the level until its page is read."),
    ["Finish the note", "Leave the unread fields blank"]))
    return track(
        "t19",
        "Skills routing and ACD",
        "Skills and ACD",
        "How a Five9 skill group routes work, and which ACD details this check could not read.",
        "Routing",
        "Practice",
        "A skill group is the queue the admin chapter describes. The general word ACD stays on its own page.",
        R,
    )
