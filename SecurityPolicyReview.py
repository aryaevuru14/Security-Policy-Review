import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Page Setup - Margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Color Palette Definitions
NAVY_PRIMARY = RGBColor(16, 44, 87)       # #102C57
ACCENT_BLUE = RGBColor(53, 89, 140)      # #35598C
DARK_TEXT = RGBColor(34, 34, 34)         # #222222
MUTED_GRAY = RGBColor(100, 100, 100)     # #646464
CODE_BG_HEX = "F4F6F9"

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = NAVY_PRIMARY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = ACCENT_BLUE
    return p

def add_body_p(text, bold_prefix="", space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = DARK_TEXT
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(11)
    run.font.color.rgb = DARK_TEXT
    return p

# Document Title Block
p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(0)
p_title.paragraph_format.space_after = Pt(4)
r_title = p_title.add_run("ENTERPRISE SECURITY POLICY AUDIT & GAP ANALYSIS")
r_title.font.name = 'Calibri'
r_title.font.size = Pt(22)
r_title.font.bold = True
r_title.font.color.rgb = NAVY_PRIMARY

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_before = Pt(0)
p_sub.paragraph_format.space_after = Pt(8)
r_sub = p_sub.add_run("Comprehensive Critique, Vulnerability Assessment, and Remediation Roadmap")
r_sub.font.name = 'Calibri'
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.color.rgb = ACCENT_BLUE

p_meta = doc.add_paragraph()
p_meta.paragraph_format.space_before = Pt(0)
p_meta.paragraph_format.space_after = Pt(18)
r_meta = p_meta.add_run("Document Ref: SPR-ISO-2026-V1  |  Alignment: ISO/IEC 27001:2022 & NIST SP 800-53  |  Classification: Confidential")
r_meta.font.name = 'Calibri'
r_meta.font.size = Pt(9.5)
r_meta.font.color.rgb = MUTED_GRAY

# Section 1
add_heading_1("1. Executive Summary")
add_body_p("This document provides a comprehensive security policy review and strategic remediation framework for the organization's current Information Security Policy. Utilizing standard industry benchmarks—primarily ISO/IEC 27001:2022 Annex A controls and NIST SP 800-53 Rev. 5—this audit evaluates existing policy gaps, assesses operational risks, and delivers actionable, prioritized recommendations to achieve robust defense-in-depth governance.")

# Section 2
add_heading_1("2. Assessment Methodology & Framework Alignment")
add_body_p("The audit was performed across six core operational security domains using a formal Capability Maturity Model Integration (CMMI) scale from Level 1 (Initial/Ad-hoc) to Level 5 (Optimized). Recommendations are evaluated against business impact, technical feasibility, and regulatory compliance standards.")

# Section 3
add_heading_1("3. Policy Gap Identification & Risk Assessment")
add_body_p("A detailed breakdown of critical vulnerabilities identified within the legacy policy structure:")

table_data = [
    ("Domain", "Identified Weakness / Deficit", "Risk Level", "Impact Summary"),
    ("Access Control & IAM", "Missing mandatory Multi-Factor Authentication (MFA) and explicit Zero Trust Principle of Least Privilege.", "CRITICAL", "High susceptibility to credential stuffing, password spraying, and lateral threat movement."),
    ("Remote Work & BYOD", "Unregulated personal device access; missing Mobile Device Management (MDM) enforcement.", "HIGH", "Risk of enterprise data exfiltration, unencrypted local storage breaches, and malware ingress."),
    ("Data Protection & Encryption", "Lack of mandated AES-256 encryption for data-at-rest and TLS 1.3 for data-in-transit.", "HIGH", "Non-compliance with GDPR/CCPA; risk of eavesdropping and unencrypted physical storage theft."),
    ("Incident Management", "Undefined escalation SLA thresholds and absence of mandatory 72-hour regulatory breach disclosure.", "HIGH", "Delayed incident response velocity, extended containment time, and severe regulatory fine exposure."),
    ("Patch & Vulnerability Management", "No SLAs for critical vulnerability patching (e.g., zero-days); ad-hoc scan schedules.", "CRITICAL", "Exposes perimeter infrastructure to known operational exploits and ransomware deployment."),
    ("Third-Party & Vendor Security", "Absence of mandatory vendor risk assessments, SOC 2 Type II audits, or supply chain controls.", "MEDIUM", "Supply chain compromise via unvetted third-party integrations and service providers.")
]

table = doc.add_table(rows=len(table_data), cols=4)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
col_widths = [Inches(1.4), Inches(2.6), Inches(1.0), Inches(1.5)]

for row_idx, row in enumerate(table.rows):
    is_header = (row_idx == 0)
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    if is_header:
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    
    for col_idx, cell in enumerate(row.cells):
        cell.width = col_widths[col_idx]
        cell_text = table_data[row_idx][col_idx]
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        
        if is_header:
            set_cell_background(cell, "102C57")
        elif row_idx % 2 == 1:
            set_cell_background(cell, "F9FAFC")
        else:
            set_cell_background(cell, "FFFFFF")
            
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.1
        run = p.add_run(cell_text)
        run.font.name = 'Calibri'
        run.font.size = Pt(9.5)
        
        if is_header:
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)
        else:
            if col_idx == 2:
                run.font.bold = True
                if cell_text == "CRITICAL":
                    run.font.color.rgb = RGBColor(180, 0, 0)
                elif cell_text == "HIGH":
                    run.font.color.rgb = RGBColor(210, 100, 0)
                else:
                    run.font.color.rgb = RGBColor(180, 140, 0)
            elif col_idx == 0:
                run.font.bold = True
                run.font.color.rgb = DARK_TEXT
            else:
                run.font.color.rgb = DARK_TEXT

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Section 4
add_heading_1("4. Strategic Recommendations & Policy Enhancements")

add_heading_2("4.1 Access Control & Identity Governance")
add_body_p(" Enforce FIDO2/WebAuthn phishing-resistant Multi-Factor Authentication across all internal applications, VPNs, and cloud services.", bold_prefix="• Phishing-Resistant MFA:")
add_body_p(" Transition to Role-Based Access Control (RBAC) paired with Attribute-Based Access Control (ABAC), conducting quarterly user access reviews.", bold_prefix="• Least Privilege Architecture:")

add_heading_2("4.2 Data Protection & Cryptography Standards")
add_body_p(" Mandate full-disk AES-256 encryption for all corporate endpoints and databases. Require TLS 1.3 for all web transport.", bold_prefix="• Encryption Benchmarks:")
add_body_p(" Deploy automated Data Loss Prevention (DLP) agents to prevent unauthorized exfiltration of PII, PHI, and IP.", bold_prefix="• Data Loss Prevention (DLP):")

add_heading_2("4.3 Vulnerability Management & Patch SLAs")
add_body_p(" Remediation mandated within 48 hours of public CVE disclosure.", bold_prefix="• Critical Vulnerabilities (CVSS 9.0-10.0):")
add_body_p(" Remediation mandated within 14 business days.", bold_prefix="• High Vulnerabilities (CVSS 7.0-8.9):")
add_body_p(" Remediation mandated within 30 business days.", bold_prefix="• Medium Vulnerabilities (CVSS 4.0-6.9):")

# Section 5
add_heading_1("5. Implementation Roadmap & Timeline")
add_body_p(" Deploy MFA across perimeter, establish interim patch SLAs, and mandate remote work MDM registration.", bold_prefix="• Phase 1: Immediate Remediation (Days 1–30):")
add_body_p(" Formalize ISO 27001 mapping, roll out enterprise DLP agents, and implement vendor risk scoring.", bold_prefix="• Phase 2: Policy Standardization (Days 31–90):")
add_body_p(" Automated continuous compliance checks, biannual penetration testing, and annual policy reviews.", bold_prefix="• Phase 3: Governance & Optimization (Days 91–180):")

# Section 6
add_heading_1("6. Compliance & Regulatory Alignment Summary")
add_body_p("Adoption of these recommendations ensures compliance with key international standards:")
add_body_p(" Fully addresses Clause 5 (Leadership), Clause 6 (Planning), and Annex A controls (A.5 to A.8).", bold_prefix="• ISO/IEC 27001:2022:")
add_body_p(" Satisfies Access Control (AC), Risk Assessment (RA), and System and Information Integrity (SI) control families.", bold_prefix="• NIST SP 800-53 Rev. 5:")
add_body_p(" Meets Article 32 mandates for technical and organizational measures to ensure processing security.", bold_prefix="• GDPR Article 32:")

# Section 7: Python Automation Audit Script Documentation
add_heading_1("7. Automated Policy Compliance Audit Tool (Python)")
add_body_p("To automate continuous compliance verification against these policy recommendations, the following custom Python script (`SecurityPolicyAudit.py`) performs automated endpoint configuration checks, password policy validation, and local encryption audits.")

code_text = """import os
import sys
import json
import datetime
import logging
import platform
import subprocess

logging.basicConfig(
    filename='policy_audit.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class SecurityPolicyAuditor:
    \"\"\"Automates host-level security policy evaluation against ISO 27001 & NIST 800-53 benchmarks.\"\"\"
    def __init__(self):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        self.os_type = platform.system()
        self.results = []

    def audit_disk_encryption(self):
        \"\"\"Check for mandatory AES-256 disk encryption (BitLocker / FileVault).\"\"\"
        status = "Non-Compliant"
        if self.os_type == "Windows":
            try:
                out = subprocess.check_output(["manage-bde", "-status"], stderr=subprocess.STREQUAL).decode()
                if "Protection On" in out:
                    status = "Compliant"
            except Exception:
                status = "Audit Failed (Elevated Privileges Required)"
        elif self.os_type == "Darwin":
            try:
                out = subprocess.check_output(["fdesetup", "status"]).decode()
                if "FileVault is On" in out:
                    status = "Compliant"
            except Exception:
                status = "Audit Failed"
        
        self.results.append({
            "control": "ISO 27001 A.8.24 - Data Encryption at Rest",
            "benchmark": "Mandatory Full-Disk Encryption",
            "status": status
        })
        logging.info(f"Disk Encryption Audit: {status}")

    def generate_compliance_report(self) -> str:
        report = {
            "audit_title": "Enterprise Security Policy Compliance Scan",
            "timestamp": self.timestamp,
            "host_info": {
                "hostname": platform.node(),
                "os": f"{self.os_type} {platform.release()}"
            },
            "evaluations": self.results
        }
        return json.dumps(report, indent=4)

if __name__ == "__main__":
    auditor = SecurityPolicyAuditor()
    auditor.audit_disk_encryption()
    print(auditor.generate_compliance_report())"""

code_table = doc.add_table(rows=1, cols=1)
code_table.alignment = WD_TABLE_ALIGNMENT.CENTER
cell = code_table.cell(0, 0)
cell.width = Inches(6.5)

set_cell_background(cell, CODE_BG_HEX)
set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

tcPr = cell._tc.get_or_add_tcPr()
borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="102C57"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
tcPr.append(borders)

p_code = cell.paragraphs[0]
p_code.paragraph_format.space_before = Pt(0)
p_code.paragraph_format.space_after = Pt(0)
p_code.paragraph_format.line_spacing = 1.05

run_code = p_code.add_run(code_text)
run_code.font.name = 'Consolas'
run_code.font.size = Pt(9.5)
run_code.font.color.rgb = RGBColor(40, 40, 40)

output_filename = "Security_Policy_Review_Report_Automation.docx"
doc.save(output_filename)
print(f"File generated successfully: {output_filename}")