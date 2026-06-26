import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from audio_buffer import AudioBuffer

class LiveTranscriber:
    def __init__(self, model_size="small", device="cpu"):
        self.model = WhisperModel(model_size, device=device, compute_type="int8")
        self.buffer = AudioBuffer()
        self.samplerate = 16000
        self.block_size = int(self.samplerate * 0.5)  # 0.5s chunks

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        audio_bytes = indata.copy().tobytes()
        self.buffer.add_chunk(audio_bytes)

    def start(self):
        print("[INFO] Live transcription started...")
        with sd.InputStream(
            channels=1,
            samplerate=self.samplerate,
            callback=self.audio_callback
        ):
            while True:
                raw = self.buffer.get_all()
                if not raw:
                    continue

                audio_np = np.frombuffer(raw, dtype=np.float32)

                segments, _ = self.model.transcribe(audio_np, language="pl")
                for seg in segments:
                    print(">>", seg.text.strip())
