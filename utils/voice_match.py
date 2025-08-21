# utils/voice_match.py
from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import os
import speech_recognition as sr

encoder = VoiceEncoder()

def get_embedding(audio_path):
    wav = preprocess_wav(audio_path)
    return encoder.embed_utterance(wav)

def compare_voices(path1, path2, threshold=0.75):
    emb1 = get_embedding(path1)
    emb2 = get_embedding(path2)
    sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    return sim, sim >= threshold

# ✅ Add this:
def match_text(spoken_text, expected_text):
    if expected_text is None:
        print("[ERROR] No passphrase found for user.")
        return False  # or raise an exception if needed
    return spoken_text.strip().lower() == expected_text.strip().lower()


def match_text(spoken_text, expected_text):
    return spoken_text.strip().lower() == expected_text.strip().lower()

def match_voice(path1, path2, threshold=0.75):
    return compare_voices(path1, path2, threshold)

#######################################################################################################
