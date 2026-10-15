from curriculum_lib import PLAN, SKILLS, INBOUND, LISTS, DISP, PROFILES, PROFILEHOW, lesson, stack, path, compare, track

def build():
    A = []
    A.append(lesson("l01", "A contact center is not a phone system", "foundation", [
        "A PBX connects extensions. A contact center adds queues, skills, lists, dispositions, and reports around those calls. Five9 Virtual Contact Center is that layer, hosted as a domain rather than as servers you rack.",
        "The planning topic does not start with a trunk. An outbound build starts with skill groups, user profiles, users, contact fields, lists, dispositions, and campaign profiles, and only then the campaign. Inbound and autodial add prompts and IVR scripts on that path.",
    ], [PLAN, SKILLS], stack("Outbound build order", "Published planning order, before the campaign exists.", ["Skill groups", "User profiles and users", "Contact fields and lists", "Dispositions", "Campaign profiles", "Campaigns"]),
    "Outbound build order", ["Admin", "Domain"], [
        ("Admin", "Skills", "Create the queues agents will belong to.", "skill groups"),
        ("Admin", "Users", "Profiles, then accounts.", "users"),
        ("Admin", "Lists", "Fields, then reconciled lists.", "lists"),
        ("Admin", "Codes", "Dispositions the dialer and the reports share.", "dispositions"),
        ("Admin", "Profile", "ANI and list behavior sit on the profile.", "profile"),
        ("Domain", "Campaign", "Create the campaign and attach one profile.", "campaign"),
    ], [
        ("What is built before an outbound campaign?", ["Only a SIP trunk", "Skills, users, lists, dispositions, and profiles", "A Studio task", "An E911 location"], 1, "The planning topic lists those objects before campaigns."),
        ("Which roadmaps add IVR scripts?", ["Outbound only", "Inbound and autodial", "Reporting only", "Headset setup only"], 1, "Inbound and autodial add prompts and IVR scripts."),
        ("Where do agents get grouped for a queue?", ["In a CUCM partition", "In a skill group", "In an ANI field", "In the call log"], 1, "Skill groups hold agents and supervisors for campaign queues."),
        ("A Five9 domain is", ["One agent station", "The tenant you configure", "A single DNIS", "A disposition code"], 1, "Users, campaigns, and lists belong to the domain."),
        ("Why is the IVR not step one?", ["Scripts cannot play audio", "The script names skills and dispositions that must already exist", "IVR is outbound-only", "Profiles replace scripts"], 1, "The roadmap creates the objects the script will reference."),
    ], [("Outbound, what comes first?", "Skill groups, then users, lists, dispositions, profiles, campaigns."), ("Which builds add IVR?", "Inbound and autodial."), ("What is a skill group?", "Agents and supervisors for a campaign queue."), ("What is a domain?", "The VCC tenant.")],
    ("Order the build", "Put the outbound objects in the published order.", ["List the six layers", "Check them against the planning topic", "Mark where IVR would insert for inbound"], "You can say why a campaign with no skill cannot route."),
    ("Busy test number on day one", "The new DNIS plays busy and no agent phone rings.", "CAMPAIGN Retail state=NOT_RUNNING dnis=8005550101", ["The inbound campaign is not running", "G.711 was removed", "TCPA blocked the caller", "WEM deleted the DNIS"], 0, "A stopped inbound campaign does not answer.", "Start the campaign. Callers otherwise hear busy."),
    ["Name the outbound build order", "Say where IVR enters an inbound build"], callout=("First check", "A busy DNIS is often a campaign that was never started.")))

    A.append(lesson("l02", "The domain is the tenant", "foundation", [
        "You sign into one domain. Skill groups, users, lists, prompts, scripts, and campaigns live there. Another domain does not inherit them.",
        "Five9 does not use CUCM-style partitions and calling search spaces. If you are coming from Unified Communications Manager, do not look for a partition table. Look for the domain, then skills and campaigns. That mapping is a teaching bridge, not a vendor migration wizard.",
    ], [PLAN, SKILLS], stack("Inside one domain", "Objects that do not leak into the next domain.", ["Users and profiles", "Skill groups", "Lists and fields", "Dispositions", "IVR scripts", "Campaigns"]),
    "Sign in and name the boundary", ["Admin", "Domain"], [
        ("Admin", "Login", "The administrator opens one domain.", "domain login"),
        ("Domain", "Users", "Accounts exist only here.", "users"),
        ("Domain", "Skills", "Queues exist only here.", "skills"),
        ("Domain", "Lists", "Contact rows exist only here.", "lists"),
        ("Admin", "Check", "A second domain is a separate build.", "no inheritance"),
        ("Admin", "Bridge", "Write 'no partitions' on the cutover notes.", "teaching map"),
    ], [
        ("Can campaign A in domain East use a list from domain West?", ["Yes, lists are global", "No. Lists belong to the domain", "Only on Tuesdays", "Only if the ANI matches"], 1, "The domain is the boundary."),
        ("What replaces a CUCM partition in this lab's map?", ["A calling search space", "The domain, then skills and campaigns", "A SIP 180", "A disposition"], 1, "Five9 public admin docs describe domains and skills, not CUCM partitions."),
        ("Who can sit in a skill group?", ["Only reporting users", "Users with the agent or supervisor role", "Only Studio API keys", "Only the ITSP"], 1, "The skill group topic says agent or supervisor roles."),
        ("A user can be in how many skill groups?", ["Exactly one", "More than one", "None, skills are on the trunk", "Only three"], 1, "Users can be assigned to multiple skill groups."),
        ("A campaign can have how many skill groups?", ["One only", "More than one", "Zero, always", "Only the Default queue"], 1, "Campaigns can have multiple skill groups."),
    ], [("Domain boundary?", "Users, lists, skills, and campaigns stay in that domain."), ("CUCM partition equivalent?", "There isn't one. Teach domain, skills, campaigns."), ("Skill membership?", "Agent or supervisor users, and a user may have several skills."), ("Multiple skills on a campaign?", "Yes."),],
    ("Draw the boundary", "Sketch two domains and refuse to share a list between them.", ["Name three objects that stay inside a domain", "Write the CUCM idea you will not look for", "Say which roles can join a skill"], "A teammate can repeat the boundary without saying 'partition'."),
    ("Agent missing from the queue", "The agent is logged in and Ready, and the queue never offers the call.", "USER ada READY skills=[] CAMPAIGN Billing skills=[Billing]", ["The user has no skill assignment", "The carrier revoked TLS", "Paste is disabled", "The profile has two ANIs"], 0, "A Ready agent with no matching skill is not in that queue.", "Add the user to the Billing skill group."),
    ["State the domain boundary", "Say which roles join a skill group"], uncertain=["This lesson's CUCM comparison is a teaching map. Five9 does not publish it as a migration product."]))

    A.append(lesson("l03", "Roles on the floor", "foundation", [
        "The same person is not every role. Agents take contacts. Supervisors can sit in skill groups with agents. Administrators configure the domain. Reporting is its own permission: standard reports do not appear without the Reporting role and at least one reporting permission.",
        "Administrator permissions are finer than the job title. Editing call variables, for example, depends on 'User Can Edit Call Variables' on the administrator role. Skipping a permission looks like a missing feature.",
    ], [SKILLS, cite_reports()], stack("Roles", "Separate the person from the permission.", ["Agent", "Supervisor", "Administrator", "Reporting"]),
    "Who can do what", ["User", "VCC"], [
        ("User", "Agent", "Takes the contact from a skill.", "agent"),
        ("User", "Supervisor", "May also belong to a skill group.", "supervisor"),
        ("User", "Admin", "Builds campaigns, scripts, and users.", "admin"),
        ("VCC", "Deny", "A report menu stays hidden without the Reporting role.", "reporting role"),
        ("User", "Permission", "Call-variable edits need an explicit permission.", "CAV permission"),
        ("VCC", "Audit", "Write the role next to every login in the design.", "audit"),
    ], [
        ("A supervisor wants a call log and the menu is missing. First check?", ["The codec", "The Reporting role and a reporting permission", "TCPA mode", "The Equinix port"], 1, "Dashboard and reports require the Reporting role plus a permission."),
        ("Can a supervisor be placed in a skill group?", ["No", "Yes. The skill topic includes the supervisor role", "Only in UK domains", "Only for autodial"], 1, "Skill groups organize agent or supervisor users."),
        ("Editing call variables requires", ["The agent headset", "User Can Edit Call Variables on the administrator role", "A Studio Build key only", "SAML for every user"], 1, "The call-variable article names that permission."),
        ("Agents configure IVR scripts. True or false?", ["True", "False. That is administrator work", "True on Sundays", "True in preview mode"], 1, "Script editing is an administrator task in the IVR folders."),
        ("Reporting data the agent sees on a screen pop is the same as a standard report. True or false?", ["True, always", "False. Reports are a separate application and role", "True if the ANI matches", "False because reports are illegal"], 1, "Standard reports live in Dashboard and Reports."),
    ], [("Reporting menu missing?", "Check the Reporting role and a reporting permission."), ("Supervisor in a skill?", "Yes, the skill topic allows it."), ("Call variable permission?", "User Can Edit Call Variables."), ("Who edits IVR?", "An administrator.")],
    ("Role card", "Write four logins and the one task each is allowed to do.", ["Name an agent task", "Name an admin task", "Name the reporting gate"], "You did not give the agent the IVR folder."),
    ("Hidden reports", "A supervisor says reporting is broken.", "LOGIN sam roles=[Supervisor] reportingPerm=none", ["The Reporting role or permission is absent", "SBC A is down", "The list is in vertical mode", "Java is missing on a Mac"], 0, "The report catalog is permissioned.", "Add the Reporting role and a reporting permission."),
    ["Separate agent, supervisor, admin, and reporting", "Name one fine-grained admin permission"]))

    A.append(lesson("l04", "Three campaign types", "foundation", [
        "Public admin topics describe three campaign types: inbound, outbound, and autodial. Inbound answers a DNIS and runs the campaign IVR. Outbound uses the dialer and an agent. Autodial also dials a list, and the planning topic groups it with inbound when you add prompts and IVR.",
        "Blended, on the product page, is agents moving between inbound and outbound. It is not a fourth campaign type in the planning roadmap. Do not create an object named Blended and expect the admin guide to define it.",
    ], [PLAN, INBOUND, cite_out()], compare("Campaign types", "Three types in the admin roadmap. Blended is an operating description.", "Campaign type", ["Inbound", "Outbound", "Autodial"], "Not a type", ["Blended agent work", "A CUCM partition", "A report layout"]),
    "Which object do you create?", ["Designer", "VCC"], [
        ("Designer", "Inbound", "A DNIS, a running campaign, an IVR script.", "inbound"),
        ("Designer", "Outbound", "A list, a dialing mode, agents in skills.", "outbound"),
        ("Designer", "Autodial", "A list plus prompts and an IVR path.", "autodial"),
        ("VCC", "Run", "Inbound answers only while the campaign runs.", "state"),
        ("Designer", "Blend", "Staff agents on both inbound and outbound skills.", "blend"),
        ("VCC", "Refuse", "Do not look for a campaign type called Blended.", "no fourth type"),
    ], [
        ("Which type answers a DNIS?", ["Outbound", "Inbound", "Preview", "TCPA"], 1, "Inbound campaigns receive calls from a DNIS."),
        ("What happens if that inbound campaign is stopped?", ["Calls whisper", "Callers hear busy", "Calls go to Studio", "Calls become emails"], 1, "The inbound topic says callers hear a busy signal."),
        ("Autodial is grouped with which build steps?", ["Headset drivers", "Prompts and IVR scripts", "Equinix Fabric only", "STIR/SHAKEN only"], 1, "The planning topic adds prompts and IVR for autodial and inbound."),
        ("Blended is", ["A fourth campaign type in the planning list", "A way of staffing agents across inbound and outbound", "A TLS cipher", "A report layout"], 1, "The outbound product page describes blended agent work. The planning list has three campaign types."),
        ("Outbound campaigns are for", ["DNIS treatment only", "Dialer calls to listed contacts", "911 only", "IVR with no list"], 1, "Outbound uses lists and dialing modes."),
    ], [("Three types?", "Inbound, outbound, autodial."), ("Stopped inbound?", "Busy signal."), ("What is blended?", "Agents working inbound and outbound, not a fourth type."), ("Autodial needs?", "List plus prompts and IVR, per the planning topic.")],
    ("Pick the type", "Match three requests to inbound, outbound, or autodial.", ["A support number that must answer", "A list of renewals an agent should dial", "A reminder the IVR speaks before any agent"], "Each request has one type, and none of them is named Blended."),
    ("Wrong type", "Renewal calls are placed by hand from a DID because someone built an inbound campaign.", "CAMPAIGN Renewals type=INBOUND list=none", ["The team needed an outbound campaign and a list", "They needed a shorter TLS key", "They needed vertical dialing on a DNIS", "They needed to delete skills"], 0, "A list is dialed by outbound or autodial, not by an empty inbound campaign.", "Create an outbound campaign, load the list, and choose a dialing mode."),
    ["Name the three campaign types", "Explain blended without inventing a fourth type"], minutes=14))

    A.append(lesson("l05", "Contacts, fields, and lists", "foundation", [
        "A contact record is a row of fields. number1, number2, and number3 are the usual phone slots the dialer walks. Lists are sets of those rows attached to outbound and autodial campaigns.",
        "The list-mode article says a final disposition stops every number on that record for that campaign. Resetting a disposition later is a separate, explicit action. Loading a list does not by itself start dialing.",
    ], [LISTS, DISP, PLAN], path("From row to dial", "The record is not the campaign.", ["Fields", "Contact row", "List", "Campaign", "Dialer"]),
    "A record joins a campaign", ["List", "Dialer"], [
        ("List", "Fields", "number1 is the first phone slot.", "fields"),
        ("List", "Row", "One person, possibly three numbers.", "record"),
        ("List", "Load", "The list is attached to the campaign.", "attach"),
        ("Dialer", "Mode", "List penetration or vertical decides the walk.", "mode"),
        ("Dialer", "Final", "A final disposition stops the whole record.", "final"),
        ("Dialer", "Reset", "Reset Disposition is how you allow another try.", "reset"),
    ], [
        ("What does a final disposition do to a record?", ["It dials number3 next", "It stops further attempts on every number for that campaign", "It deletes the domain", "It starts the IVR"], 1, "The list-mode article says no further attempts are made on any number for that record."),
        ("Which campaign types use lists?", ["Inbound only", "Outbound and autodial", "Reporting only", "E911 only"], 1, "The disposition and list topics talk about outbound and autodial lists."),
        ("number1 is", ["The agent's extension", "A phone field on the contact", "The DNIS", "The abandon cap"], 1, "List penetration examples walk number1, then number2, then number3."),
        ("Uploading a list starts the dialer. True or false?", ["True", "False. The campaign still has to run, with a mode and agents or an IVR", "True in TCPA domains", "True if the file is CSV"], 1, "A list is an input. Run state and dialing mode are separate."),
        ("Reset Disposition applies to", ["Every domain on the cluster", "Lists currently loaded in that campaign", "Only inbound DNIS", "Only voicemail"], 1, "The disposition topic says the reset applies to lists currently loaded in the campaign."),
    ], [("Final disposition?", "Stops all numbers on that record for the campaign."), ("Which types load lists?", "Outbound and autodial."), ("What is number1?", "The first phone field the dial order can use."), ("Does upload start dialing?", "No.")],
    ("Read a row", "Given number1, number2, and a final disposition, say what the dialer will not do.", ["Mark the final outcome", "State that number2 will not be tried", "Name the action that would allow a later retry"], "You named Reset Disposition, not a second upload, as the retry tool."),
    ("List loaded, nothing dials", "The CSV imported and the campaign stays silent.", "LIST renewals rows=40000 CAMPAIGN state=NOT_RUNNING mode=none", ["The campaign is not running and has no dialing mode", "number1 must be an email", "Final dispositions dial first", "IVR Menu blocked CSV"], 0, "A list without a running outbound or autodial campaign does not dial.", "Start the campaign and set the dialing mode."),
    ["Describe a contact row", "Explain a final disposition"]))

    A.append(lesson("l06", "Dispositions are the dialer's memory", "foundation", [
        "A disposition is the outcome stored on a record. System dispositions and custom dispositions both exist. The disposition topic says many system dispositions are redialed five times if you leave the default redial count, and you can reset that count.",
        "You can update dispositions in a batch from the campaign menu, including a CSV through a scheduled upload. A list-details report shows the last disposition for outbound campaigns. Do not reset a disposition you are not willing to dial again.",
    ], [DISP, LISTS], stack("Disposition effects", "The code decides whether the number is alive.", ["System or custom code", "Redial count", "Final flag", "Reset window", "List details report"]),
    "From outcome to next attempt", ["Agent", "Dialer"], [
        ("Agent", "Code", "The agent or the system sets a disposition.", "set"),
        ("Dialer", "Count", "Default system redial is often five.", "five"),
        ("Dialer", "Stop", "A final code ends the record.", "final"),
        ("Agent", "Reset", "An admin resets a date range on purpose.", "reset"),
        ("Dialer", "Retry", "Only the selected codes are eligible again.", "eligible"),
        ("Agent", "Report", "List details shows the last disposition.", "report"),
    ], [
        ("Default redial behavior for many system dispositions is", ["Never", "Five times, if the default redial count is in use", "Fifty times", "Only on inbound"], 1, "The disposition topic says many system dispositions are redialed five times with the default count."),
        ("Reset Disposition redials", ["Every code you did not touch", "The dispositions you select, on lists currently loaded", "Only voicemail greetings", "Only UK domains"], 1, "You choose the codes and a date range. It applies to loaded lists."),
        ("A safe reset rule is", ["Reset all codes nightly", "Reset only codes you know are safe to dial again", "Reset final sales as a habit", "Reset from the agent headset button"], 1, "The topic says to reset only dispositions you know are safe to redial."),
        ("Batch disposition updates can come from", ["A headset mute button", "A manual entry or a CSV, including a schedule", "The SIP trunk alone", "RedSky"], 1, "Update Dispositions supports manual input and scheduled CSV."),
        ("Where do you confirm the last outbound disposition?", ["A list details report", "The TLS cipher list", "MyE911", "The Equinix SLA"], 1, "The update article points at the list details report for outbound."),
    ], [("Default system redials?", "Often five, if the default count is left in place."), ("What does reset change?", "Selected codes on lists currently loaded."), ("Safe reset rule?", "Only codes you are willing to dial."), ("Batch update?", "Manual rows or scheduled CSV.")],
    ("Mark final vs retry", "Label five sample codes as final or retryable.", ["Sale as final", "No answer as retryable", "Say what Reset would do to No answer"], "You refused to reset Sale."),
    ("Sold customers called again", "Last week's sales are back in the hopper.", "ACTION ResetDisposition codes=[Sale,NoAnswer] range=7d", ["Sale was included in a reset", "The codec changed", "DNIS was busy", "IVA contained the call"], 0, "Reset makes the selected codes dialable again.", "Reset only No Answer. Leave Sale alone."),
    ["Explain redial count versus a final code", "Say what a reset is allowed to touch"]))

    A.append(lesson("l07", "One profile, many campaigns", "foundation", [
        "A campaign profile overrides campaign defaults such as the ANI. You may create many profiles. A campaign uses one profile at a time. The same profile can be on more than one campaign. You attach it in Advanced mode, and workflow rules can swap it.",
        "Profiles also filter and sort lists, control pop-up windows in the agent interface, and manage disposition counts. They are not a second copy of the dialing mode.",
    ], [PROFILES, PROFILEHOW], compare("Profile vs campaign", "The profile decorates the campaign. It does not replace it.", "Profile", ["ANI override", "List filter and sort", "Pop-up behavior", "Disposition counts"], "Campaign", ["Type", "Run state", "Dialing mode", "Skill assignment"]),
    "Attach a profile", ["Admin", "Campaign"], [
        ("Admin", "Create", "Add a profile from the Campaign Profile folder.", "add"),
        ("Admin", "ANI", "Override the default ANI.", "ani"),
        ("Admin", "Filter", "Filter and sort the list.", "filter"),
        ("Campaign", "Advanced", "Choose the profile in Advanced mode.", "assign"),
        ("Campaign", "One", "Only one profile is associated.", "one"),
        ("Campaign", "Swap", "A workflow rule can change it later.", "workflow"),
    ], [
        ("How many profiles can a campaign use at once?", ["As many as it has skills", "One", "Two, inbound and outbound", "Zero, profiles are optional and ignored"], 1, "You can associate only one profile per campaign."),
        ("Can two campaigns share a profile?", ["No", "Yes. A profile can be used by more than one campaign", "Only autodial", "Only if ANI is blank"], 1, "The profile topic says a profile can be used simultaneously by more than one campaign."),
        ("Where do you assign it?", ["On the SIP trunk", "Advanced mode on the campaign", "Inside a flashcard", "On the agent headset"], 1, "Assignment is in Advanced mode when you start or edit the campaign."),
        ("A profile can override", ["The laws of the FTC", "Defaults such as the ANI", "The Reporting role", "TLS 1.2"], 1, "Profiles override campaign defaults such as the default ANI."),
        ("Workflow rules can", ["Delete the domain", "Change the profile on the campaign", "Disable TCPA typing", "Replace Five9 with a PBX"], 1, "The profile topic says workflow rules can change the profile."),
    ], [("Profiles per campaign?", "One."), ("Can a profile be shared?", "Yes, across campaigns."), ("What can it override?", "Defaults such as the ANI."), ("How can it change later?", "Workflow rules.")],
    ("Pick an ANI", "Write two profiles with two ANIs and assign one to a campaign.", ["Name the Advanced mode step", "Say what the second campaign could reuse", "Say what the profile does not set"], "You did not put the dialing mode on the profile."),
    ("Wrong caller ID", "Outbound calls show the default ANI after a morning change.", "PROFILE west-ani NOT ASSIGNED CAMPAIGN mode=BASIC", ["The new profile was never selected in Advanced mode", "Predictive requires 10 agents to show ANI", "Menu module erased ANI", "RedSky replaced the caller ID"], 0, "A profile does nothing until the campaign uses it.", "Assign it in Advanced mode."),
    ["Assign one profile", "Name two things a profile is for"]))
    return track("t01", "Foundations and the domain", "Foundations", "What a Five9 domain contains before anyone dials.", "Platform", "Foundation", "A domain is the tenant. Campaigns come after skills, users, lists, dispositions, and a profile.", A)

def cite_reports():
    from curriculum_lib import REPORTS, CAV
    return REPORTS

def cite_out():
    from curriculum_lib import OUTBOUND
    return OUTBOUND
