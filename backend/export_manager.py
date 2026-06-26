import json
from pathlib import Path
from datetime import datetime

class ExportManager:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def _timestamp(self):
        return datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

    def export_transcript(self, text: str):
        """Save transcript.txt to output/"""
        filename = f"transcript_{self._timestamp()}.txt"
        path = self.output_dir / filename

        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

        return str(path)

    def export_metadata(self, metadata: dict):
        """Save metadata.json to output/"""
        filename = f"metadata_{self._timestamp()}.json"
        path = self.output_dir / filename

        with open(path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        return str(path)

    def export_audio(self, audio_bytes: bytes):
        """Save audio.wav to output/"""
        filename = f"audio_{self._timestamp()}.wav"
        path = self.output_dir / filename

        with open(path, "wb") as f:
            f.write(audio_bytes)

        return str(path)
