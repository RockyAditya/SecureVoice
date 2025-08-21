# model/voice_auth.py
import os
from utils.audio_processing import record_audio, reduce_noise, transcribe_audio
from utils.voice_match import match_voice, match_text
from utils.file_storage import save_user_profile, load_user_profile

class VoiceAuthenticator:
    def __init__(self, username="default_user"):
        self.username = username
        self.voice_path_enroll = "recordings/user_voice.wav"
        self.voice_path_auth = "recordings/auth_attempt.wav"

    def enroll_user(self, passphrase, log):
        if not passphrase.strip():
            log("⚠️ Please enter a passphrase.")
            return
        log("🎤 Recording voice for enrollment...")
        record_audio(self.voice_path_enroll)
        log("🔊 Reducing background noise...")
        reduce_noise(self.voice_path_enroll, self.voice_path_enroll)
        save_user_profile(self.username, passphrase, self.voice_path_enroll)
        log("✅ Enrollment successful! You can now authenticate.")

    def authenticate_user(self, passphrase, log):
        if not passphrase.strip():
            log("⚠️ Please enter your passphrase.")
            return
        user_data = load_user_profile(self.username)
        if not user_data:
            log("❌ No user enrolled. Please enroll first.")
            return
        log("🎤 Recording voice for authentication...")
        record_audio(self.voice_path_auth)
        log("🔊 Reducing background noise...")
        reduce_noise(self.voice_path_auth, self.voice_path_auth)
        log("🧠 Matching voice...")
        similarity, voice_ok = match_voice(self.voice_path_auth, user_data["voice_path"])
        log(f"🎙️ Voice match similarity: {similarity:.2f}")
        log("🧾 Matching passphrase...")
        spoken_text = transcribe_audio(self.voice_path_auth)
        log(f"🗣️ You said: {spoken_text}")
        text_ok = match_text(spoken_text, user_data["sentence"])
        if voice_ok and text_ok:
            log("✅ Authentication successful! 🎉")
        else:
            log("❌ Authentication failed. Please try again.")

########################################################################################################
