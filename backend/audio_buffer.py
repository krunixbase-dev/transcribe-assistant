import threading
from collections import deque

class AudioBuffer:
    def __init__(self, max_chunks=50):
        self.buffer = deque(maxlen=max_chunks)
        self.lock = threading.Lock()

    def add_chunk(self, chunk: bytes):
        """Add raw audio bytes to the buffer."""
        with self.lock:
            self.buffer.append(chunk)

    def get_all(self) -> bytes:
        """Return all buffered audio and clear the buffer."""
        with self.lock:
            data = b"".join(self.buffer)
            self.buffer.clear()
            return data

    def clear(self):
        """Clear buffer manually."""
        with self.lock:
            self.buffer.clear()
