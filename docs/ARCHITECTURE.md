# 🏗 Architecture — transcribe-assistant

## Overview
The engine is built around a low-latency streaming loop using Faster-Whisper.

## Structure

```
transcribe-assistant/
 ├── backend/
 │    ├── audio_buffer.py
 │    ├── live_transcriber.py
 │    └── whisper_engine.py
 ├── sessions/
 ├── output/
 ├── main.py
 ├── requirements.txt
 └── README.md
```

## Pipeline

Audio Input → Buffer → Whisper Engine → Tokens → Text → Session → Export

## Deterministic PRO Version
The deterministic version includes:

- fixed window sizes  
- deterministic timestamp alignment  
- deterministic VAD  
- deterministic diarization  
- reproducible pipeline  

This is part of the Krunixbase PRO ecosystem.

---
