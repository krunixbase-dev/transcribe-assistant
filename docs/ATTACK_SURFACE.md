# 🎯 Attack Surface — transcribe-assistant

This document describes the attack surface of the **public (non-deterministic)** version of transcribe-assistant.  
The deterministic PRO version has an extended, hardened attack surface (see bottom section).

---

## 1. Overview

transcribe-assistant is an **offline**, **local-only**, **zero-telemetry** speech-to-text engine.  
Its attack surface is intentionally minimal:

- no network stack  
- no cloud APIs  
- no remote calls  
- no telemetry  
- no background services  

The only meaningful attack vectors come from the **local environment**, not the application itself.

---

## 2. Attack Surface Summary

| Component | Exposure | Notes |
|----------|----------|-------|
| Audio Input | Medium | Microphone access; OS-level risk |
| Local Filesystem | Medium | Transcript storage; user-controlled |
| Python Runtime | Medium | Dependency integrity; supply-chain risk |
| Whisper Model | Low | Loaded locally; no remote calls |
| Network | **None** | No outbound or inbound connections |
| Cloud APIs | **None** | No integration with OpenAI/Google/Azure |
| Telemetry | **None** | No analytics, no tracking |
| UI / API | Low | Local-only; no remote endpoints |

---

## 3. Detailed Attack Vectors

### 3.1 Microphone Access (OS-Level)
**Vector:**  
Malware or compromised OS capturing raw audio before transcribe-assistant processes it.

**Mitigation:**  
- transcribe-assistant does not elevate microphone permissions  
- relies on OS security model  
- users should run on trusted machines  

---

### 3.2 Local Filesystem Exposure
**Vector:**  
Transcripts stored unencrypted could be accessed by:

- other local users  
- malware  
- backup sync services  

**Mitigation:**  
- user-controlled storage path  
- compatible with OS-level encryption (BitLocker, LUKS, FileVault)  
- no hidden caches  

---

### 3.3 Dependency Supply-Chain
**Vector:**  
Malicious Python packages or tampered Whisper models.

**Mitigation:**  
- pinned versions in `requirements.txt`  
- local model loading  
- no dynamic downloads  
- reproducible environments recommended  

---

### 3.4 Malicious Plugins / Integrations
**Vector:**  
If a user integrates transcribe-assistant into a larger system, insecure code may introduce:

- network exfiltration  
- remote execution  
- privilege escalation  

**Mitigation:**  
- core engine has no network code  
- integrations must document their own threat model  

---

### 3.5 OS Compromise
**Vector:**  
If the OS is compromised, an attacker can:

- read transcripts  
- capture audio  
- modify dependencies  
- inject malicious code  

**Mitigation:**  
Out of scope — transcribe-assistant assumes a trusted OS.

---

### 3.6 Model-Level Risks (Whisper/Faster-Whisper)
**Vector:**  
- probabilistic output  
- timestamp drift  
- segmentation inconsistencies  

**Mitigation:**  
- acceptable for public version  
- fully addressed in deterministic PRO version  

---

## 4. What transcribe-assistant *does not* expose

### ❌ No network ports  
### ❌ No HTTP server  
### ❌ No WebSocket server  
### ❌ No cloud API keys  
### ❌ No telemetry  
### ❌ No remote logging  
### ❌ No background daemons  
### ❌ No auto-update mechanism  

This dramatically reduces the attack surface compared to cloud-based ASR tools.

---

## 5. Out-of-Scope Threats

- compromised OS or hardware  
- physical access attacks  
- firmware-level attacks  
- malicious microphones  
- kernel-level keyloggers  
- hypervisor compromise  

These are outside the responsibility of the application.

---

## 6. Attack Surface — Deterministic PRO Version

The PRO version introduces:

- deterministic audio windows  
- deterministic timestamp alignment  
- deterministic diarization  
- deterministic VAD  
- reproducible pipeline  
- cryptographic session hashing  
- audit-ready logs  
- hardened mode (optional)  

This reduces:

- model-level uncertainty  
- reproducibility issues  
- timestamp drift  
- auditability gaps  

And adds:

- compliance-grade security  
- forensic integrity  
- tamper-evident logs  

---

## 7. Recommendations for Users

- run on a trusted OS  
- enable full-disk encryption  
- restrict access to transcript files  
- avoid untrusted Python packages  
- use air-gapped mode for sensitive audio  
- keep OS and dependencies updated  

---

## 8. Reporting Security Issues

📧 **krunixbase@gmail.com**

Please include:

- description  
- reproduction steps  
- environment  
- potential impact  

We respond promptly and responsibly.
