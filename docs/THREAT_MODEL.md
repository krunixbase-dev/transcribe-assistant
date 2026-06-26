# 🔐 Threat Model — transcribe-assistant

## 1. Overview

transcribe-assistant is an offline, low-latency speech-to-text engine designed for:

- privacy-sensitive environments  
- NGO and journalism workflows  
- offline and air‑gapped systems  
- automation and assistants  
- accessibility tools  

This threat model describes risks, assumptions, and mitigations for the **public (non-deterministic)** version.

The deterministic PRO version has an extended threat model (compliance, reproducibility, audit logs).

---

## 2. Security Assumptions

### Trusted:
- local machine hardware  
- local OS (not compromised)  
- local filesystem  
- local execution environment  

### Not trusted:
- external networks  
- cloud APIs  
- remote servers  
- browser environments  
- unverified plugins or extensions  

transcribe-assistant is designed to operate **without trusting any external service**.

---

## 3. Threat Categories

### 3.1 External Threats
- malware capturing microphone input  
- OS-level keyloggers or screen recorders  
- compromised system libraries  
- supply-chain attacks in dependencies  
- malicious Python packages  

### 3.2 Internal Threats
- user misconfiguration  
- insecure storage of transcripts  
- accidental exposure of audio files  
- running on an untrusted machine  

### 3.3 Environmental Threats
- physical access to device  
- shoulder surfing  
- theft of laptop or workstation  
- corrupted filesystem  

### 3.4 Model-Level Threats
- probabilistic output (non-deterministic)  
- timestamp drift  
- inconsistent segmentation  
- language auto-detection errors  

These are inherent to Whisper/Faster‑Whisper and not unique to this project.

---

## 4. Attack Vectors

### 4.1 OS Compromise
If the OS is compromised, an attacker may:

- capture audio before processing  
- read transcripts from disk  
- inject malicious dependencies  

**Mitigation:**  
transcribe-assistant assumes a trusted OS.  
Users should apply OS-level security (encryption, updates, anti-malware).

---

### 4.2 Network Exfiltration
Although the engine is offline, malware could:

- send transcripts to remote servers  
- capture microphone input  
- monitor local files  

**Mitigation:**  
- no network code in the engine  
- no cloud APIs  
- no telemetry  
- offline-only architecture  

---

### 4.3 Supply-Chain Attacks
Risk: malicious Python packages or tampered Whisper models.

**Mitigation:**  
- pinned dependencies  
- reproducible environment  
- local model loading  
- no dynamic remote downloads  

---

### 4.4 Data Exposure
Risk: transcripts stored unencrypted.

**Mitigation:**  
- user-controlled storage location  
- compatibility with OS-level encryption  
- no hidden caches  

---

## 5. Residual Risks

These risks cannot be fully eliminated in the public version:

- OS-level compromise  
- hardware keyloggers  
- malicious firmware  
- probabilistic model behavior  
- timestamp inconsistencies  
- non-deterministic output  

These are addressed in the **deterministic PRO version**.

---

## 6. Deterministic PRO Version (Extended Threat Model)

The PRO version introduces:

- deterministic audio windows  
- deterministic timestamp alignment  
- deterministic VAD  
- deterministic diarization  
- reproducible pipeline  
- audit-ready logs  
- compliance workflows  
- cryptographic session hashing  

This reduces:

- model-level uncertainty  
- timestamp drift  
- reproducibility issues  
- auditability gaps  

---

## 7. Mitigation Summary

| Threat | Mitigation |
|--------|------------|
| Network exfiltration | Offline-only architecture |
| Cloud dependency | No external APIs |
| Supply-chain | Pinned dependencies, local models |
| Data exposure | User-controlled storage, OS encryption |
| Timestamp drift | Addressed in PRO version |
| Non-determinism | Addressed in PRO version |
| OS compromise | Out of scope (user responsibility) |

---

## 8. Recommendations for Users

- run on a trusted machine  
- use disk encryption (BitLocker, LUKS, FileVault)  
- restrict access to transcript files  
- keep OS and Python updated  
- avoid installing untrusted packages  
- use air‑gapped mode for sensitive audio  

---

## 9. Reporting Security Issues

If you discover a vulnerability:

📧 **krunixbase@gmail.com**

Please include:

- description  
- reproduction steps  
- potential impact  
- environment details  

We respond promptly and responsibly.

