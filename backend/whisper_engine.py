from faster_whisper import WhisperModel
from pathlib import Path

class FasterWhisperEngine:
    def __init__(self, model_size="small", device="cpu", compute_type="int8"):
        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type
        )

    def transcribe(self, audio_path: Path):
        """Transcribe an audio file and return plain text."""
        segments, info = self.model.transcribe(str(audio_path))

        text = "\n".join(seg.text.strip() for seg in segments)
        return text
