"""Glossary, certifications, interview deck, and boss incidents. Facts match the lessons."""

PLAN = ("Planning your implementation", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/intro/planning-your-implementation.htm")
SKILLS = ("Skill groups", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/skill-groups/_ch-skill-groups.htm")
PROFILES = ("Campaign profiles", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/campaign-profiles/_ch-campaign-profiles.htm")
INBOUND = ("Inbound campaigns", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/creating-campaigns/types-of-campaigns/inbound-campaigns.htm")
DEFAULTS = ("Default campaign settings", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-dialing-modes/default-campaign-settings.htm")
MODULES = ("IVR modules", "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/_ch-modules.htm")
LISTS = ("List dialing modes", "https://community.five9.com/s/article/Administrator-List-Dialing-Modes-and-its-Differences?language=en_US")
TCPA = ("TCPA manual touch", "https://community.five9.com/s/article/Administrator-TCPA-Manual-Touch-Dialing-Mode?language=en_US")
DIALER = ("Dialer product page", "https://www.five9.com/products/capabilities/dialer-system")
OUTBOUND = ("Outbound product page", "https://www.five9.com/products/capabilities/outbound-contact-center")
ADP = ("Agent Desktop", "https://www.five9.com/products/capabilities/agent-desktop")
WEM = ("Workforce engagement management", "https://www.five9.com/products/capabilities/workforce-optimization")
GENAI = ("GenAI Studio", "https://www.five9.com/products/capabilities/gen-ai-studio")
APIS = ("APIs and SDKs", "https://www.five9.com/platform/integrations-and-ecosystem/apis-and-sdks")
TECH = ("Technical requirements PDF", "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf")
E911 = ("E911 data sheet", "https://www.five9.com/sites/default/files/2022-11/Data-sheet-Five9-emergency-services%20%28E911%29.PDF")
EULA = ("End user license agreement", "https://www.five9.com/legal/end-user-license-agreement")
RETAIN = ("Data retention", "https://www.five9.com/legal/dataretention")
MYE911 = ("MyE911 call history", "https://community.five9.com/s/article/MyE911-Call-History?language=en_US")
STIR = ("Certified Caller", "https://www.five9.com/resources/five9_certified_caller")
UNIV = ("Five9 University", "https://www.five9.com/contact-center-services/training")
UNIVADMIN = ("Administrator training classes", "https://community.five9.com/s/article/Five9-University-Five9-Administrator-Training-Classes?language=en_US")
UNIVPDF = ("University curriculum brief, April 2023", "https://www.five9.com/sites/default/files/2023-04/Five9_University_Curriculum_Brief_v5.pdf")
BADGE = ("IVA Sales Certified badge", "https://www.credly.com/org/five9/badge/five9-iva-sales-certified")
REPORTS = ("Generating standard reports", "https://community.five9.com/s/article/Reporting-I-Generating-Standard-Reports")
CALLLOG = ("Call log filters", "https://community.five9.com/s/article/Reporting-Apply-Filter-s-in-the-Call-Log-Report")
CAV = ("Call variables for reporting", "https://community.five9.com/s/article/Administrator-Enabling-Call-Variables-for-Reporting?language=en_US")
SKILLMOD = ("Skill Transfer functions", "https://community.five9.com/s/article/Administrator-IVR-Skill-Transfer-Module-Functions-and-Features")
STUDIO = ("Studio digital IVA with VCC", "https://community.five9.com/s/article/Studio-7-Integrate-Digital-IVA-in-Studio-with-VCC?language=en_US")
RFC3261 = ("RFC 3261", "https://www.rfc-editor.org/rfc/rfc3261")
RFC4733 = ("RFC 4733", "https://www.rfc-editor.org/rfc/rfc4733")
SNOW = ("ServiceNow Plus adapter", "https://documentation.five9.com/bundle/servicenowadmins/page/crm-admins/ServiceNow/introduction/_ch-configuring-the-five9-plus-adapter-for-servicenow.htm")

MAP = """<svg viewBox="0 0 720 420" role="img" aria-label="Neighbors of a Five9 domain">
<rect width="720" height="420" fill="#041018"></rect>
<rect x="250" y="160" width="220" height="90" rx="14" fill="#102033" stroke="#3ee0ff"></rect>
<text x="360" y="198" text-anchor="middle" fill="#e7eef8" font-size="16">Five9 domain</text>
<text x="360" y="220" text-anchor="middle" fill="#9aefff" font-size="12">skills, campaigns, IVR</text>
<g fill="#102033" stroke="#f5b942" font-size="12">
<rect x="40" y="40" width="160" height="52" rx="10"></rect>
<rect x="280" y="36" width="160" height="52" rx="10"></rect>
<rect x="520" y="40" width="160" height="52" rx="10"></rect>
<rect x="40" y="300" width="160" height="52" rx="10"></rect>
<rect x="250" y="310" width="220" height="52" rx="10"></rect>
<rect x="520" y="300" width="160" height="52" rx="10"></rect>
</g>
<g fill="#e7eef8" font-size="13">
<text x="120" y="70" text-anchor="middle">SIP path</text>
<text x="360" y="66" text-anchor="middle">Agent desktop</text>
<text x="600" y="70" text-anchor="middle">CRM adapter</text>
<text x="120" y="330" text-anchor="middle">E911 / RedSky</text>
<text x="360" y="340" text-anchor="middle">WEM and reports</text>
<text x="600" y="330" text-anchor="middle">IVA and GenAI</text>
</g>
</svg>"""


def glossary():
    rows = [
        ("Domain", "The VCC tenant. Skills, users, lists, and campaigns stay inside it.", PLAN),
        ("Skill group", "Agents or supervisors who can take a campaign's work. A user and a campaign can have more than one.", SKILLS),
        ("User profile", "The permission template for a person. Not a campaign profile.", PLAN),
        ("Campaign profile", "Overrides defaults such as ANI. One profile is assigned to a campaign. The same profile can be reused.", PROFILES),
        ("Campaign", "Inbound, outbound, or autodial. Blended is staffing language, not a fourth type.", INBOUND),
        ("DNIS", "The number an inbound campaign answers. A stopped campaign does not answer.", INBOUND),
        ("Disposition", "The outcome code on a call. Final disposition stops the other numbers on that record for the campaign.", LISTS),
        ("List penetration", "The default list walk: first number on every record, then the next number.", LISTS),
        ("Vertical dialing", "Finishes the numbers on one record before moving on. Community notes say the compass wording is easy to misread.", LISTS),
        ("Preview", "The agent sees CRM history before the dial.", DIALER),
        ("Progressive", "The outbound page describes one customer call per available agent. The dialer page also says adaptive pace. Quote the page you mean.", OUTBOUND),
        ("Power", "A configured number of calls per agent, with an abandon throttle.", DIALER),
        ("Predictive", "Algorithmic pacing. Product guidance talks about teams larger than about ten agents.", DIALER),
        ("Manual touch", "No automatic dial. TCPA manual touch adds typing, blocks paste, and enables Dial on a match.", TCPA),
        ("Max Abandoned Call Percentage", "A campaign field with a warning if you change it. This lab does not state a numeric default.", DEFAULTS),
        ("IVR module", "A named block in the IVR Administrator's Guide, such as Menu, Play, If/Else, or Skill Transfer.", MODULES),
        ("Skill Transfer", "Sends the call toward one or more skills. No skill selected means the Default queue in the community write-up.", SKILLMOD),
        ("Default queue", "Where a Skill Transfer with no skill goes, per the community article.", SKILLMOD),
        ("Call variable", "Reportable only after the edit permission and the reporting flag. Not historical.", CAV),
        ("Reporting role", "Required, with a reporting permission, before standard reports appear.", REPORTS),
        ("Call log", "A report with filters. A July 2026 community article describes about 60 days unless retention is extended.", CALLLOG),
        ("Web2Campaign", "One of the API names on the APIs and SDKs page.", APIS),
        ("CRM SDK", "The path for a CRM that is not a named Plus adapter.", APIS),
        ("Web Connector", "Opens a URL. Not the same object as a Plus adapter.", APIS),
        ("Plus adapter", "The listed CRM integrations, using HTTPS and Secure WebSocket.", TECH),
        ("G.711", "The default codec in the technical requirements, described as uncompressed.", TECH),
        ("DNS SRV", "The preferred lookup for SIP targets in the technical requirements.", TECH),
        ("TLS 1.2", "The required TLS version. TLS 1.1 is not supported.", TECH),
        ("Direct Connect", "Layer-3 handoff, full duplex, BGP failover, in the technical requirements.", TECH),
        ("Certified Caller", "Five9's STIR/SHAKEN program. Not the same thing as a local ANI on a profile.", STIR),
        ("E911", "Direct 911 with a dispatchable location. The data sheet names RedSky.", E911),
        ("Dispatchable location", "The place responders can find the caller. A stale HQ address fails that test.", E911),
        ("MyE911", "Org-admin history: time, user, number, location, recording, SIP invite.", MYE911),
        ("WEM", "Workforce, quality, analytics, surveys, and recording. Native suite and a Verint partnership are both on the product page.", WEM),
        ("GenAI Studio", "Knowledge and prompts for Five9 AI apps. This lab does not name a default model.", GENAI),
        ("Studio task key", "The key copied from a ChatBot task into VCC for a digital IVA.", STUDIO),
        ("Agent Desktop Plus", "The single agent screen. Same underlying technology as the prebuilt CRM adapters, per the desktop page.", ADP),
        ("Retention", "Separate clocks for audio, E911 recordings, agent data, campaign state, domains, and DIDs.", RETAIN),
        ("RFC 3261", "The SIP specification. It does not choose your dial plan.", RFC3261),
        ("RFC 4733", "Telephone events, the usual way DTMF rides in the media.", RFC4733),
    ]
    return [{"term": t, "meaning": m, "url": u, "source": s} for t, m, (s, u) in rows]


def integrations():
    rows = [
        ("Salesforce Plus adapter", "Named in the technical requirements, with Lightning CTI. Package 2.46 is a dated PDF figure.", TECH),
        ("Salesforce IVR module", "A script module, including SFDC Einstein. Different from the desktop adapter.", MODULES),
        ("ServiceNow Plus adapter", "Service Operations and Configurable workspaces. Release names in the PDF this lab read: Australia, Zurich, Yokohama.", SNOW),
        ("Dynamics 365, Zendesk, Oracle, NetSuite, Epic", "Each is a named Plus adapter. This lab does not copy a package number for them.", TECH),
        ("CRM SDK", "Bring-your-own CRM when no named adapter exists.", APIS),
        ("Zoom Phone and Microsoft Teams", "Named prebuilt connections. A local UC client is also about 320 kbps.", APIS),
        ("Verint", "Named on the WEM page as a partnership. Not a synonym for native WEM.", WEM),
        ("RedSky", "Emergency-location partner on the E911 data sheet. Not the ITSP.", E911),
        ("Five9 ITSP", "One of three SIP stories. The others are your ITSP to Five9 SBCs, or a gateway.", TECH),
        ("Cisco, Avaya, or Asterisk gateway", "Gateway-to-gateway over internet, VPN, or Direct Connect. Not a UCCX importer.", TECH),
        ("Studio digital IVA", "A ChatBot task key from the matching regional Studio portal into VCC.", STUDIO),
        ("GenAI Studio", "Prompts and knowledge. Agent Assist summaries are the initial consumer the page names.", GENAI),
        ("Statistics and Reporting web services", "Two different API names. A wallboard and a standard report are different pipes.", APIS),
        ("Certified Caller", "STIR/SHAKEN attestation for FCC and CRTC. Separate from profile ANI.", STIR),
    ]
    return [{"system": n, "how": h, "url": u, "source": s} for n, h, (s, u) in rows]


def certs():
    return {
        "intro": "These are the training names this lab could verify on a public page. Empty exam codes are intentional.",
        "items": [
            {"name": "Five9 University", "status": "Verified", "detail": "Public training front door for contact-center classes.", "url": UNIV[1], "source": UNIV[0]},
            {"name": "Online, webinar, instructor-led, train-the-trainer, custom", "status": "Verified", "detail": "Formats named in the curriculum brief dated April 2023. The live catalog wins.", "url": UNIVPDF[1], "source": UNIVPDF[0]},
            {"name": "Administrator training and assessments", "status": "Verified", "detail": "Administrator classes and assessments are described publicly. No exam code is printed there for this lab to repeat.", "url": UNIVADMIN[1], "source": UNIVADMIN[0]},
            {"name": "Five9 IVA Sales Certified", "status": "Verified", "detail": "Credly badge: 5 modules, 20-question final, 80 percent. Partner sales certification, not a VCC engineering exam.", "url": BADGE[1], "source": BADGE[0]},
            {"name": "Five9-CA-xxx or any numbered admin exam", "status": "Not found", "detail": "This lab will not print a code it cannot cite. Treat third-party codes as unverified.", "url": UNIV[1], "source": UNIV[0]},
        ],
        "uncertain": [
            "The curriculum brief is from April 2023. Course names move.",
            "Badge attempt rules should be re-read on Credly before you depend on them.",
            "No public administrator exam code was found. Absence here is not proof a private assessment never exists.",
        ],
    }


def interview():
    qa = [
        ("What do you build before an outbound campaign?", "Skill groups, user profiles, users, contact fields, lists, dispositions, and campaign profiles. Then the campaign.", PLAN),
        ("Which builds add IVR scripts on the planning roadmap?", "Inbound and autodial.", PLAN),
        ("What is a Five9 domain?", "The tenant boundary. Lists and skills do not leak into the next domain.", PLAN),
        ("Does Five9 use CUCM partitions?", "Not in the admin model this lab cites. The boundary is the domain. Mapping partitions to anything is a teaching bridge.", SKILLS),
        ("Who can be in a skill group?", "Users with the agent or supervisor role. A user can be in more than one skill, and a campaign can have more than one skill.", SKILLS),
        ("How many campaign profiles can a campaign use at once?", "One. A profile can still be reused by several campaigns. Assign it in Advanced mode.", PROFILES),
        ("What can a campaign profile override?", "Defaults such as the ANI. Workflow rules can swap the profile.", PROFILES),
        ("What happens if an inbound campaign is stopped?", "It does not answer. Callers can hear busy.", INBOUND),
        ("Name the three campaign types.", "Inbound, outbound, and autodial. Blended is how you staff, not a fourth type.", OUTBOUND),
        ("What is list penetration?", "The default walk: the first number on every record, then the next.", LISTS),
        ("What is vertical list dialing?", "The dialer finishes the numbers on one record before it moves on.", LISTS),
        ("What does a final disposition do to the other numbers on a record?", "It stops them for that campaign.", LISTS),
        ("Name the dialing modes on the product pages.", "Preview, progressive, power, predictive, and manual touch.", DIALER),
        ("How does the outbound page describe progressive?", "One customer call per available agent.", OUTBOUND),
        ("Why will you not state a numeric abandon default?", "The defaults page warns if Max Abandoned Call Percentage changes. It does not give this lab a percent worth repeating.", DEFAULTS),
        ("What abandon windows does the defaults page describe?", "A US rolling 30 days and a UK window of 24 hours, set with a Five9 representative.", DEFAULTS),
        ("What does TCPA manual touch block?", "Paste and drag. The agent types the external number. Dial enables when it matches. Preview timeout sets Not Ready and does not auto-dial.", TCPA),
        ("Which permission allows skipping records in TCPA manual touch?", "User Can Skip Contact Records in TCPA Manual Touch.", TCPA),
        ("Name four IVR modules.", "Play, Menu, If/Else, and Skill Transfer are in the modules chapter, among others.", MODULES),
        ("Where does a Skill Transfer with no skill go?", "The community article says the Default queue.", SKILLMOD),
        ("Are call variables historical?", "No. Enable reporting before the calls you need. Apply to All Dispositions skips custom dispositions.", CAV),
        ("Who can run standard reports?", "A user with the Reporting role and at least one reporting permission.", REPORTS),
        ("Why is a matrix a bad CSV?", "The reporting article treats matrix as a layout, not a direct CSV export.", REPORTS),
        ("How long is the call log, per the July 2026 article?", "About 60 days unless retention is extended. Audio follows a different clock.", CALLLOG),
        ("How long does the retention page keep VCC audio?", "The sooner of 30 days, a successful SFTP or FTP offload, or the contract.", RETAIN),
        ("How long are DIDs kept after a domain closes?", "90 days. A disabled domain itself is 120 days after closure.", RETAIN),
        ("Name two API families without guessing SOAP versus REST.", "Reporting Web Services and Statistics Web Services. The overview also says REST. The transport per family stays unconfirmed here.", APIS),
        ("What is the default codec?", "G.711, described as uncompressed. DNS SRV is preferred for SIP targets.", TECH),
        ("Which TLS versions matter?", "TLS 1.2 is required. TLS 1.1 is not supported. TLS 1.3 inbound ciphers are listed.", TECH),
        ("Is satellite a supported agent path?", "No. Cellular and 5G are not supported either. One-way latency should stay under 150 ms.", TECH),
        ("What does the E911 data sheet say you dial?", "911 directly, with no prefix, and a dispatchable location. The partner named is RedSky.", E911),
        ("What does MyE911 history show an org admin?", "Time, user, number, location, recording, and the SIP invite.", MYE911),
        ("Is a campaign-profile ANI the same as Certified Caller?", "No. Certified Caller is the STIR/SHAKEN program associated with FCC and CRTC.", STIR),
        ("What is on the WEM product page?", "Workforce management, quality, analytics, surveys, recording, and a Verint partnership.", WEM),
        ("Does this lab name GenAI Studio's default model?", "No. The page describes an engine-agnostic studio and names Agent Assist summaries as an early consumer.", GENAI),
        ("What credential will you not invent?", "An administrator exam code. IVA Sales Certified is a partner sales badge: 5 modules, 20 questions, 80 percent.", BADGE),
    ]
    return {"items": [{"q": q, "a": a, "url": u, "source": s} for q, a, (s, u) in qa]}


def boss():
    def step(q, choices, answer, why):
        return {"q": q, "choices": choices, "answer": answer, "why": why}

    items = [
        {
            "id": "busy-dnis",
            "severity": "Sev 2",
            "title": "The new DNIS is busy",
            "symptom": "Callers hear busy. No agent phone rings.",
            "log": "CAMPAIGN Retail type=inbound state=NOT_RUNNING dnis=8005550101 script=hours agents_ready=6",
            "url": INBOUND[1], "source": INBOUND[0],
            "resolution": "Start the inbound campaign. A stopped campaign does not answer, even when agents are Ready and a script exists.",
            "steps": [
                step("What do you check first?", ["The Equinix edge", "Whether the inbound campaign is running", "The sales badge", "The theme"], 1, "The inbound topic: a campaign that is not running does not answer."),
                step("Agents are Ready. Does that answer the DNIS?", ["Yes", "No. The campaign still has to be running", "Only if the codec is G.729", "Only on a matrix report"], 1, "Ready agents do not help a stopped campaign."),
                step("After it is started, what else must be true?", ["A fake exam code", "The script and the DNIS belong to that running campaign", "TLS 1.1", "Analog headsets"], 1, "The campaign needs its script and its number."),
            ],
        },
        {
            "id": "blend-abandon",
            "severity": "Sev 1",
            "title": "Predictive lines and an inbound queue",
            "symptom": "Abandon rate climbs after inbound agents were told to 'also take outbound'.",
            "log": "MODE predictive agents_outbound=4 agents_also_inbound=4 ABANDON climbing WINDOW=US-30d",
            "url": DIALER[1], "source": DIALER[0],
            "resolution": "Stop treating blended bodies as dedicated predictive agents. The dialer page's guidance is a larger dedicated team. Do not invent a new abandon percent.",
            "steps": [
                step("What is wrong with the staffing?", ["Nothing, blended is a fourth campaign type", "Predictive guidance wants a dedicated team, and these agents are also on inbound", "G.711 is uncompressed", "The profile has an ANI"], 1, "Blended is staffing. Predictive product guidance is about team size and dedication."),
                step("Do you type a new Max Abandoned Call Percentage from memory?", ["Yes, 3", "No. The page warns, and this lab does not cite a default percent", "Yes, 20", "Yes, 0"], 1, "Do not invent the number."),
                step("Who is involved if the measurement window itself must change?", ["The theme picker", "A Five9 representative. US is described as a rolling 30 days", "RedSky", "The Menu module"], 1, "The defaults page says a representative sets the window."),
            ],
        },
        {
            "id": "tcpa-paste",
            "severity": "Sev 3",
            "title": "Dial stays grey",
            "symptom": "Agents paste from the CRM. Dial never enables.",
            "log": "MODE tcpa_manual_touch paste=blocked typed= dial=disabled preview_timeout=not_ready",
            "url": TCPA[1], "source": TCPA[0],
            "resolution": "The control is working. Type the external number. Dial enables on a match. Do not flip the campaign to another mode to get around it.",
            "steps": [
                step("Why is Dial disabled?", ["The skill is empty", "Paste is blocked and nothing was typed", "The call log expired", "SRV failed"], 1, "TCPA manual touch requires typing."),
                step("A preview times out. What happens?", ["The record auto-dials", "The agent goes Not Ready and nothing auto-dials", "The DID is released", "A matrix exports"], 1, "That is the article."),
                step("Which permission is about skipping, not pasting?", ["User Can Edit Call Variables", "User Can Skip Contact Records in TCPA Manual Touch", "Reporting", "WEM admin"], 1, "Skipping is its own permission."),
            ],
        },
        {
            "id": "default-queue",
            "severity": "Sev 2",
            "title": "Everyone lands on Default",
            "symptom": "The IVR sounds right. The Billing skill never sees the call.",
            "log": "MODULE SkillTransfer skills=[] queue=Default disp_default=Abandon",
            "url": SKILLMOD[1], "source": SKILLMOD[0],
            "resolution": "Select the Billing skill on the Skill Transfer. The community article says no skill routes to Default.",
            "steps": [
                step("Why Default?", ["The campaign is stopped", "The module has no skill selected", "Paste was used", "The ANI is local"], 1, "No skill selected goes to Default."),
                step("How many skills should you put on the module if you want a clean report?", ["As many as possible", "The community article recommends one skill per module", "Zero", "Only Default"], 1, "One skill keeps the report readable."),
                step("What is the default disposition named for that module?", ["Sale", "Abandon", "Final", "Busy"], 1, "The article says Abandon."),
            ],
        },
        {
            "id": "variables-late",
            "severity": "Sev 3",
            "title": "Last month's column is empty",
            "symptom": "A call variable was enabled this morning. Historical rows are blank.",
            "log": "CAV name=CustomerType reporting=on since=today custom_disp=Sale checked=no",
            "url": CAV[1], "source": CAV[0],
            "resolution": "Call variables are not historical. New calls can populate. Also check the custom disposition; Apply to All does not cover it.",
            "steps": [
                step("Will yesterday backfill?", ["Yes", "No", "Only for inbound", "Only as a CSV"], 1, "The article says they are not historical."),
                step("The Sale disposition is custom and still empty. Why?", ["Apply to All skipped custom dispositions", "G.711", "The domain closed", "RedSky"], 0, "Custom dispositions need their own check."),
                step("Which permission edits the variables?", ["User Can Edit Call Variables", "User Can Skip Contact Records in TCPA Manual Touch", "A sales badge", "Java on Mac ARM"], 0, "That is the permission name."),
            ],
        },
        {
            "id": "wss-pop",
            "severity": "Sev 2",
            "title": "Voice is up, Salesforce is blank",
            "symptom": "Agents hear the caller. The Lightning adapter never pops.",
            "log": "VOICE rtp=ok ADAPTER=salesforce WSS=blocked proxy=corporate package_pdf=2.46",
            "url": TECH[1], "source": TECH[0],
            "resolution": "The proxy must pass Secure WebSocket. Voice and the adapter are different channels. Recheck the package version against the current PDF before you freeze 2.46.",
            "steps": [
                step("What does a live call prove about the adapter?", ["That WSS works", "Nothing. The adapter is a separate path", "That the package is current", "That E911 is registered"], 1, "Plus adapters use HTTPS and WSS."),
                step("The corporate proxy drops WebSocket. What do you change?", ["The abandon percent", "The proxy, so it supports WSS", "The skill name", "List penetration"], 1, "The requirements say the proxy must support WSS."),
                step("How should 2.46 appear in the ticket?", ["As a permanent law", "As the number in the PDF you read, with a date", "As an exam code", "As the ANI"], 1, "Versions move."),
            ],
        },
        {
            "id": "stale-e911",
            "severity": "Sev 1",
            "title": "Home agents would send the HQ address",
            "symptom": "A test shows the downtown office for an agent who works from home.",
            "log": "E911 user=sam loc=HQ actual=home history=invite_contains_HQ",
            "url": E911[1], "source": E911[0],
            "resolution": "Register the dispatchable home location and retest. MyE911 history should then show that place. Do not add a dialing prefix.",
            "steps": [
                step("What is wrong?", ["The codec", "The registered location is not where the agent is", "The sales badge", "The matrix layout"], 1, "Dispatchable location has to be real."),
                step("How should the agent dial?", ["9-911", "911, no prefix", "A skill number", "The ANI"], 1, "The data sheet says direct 911."),
                step("What confirms the fix?", ["A green theme", "MyE911 history shows the home location and the invite", "A shorter call log", "Vertical dialing"], 1, "History includes location and the SIP invite."),
            ],
        },
        {
            "id": "one-way-audio",
            "severity": "Sev 2",
            "title": "The caller hears silence after a pause",
            "symptom": "Audio works for a few seconds, then the caller hears nothing.",
            "log": "NAT layers=1 UDP_idle=15s keepalive=off codec=G.711 path=vpn split_tunnel_excludes=five9",
            "url": TECH[1], "source": TECH[0],
            "resolution": "Lengthen the UDP binding toward 30 seconds or add keepalives, and stop excluding Five9 from the split tunnel. Keep G.711. Do not treat a 20 ms ptime rumor as the PDF.",
            "steps": [
                step("Which timer matches the symptom?", ["The 60-day call log", "UDP idle shorter than 30 seconds with no keepalive", "DID retention", "The UK 24-hour abandon window"], 1, "The requirements use 30 seconds as the UDP idle planning number."),
                step("The VPN excludes Five9 names. Is that correct?", ["Yes", "No. Do not exclude them from the split tunnel", "Only for Studio ports", "Only for analog headsets"], 1, "Keep Five9 inside the tunnel."),
                step("What do you refuse to claim?", ["G.711 is the default", "That 20 ms ptime is a Five9 requirement", "TLS 1.2 is required", "Double NAT is rejected"], 1, "20 ms is a practitioner note, not a figure this lab quotes from the PDF."),
            ],
        },
    ]
    return {"items": items}


def ecosystem():
    return {
        "map": MAP,
        "mapCaption": "A teaching map. Each box fails on its own. SIP up does not prove the adapter, the location, or the bot.",
        "glossary": glossary(),
        "integrations": integrations(),
        "uncertain": [
            "Progressive pacing is worded differently on the dialer page and the outbound page. The glossary says so.",
            "Salesforce package 2.46 and the ServiceNow release names are from the technical requirements read in October 2026.",
            "The call-log window of about 60 days is from a community article dated 14 July 2026.",
            "SOAP versus REST is not assigned per API family.",
        ],
    }
