from backend.live_transcriber import LiveTranscriber
from backend.export_manager import ExportManager
from datetime import datetime

def main():
    transcriber = LiveTranscriber()
    exporter = ExportManager()

    print("[INFO] Starting live transcription...")

    # Start transcription loop
    # (minimal version prints text live)
    # After stopping, we export the final transcript

    try:
        transcriber.start()
    except KeyboardInterrupt:
        print("\n[INFO] Stopping transcription...")

    # Build transcript text from collected segments
    text = "\n".join(transcriber.collected_segments)

    # Prepare metadata
    metadata = {
        "session_id": datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S"),
        "model": transcriber.model_size,
        "language": "pl",
        "samplerate": transcriber.samplerate,
        "duration_seconds": transcriber.total_duration
    }

    # Export transcript
    transcript_path = exporter.export_transcript(text)
    print(f"[EXPORT] Transcript saved to: {transcript_path}")

    # Export metadata
    metadata_path = exporter.export_metadata(metadata)
    print(f"[EXPORT] Metadata saved to: {metadata_path}")

if __name__ == "__main__":
    main()

