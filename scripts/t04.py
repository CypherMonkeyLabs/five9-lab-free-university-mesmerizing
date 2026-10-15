from curriculum_lib import LISTS, DISP, PROFILES, DEFAULTS, VERTICAL, OUTBOUND, STIR, CALLLOG, lesson, stack, compare, path, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "A list is not a campaign", "foundation", [
        "Outbound and autodial campaigns dial lists of contact records. The list has an order. The campaign has a run state and a dialing mode. Uploading a CSV does neither of those.",
        "The disposition topic says you reset list position and dispositions on the lists currently loaded in that campaign. A list sitting in the library and a list loaded in the campaign are not the same moment.",
    ], [LISTS, DISP], path("List lifecycle", "Upload, load, run, then dial.", ["CSV", "List object", "Loaded on campaign", "Running mode"]),
    "From file to dial", ["Admin", "Campaign"], [
        ("Admin", "Upload", "The CSV becomes a list.", "csv"),
        ("Admin", "Fields", "number1 maps to a phone field.", "map"),
        ("Campaign", "Load", "The list is loaded on the campaign.", "load"),
        ("Campaign", "Mode", "A dialing mode is selected.", "mode"),
        ("Campaign", "Run", "The campaign is running.", "run"),
        ("Campaign", "Dial", "Records leave the top of the order.", "dial"),
    ], [
        ("Uploading a CSV starts dialing. True or false?", ["True", "False. The campaign must load it, have a mode, and run", "True for inbound", "True if the file is xlsx only"], 1, "The list is an input."),
        ("Reset list position affects", ["Every list in the domain", "Lists currently loaded in that campaign", "Only IVR prompts", "Only 911 recordings"], 1, "The disposition topic limits the reset to loaded lists."),
        ("number1 is", ["The DNIS", "A phone field on the contact", "The agent extension", "The pause timer"], 1, "List examples walk number1, number2, number3."),
        ("An inbound campaign is the right place for a sales list. True or false?", ["True", "False. Lists belong on outbound or autodial", "True at night", "True if the DNIS is 800"], 1, "Inbound answers a DNIS."),
        ("A reconciled list is on which roadmap?", ["The headset page", "The planning roadmap, before campaigns", "Only Studio", "Only WEM"], 1, "Planning says to define and reconcile call lists before campaigns."),
    ], [("Does upload dial?", "No."), ("Which lists does reset touch?", "Lists loaded in the campaign."), ("number1?", "A phone field."), ("Sales list campaign type?", "Outbound or autodial.")],
    ("Map a file", "Name the column that becomes number1.", ["Pick the phone column", "Say the campaign type", "Say the state required before dialing"], "You did not attach the file to an inbound campaign."),
    ("Forty thousand rows and no calls", "Import succeeded yesterday.", "LIST rows=40000 CAMPAIGN loaded=no state=NOT_RUNNING", ["Load the list and start a dialing mode", "Change the greeting WAV", "Enable IE", "Set pause to 0"], 0, "The list is not loaded on a running campaign.", "Load it, set the mode, start the campaign."),
    ["Separate file, list, and running campaign", "Map number1"]))

    R.append(L("l02", "Profiles filter the list the agent sees", "practice", [
        "Campaign profiles filter and sort lists, control agent pop-ups, and manage disposition counts. They also override defaults such as the ANI. One campaign, one profile. Workflow rules can swap the profile.",
        "A filter on the profile changes which rows are eligible. It does not change list penetration versus vertical. That choice is the list dialing mode on the campaign.",
    ], [PROFILES, LISTS], compare("Profile versus list mode", "Both touch the list. They do different jobs.", "Profile", ["Filter", "Sort", "ANI", "Pop-ups"], "List dialing mode", ["Penetration", "Vertical", "Which number next"]),
    "A filtered morning list", ["Admin", "Dialer"], [
        ("Admin", "Filter", "The profile keeps today's time zone or segment.", "filter"),
        ("Admin", "Assign", "Advanced mode attaches that one profile.", "assign"),
        ("Dialer", "Mode", "Penetration walks number1 across the filtered rows.", "pen"),
        ("Dialer", "Skip", "Rows the filter excluded never dial.", "skip"),
        ("Admin", "Swap", "A workflow can change the profile at noon.", "swap"),
        ("Dialer", "ANI", "The caller ID follows the profile override.", "ani"),
    ], [
        ("A profile filter and vertical dialing are", ["The same setting", "Different settings", "Both TLS ciphers", "Both headsets"], 1, "Filter selects rows. Vertical selects which phone on a row."),
        ("How many profiles on one campaign?", ["One", "One per skill", "Unlimited simultaneous", "Zero"], 1, "Only one profile is associated."),
        ("Caller ID override lives on", ["The skill greeting", "The campaign profile", "The JRE", "The flashcard"], 1, "Profiles override defaults such as ANI."),
        ("A workflow rule can", ["Delete Five9", "Change which profile the campaign uses", "Disable RFC 3261", "Replace a DNIS with a skill"], 1, "The profile topic includes workflow rules."),
        ("Pop-up windows in the agent UI are", ["Uncontrollable", "Something a profile can control", "A carrier option", "A matrix export"], 1, "The profile topic lists pop-up control."),
    ], [("Filter vs vertical?", "Different."), ("Profiles at once?", "One."), ("ANI override?", "On the profile."), ("Pop-ups?", "A profile can control them.")],
    ("Two mornings", "Write a profile that would dial only one segment.", ["Name the filter", "Assign it in Advanced mode", "Leave the dialing mode on the campaign"], "The mode and the filter are on different objects."),
    ("Noon calls use the morning ANI", "A workflow was supposed to swap profiles.", "PROFILE now=morning RULE noon=missing", ["The workflow rule never changed the profile", "G.711 ptime", "Pause is 0", "The menu has three digits"], 0, "The campaign is still on the morning profile.", "Add the workflow or assign the afternoon profile in Advanced mode."),
    ["Filter with a profile", "Keep dialing mode on the campaign"]))

    R.append(L("l03", "List penetration and vertical dialing", "practice", [
        "List penetration is the default. The dialer tries the first phone on every record, then the next phone on a later pass. Vertical dialing stays with one contact and moves across that contact's numbers before it moves on.",
        "The community article's wording is easy to twist: it says the physical direction of list penetration is vertical, while the industry phrase vertical dialing means walking numbers across a record. Use the article's definitions, not the compass words. A final disposition stops every number on the record in either mode.",
    ], [LISTS, VERTICAL], compare("Two walks", "Same list, different next number.", "List penetration (default)", ["All number1 values first", "Then number2", "Next pass waits until the record comes around"], "Vertical", ["All numbers for one record", "Then the next record", "Retry timing follows minimum duration"]),
    "Three people, three numbers", ["Dialer", "List"], [
        ("List", "Pen pass 1", "Ada number1, Bo number1, Cia number1.", "n1"),
        ("List", "Pen pass 2", "Ada number2, and so on.", "n2"),
        ("List", "Vertical", "Ada number1, Ada number2, Ada number3, then Bo.", "vert"),
        ("Dialer", "Final", "A final code stops Ada's remaining numbers.", "final"),
        ("Dialer", "Wait", "Minimum duration before a number is retried.", "min"),
        ("Dialer", "Default", "If you never chose, penetration is the default.", "default"),
    ], [
        ("Which mode is the default?", ["Vertical", "List penetration", "Predictive", "TCPA"], 1, "The list-mode article says list penetration is the default."),
        ("Vertical dialing tries to", ["Call every record's first number before any second number", "Finish the numbers on one record before moving on", "Ignore final dispositions", "Dial only DNIS"], 1, "That is the contrast the article draws."),
        ("The article says list penetration's physical direction looks vertical. That means", ["Penetration and vertical are the same mode", "Do not trust the compass word. Read the definition", "You must use vertical", "ANI changes"], 1, "The article itself warns about the industry phrase."),
        ("A final disposition in either mode", ["Dials the next number", "Stops the record's remaining numbers for that campaign", "Starts the IVR", "Resets the profile"], 1, "The article says no further attempts on any number for that record."),
        ("Minimum duration before redial is", ["A headset setting", "A campaign dialing option the article tells you not to skip", "A JRE flag", "Always zero"], 1, "The article refers to Minimum Duration Before Redialing Number on Dialing Options."),
    ], [("Default list mode?", "List penetration."), ("Vertical in one sentence?", "Finish one record's numbers, then move on."), ("Compass words?", "Use the definitions, not 'vertical' as a direction."), ("Final disposition?", "Stops the whole record.")],
    ("Walk six calls", "Write the first six dials for penetration and for vertical on three records.", ["Penetration: three number1 dials", "Vertical: one record's numbers", "Mark a final code and stop"], "The two lists of six are not the same."),
    ("Second phones never dial", "The list is in vertical mode and the first number on each hot record is a final no-contact that was mis-coded as final.", "MODE vertical DISP final on number1", ["The final flag stopped the rest of the record", "TLS failed", "The DNIS is busy", "Pause is 30"], 0, "Final stops every number on the record.", "Use a retryable code when other numbers should still be tried."),
    ["Walk both list modes on paper", "Respect a final disposition"], uncertain=["The documentation portal has a vertical-dialing chapter. This lesson follows the community article's definitions because that page returned readable text. Confirm the portal chapter in your own admin guide."]))

    R.append(L("l04", "Reset is a loaded gun", "practice", [
        "Reset list position sends the dialer back to the top. Reset Disposition clears selected outcomes so those rows can dial again. Both act on lists currently loaded. The disposition topic says to reset only codes you know are safe.",
        "A scheduled disposition update from CSV can also stamp codes, using a key field such as the phone column. The list details report is how you prove the stamp landed, for outbound.",
    ], [DISP], stack("Two resets", "They are not the same button.", ["Reset list position", "Reset selected dispositions", "CSV disposition update", "List details report"]),
    "After a bad week", ["Admin", "List"], [
        ("Admin", "Choose", "Only No Answer, not Sale.", "choose"),
        ("Admin", "Range", "Pick the date window.", "range"),
        ("List", "Loaded", "The reset hits lists in the campaign.", "loaded"),
        ("List", "Dial", "Those rows are eligible again.", "dial"),
        ("Admin", "CSV", "A key column updates other rows later.", "csv"),
        ("Admin", "Proof", "List details shows last disposition.", "proof"),
    ], [
        ("Reset Disposition should include Sale. True or false?", ["True, every Friday", "False, unless you intend to call buyers again", "True in vertical mode", "True for inbound DNIS"], 1, "Reset only codes that are safe to redial."),
        ("The reset applies to", ["Unloaded library lists only", "Lists currently loaded in the campaign", "Every domain", "Voicemail greetings"], 1, "The topic says currently loaded lists."),
        ("List position reset", ["Changes ANI", "Sends the dialer back toward the top of the list", "Deletes skills", "Stops inbound"], 1, "Position and disposition resets are different."),
        ("A CSV disposition update needs", ["A key field to find the record", "A new JRE", "An Equinix port", "A matrix layout"], 1, "The update flow asks for key fields."),
        ("Proof for outbound is", ["MyE911", "A list details report", "The headset LED", "A SIP INVITE"], 1, "The update article points at list details."),
    ], [("Reset Sale?", "Only if you mean to call them again."), ("Which lists?", "Currently loaded."), ("Position reset?", "Back toward the top."), ("Proof?", "List details.")],
    ("Write the reset ticket", "Name the codes, the dates, and the list.", ["Exclude Sale", "Include No Answer", "Name the campaign"], "Sale is not in the ticket."),
    ("Buyers called the morning after a cleanup", "The night operator reset every code.", "RESET codes=ALL including Sale", ["Sale was reset", "The codec list changed", "IVR Menu lost a digit", "WEM scheduled a break"], 0, "All-codes reset redials finals.", "Reset only the retryable codes and apologize from the list details proof."),
    ["Reset codes on purpose", "Prove it with list details"]))

    R.append(L("l05", "Time zone and call analysis are guarded defaults", "advanced", [
        "The campaign admin tree includes time zone dialing options, and the default-settings topic says call analysis and voice detection level ship with vendor defaults. Changing defaults can raise a compliance warning. The same topic says US domains watch abandon rate for 30 rolling days and UK domains for 24 hours, and that a Five9 representative sets which kind of domain you have.",
        "This lab will not invent the legal calling window or the numeric abandon default. Both move, and both are jurisdiction-specific. Open the current page and the current rule before you widen either one.",
    ], [DEFAULTS], stack("Leave the guardrails until you have read them", "The warning exists because the defaults are the vendor's compliance posture.", ["Time zone options", "Call analysis", "Voice detection", "Abandon window", "US 30 days or UK 24 hours"]),
    "Someone wants to dial later", ["Admin", "Policy"], [
        ("Admin", "Find", "Open time zone dialing options.", "tz"),
        ("Policy", "Read", "Read the current rule for that country.", "rule"),
        ("Admin", "Default", "Notice the warning if a default changes.", "warn"),
        ("Admin", "Domain", "Confirm US versus UK abandon window.", "window"),
        ("Admin", "Analysis", "Call analysis stays at the default unless you know why.", "amd"),
        ("Policy", "Write", "Record the page you read, not a rumor.", "cite"),
    ], [
        ("US abandon monitoring, per the default-settings topic, uses", ["24 hours", "A rolling 30 days", "7 days", "The agent's shift"], 1, "US domains use 30 days. UK domains use 24 hours."),
        ("Who sets a domain to US or UK behavior?", ["Any agent", "A Five9 business representative, according to that topic", "The IVR Menu", "The headset vendor"], 1, "The topic says customers request a Five9 representative."),
        ("Changing Max Abandoned Call Percentage", ["Is silent", "Can show a warning that you may leave compliance", "Deletes the list", "Switches codecs"], 1, "The topic uses that field as the example warning."),
        ("This lab states the numeric default abandon percent as", ["3", "2", "It does not. Read the live default in your domain", "10"], 2, "The page says there is a preset. It does not need this lab to repeat a number that can change."),
        ("Call analysis is", ["A campaign field with a vendor default", "A CUCM partition", "A Credly exam", "A Wi-Fi SSID"], 1, "Default settings list Call Analysis and Voice Detection level."),
    ], [("US abandon window?", "Rolling 30 days."), ("UK window?", "24 hours."), ("Who sets US vs UK?", "A Five9 representative, per the topic."), ("Numeric default in this lab?", "Not stated. Read the domain.")],
    ("Read, don't copy", "Open the default-settings section in your own guide and write down the warning text you see.", ["Find Max Abandoned Call Percentage", "Do not change it in production", "Note US or UK"], "You left the live value alone."),
    ("Night calls to the wrong coast", "An admin turned time zone controls off to 'finish the list'.", "TZ disabled CALLS 22:10 local-east", ["Turn the time-zone control back on and read the current rule", "Raise predictive pace", "Stop inbound so agents are free", "Use analog headsets"], 0, "Finishing the list is not a reason to ignore the guardrail.", "Restore the option and confirm the domain's rule set."),
    ["Name the 30-day and 24-hour windows", "Refuse to invent the legal dialing hours"], uncertain=["The exact hour-by-hour time zone matrix is in the campaign guide and was not copied here. Local telemarketing law is not Five9's default screen."]))

    R.append(L("l06", "Call analysis is not a guarantee", "advanced", [
        "Call analysis and voice detection level are defaulted campaign fields. Product pages also list answering-machine detection and automatic voicemail as agent-efficiency tools. None of those pages give you a percent accuracy you can put in a contract.",
        "A live person marked as a machine is a silent failure: the agent never hears them, or a voicemail template talks to a human. Treat detection as a tuned setting with a monitoring report, not as a fact about the callee.",
    ], [DEFAULTS, OUTBOUND], stack("What the pages actually name", "Capability names, not accuracy claims.", ["Call analysis", "Voice detection level", "Answering machine detection", "Automatic voicemail"]),
    "A machine and a person", ["Dialer", "Detect", "Agent"], [
        ("Dialer", "Place", "The outbound call is analyzed.", "place"),
        ("Detect", "Live", "A live detection can connect an agent.", "live"),
        ("Detect", "Machine", "A machine detection can take the voicemail path.", "amd"),
        ("Agent", "Miss", "A wrong machine label means no agent.", "miss"),
        ("Admin", "Level", "Voice detection level is the documented knob.", "level"),
        ("Admin", "Report", "Listen to samples before you trust the week.", "qa"),
    ], [
        ("Voice detection level is", ["A SIP port", "A defaulted campaign field", "A Credly score", "A headset model"], 1, "It is listed with the default campaign settings."),
        ("This lab's accuracy number for answering-machine detection is", ["99 percent", "95 percent", "Not published here, because the cited pages do not give one", "50 percent"], 2, "Do not invent an accuracy."),
        ("Automatic voicemail is listed on", ["The outbound product page as an agent-efficiency tool", "The JRE page", "The E911 data sheet only", "RFC 3261"], 1, "The outbound product page names it."),
        ("A false machine detection", ["Improves occupancy honestly", "Can drop a live person out of the agent path", "Starts inbound", "Resets Sale"], 1, "The person never reaches an agent."),
        ("The right operational habit is", ["Max the detection and walk away", "Sample the results and keep the default until you know why you moved it", "Disable reports", "Use cellular agents"], 1, "Defaults exist for a reason, and detection can be wrong."),
    ], [("Where is voice detection level?", "Campaign dialing defaults."), ("Published accuracy?", "Not in this lab."), ("Automatic voicemail?", "Named on the outbound product page."), ("False machine?", "A live person misses the agent.")],
    ("Sample ten calls", "Describe how you would audit detection without a fake accuracy number.", ["Pull a small set of recordings", "Mark live versus machine by ear", "Compare to the disposition"], "You refused to write '99 percent'."),
    ("Customers say an agent never came on the line", "Detection is aggressive and voicemail templates are on.", "VOICE detection=aggressive VM=on COMPLAINT=live-person", ["Relax detection and sample recordings", "Stop the inbound campaign", "Delete all skills", "Enable TLS 1.1"], 0, "Live people are being treated as machines.", "Restore a conservative level and listen before the next list pass."),
    ["Treat detection as a tuned field", "Do not quote a fake accuracy"]))

    R.append(L("l07", "Local caller ID is a profile choice", "practice", [
        "The outbound product page lists local caller ID as a business-efficiency tool, and campaign profiles are the documented place to override the default ANI. Showing a local number is a profile and number-plan problem, not a skill-group problem.",
        "Certified Caller, on its own page, is the STIR/SHAKEN story. A local ANI does not by itself mean the call is signed. Keep those projects separate.",
    ], [OUTBOUND, PROFILES, STIR, CALLLOG], compare("Two caller-ID projects", "Both affect trust. They are different products.", "Local ANI", ["Profile override", "Which number you present"], "Certified Caller", ["STIR/SHAKEN", "Attestation, not the profile filter"]),
    "A west-coast list", ["Admin", "PSTN"], [
        ("Admin", "Numbers", "You have ANIs in the list's region.", "stock"),
        ("Admin", "Profile", "The profile overrides the default ANI.", "profile"),
        ("Admin", "Assign", "Advanced mode binds it to the campaign.", "bind"),
        ("PSTN", "Show", "The callee sees that ANI.", "show"),
        ("Admin", "Sign", "STIR/SHAKEN is a separate feature.", "stir"),
        ("Admin", "Report", "Call log can filter on ANI.", "report"),
    ], [
        ("Local caller ID is listed as", ["A skill greeting", "A business-efficiency tool on the outbound product page", "A JRE update", "An IVR Menu digit"], 1, "The outbound page lists it."),
        ("The admin object that overrides ANI is", ["The skill group", "The campaign profile", "The pause timer", "The reporting role"], 1, "Profiles override the default ANI."),
        ("STIR/SHAKEN signing is", ["Automatic if the ANI is local", "Certified Caller, a separate published feature", "The Set DNC module", "List penetration"], 1, "Do not collapse the two projects."),
        ("A profile that is not assigned", ["Still changes the live ANI", "Does not change the campaign", "Deletes the list", "Stops inbound"], 1, "Assignment is a separate step."),
        ("Call log criteria can include ANI. True or false?", ["False", "True. The call-log articles include ANI as a filter", "Only for matrix exports to CSV", "Only in Studio"], 1, "Call log filters include ANI and DNIS."),
    ], [("Where is local caller ID marketed?", "Outbound product page."), ("Which object overrides ANI?", "Campaign profile."), ("Is that STIR/SHAKEN?", "No. Certified Caller is separate."), ("Unassigned profile?", "No effect.")],
    ("Pick an ANI", "Name the profile field and the assignment click.", ["Choose the ANI", "Assign in Advanced mode", "Say what you did not configure"], "You did not call it a skill."),
    ("Calls show the corporate toll-free", "The local profile was built and left unassigned.", "PROFILE local-ani assigned=no", ["Assign the profile", "Enable Efficiency Mode", "Switch to vertical and hope", "Delete reporting"], 0, "An unused profile does not present its ANI.", "Assign it in Advanced mode."),
    ["Override ANI with a profile", "Keep STIR/SHAKEN as its own project"], href="#/pacing"))
    return track("t04", "Outbound lists", "Outbound", "Lists, profiles, penetration versus vertical, resets, and the guardrails around time and detection.", "Voice", "Practice", "Outbound dials a loaded list under a mode. Resets and ANI changes are explicit.", R)
