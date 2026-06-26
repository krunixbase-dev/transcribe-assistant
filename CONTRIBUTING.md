# 🤝 Contributing to transcribe-assistant

Thank you for your interest in contributing to **transcribe-assistant** — an offline, low-latency speech-to-text engine built for automation workflows, assistants, accessibility tools and privacy‑sensitive environments.

This document describes how to contribute, how branches are organized, how to propose changes, and how to maintain code quality.

---

## 📌 Branch Model

transcribe-assistant uses a structured Git workflow:

### Main branches
- **main** — stable, production-ready code  
- **dev** — active development branch

### Working branches
- **feature/<name>** — new features  
  Example: `feature/websocket-streaming`  
  **Learn more**

- **fix/<name>** — bug fixes  
  Example: `fix/timestamp-drift`  
  **Learn more**

- **hotfix/<name>** — urgent production fixes  
  Example: `hotfix/startup-crash`  
  **Learn more**

- **release/<version>** — preparing a new release  
  Example: `release/v1.0.0`  
  **Learn more**

---

## 🧩 How to Contribute

### 1. Fork the repository
Create your own fork and clone it locally.

### 2. Create a working branch
Use one of the recommended formats:

```
feature/<name>
fix/<name>
docs/<name>
hotfix/<name>
release/<version>
```

### 3. Make your changes
Follow the coding guidelines and commit style described below.

### 4. Submit a Pull Request
- PRs should target **dev**, not main  
- Keep PRs small and focused  
- Include a clear description of the change  
- Reference related issues if applicable  

---

## 🧪 Commit Style

Use the conventional commit format:

```
type(scope): message
```

### Allowed types
- **feat:** new feature  
- **fix:** bug fix  
- **docs:** documentation  
- **refactor:** code restructuring  
- **perf:** performance improvements  
- **chore:** maintenance tasks  

### Examples
```
feat(vad): add voice activity detection module
fix(latency): reduce inference delay by 40ms
docs(api): update streaming API section
```

---

## 🧱 Code Quality Guidelines

- Keep functions small and modular  
- Avoid unnecessary dependencies  
- Use type hints where possible  
- Document public functions and modules  
- Ensure code runs offline (no network calls)  
- Follow the project’s architecture conventions  
  **Architecture**

---

## 🔐 Security & Privacy

transcribe-assistant is an offline, privacy-first engine.  
Contributions must respect:

- zero telemetry  
- no cloud dependencies  
- local-only inference  
- transparent, auditable code  

Relevant documents:

- **Security Policy**  
- **Threat Model**  
- **Attack Surface**  

---

## 🧭 Documentation

All documentation lives in the `docs/` folder.

If your PR changes behavior, update:

- **docs/usage.md**  
- **docs/api.md**  
- **docs/architecture.md**  

---

## 🧪 Testing

Before submitting a PR:

- test your changes locally  
- ensure no regressions in latency  
- verify offline behavior  
- check that transcripts export correctly  

---

## 🗣️ Communication

If you want to propose a major change:

1. Open an Issue  
2. Describe the motivation  
3. Provide a minimal design proposal  
4. Wait for discussion before implementing  

---

## 📦 Releases

Releases follow semantic versioning:

```
MAJOR.MINOR.PATCH
```

Release branches:

```
release/v1.0.0
release/v1.1.0
```

Each release includes:

- changelog  
- version bump  
- tag  
- updated docs  

---

## ❤️ Thank You

Your contributions help make transcribe-assistant a powerful, privacy‑first tool for real-time transcription.


---
