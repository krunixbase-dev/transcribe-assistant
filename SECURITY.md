# 🔐 Security Policy — transcribe-assistant

## 1. Overview

transcribe-assistant is an offline, low-latency speech-to-text engine.  
Security and privacy are core design principles:

- no cloud APIs  
- no external telemetry  
- local-only processing  
- audit-ready sessions (PRO roadmap)

---

## 2. Data Flow & Privacy

- All audio is processed **locally** on the user’s machine.
- No audio, transcripts, or metadata are sent to:
  - OpenAI
  - Google Cloud
  - Azure
  - any third-party API or service.
- No tracking, analytics, or telemetry are embedded in the engine.

**Conclusion:**  
All data stays on the device where transcribe-assistant is running.

---

## 3. Dependencies & Model

- The engine uses **Faster-Whisper** as a local ASR backend.
- Models are loaded from disk and executed locally.
- No remote model calls are performed.

Users are encouraged to:

- review dependencies in `requirements.txt`
- pin versions for reproducibility

---

## 4. Storage & Sessions

- Transcription sessions may be stored locally as:
  - text files (TXT)
  - structured data (JSON)
- Storage location is configurable.
- Users are responsible for:
  - filesystem-level access control
  - encryption at rest (if required)
  - backup policies

---

## 5. Network Usage

By default:

- transcribe-assistant does **not** require internet access.
- no outbound connections are made by the core engine.

If you integrate transcribe-assistant into a larger system (API, SaaS):

- you must document your own network and security model.
- this repo does **not** include any cloud integration by default.

---

## 6. Threat Model (High-Level)

transcribe-assistant is designed for:

- offline environments
- sensitive audio (NGO, legal, medical, journalism)
- systems where cloud-based ASR is not acceptable

Primary protections:

- no external data exfiltration
- local-only processing
- transparent, inspectable open-source code

---

## 7. Deterministic PRO Version (Roadmap)

The planned deterministic PRO engine will add:

- reproducible pipelines
- deterministic timestamp alignment
- audit-ready logs
- compliance-focused workflows

These features are intended for:

- regulated environments
- forensics
- legal and compliance use cases

---

## 8. Reporting Vulnerabilities

If you discover a security issue:

- please contact: **krunixbase@gmail.com**
- include:
  - description of the issue
  - steps to reproduce
  - potential impact

We aim to:

- acknowledge reports promptly
- provide fixes in a reasonable timeframe
- document security-relevant changes in release notes

---

## 9. Best Practices for Users

We recommend:

- running transcribe-assistant on trusted machines
- using up-to-date OS and security patches
- restricting access to stored transcripts
- using disk encryption where appropriate

---

## 10. Disclaimer

transcribe-assistant is provided “as is”, under the MIT License.  
Security in production environments depends on:

- your infrastructure
- your OS configuration
- your access control and policies

Always review and adapt this tool to your specific threat model.
