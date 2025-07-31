from faster_whisper import WhisperModel
import gc

def transcribe_audio(file_path):
    """Transcribes the given audio file into text using the Whisper model."""
    # Load the Whisper model (tiny version) with CPU and int8 precision
    model = WhisperModel("tiny", device="cpu", compute_type="int8")

    # Transcribe the audio file and get the segments
    segments, _ = model.transcribe(file_path)

    # Combine all segment texts into a single string
    text = " ".join([seg.text for seg in segments])

    # Clean up model and free memory
    del model
    gc.collect()  # clear memory
    return text