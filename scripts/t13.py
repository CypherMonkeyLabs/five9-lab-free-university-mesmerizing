from curriculum_lib import TECH, SIP, RFC3261, RFC4733, E911, cite, lesson, stack, path, compare, track

RFC1918 = cite("RFC 1918", "https://www.rfc-editor.org/rfc/rfc1918")

def build():
    L = lesson
    R = []
    R.append(L("l01", "Three ways a call can enter", "foundation", [
        "The technical requirements describe three SIP stories. Five9 can provide ITSP trunks. Your ITSP can connect to Five9 session border controllers, and there is a checklist for that. Or a gateway you already own — Avaya, Cisco, or Asterisk — can talk to Five9 over the internet, a VPN, or Direct Connect.",
        "Cisco in that sentence is a gateway type, not a promise that a UCCX script will import. Pick the story before you draw a codec or a DNIS.",
    ], [TECH, SIP, RFC3261], stack("SIP stories in the requirements", "Name one before you open a firewall ticket.", ["Five9 ITSP trunks", "Your ITSP to Five9 SBCs", "Gateway to gateway: Avaya, Cisco, or Asterisk"]),
    "Choose the path", ["Buyer", "Carrier", "Gateway"], [
        ("Buyer", "Ask", "Who provides the trunk?", "who"),
        ("Carrier", "Five9", "Five9 ITSP is the first story.", "itsp"),
        ("Carrier", "Yours", "Your ITSP to Five9 SBCs is the second.", "sbc"),
        ("Gateway", "Owned", "Avaya, Cisco, or Asterisk is the third.", "gw"),
        ("Gateway", "Link", "Internet, VPN, or Direct Connect is the transport.", "link"),
        ("Admin", "Write", "The design names one story.", "named"),
    ], [
        ("Five9 can provide the ITSP trunks. True or false?", ["False", "True", "Only for Studio", "Only for E911"], 1, "The requirements list Five9 ITSP trunks as an option."),
        ("A customer ITSP connects toward", ["Agent headsets", "Five9 SBCs, with a checklist", "The campaign profile", "WEM"], 1, "That is the second story."),
        ("Named gateway types include", ["Only a cell phone", "Avaya, Cisco, or Asterisk", "Only CUCM partitions", "Only RedSky"], 1, "Those three names are in the requirements."),
        ("Transports named for gateway-to-gateway are", ["Satellite only", "Internet, VPN, or Direct Connect", "Analog only", "Fax only"], 1, "Those three."),
        ("A Cisco gateway option means UCCX scripts import. True or false?", ["True", "False. It is a SIP gateway type", "True for predictive", "True on Mac"], 1, "The requirements name a gateway, not a script importer."),
    ], [("Five9 ITSP?", "One of the three stories."), ("Customer ITSP lands on?", "Five9 SBCs."), ("Gateway names?", "Avaya, Cisco, Asterisk."), ("Does Cisco here import UCCX?", "No.")],
    ("Name the story", "Write which of the three paths a fictional site will use.", ["Who owns the trunk", "Which gateway, if any", "Which transport"], "The sentence uses one of the published names."),
    ("The diagram says 'SIP' and nothing else", "Nobody can say whose trunk it is.", "PATH unlabeled", ["Pick ITSP, SBC, or gateway before the firewall ticket", "Add predictive lines", "Reset the list", "Change the theme"], 0, "The requirements split the work into three stories.", "Label the path."),
    ["Name the three SIP stories", "Refuse to treat a Cisco gateway as a UCCX import"]))
    R.append(L("l02", "DNS, codecs, and the default voice", "practice", [
        "The requirements prefer DNS SRV for the SIP targets. G.711 is the default codec, and the PDF describes it as uncompressed. Do not invent a packetization time. A 20 millisecond ptime shows up in practitioner notes about Cisco gateways. It is not a number this lab will attribute to the Five9 PDF.",
        "RFC 3261 is the SIP signaling baseline. RFC 4733 is the telephone-event way digits often ride once the call is up. DTMF design is a separate sentence from the codec.",
    ], [TECH, SIP, RFC3261, RFC4733], compare("What the PDF states", "Keep practitioner numbers in their own column.", "In the requirements", ["DNS SRV preferred", "G.711 default", "Uncompressed voice"], "Not in that sentence", ["20 ms ptime", "A numeric abandon default", "A UCCX import"]),
    "A one-way-audio rumor", ["PDF", "Gateway", "Design"], [
        ("PDF", "SRV", "DNS SRV is the preferred lookup.", "srv"),
        ("PDF", "Codec", "G.711 is the default.", "g711"),
        ("Gateway", "Ptime", "20 ms is written as a practitioner note, marked uncertain.", "ptime"),
        ("Design", "DTMF", "RFC 4733 is named if digits must survive.", "dtmf"),
        ("Design", "Signaling", "RFC 3261 is the signaling reference.", "sip"),
        ("Admin", "Split", "The two columns stay split in the ticket.", "split"),
    ], [
        ("Preferred DNS for SIP targets is", ["A single A record only, always", "SRV, per the requirements", "A hosts file", "NetBIOS"], 1, "The PDF prefers DNS SRV."),
        ("The default codec named is", ["G.729 only", "G.711", "Opus only", "Fax"], 1, "G.711 is the default."),
        ("A 20 ms ptime is", ["The Five9 abandon default", "A practitioner note. Do not attribute it to the PDF", "Required by TCPA", "A skill level"], 1, "This lab did not find that number in the requirements text it used."),
        ("Telephone-event digits are discussed in", ["RFC 4733", "The disposition list", "WEM bidding", "The theme picker"], 0, "RFC 4733 covers telephone events."),
        ("SIP itself is", ["RFC 3261", "A campaign profile", "A list mode", "A headset brand"], 0, "RFC 3261 is the SIP specification."),
    ], [("DNS?", "SRV preferred."), ("Default codec?", "G.711."), ("20 ms?", "Practitioner, uncertain, not a PDF quote here."), ("Digit RFC?", "4733.")],
    ("Split the ticket", "Write the PDF facts and the practitioner note on two lines.", ["SRV and G.711", "ptime as uncertain", "RFC 4733 if DTMF matters"], "A reader can see which line is official."),
    ("Someone 'fixed' audio by forcing an unstated ptime", "The PDF was never opened.", "CHANGE ptime=20 source=chat", ["Revert to the documented default and test G.711", "Also change the abandon percentage", "Delete DNIS", "Disable SRV and hope"], 0, "Start from the codec the requirements name.", "Test G.711. Treat 20 ms as an unproven extra."),
    ["Prefer DNS SRV", "Keep G.711 as the default you can cite"], uncertain=["A 20 ms packet time is a practitioner note about Cisco gateways, not a figure quoted from the Five9 technical requirements in this lab."]))
    R.append(L("l03", "How much bandwidth a seat costs", "practice", [
        "The requirements give planning numbers. Agent Desktop Plus and the Plus adapters are 128 kbps. The Java agent is 88 kbps. Agent Assist adds about 12 kbps. A VPN adds about 64. CRM or other business apps add about 64. A UC client such as Teams, Zoom, Office@Hand, RingCentral, or Nextiva is called out around 320 kbps.",
        "One-way latency should stay under 150 ms. Wi-Fi is acceptable when the bandwidth is actually there. Wired is preferred. Satellite is not supported. Cellular and 5G are not supported. Those are support statements, not opinions.",
    ], [TECH], stack("Add the seat, then the extras", "Numbers from the technical requirements.", ["Plus adapter 128 kbps", "Java agent 88 kbps", "Assist about +12", "VPN about +64", "CRM apps about +64", "UC client about 320"]),
    "Size a remote seat", ["Seat", "Path", "Decision"], [
        ("Seat", "Client", "Plus or Java is chosen.", "client"),
        ("Seat", "Assist", "Assist is added only if it is on.", "assist"),
        ("Path", "VPN", "VPN overhead is added if the path is a VPN.", "vpn"),
        ("Path", "Apps", "CRM and UC are added when they share the link.", "apps"),
        ("Decision", "Latency", "The path is checked against 150 ms one way.", "lat"),
        ("Decision", "Medium", "Satellite and cellular are rejected.", "no"),
    ], [
        ("Plus adapter bandwidth in the PDF is", ["8 kbps", "128 kbps", "1 Gbps", "320 only"], 1, "128 kbps."),
        ("The Java agent figure is", ["128 kbps", "88 kbps", "The same as Teams", "Unstated"], 1, "88 kbps."),
        ("Agent Assist adds about", ["12 kbps", "320 kbps", "Nothing, ever", "A trunk"], 0, "About 12 kbps."),
        ("One-way latency target is", ["Under 150 ms", "Under 2 seconds", "Any", "150 minutes"], 0, "Under 150 ms one way."),
        ("Satellite and cellular are", ["Preferred for agents", "Not supported", "Required for predictive", "The E911 path"], 1, "The requirements say they are not supported."),
    ], [("Plus?", "128 kbps."), ("Java agent?", "88 kbps."), ("Assist?", "About +12."), ("Satellite?", "Not supported.")],
    ("Add a seat", "Total a Plus agent with VPN and a CRM app. Leave Teams off, then add it.", ["128 plus 64 plus 64", "Say the latency cap", "Reject cellular"], "You can show the arithmetic from the PDF."),
    ("Agents on hotel 5G sound broken", "The link is a medium the PDF does not support.", "PATH cellular latency=high", ["Move them to a supported wired or qualifying Wi-Fi path", "Raise Max Abandoned", "Change the skill name", "Disable G.711"], 0, "Cellular is not a supported agent path.", "Change the network, not the campaign."),
    ["Add the published per-seat numbers", "Reject satellite and cellular"]))
    R.append(L("l04", "NAT, idle timers, and split tunnels", "advanced", [
        "NAT and PAT are acceptable. Double NAT is not. UDP bindings that idle out cause one-way audio. The requirements use a 30 second UDP idle timeout as the planning number, and they tell you to send keepalives when the binding is shorter.",
        "On a VPN, translate RFC 1918 space to a public address the far side can route. Do not exclude Five9 domains from a split tunnel and then wonder why signaling dies. Do not restrict SIP or RTP between sites.",
    ], [TECH, RFC1918, RFC3261], path("A call that can return", "Each hop has to pass media, not just the invite.", ["Single NAT or PAT", "UDP idle at least 30 seconds", "Keepalives if shorter", "Five9 domains inside the tunnel"]),
    "One-way audio", ["Phone", "Firewall", "VPN"], [
        ("Phone", "Symptom", "The agent hears the caller. The caller hears nothing.", "oneway"),
        ("Firewall", "NAT", "Count the NAT layers. Two is too many.", "nat"),
        ("Firewall", "UDP", "The idle timer is compared with 30 seconds.", "udp"),
        ("VPN", "Split", "Five9 names are not excluded.", "split"),
        ("VPN", "RFC1918", "Private addresses are translated.", "nat64"),
        ("Admin", "RTP", "SIP and RTP are both allowed between the sites.", "rtp"),
    ], [
        ("Double NAT is", ["Recommended", "Not acceptable", "Required for TLS 1.3", "A list mode"], 1, "The requirements reject double NAT."),
        ("UDP idle planning number is", ["30 seconds", "30 minutes", "24 hours", "120 days"], 0, "30 seconds."),
        ("A shorter binding needs", ["A new campaign", "Keepalives", "Predictive mode", "A longer ANI"], 1, "Keepalives."),
        ("Split tunnel advice is", ["Exclude every Five9 name", "Do not exclude Five9 domains", "Disable RTP", "Use satellite"], 1, "Keep Five9 inside the tunnel."),
        ("RFC 1918 addresses on a VPN should be", ["Left as-is toward Five9", "Translated to a public address", "Used as the ANI", "Put in the skill name"], 1, "NAT them to public space."),
    ], [("Double NAT?", "No."), ("UDP idle?", "30 seconds."), ("Shorter timer?", "Keepalives."), ("Split tunnel?", "Do not exclude Five9.")],
    ("Trace one-way audio", "List NAT count, UDP timer, and whether Five9 is inside the tunnel.", ["NAT layers", "Idle timer", "Split-tunnel check"], "You did not start with the dialer mode."),
    ("Audio dies after half a minute of silence", "The firewall drops UDP before 30 seconds and nothing keepalive is sent.", "UDP idle=15s keepalive=off", ["Lengthen the binding or add keepalives", "Switch to vertical dialing", "Delete the profile", "Turn off SRV"], 0, "The timer matches the symptom.", "Fix the binding."),
    ["Reject double NAT", "Keep Five9 inside the VPN"]))
    R.append(L("l05", "Direct Connect and the edges", "advanced", [
        "Direct Connect in the requirements is a Layer-3 handoff. There is no Layer-2 requirement. The port is 10, 100, or 1000 full duplex, and failover uses BGP. Equinix Fabric edges named in the PDF this lab read are Chicago CH3, Washington DC10, London LD5, Amsterdam AM4, Frankfurt FR8, São Paulo SP4, Tokyo TY11, and Sydney SY5.",
        "Those city codes are a snapshot. A new PDF can add or retire an edge. Write the date next to the list before a circuit is ordered.",
    ], [TECH], stack("Edges named in the PDF we read", "Confirm before you order. October 2026 snapshot.", ["Chicago CH3", "Washington DC10", "London LD5", "Amsterdam AM4", "Frankfurt FR8", "São Paulo SP4", "Tokyo TY11", "Sydney SY5"]),
    "Order a circuit", ["PDF", "Order", "Routing"], [
        ("PDF", "Date", "The edge list is copied with a date.", "date"),
        ("Order", "Metro", "The metro is on that list.", "metro"),
        ("Order", "Handoff", "The handoff is Layer 3.", "l3"),
        ("Order", "Speed", "The port is 10, 100, or 1000 full duplex.", "speed"),
        ("Routing", "BGP", "Failover is BGP.", "bgp"),
        ("Admin", "No L2", "Nobody asks the provider for a Layer-2 LAN extension.", "nol2"),
    ], [
        ("Direct Connect handoff is", ["Layer 2 required", "Layer 3", "Analog", "Wi-Fi"], 1, "Layer 3."),
        ("Failover protocol named is", ["RIP", "BGP", "Static only", "NetBIOS"], 1, "BGP."),
        ("A port speed in the list is", ["10/100/1000 full duplex", "Only 100 Gbps", "Satellite", "5G"], 0, "Those three, full duplex."),
        ("London's code in that PDF is", ["LD5", "LHR1", "UK-SIP", "AM4"], 0, "LD5."),
        ("You should treat the city list as permanent. True or false?", ["True", "False. Date it and re-read", "True outside the US", "True for Java only"], 1, "Edges move."),
    ], [("Handoff?", "Layer 3."), ("Failover?", "BGP."), ("London?", "LD5 in that PDF."), ("Is the list forever?", "No.")],
    ("Date an edge", "Copy one metro code and write why you will re-check it.", ["Open the current PDF", "Copy the code with a date", "Name BGP and full duplex"], "The order form has a date."),
    ("The order asks for a Layer-2 extension to a city code from memory", "The PDF was not opened, and Layer 2 is the wrong handoff.", "ORDER l2=yes metro=remembered", ["Re-read the PDF and order Layer 3 with BGP", "Ship it", "Use cellular failover as the design", "Disable TLS"], 0, "Both the layer and the metro need the current document.", "Correct the order."),
    ["Order Layer 3 with BGP", "Date the Equinix edge list"], uncertain=["CH3, DC10, LD5, AM4, FR8, SP4, TY11, and SY5 are the Equinix Fabric edges in the technical requirements read in October 2026."]))
    R.append(L("l06", "TLS, and ports that are not universal", "advanced", [
        "Unencrypted APIs are not the story. TLS 1.2 is required. TLS 1.1 is not supported. The requirements also list TLS 1.3 inbound ciphers: AES-128-GCM, AES-256-GCM, and CHACHA20.",
        "Studio portal hosts and Studio SIP ports live in the Studio section of that PDF: UDP 5060, TCP 5061 described as beta, proxy UDP 5189 and TCP 5161, a legacy UDP 5188, plus RTP ranges. Do not paste those Studio numbers onto every VCC ITSP trunk. If the trunk guide does not say them, they are not the trunk.",
    ], [TECH, SIP], compare("Two port lists", "Studio media is not every VCC trunk.", "Domain requirements", ["TLS 1.2 required", "TLS 1.1 unsupported", "TLS 1.3 ciphers listed"], "Studio section only", ["UDP 5060", "TCP 5061 beta", "Proxy 5189 / 5161"]),
    "A firewall request arrives", ["Ask", "TLS", "Ports"], [
        ("Ask", "Which", "Is this VCC voice or Studio?", "which"),
        ("TLS", "Floor", "TLS 1.2 is the floor.", "12"),
        ("TLS", "Drop", "TLS 1.1 is removed.", "11"),
        ("Ports", "Studio", "Studio ports are copied only for Studio.", "studio"),
        ("Ports", "Trunk", "The trunk uses its own guide.", "trunk"),
        ("Admin", "Label", "The rule is labeled so the next person does not merge them.", "label"),
    ], [
        ("Required TLS version is", ["1.0", "1.2", "Any", "None"], 1, "TLS 1.2."),
        ("TLS 1.1 is", ["Preferred", "Not supported", "Required for Java", "The E911 cipher"], 1, "Not supported."),
        ("A TLS 1.3 inbound cipher named is", ["AES-256-GCM", "DES", "RC4", "Null"], 0, "AES-128-GCM, AES-256-GCM, and CHACHA20 are listed."),
        ("Studio UDP 5060 should be applied to", ["Every VCC ITSP trunk automatically", "Studio, when that section applies", "Headsets", "Lists"], 1, "Do not smear Studio ports across every trunk."),
        ("TCP 5061 in that Studio note is", ["Called generally available with no caveat", "Described as beta in the PDF this lab read", "A disposition", "A skill"], 1, "The note says beta. Re-read before you rely on it."),
    ], [("TLS floor?", "1.2."), ("TLS 1.1?", "Not supported."), ("Studio 5060 on every trunk?", "No."), ("5061 caveat?", "Beta in that PDF.")],
    ("Label the rule", "Write one firewall line for TLS and one for Studio, and refuse to merge them.", ["TLS 1.2", "Studio ports marked Studio", "A note that the trunk guide is separate"], "The two rules have different names."),
    ("Voice fails after a 'cleanup' that left TLS 1.1", "The floor is 1.2.", "TLS offered=1.1 result=fail", ["Offer TLS 1.2 or the listed 1.3 ciphers", "Drop to cleartext", "Open 5060 on the ITSP because Studio uses it", "Disable NAT"], 0, "Cleartext is also out. Studio ports are a different box.", "Restore a supported TLS version."),
    ["Require TLS 1.2", "Keep Studio ports in the Studio box"], uncertain=["Studio TCP 5061 is described as beta in the PDF read for this lab. Confirm before you depend on it."]))
    R.append(L("l07", "Headsets, and the call that only fails one way", "practice", [
        "USB noise-canceling headsets are the recommendation. Analog headsets are not supported. Wireless is not recommended once you are above roughly ten agents. Windows 11 Efficiency Mode can drop live calls. Java admin is not the Mac ARM path; use the web admin there. None of that is a SIP trunk, and all of it still stops a call.",
        "When audio fails, walk the stack this track just built: path type, codec, bandwidth medium, NAT, TLS, then the headset. The topology tool lets you pull the ITSP or the SBC and hear the symptom described. It is a model.",
    ], [TECH], path("Debug order for dead audio", "Leave the dialer mode alone until the path is honest.", ["Which SIP story", "G.711 and bandwidth", "NAT and UDP timer", "TLS version", "Headset and PC power mode"]),
    "A silent agent", ["PC", "Path", "Headset"], [
        ("PC", "Power", "Efficiency Mode is checked on Windows 11.", "eff"),
        ("Path", "Medium", "The link is not cellular or satellite.", "med"),
        ("Path", "TLS", "The offer is TLS 1.2 or better.", "tls"),
        ("Headset", "USB", "The headset is USB, not analog.", "usb"),
        ("Headset", "Wireless", "A large floor is not all on wireless.", "wifi"),
        ("Admin", "Model", "The topology toggle is used as a picture, not as proof.", "topo"),
    ], [
        ("Recommended headset style is", ["Analog", "USB noise-canceling", "Speakerphone only", "None"], 1, "USB noise-canceling."),
        ("Analog headsets are", ["Required", "Not supported", "The TLS 1.3 cipher", "Fine above 10 agents"], 1, "Not supported."),
        ("Wireless headsets above about ten agents are", ["Mandatory", "Not recommended", "The only supported option", "A campaign type"], 1, "Not recommended at that scale."),
        ("Windows 11 Efficiency Mode can", ["Improve abandon rate", "Drop live calls", "Replace DNS SRV", "Sign recordings"], 1, "The PDF warns it can drop live calls."),
        ("Java admin on Mac ARM is", ["The required console", "Not the path. Use web admin", "The ITSP", "E911"], 1, "The PDF says Java admin is not for Mac ARM."),
    ], [("Headset?", "USB noise-canceling."), ("Analog?", "Not supported."), ("Wireless at scale?", "Not recommended."), ("Efficiency Mode?", "Can drop live calls.")],
    ("Walk a silent seat", "Use the debug order on a fictional one-way call.", ["Path", "NAT", "Headset"], "You named a layer before you named a vendor ticket."),
    ("Every agent on a 40-person team uses a wireless headset and analog adapters", "The PDF already argued with that cart.", "HEADSET wireless=40 analog=yes", ["Move to wired USB noise-canceling sets", "Add lines per agent", "Change list penetration", "Disable SRV"], 0, "The scale and the analog adapters are both outside the recommendation.", "Replace the sets."),
    ["Specify USB headsets", "Check Efficiency Mode before you blame the trunk"], href="#/topology"))
    return track("t13", "SIP and carriers", "SIP", "ITSP trunks, your SBC, gateways, bandwidth, NAT, and the ports that belong only to Studio.", "Systems", "Advanced", "Name the path. G.711 is the default you can cite. Studio ports are not every trunk.", R)
