from curriculum_lib import E911, EULA, RETAIN, MYE911, STIR, DEFAULTS, TCPA, TECH, cite, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "911 is a location, not a prefix", "foundation", [
        "The E911 data sheet says agents dial 911 directly, with no prefix, and that the service sends a dispatchable location. It names the United States and its territories, Kari's Law, and RAY BAUM'S Act. The partner named on that sheet is RedSky.",
        "The end-user license also discusses emergency calling and names the United States or Canada. It says the call can fail if the address is wrong or unregistered, if power or internet is lost, if the service is suspended, during an outage, or with bad gear. The data sheet and the EULA do not draw the same map. Say which document you are quoting.",
    ], [E911, EULA], compare("Two public texts", "Do not average them.", "Data sheet", ["Direct 911, no prefix", "Dispatchable location", "US and territories", "RedSky"], "EULA", ["Also says US or Canada", "Wrong address fails", "Power, internet, suspension, outage, gear"]),
    "An agent asks how to dial", ["Dial", "Place", "Doc"], [
        ("Dial", "Digits", "They dial 911, not a prefix plus 911.", "911"),
        ("Place", "Location", "The registered location is where they are.", "loc"),
        ("Doc", "Sheet", "The data sheet is cited for the partner and the Act names.", "sheet"),
        ("Doc", "EULA", "The EULA is cited for failure cases and the Canada line.", "eula"),
        ("Admin", "Gap", "The geography gap is written down, not smoothed over.", "gap"),
        ("Admin", "Test", "A test is not a real emergency, and the history page is the audit.", "test"),
    ], [
        ("The data sheet says agents dial 911", ["With a campaign prefix", "Directly, with no prefix", "Only through a skill", "Only from HQ"], 1, "No prefix."),
        ("The partner named on the data sheet is", ["A generic ITSP", "RedSky", "Equinix", "Verint"], 1, "RedSky."),
        ("A wrong or unregistered address, per the EULA,", ["Still routes", "Can fail the emergency call", "Only affects recordings", "Changes the ANI profile"], 1, "The EULA lists that failure."),
        ("The data sheet's geography and the EULA's geography are", ["Identical in this lab's reading", "Not the same. Cite the one you mean", "Both global", "Both only Canada"], 1, "US and territories versus US or Canada."),
        ("Kari's Law and RAY BAUM'S Act are named on", ["The dialer pacing page", "The E911 data sheet", "The IVR module list", "The call-log article"], 1, "The data sheet."),
    ], [("Prefix?", "None. Dial 911."), ("Partner on the sheet?", "RedSky."), ("Wrong address?", "The EULA says the call can fail."), ("Same map on both docs?", "No. Cite which one.")],
    ("Quote the right page", "Write the dialing rule, the partner, and the geography gap.", ["No prefix", "RedSky", "Which document says Canada"], "You did not merge the two maps."),
    ("A wallboard says 'dial 9-911'", "That prefix fights the data sheet.", "SIGN prefix=9", ["Change the sign to 911 and confirm the location", "Add the 9 in the IVR", "Raise abandon rate", "Disable TLS"], 0, "Direct 911 is the published behavior.", "Fix the sign and the address."),
    ["Dial 911 with no prefix", "Cite the data sheet and the EULA separately"], uncertain=["The 2022 data sheet says US and territories. The EULA text this lab read also says US or Canada. Re-read both before you publish a coverage map."]))
    R.append(L("l02", "The address has to be the room they are in", "practice", [
        "A dispatchable location is the place responders can find a person. A headquarters address while the agent is at home is the failure the EULA describes. Remote and hybrid floors have to register the location the agent is actually using.",
        "MyE911 call history, for an organization admin, shows time, user, number, location, recording, and the SIP invite. That is the audit after a test or a real call. It is not a substitute for registering the address first.",
    ], [E911, EULA, MYE911], path("Location before the call", "History only helps after.", ["Register the real place", "Agent dials 911", "History shows user, place, invite"]),
    "A home agent", ["Where", "Register", "Audit"], [
        ("Where", "Ask", "The agent is not in the HQ building.", "ask"),
        ("Register", "Home", "The home location is registered if that is the workplace.", "reg"),
        ("Register", "Move", "A move means a new registration.", "move"),
        ("Audit", "History", "After a test, history shows the location that was sent.", "hist"),
        ("Audit", "Invite", "The SIP invite is part of that history.", "sip"),
        ("Admin", "Stop", "A stale HQ row stops a remote rollout.", "stop"),
    ], [
        ("Dispatchable location means", ["The data center", "A place responders can find the caller", "The ANI", "The skill name"], 1, "The data sheet's point."),
        ("An org admin's MyE911 history includes", ["Only the theme", "Time, user, number, location, recording, and SIP invite", "The dialer algorithm", "WEM schedules"], 1, "That is the community article."),
        ("History replaces registration. True or false?", ["True", "False", "True for Canada only", "True if the prefix is 9"], 1, "Register first."),
        ("A move to a new apartment requires", ["Nothing until the next contract", "A new registered location", "A new codec", "A matrix report"], 1, "The old address would be wrong."),
        ("Power loss or internet loss, per the EULA,", ["Improves location", "Can prevent the emergency call", "Only hides reports", "Is unsupported advice"], 1, "The EULA lists both."),
    ], [("Dispatchable?", "Where responders can find the person."), ("History fields?", "Time, user, number, location, recording, SIP invite."), ("History instead of registration?", "No."), ("A move?", "Register again.")],
    ("Write a home-agent rule", "Say what gets registered and what you will look up after a test.", ["The place", "The history fields", "What you will not use as a location"], "HQ is not the default for a home agent."),
    ("History shows the downtown office for an agent who was at home", "The registered address was never updated.", "E911 user=sam loc=HQ", ["Register the home location and retest", "Change predictive pacing", "Add a Menu module", "Shorten the call log"], 0, "The invite carried the stale place.", "Fix the registration."),
    ["Register where the agent is", "Use MyE911 history as the audit"]))
    R.append(L("l03", "Recording is the customer's duty too", "practice", [
        "The EULA treats recordings as customer data. It says calls can be recorded while the caller is on hold and after a transfer. It puts notice and consent on the customer, who has to follow the laws that apply to their calls.",
        "This lab will not invent a script that 'covers every state.' Play the notice your counsel wrote. Put it in the IVR before the surprise, and do not assume hold music erases the recorder.",
    ], [EULA, RETAIN], stack("What the EULA puts on you", "The platform records. You own the duty.", ["Recordings are customer data", "Hold can be recorded", "After transfer can be recorded", "Notice and consent are yours"]),
    "A new IVR", ["Counsel", "Script", "Hold"], [
        ("Counsel", "Words", "The notice is the one counsel approved.", "words"),
        ("Script", "Play", "Play runs before the recording would surprise someone.", "play"),
        ("Hold", "Still", "Hold is not assumed to be a gap.", "hold"),
        ("Transfer", "Still", "A transfer does not assumed to stop the recorder.", "xfer"),
        ("Admin", "Laws", "The campaign's jurisdictions are listed.", "laws"),
        ("Admin", "No", "A generic sentence is not substituted for counsel.", "no"),
    ], [
        ("Who must meet notice and consent laws?", ["The ITSP alone", "The customer, per the EULA", "The headset vendor", "Nobody"], 1, "The EULA places that duty on the customer."),
        ("Recording on hold is", ["Impossible", "Described by the EULA as something that happens", "Only in Studio", "Only for E911"], 1, "Hold is not a silent gap."),
        ("A transfer", ["Deletes the recording", "Can still be recorded", "Changes TLS", "Ends the domain"], 1, "The EULA says so."),
        ("This lab supplies a notice that covers every region. True or false?", ["True", "False", "True for the US", "True for preview dialing"], 1, "Counsel writes the notice."),
        ("Recordings in the EULA are", ["Five9's marketing assets", "Customer data", "A skill group", "A report layout"], 1, "Customer data."),
    ], [("Who owns notice?", "The customer."), ("Hold recorded?", "The EULA says it can be."), ("Transfer?", "Can still be recorded."), ("Universal script?", "No.")],
    ("Place the notice", "Say where Play sits relative to the rest of a fictional inbound script.", ["Counsel's words", "Before the surprise", "Hold is still in scope"], "You did not write legal advice of your own."),
    ("Agents tell callers 'hold is private'", "The EULA disagrees.", "SCRIPT notice=none hold=promised-private", ["Play the approved notice and correct the agents", "Disable all recording and ignore counsel", "Change the codec", "Delete DNC"], 0, "The promise is false.", "Fix the script and the coaching."),
    ["Play the notice counsel wrote", "Assume hold and transfer can be recorded"]))
    R.append(L("l04", "Retention is several clocks", "practice", [
        "The public retention page splits the clocks. VCC audio is the sooner of 30 days, a successful SFTP or FTP offload, or the contract. E911 recordings are 30 days. Agent data is 60 days. Campaign state is 120 days. A disabled domain is 120 days after closure. DIDs and toll-free numbers are 90 days after closure.",
        "Quote the line that matches the object. 'We keep everything 30 days' is already wrong.",
    ], [RETAIN], stack("Clocks on the retention page", "Pick the row before you promise a date.", ["VCC audio: 30 days, offload, or contract", "E911 recordings: 30 days", "Agent data: 60 days", "Campaign state: 120 days", "Disabled domain: 120 days after closure", "DIDs and TFNs: 90 days after closure"]),
    "Legal asks for a hold", ["Object", "Clock", "Copy"], [
        ("Object", "Name", "Audio, E911 recording, agent data, or a number?", "name"),
        ("Clock", "Row", "The matching row is read.", "row"),
        ("Copy", "Offload", "If audio must outlive the platform, offload is the design.", "off"),
        ("Copy", "Own", "The offloaded copy follows your policy.", "own"),
        ("Admin", "DID", "Numbers are not given the domain's 120 days.", "did"),
        ("Admin", "E911", "E911 recordings are not given the campaign-state clock.", "e911"),
    ], [
        ("E911 recordings on the retention page are kept", ["120 days", "30 days", "90 days", "Forever"], 1, "30 days."),
        ("Agent data is", ["30 days", "60 days", "The same as DIDs", "10 years"], 1, "60 days."),
        ("DIDs after closure are", ["90 days", "120 days", "30 days", "Until you notice"], 0, "90 days."),
        ("Successful offload can end the platform's audio copy", ["Never", "Yes. Sooner of 30 days, offload, or contract", "Only for E911", "Only for lists"], 1, "That is the audio line."),
        ("Campaign state is", ["120 days", "30 days", "The call log window", "A SIP timer"], 0, "120 days."),
    ], [("E911 recordings?", "30 days."), ("Agent data?", "60 days."), ("DIDs?", "90 days after closure."), ("Audio?", "Sooner of 30 days, offload, or contract.")],
    ("Match four objects", "Write the clock next to audio, E911 recording, agent data, and a DID.", ["Four clocks", "Which one offload changes"], "You did not use one number for all four."),
    ("A litigation hold assumed the platform keeps audio for 120 days", "That number is campaign state, not audio.", "HOLD assumed=120 object=audio", ["Offload under your own hold, and correct the assumption", "Extend the DID timer", "Delete the domain today", "Change pacing"], 0, "The wrong row was quoted.", "Take a copy and cite the audio line."),
    ["Quote the clock for the object", "Offload audio you must keep"]))
    R.append(L("l05", "Attestation is not an ANI field", "advanced", [
        "Certified Caller is Five9's published STIR/SHAKEN program, tied to FCC and CRTC expectations. A campaign profile that overrides ANI changes what you present. It does not, by itself, mean the call is attested.",
        "Say 'we set local ANI' or 'we are in Certified Caller.' If you cannot point at the Certified Caller page for the second sentence, do not say it.",
    ], [STIR, DEFAULTS], compare("Two caller-ID projects", "A profile is not an attestation product.", "Campaign profile", ["Overrides ANI", "One profile on the campaign", "Assigned in Advanced mode"], "Certified Caller", ["STIR/SHAKEN program", "FCC and CRTC", "A separate project"]),
    "The caller ID looks right and the call is still labeled spam", ["ANI", "Trust", "Words"], [
        ("ANI", "Profile", "The profile is assigned and the number is intended.", "ani"),
        ("Trust", "Page", "Certified Caller is checked as its own project.", "page"),
        ("Trust", "Gap", "If it is not in scope, the deck says so.", "gap"),
        ("Words", "Precise", "People stop saying the profile 'signs' the call.", "words"),
        ("Admin", "Laws", "The abandon and dialing rules are a third project.", "abd"),
        ("Admin", "Report", "Spam labels are not fixed from the matrix layout.", "rep"),
    ], [
        ("Certified Caller is about", ["List penetration", "STIR/SHAKEN attestation", "Headset choice", "Report layouts"], 1, "The product page."),
        ("A local ANI on a profile", ["Is Certified Caller", "Presents a number. Attestation is separate", "Sets TLS 1.3", "Registers E911"], 1, "Do not merge them."),
        ("Regulators named on the Certified Caller page include", ["Only a state PUC", "FCC and CRTC", "Ofcom only", "None"], 1, "FCC and CRTC."),
        ("You may say a profile signs the call. True or false?", ["True", "False", "True if ANI is 10 digits", "True for predictive"], 1, "Signing is the attestation program."),
        ("Spam labeling with a correct ANI means", ["G.711 is off", "You still have to ask whether attestation is in place", "The skill is Default", "The call log expired"], 1, "Presentation and trust differ."),
    ], [("Certified Caller?", "STIR/SHAKEN program."), ("Profile ANI equals attestation?", "No."), ("Regulators named?", "FCC and CRTC."), ("Can you say the profile signs calls?", "No.")],
    ("Split the slide", "One box for ANI, one box for attestation, one box for what you have not bought.", ["Profile", "Certified Caller", "The gap"], "The gap box is allowed to say 'not in scope'."),
    ("Marketing says the new ANI is 'SHAKEN signed' because the profile saved", "Nobody enrolled the attestation program.", "ANI=set ATTEST=unknown", ["Stop the claim until Certified Caller is actually in place", "Add a prefix to 911", "Change the theme", "Export a matrix"], 0, "The profile is not the program.", "Correct the claim."),
    ["Keep ANI and attestation in separate sentences", "Cite Certified Caller before you say signed"]))
    R.append(L("l06", "Abandon rate is a regulated posture", "advanced", [
        "Default campaign settings call out a warning if you change Max Abandoned Call Percentage. Other fields on that page include Max Queue Time, Show Out of Numbers Alert, Monitor Abandoned Call Percentage, Call Analysis, Voice Detection level, and Action on Max Queue Time Expiration.",
        "The measurement window is not a number you type for fun. The page describes a US rolling 30 days and a UK window of 24 hours, set with a Five9 representative. This lab does not invent the numeric default inside Max Abandoned Call Percentage. TCPA manual touch is a different control: type the number, no paste, Dial enables only on a match.",
    ], [DEFAULTS, TCPA], path("Before you touch the abandon field", "The warning is the point.", ["Read the warning", "Know which window: 30 days or 24 hours", "Do not invent the default percent", "Manual touch is a different mode"]),
    "Someone wants more lines", ["Warn", "Window", "Mode"], [
        ("Warn", "Read", "The warning on Max Abandoned Call Percentage is read.", "warn"),
        ("Window", "US", "US is described as a rolling 30 days.", "us"),
        ("Window", "UK", "UK is described as 24 hours.", "uk"),
        ("Window", "Who", "A Five9 representative sets that window.", "rep"),
        ("Mode", "TCPA", "Manual touch is chosen when retyping is the control.", "tcpa"),
        ("Admin", "No", "A guessed percent is not typed.", "no"),
    ], [
        ("Changing Max Abandoned Call Percentage", ["Is silent", "Raises a warning", "Deletes the list", "Sets the codec"], 1, "The defaults page warns you."),
        ("The US window described is", ["24 hours", "A rolling 30 days", "120 days", "90 days"], 1, "Rolling 30 days."),
        ("The UK window described is", ["30 days", "24 hours", "60 days", "7 days"], 1, "24 hours."),
        ("Who sets that window, per the page?", ["The agent", "A Five9 representative", "The IVR Menu", "RedSky"], 1, "A Five9 representative."),
        ("This lab's numeric default for max abandon is", ["3 percent", "Not stated. It was not in the quoted page", "0", "10"], 1, "Do not invent it."),
    ], [("Warning?", "Yes, if you change the max abandon percentage."), ("US window?", "Rolling 30 days."), ("UK window?", "24 hours."), ("Who sets the window?", "A Five9 representative.")],
    ("Write the warning", "Say what you will not change, and which country's window applies to a fictional US campaign.", ["The warning", "30 days", "No invented percent"], "Manual touch is not used as a synonym."),
    ("A admin types 20 into Max Abandoned Call Percentage to 'clear the list'", "The warning existed and the window is a legal posture.", "ABANDON set=20 by=guess", ["Put the field back and talk to the representative before any change", "Also disable call analysis", "Paste numbers in TCPA mode", "Hide the warning"], 0, "Guessing a percent is the fault.", "Restore it and get the real guidance."),
    ["Read the abandon warning", "Keep the US 30-day and UK 24-hour windows straight"], uncertain=["This lab does not publish a numeric default for Max Abandoned Call Percentage. The defaults page describes the windows and the warning, not a percent we are willing to repeat."]))
    R.append(L("l07", "TCPA manual touch is a physical control", "practice", [
        "On domains where TCPA manual touch is enabled, other dialing modes are not available. Agents type the external number. Paste and drag are blocked. Dial enables only when the typed number matches. If preview times out, the agent goes Not Ready and nothing auto-dials.",
        "The community article says this covers click-to-dial, previews, queue callbacks, and voicemail callbacks. Internal speed dial and a third-party transfer do not make you retype. The permission User Can Skip Contact Records in TCPA Manual Touch is how skipping is allowed. The pacing lab includes this drill so your hands learn the rule.",
    ], [TCPA, DEFAULTS], path("A number that is allowed to dial", "Typing is the control.", ["Mode is manual touch only", "Type the external number", "Dial lights on a match", "Timeout means Not Ready, no auto dial"]),
    "Dial stays grey", ["Mode", "Hands", "Timeout"], [
        ("Mode", "Only", "No other mode is on.", "mode"),
        ("Hands", "Type", "The agent types. Paste is refused.", "type"),
        ("Hands", "Match", "Dial enables when the digits match.", "match"),
        ("Timeout", "NR", "A preview timeout sets Not Ready.", "nr"),
        ("Timeout", "No", "Nothing dials itself.", "no"),
        ("Admin", "Skip", "Skipping requires the named permission.", "skip"),
    ], [
        ("Paste in TCPA manual touch", ["Is the fastest compliant path", "Is blocked", "Works for external numbers", "Sets the ANI"], 1, "The article says paste and drag are blocked."),
        ("Dial enables when", ["The campaign is predictive", "The typed number matches", "Any key is pressed", "The agent is Not Ready"], 1, "Match."),
        ("Preview timeout", ["Auto-dials", "Sets Not Ready and does not auto-dial", "Deletes the contact", "Opens a report"], 1, "Not Ready, no auto dial."),
        ("Internal speed dial requires retyping. True or false?", ["True", "False", "True for Canada", "True for E911"], 1, "The article exempts internal speed dial and third-party transfer."),
        ("Skipping records requires", ["The Reporting role", "User Can Skip Contact Records in TCPA Manual Touch", "A matrix layout", "RedSky"], 1, "That permission."),
    ], [("Paste?", "Blocked."), ("When does Dial enable?", "When the typed number matches."), ("Timeout?", "Not Ready, no auto dial."), ("Skip permission?", "User Can Skip Contact Records in TCPA Manual Touch.")],
    ("Do the drill", "In the pacing lab, type the sample number. Do not paste.", ["Select TCPA", "Type", "Watch Dial"], "Dial stayed disabled until the digits matched."),
    ("Agents paste from the CRM and Dial never lights", "Paste is the block, not a bug in the skill.", "TCPA paste=blocked dial=disabled", ["Type the number", "Switch the campaign to predictive to save time", "Disable the permission and paste anyway", "Change G.711"], 0, "The control is working.", "Type it. Do not turn the mode off to dodge it."),
    ["Type external numbers in manual touch", "Treat a grey Dial button as the control working"], href="#/pacing"))
    return track("t16", "Safety and compliance", "Safety", "E911, recording, retention clocks, attestation, abandon windows, and TCPA typing.", "Platform", "Advanced", "Quote the document. Quote the clock. Do not invent a percent or a coverage map.", R)
