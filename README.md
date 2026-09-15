# Enterprise Security Policy Review & Audit Framework

![ISO 27001](https://img.shields.io/badge/Alignment-ISO%2FIEC%2027001%3A2022-blue)
![NIST SP 800-53](https://img.shields.io/badge/Alignment-NIST%20SP%20800--53%20Rev.%205-navy)
![License](https://img.shields.io/badge/License-MIT-green)

## Executive Summary
This project delivers a formal gap analysis and strategic remediation framework for an enterprise Information Security Policy. Built upon **ISO/IEC 27001:2022** and **NIST SP 800-53 Rev. 5** standards, it bridges executive governance with hands-on technical automation.

The repository includes both a comprehensive Word document report (`Security_Policy_Review_Report_Automation.docx`) evaluating policy weaknesses and an automated Python compliance verification tool (`SecurityPolicyReview.py`).

## Key Assessment Domains
The audit evaluates legacy policy deficits and provides prioritized recommendations across six core domains:

1. **Access Control & Identity Governance (IAM):** Mandates FIDO2/WebAuthn phishing-resistant Multi-Factor Authentication (MFA) and Zero Trust Least Privilege.
2. **Remote Work & BYOD:** Enforces mandatory Mobile Device Management (MDM) enrollment and isolated network tunneling.
3. **Data Protection & Cryptography:** Sets minimum baselines of AES-256 for data-at-rest and TLS 1.3 for data-in-transit, paired with Data Loss Prevention (DLP) agents.
4. **Patch & Vulnerability Management:** Establishes strict CVSS-based SLAs (48-hour remediation window for critical zero-days).
5. **Incident Management:** Introduces mandatory escalation SLA thresholds and 72-hour statutory breach reporting timelines.
6. **Third-Party & Vendor Security:** Integrates mandatory vendor risk scoring and SOC 2 Type II audit verifications.

## Technical Audit Automation Script

The included script (`SecurityPolicyReview.py`) programmatically evaluates host compliance against policy baselines and generates structured JSON audit logs.

### Features
* **Full-Disk Encryption Audit:** Scans host platforms for active BitLocker (Windows) or FileVault (macOS) state.
* **Structured Manifest Export:** Outputs standard audit JSON manifests suitable for SIEM ingestion.
* **Audit Trail Logging:** Appends continuous evaluation telemetry to `policy_audit.log`.

### Execution
Run the compliance audit script locally:

```bash
python SecurityPolicyReview.py

### Example JSON Output

```json
{
    "audit_title": "Enterprise Security Policy Compliance Scan",
    "timestamp": "2026-09-15T12:00:00Z",
    "host_info": {
        "hostname": "SEC-AUDIT-HOST",
        "os": "Windows 11"
    },
    "evaluations": [
        {
            "control": "ISO 27001 A.8.24 - Data Encryption at Rest",
            "benchmark": "Mandatory Full-Disk Encryption",
            "status": "Compliant"
        }
    ]
}


## Deliverables & Repository Structure

```text
.
├── Security_Policy_Review_Report_Automation.docx  # Final Executive Report (DOCX)
├── SecurityPolicyReview.py                        # Automated Compliance Auditor
├── policy_audit.log                               # Audit Execution Output Log
└── README.md                                      # Repository Documentation

## Implementation Roadmap

* **Phase 1 (Days 1–30):** Perimeter MFA deployment, MDM enforcement, and emergency zero-day patch SLAs.
* **Phase 2 (Days 31–90):** Enterprise DLP agent rollout, vendor risk matrix integration, and ISO 27001 mapping.
* **Phase 3 (Days 91–180):** Automated continuous compliance scans, annual tabletop exercises, and penetration testing.
