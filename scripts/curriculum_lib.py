"""Shared builders for the Five9 Lab curriculum."""

def stack(title, caption, rows):
    return {"kind": "stack", "title": title, "caption": caption, "rows": [{"label": row} for row in rows]}


def path(title, caption, rows):
    return {"kind": "path", "title": title, "caption": caption, "rows": [{"label": row} for row in rows]}


def compare(title, caption, left_title, left, right_title, right):
    return {
        "kind": "compare",
        "title": title,
        "caption": caption,
        "leftTitle": left_title,
        "rightTitle": right_title,
        "left": left,
        "right": right,
    }


def cite(label, url, note=""):
    row = {"label": label, "url": url}
    if note:
        row["note"] = note
    return row


def lesson(
    lid,
    title,
    level,
    paragraphs,
    cites,
    figure,
    flow_title,
    lanes,
    steps,
    quiz,
    cards,
    lab,
    fault,
    objectives,
    minutes=12,
    uncertain=None,
    callout=None,
    href=None,
):
    if len(quiz) < 5:
        raise SystemExit(f"{lid} {title} needs 5 quiz items")
    if len(cards) < 4:
        raise SystemExit(f"{lid} {title} needs 4 cards")
    if len(steps) < 5:
        raise SystemExit(f"{lid} {title} needs 5 flow steps")
    body = {
        "id": lid,
        "title": title,
        "level": level,
        "minutes": minutes,
        "objectives": objectives,
        "paragraphs": paragraphs,
        "cites": cites,
        "uncertain": uncertain or [],
        "figure": figure,
        "flow": {
            "title": flow_title,
            "lanes": lanes,
            "steps": [{"lane": lane, "title": name, "detail": detail, "frame": frame} for lane, name, detail, frame in steps],
        },
        "quiz": [{"q": q, "choices": choices, "answer": answer, "why": why} for q, choices, answer, why in quiz],
        "cards": [{"front": front, "back": back} for front, back in cards],
        "lab": {"title": lab[0], "goal": lab[1], "steps": lab[2], "success": lab[3], "href": href or ""},
        "fault": {
            "title": fault[0],
            "symptom": fault[1],
            "log": fault[2],
            "choices": fault[3],
            "answer": fault[4],
            "cause": fault[5],
            "fix": fault[6],
        },
    }
    if callout:
        body["callout"] = {"title": callout[0], "body": callout[1]}
    return body


def track(tid, title, short, blurb, group, level, summary, lessons):
    return {
        "id": tid,
        "title": title,
        "short": short,
        "blurb": blurb,
        "group": group,
        "level": level,
        "summary": summary,
        "lessons": lessons,
    }


# Official and primary sources used across tracks.
PLAN = cite("Planning your implementation", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/intro/planning-your-implementation.htm")
SKILLS = cite("Skill groups", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/skill-groups/_ch-skill-groups.htm")
PROFILES = cite("Campaign profiles", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/campaign-profiles/_ch-campaign-profiles.htm")
INBOUND = cite("Inbound campaigns", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/creating-campaigns/types-of-campaigns/inbound-campaigns.htm")
DEFAULTS = cite("Default campaign settings", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-dialing-modes/default-campaign-settings.htm")
DISP = cite("Managing campaign dispositions", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-dispositions/managing-dispositions.htm")
MODULES = cite("IVR modules", "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/_ch-modules.htm")
SKILLMOD = cite("Skill Transfer functions", "https://community.five9.com/s/article/Administrator-IVR-Skill-Transfer-Module-Functions-and-Features")
PAUSE = cite("Pause before transfer", "https://community.five9.com/s/article/Administrator-Pause-Before-Transfer?language=en_US")
LISTS = cite("List dialing modes", "https://community.five9.com/s/article/Administrator-List-Dialing-Modes-and-its-Differences?language=en_US")
DIALTEST = cite("Dialing modes live testing", "https://community.five9.com/s/article/Administrator-Campaign-Dialing-Modes-and-Live-Testing-Results", "Community test notes. Wording inside the article is not uniform.")
TCPA = cite("TCPA manual touch", "https://community.five9.com/s/article/Administrator-TCPA-Manual-Touch-Dialing-Mode?language=en_US")
DIALER = cite("Dialer product page", "https://www.five9.com/products/capabilities/dialer-system")
OUTBOUND = cite("Outbound product page", "https://www.five9.com/products/capabilities/outbound-contact-center")
ADP = cite("Agent Desktop", "https://www.five9.com/products/capabilities/agent-desktop")
ENGAGE = cite("Five9 Engage", "https://www.five9.com/platform/self-service-and-engagement")
WEM = cite("Workforce engagement management", "https://www.five9.com/products/capabilities/workforce-optimization")
GENAI = cite("GenAI Studio", "https://www.five9.com/products/capabilities/gen-ai-studio")
APIS = cite("APIs and SDKs", "https://www.five9.com/platform/integrations-and-ecosystem/apis-and-sdks")
TECH = cite("Technical requirements PDF", "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf", "Fetched for this lab in October 2026. Re-read before you buy hardware or open a firewall.")
ADAPTERS = cite("Web adapter requirements", "https://documentation.five9.com/bundle/technical-reqs/page/technical-reqs/agent-integrations/web-based-adapters/application-requirements.htm")
E911 = cite("E911 data sheet", "https://www.five9.com/sites/default/files/2022-11/Data-sheet-Five9-emergency-services%20%28E911%29.PDF")
EULA = cite("End user license agreement", "https://www.five9.com/legal/end-user-license-agreement")
RETAIN = cite("Data retention", "https://www.five9.com/legal/dataretention")
MYE911 = cite("MyE911 call history", "https://community.five9.com/s/article/MyE911-Call-History?language=en_US")
STIR = cite("Certified Caller", "https://www.five9.com/resources/five9_certified_caller")
UNIV = cite("Five9 University", "https://www.five9.com/contact-center-services/training")
UNIVADMIN = cite("Administrator training classes", "https://community.five9.com/s/article/Five9-University-Five9-Administrator-Training-Classes?language=en_US")
UNIVPDF = cite("University curriculum brief, April 2023", "https://www.five9.com/sites/default/files/2023-04/Five9_University_Curriculum_Brief_v5.pdf")
BADGE = cite("IVA Sales Certified badge", "https://www.credly.com/org/five9/badge/five9-iva-sales-certified")
IVABLOG = cite("Partner IVA sales certification", "https://www.five9.com/blog/five9-partners-can-now-become-sales-certified-five9-university-partners")
STUDIO = cite("Studio digital IVA with VCC", "https://community.five9.com/s/article/Studio-7-Integrate-Digital-IVA-in-Studio-with-VCC?language=en_US")
REPORTS = cite("Generating standard reports", "https://community.five9.com/s/article/Reporting-I-Generating-Standard-Reports")
CALLLOG = cite("Call log filters", "https://community.five9.com/s/article/Reporting-Apply-Filter-s-in-the-Call-Log-Report", "Community article dated 14 July 2026.")
CAV = cite("Call variables for reporting", "https://community.five9.com/s/article/Administrator-Enabling-Call-Variables-for-Reporting?language=en_US")
QUERY = cite("XML web service IVR example", "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/examples/creating-ivr-script-xml-web-service-query.htm")
PROFILEHOW = cite("Assign a campaign profile", "https://community.five9.com/s/article/Administrator-How-to-Create-Add-a-Campaign-Profile-and-Assign-it-to-a-Campaign?language=en_US")
RFC3261 = cite("RFC 3261", "https://www.rfc-editor.org/rfc/rfc3261")
RFC4733 = cite("RFC 4733", "https://www.rfc-editor.org/rfc/rfc4733")
VERTICAL = cite("Vertical list dialing chapter", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/configuring-campaigns/configuring-list-dialing-mode/using-vertical-list-dialing.htm")
SIP = cite("SIP trunk options chapter", "https://documentation.five9.com/bundle/technical-reqs/page/technical-reqs/SIP-trunk-options/_ch-five9-sip-trunk-options.htm")
REPORTPAGE = cite("Call log reports chapter", "https://documentation.five9.com/bundle/reports-dashboards/page/reports-dashboards/description-standard-and-social-reports/call-log-reports.htm")
SNOW = cite("ServiceNow Plus adapter", "https://documentation.five9.com/bundle/servicenowadmins/page/crm-admins/ServiceNow/introduction/_ch-configuring-the-five9-plus-adapter-for-servicenow.htm")
MENU = cite("Menu module", "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/menu-module.htm")
IFELSE = cite("If/Else module", "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/ifelse-module.htm")
SKILLPAGE = cite("Skill Transfer module chapter", "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/skill-transfer-module.htm")
WEMDS = cite("WEM data sheet", "https://www.five9.com/resources/data-sheet/five9-wem")
WFM = cite("Workforce management", "https://www.five9.com/platform/insights-and-analytics/workforce-management")
QM = cite("Quality management", "https://www.five9.com/products/capabilities/call-center-quality-management-monitoring-tools")
DESK = cite("Agent Desktop", "https://www.five9.com/platform/self-service-and-engagement/agent-desktop")
ACD = cite("Automatic call distributor", "https://en.wikipedia.org/wiki/Automatic_call_distributor")
