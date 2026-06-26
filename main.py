from backend.live_transcriber import LiveTranscriber
from backend.export_manager import ExportManager
from pathlib import Path
import json

def main():
    transcriber = LiveTranscriber()
    exporter = ExportManager()

    print("[INFO] Starting live transcription...")
    text, metadata, audio_bytes = transcriber.run_session()

    # Export transcript
    transcript_path = exporter.export_transcript(text)
    print(f"[EXPORT] Transcript saved to: {transcript_path}")

    # Export metadata
    metadata_path = exporter.export_metadata(metadata)
    print(f"[EXPORT] Metadata saved to: {metadata_path}")

    # Export audio (optional)
    if audio_bytes:
        audio_path = exporter.export_audio(audio_bytes)
        print(f"[EXPORT] Audio saved to: {audio_path}")

if __name__ == "__main__":
    main()
