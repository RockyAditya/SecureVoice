# utils/audio_processing.py
import sounddevice as sd
import wave
import noisereduce as nr
import soundfile as sf
import speech_recognition as sr

def record_audio(filepath, duration=5, sample_rate=44100):
    print(f"Recording {duration}s to {filepath}...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    with wave.open(filepath, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())

def reduce_noise(input_path, output_path):
    data, rate = sf.read(input_path)
    reduced = nr.reduce_noise(y=data, sr=rate)
    sf.write(output_path, reduced, rate)

def transcribe_audio(filepath):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filepath) as src:
        audio = recognizer.record(src)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

#################################################################################################

