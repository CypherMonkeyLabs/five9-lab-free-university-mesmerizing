from curriculum_lib import APIS, REPORTS, CALLLOG, CAV, REPORTPAGE, RETAIN, TECH, ADP, cite, lesson, stack, path, compare, track

def build():
    L = lesson
    R = []
    R.append(L("l01", "The API names on the product page", "foundation", [
        "The APIs and SDKs page names CTI Web Services, Configuration Web Services, Reporting Web Services, Statistics Web Services, Web2Campaign, the CRM SDK, and Web Connectors. The same page also says REST. It does not, in the text this lab relied on, give a one-line SOAP-versus-REST label for every family.",
        "Call a family by its product name. If you have not opened that family's guide, write 'transport unconfirmed' instead of guessing SOAP or REST.",
    ], [APIS, TECH], stack("Names to use in a design", "From the APIs and SDKs page.", ["CTI Web Services", "Configuration Web Services", "Reporting Web Services", "Statistics Web Services", "Web2Campaign", "CRM SDK", "Web Connectors"]),
    "A developer asks for 'the API'", ["Ask", "Name", "Note"], [
        ("Ask", "Which", "Which job: control a call, configure, report, or pop a CRM?", "job"),
        ("Name", "Family", "The matching product name is written.", "name"),
        ("Name", "REST", "REST is acknowledged as a word on the page.", "rest"),
        ("Note", "Gap", "SOAP versus REST stays blank until the family guide is open.", "gap"),
        ("Note", "SDK", "A homegrown CRM is the CRM SDK, not a random family.", "sdk"),
        ("Admin", "TLS", "The call still rides TLS. Cleartext APIs are not the design.", "tls"),
    ], [
        ("Web2Campaign is", ["A dialer mode", "A named API on the product page", "A headset", "A list mode"], 1, "It is one of the published names."),
        ("Statistics and Reporting are", ["The same sentence", "Two different web-service names", "Both WEM", "Both codecs"], 1, "The page lists both."),
        ("A homegrown CRM starts with", ["CTI only, always", "The CRM SDK", "FTP", "The Menu module"], 1, "The product pages point bring-your-own CRM at the SDK."),
        ("This lab's rule on SOAP versus REST per family is", ["REST for all, stated as fact", "Unconfirmed until that family's guide is read", "SOAP for all", "Neither exists"], 1, "The overview says REST and also uses Web Services names."),
        ("Unencrypted API calls are", ["Fine on a VPN", "Not the design. TLS is required", "Required for Web2Campaign", "A campaign profile"], 1, "The requirements reject unencrypted APIs."),
    ], [("Web2Campaign?", "A named API."), ("Reporting versus Statistics?", "Both named, not the same label."), ("Homegrown CRM?", "CRM SDK."), ("SOAP or REST?", "Do not guess per family.")],
    ("Name the family", "Match three jobs to product names.", ["Click-to-call style control", "A nightly report extract", "A CRM that is not in the adapter list"], "You used three different names."),
    ("The ticket says 'REST is down' for every integration", "Six different families were lumped into one word.", "ALARM rest=down families=all", ["Split the alarm by product name", "Restart the dialer", "Change ANI", "Delete dispositions"], 0, "You cannot page one team for seven products.", "Name the family that failed."),
    ["Use the product names", "Leave SOAP versus REST unmarked until you read that guide"], uncertain=["The overview page says REST and also lists Web Services families. This lab does not assign a transport to each family."]))
    R.append(L("l02", "Reporting is a role", "foundation", [
        "Standard reports do not appear because you are an administrator. The community reporting article says you need the Reporting role and at least one reporting permission.",
        "Categories named there include Agent, Call Log, IVR, ACD Queue, Campaign, List, Contact, Do Not Call, Worksheet, Digital Channel, Legacy Digital, and Operational Summary. If a category is missing, check the role before you check the carrier.",
    ], [REPORTS, REPORTPAGE], stack("Report categories", "You still need the Reporting role to see them.", ["Agent", "Call Log", "IVR", "ACD Queue", "Campaign", "List and Contact", "Do Not Call", "Digital and operational"]),
    "The report list is empty", ["User", "Role", "Category"], [
        ("User", "Login", "The person is in the right domain.", "login"),
        ("Role", "Reporting", "The Reporting role is on the user.", "role"),
        ("Role", "Permission", "At least one reporting permission is on.", "perm"),
        ("Category", "Pick", "The category matches the question.", "cat"),
        ("Category", "Empty", "An empty category is not the same as a missing role.", "empty"),
        ("Admin", "Stop", "The trunk is not the first guess.", "stop"),
    ], [
        ("Who can open standard reports?", ["Any agent", "A user with the Reporting role and a reporting permission", "Only the ITSP", "Only Studio"], 1, "The reporting article says so."),
        ("IVR is", ["Not a report category", "A report category", "A codec", "A TLS version"], 1, "IVR is in the category list."),
        ("Do Not Call reports live under", ["The headset", "A named report category", "Direct Connect", "GenAI Studio only"], 1, "Do Not Call is a category."),
        ("An administrator with no Reporting role should expect", ["Every report", "Not to see standard reports", "Only the call log for 120 days", "E911 recordings"], 1, "Admin and Reporting are different."),
        ("Legacy Digital and Digital Channel are", ["The same category", "Both named, so do not merge them blindly", "Removed", "List modes"], 1, "The article lists both."),
    ], [("Role?", "Reporting, plus a permission."), ("IVR category?", "Yes."), ("Admin without the role?", "No standard reports."), ("Digital versus Legacy Digital?", "Both named.")],
    ("Grant the role", "Write the role and one category for a queue question and a DNC question.", ["Reporting role", "ACD Queue", "Do Not Call"], "You did not grant 'admin so they can see reports'."),
    ("A new supervisor sees no reports", "The account is a supervisor and not a reporting user.", "USER role=supervisor reporting=no", ["Add the Reporting role and a permission", "Restart the SBC", "Change list penetration", "Enable Efficiency Mode"], 0, "The menu is permissioned.", "Add the role."),
    ["Separate the Reporting role from administration", "Pick the category that matches the question"]))
    R.append(L("l03", "Layouts, and the matrix that will not export", "practice", [
        "The same reporting guidance describes three layouts: Tabular, Summary, and Matrix. A matrix answers a cross-tab question. It is not the layout you hand to a spreadsheet as a direct CSV.",
        "Pick the layout from the question. 'Every call' wants tabular. 'Averages by skill' wants summary. 'Skill by disposition' might want a matrix, and then a second export if someone needs rows.",
    ], [REPORTS], compare("Layout versus file", "Choose the picture, then the file.", "Layout", ["Tabular", "Summary", "Matrix"], "Export habit", ["Rows for a sheet", "Totals for a review", "Matrix is not a direct CSV"]),
    "Someone asks for a spreadsheet", ["Question", "Layout", "File"], [
        ("Question", "Grain", "Do they want calls, totals, or a cross-tab?", "grain"),
        ("Layout", "Tabular", "Calls become tabular.", "tab"),
        ("Layout", "Summary", "Totals become summary.", "sum"),
        ("Layout", "Matrix", "A cross-tab can be a matrix.", "mx"),
        ("File", "CSV", "The CSV comes from a layout that supports it.", "csv"),
        ("Admin", "Say", "You tell them the matrix is the picture, not the file.", "say"),
    ], [
        ("The three layouts are", ["Preview, power, predictive", "Tabular, Summary, Matrix", "ITSP, SBC, gateway", "Only charts"], 1, "Those three."),
        ("A matrix is", ["Always a CSV", "A cross-tab, not a direct CSV export", "A SIP method", "A headset"], 1, "Do not promise a direct CSV from the matrix."),
        ("Every call as a row suggests", ["Tabular", "Matrix only", "A WAV file", "A profile"], 0, "Tabular."),
        ("Averages by campaign suggest", ["Summary", "A packet capture", "Vertical dialing", "TLS 1.1"], 0, "Summary."),
        ("If the stakeholder needs rows from a matrix view, you", ["Email the matrix and call it CSV", "Produce a layout that exports rows", "Delete the report", "Change the ANI"], 1, "Separate the picture from the file."),
    ], [("Three layouts?", "Tabular, Summary, Matrix."), ("Matrix to CSV?", "Not directly."), ("Row-level?", "Tabular."), ("Totals?", "Summary.")],
    ("Pick a layout", "For three questions, name the layout and whether a CSV is honest.", ["Every abandoned call", "Average handle time by skill", "Skill crossed with disposition"], "The third answer does not say 'just export the matrix'."),
    ("A weekly email attaches a matrix and the sheet is empty of rows", "The layout was never the export.", "JOB layout=matrix file=csv rows=0", ["Run a tabular or summary export for the sheet", "Raise the abandon cap", "Reboot headsets", "Disable the Reporting role"], 0, "The file type and the layout disagreed.", "Export a layout that has rows."),
    ["Match the layout to the question", "Do not call a matrix a CSV"]))
    R.append(L("l04", "The call log is a window, not an archive", "practice", [
        "The call log report is the place people look for one call. The community article on filters, dated 14 July 2026, describes a window of about 60 days unless retention has been extended.",
        "Data-retention terms are a different clock: VCC audio is the sooner of 30 days, a successful SFTP or FTP offload, or the contract. A report row and a recording file do not expire on the same day. Say which one you mean.",
    ], [CALLLOG, RETAIN, REPORTPAGE], compare("Two clocks", "Do not use one number for both.", "Call log report", ["About 60 days in that article", "Unless retention is extended", "Filters live here"], "Recording file", ["Sooner of 30 days or successful offload", "Or the contract", "Not the same as the report row"]),
    "A call from last quarter is missing", ["Ask", "Report", "File"], [
        ("Ask", "Which", "Do they want the report row or the audio?", "which"),
        ("Report", "Age", "The call log window is checked.", "60"),
        ("Report", "Extend", "An extension is a configuration, not a hope.", "ext"),
        ("File", "Offload", "Audio follows the retention terms.", "off"),
        ("File", "30", "Thirty days is not sixty days.", "30"),
        ("Admin", "Say", "The answer names the clock.", "say"),
    ], [
        ("The July 2026 community article puts the call log around", ["7 days", "60 days unless extended", "10 years", "24 hours"], 1, "About 60 days unless retention is extended."),
        ("VCC audio retention is", ["Always 60 days", "The sooner of 30 days, a successful offload, or the contract", "Forever", "120 days for every file"], 1, "That is the retention page."),
        ("A missing recording at day 45 with a successful offload means", ["The report is also gone", "Look at the offload, not only the live player", "The carrier deleted SIP", "TCPA hid it"], 1, "Offload is one of the retention triggers."),
        ("You should quote 60 days as the audio law. True or false?", ["True", "False. That number was about the call log window", "True in the UK only", "True for E911 only"], 1, "Different clocks."),
        ("The article date matters because", ["Dates do not matter", "Windows can change. Cite the article you read", "It sets the codec", "It sets the ANI"], 1, "Re-read before you promise a window."),
    ], [("Call log window?", "About 60 days unless extended, per that article."), ("Audio?", "30 days, offload, or contract — whichever is sooner."), ("Same clock?", "No."), ("Why date the article?", "The window can change.")],
    ("Answer last quarter", "Say whether the row and the file should still exist.", ["Call log window", "Audio rule", "What you would tell the stakeholder"], "You used two numbers."),
    ("Leadership wants a 90-day recording from the live player", "Offload succeeded at day 10. The live copy is gone.", "AUDIO offload=ok age=90 player=miss", ["Pull the offload archive", "Rebuild the SIP trunk", "Change predictive pacing", "Delete the campaign"], 0, "The retention rule already moved the file.", "Use the archive."),
    ["Separate the call log window from audio retention", "Date the article you are quoting"], uncertain=["The 60-day call log window is from a community article dated 14 July 2026. Confirm the current window before you promise it."]))
    R.append(L("l05", "Call variables are not history", "advanced", [
        "Call variables can be reported when two things are true: the user has permission to edit them, and the variable is enabled for reporting. The community article is explicit that they are not historical. Turn the flag on today and yesterday's calls stay empty.",
        "Apply to All Dispositions does not cover custom dispositions. If the variable should stick on a custom outcome, that disposition is a separate checkbox, not a wish.",
    ], [CAV, REPORTS], path("A variable that shows up tomorrow", "Yesterday is already gone.", ["Permission: User Can Edit Call Variables", "Reporting enabled on the variable", "Custom dispositions checked one by one", "Only new calls"]),
    "The column is blank", ["Perm", "Flag", "Time"], [
        ("Perm", "Edit", "The editor permission is on.", "perm"),
        ("Flag", "Report", "The variable is enabled for reporting.", "flag"),
        ("Time", "When", "The flag's start date is written down.", "when"),
        ("Time", "Old", "Older calls are not backfilled.", "old"),
        ("Disp", "Custom", "Custom dispositions are checked individually.", "custom"),
        ("Admin", "Tell", "The stakeholder hears 'from now on'.", "tell"),
    ], [
        ("Enabling a call variable today fills history. True or false?", ["True", "False. They are not historical", "True for inbound only", "True after a reset"], 1, "The article says they are not historical."),
        ("The edit permission is named", ["User Can Edit Call Variables", "User Can Skip TCPA", "Reporting role only", "WEM admin"], 0, "That is the permission in the article."),
        ("Apply to All Dispositions covers custom dispositions. True or false?", ["True", "False", "Only in the UK", "Only for matrix reports"], 1, "Custom dispositions are not included."),
        ("A blank column on last month's calls after today's change means", ["The trunk failed", "The flag does not backfill", "ANI was wrong", "The list was vertical"], 1, "No backfill."),
        ("You enable reporting on the variable in addition to", ["The dialer mode", "The edit permission", "G.711", "A headset"], 1, "Both are required."),
    ], [("Backfill?", "No."), ("Permission name?", "User Can Edit Call Variables."), ("All dispositions includes custom?", "No."), ("Both switches?", "Permission and the reporting flag.")],
    ("Turn on a variable", "Write the permission, the flag, and the first call that can show it.", ["Permission", "Flag", "Start time"], "You promised no backfill."),
    ("A custom disposition never stores the variable", "Apply to All was checked and the custom code was not.", "DISP custom=Sale variable=empty all=yes", ["Edit that custom disposition", "Rebuild reports from last year", "Change the codec", "Disable TLS"], 0, "The bulk switch skipped it.", "Set the custom disposition."),
    ["Enable reporting before you need the column", "Check custom dispositions one by one"]))
    R.append(L("l06", "Prebuilt UC and the connector that is not an adapter", "practice", [
        "The product material names prebuilt connections for Zoom Phone and Microsoft Teams. A prebuilt path is a product. A Web Connector that opens a URL is also a product. They are not the bandwidth line you add for a Teams client on the agent's PC.",
        "The technical requirements treat a Teams, Zoom, Office@Hand, RingCentral, or Nextiva client on the workstation as about 320 kbps of extra traffic. Integrating the UC platform and running its app are two designs.",
    ], [APIS, TECH, ADP], compare("Two Teams stories", "Say which one the project is.", "A prebuilt integration", ["A named product path", "Not a headset", "Configured as that product"], "The app on the PC", ["About 320 kbps", "Shares the agent link", "Can exist with no integration"]),
    "Teams is in the design", ["Word", "Path", "Seat"], [
        ("Word", "Which", "Prebuilt integration or local client?", "which"),
        ("Path", "Product", "The prebuilt name is written if that is the project.", "pre"),
        ("Seat", "Kbps", "320 kbps is added if the client runs on the PC.", "bw"),
        ("Seat", "Adapter", "The CRM adapter is still its own line.", "ad"),
        ("Admin", "Connector", "A URL pop is called a connector.", "url"),
        ("Admin", "Avoid", "One slide does not say all three are the same.", "avoid"),
    ], [
        ("Zoom Phone and Teams appear as", ["Codecs", "Prebuilt connections in the product material", "List modes", "E911 vendors"], 1, "They are named prebuilt paths."),
        ("A Teams client on the agent PC is budgeted around", ["12 kbps", "320 kbps", "Zero, because of the integration", "88 kbps"], 1, "The requirements call out about 320 kbps."),
        ("A URL pop is", ["Always the Teams integration", "A Web Connector until you say otherwise", "A skill", "A report layout"], 1, "Connectors open URLs."),
        ("Buying the prebuilt path removes the bandwidth if the app still runs. True or false?", ["True", "False", "True on Mac", "True for Java"], 1, "The app still uses the link."),
        ("Office@Hand, RingCentral, and Nextiva are grouped with", ["Dispositions", "The UC bandwidth note", "IVR modules", "Equinix only"], 1, "They sit in that workstation note."),
    ], [("Prebuilt names?", "Zoom Phone and Teams, among the product lines."), ("Local Teams client?", "About 320 kbps."), ("URL pop?", "Web Connector."), ("Does prebuilt erase bandwidth?", "No.")],
    ("Split the Teams slide", "Write the integration and the workstation as two lines.", ["Prebuilt or not", "Bandwidth if the app is local", "Connector if it is only a URL"], "A reader sees two projects."),
    ("The link saturates after Teams is installed 'for free'", "The 320 kbps line was never added.", "BW teams=on budget=voice-only", ["Add the UC bandwidth or remove the client", "Lower TLS", "Change the matrix layout", "Reset dispositions"], 0, "The client is traffic.", "Budget it or remove it."),
    ["Name prebuilt UC separately from the desktop app", "Budget about 320 kbps when the UC client runs locally"]))
    R.append(L("l07", "What an extract is allowed to remember", "advanced", [
        "Reporting Web Services can move numbers out of the domain. Retention still applies to what Five9 keeps, not to the warehouse you built. Once a row is in your bucket, your policy owns it.",
        "Disabled domains, campaign state, agent data, and numbers have their own retention lines: agent data 60 days, campaign state 120 days, a disabled domain 120 days after closure, DIDs and toll-free numbers 90 days after closure. Do not design a 'temporary' domain and expect the DIDs to wait forever.",
    ], [RETAIN, APIS, REPORTS], stack("Retention lines that surprise a migration", "From the public retention terms.", ["Agent data 60 days", "Campaign state 120 days", "Disabled domain 120 days after closure", "DIDs and TFNs 90 days after closure"]),
    "A domain is closing", ["Export", "Clock", "Numbers"], [
        ("Export", "Now", "The reports you need are pulled while the role still works.", "now"),
        ("Clock", "State", "Campaign state is not a forever archive.", "state"),
        ("Clock", "Agent", "Agent data follows its own line.", "agent"),
        ("Numbers", "90", "DIDs and TFNs are planned inside 90 days of closure.", "did"),
        ("Numbers", "Domain", "120 days after closure is the domain line, not the DID line.", "dom"),
        ("Admin", "Own", "The warehouse copy is yours after export.", "own"),
    ], [
        ("Agent data retention on the public page is", ["60 days", "Forever", "7 days", "The call log window"], 0, "60 days."),
        ("Campaign state is", ["30 days", "120 days", "90 days", "10 years"], 1, "120 days."),
        ("DIDs and toll-free numbers after closure are", ["90 days", "120 days", "Kept while you remember them", "30 days of audio"], 0, "90 days."),
        ("A disabled domain's line is", ["90 days", "120 days after closure", "The same as a DID", "24 hours"], 1, "120 days after closure."),
        ("A row you already exported is governed by", ["Only Five9's page", "Your own policy as well", "The dialer mode", "RFC 4733"], 1, "Your copy is yours."),
    ], [("Agent data?", "60 days."), ("Campaign state?", "120 days."), ("DIDs after closure?", "90 days."), ("Disabled domain?", "120 days after closure.")],
    ("Close a domain on paper", "List what you will export and which clock kills the rest.", ["Reports", "DIDs", "Your warehouse policy"], "You did not assume the DID waits 120 days."),
    ("A number is reclaimed and the old domain cannot be reopened to read it", "Closure plus 90 days already passed.", "DID age=100d domain=closed", ["Treat the number as gone and use the export", "Open a codec ticket", "Change pacing", "Add a skill"], 0, "The retention page described this.", "Use the export you took while the domain was alive."),
    ["Export before the clocks run out", "Keep DID retention separate from domain retention"]))
    return track("t14", "APIs and reporting", "APIs", "Named web services, the Reporting role, layouts, call variables, and the clocks that delete evidence.", "Systems", "Advanced", "Name the API family. Name the report layout. Name which clock you mean.", R)
