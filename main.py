# main.py
import tkinter as tk
import threading
import os
from utils.audio_processing import record_audio, reduce_noise, transcribe_audio
from utils.voice_match import match_voice, match_text
from utils.file_storage import save_user_profile, load_user_profile

USERNAME = "default_user"
VOICE_PATH_ENROLL = "recordings/user_voice.wav"
VOICE_PATH_AUTH = "recordings/auth_attempt.wav"

# Logging to GUI
def log_message(message):
    log_text.configure(state='normal')
    log_text.insert(tk.END, message + '\n')
    log_text.see(tk.END)
    log_text.configure(state='disabled')

# Enroll process
def enroll():
    def process():
        passphrase = entry.get().strip()
        if not passphrase:
            log_message("⚠️ Please enter a passphrase.")
            return

        log_message("🎤 Recording voice for enrollment...")
        record_audio(VOICE_PATH_ENROLL)

        log_message("🔊 Reducing background noise...")
        reduce_noise(VOICE_PATH_ENROLL, VOICE_PATH_ENROLL)

        save_user_profile(USERNAME, passphrase, VOICE_PATH_ENROLL)
        log_message("✅ Enrollment successful! You can now authenticate.")

    threading.Thread(target=process).start()

# Authenticate process
def authenticate():
    def process():
        passphrase = entry.get().strip()
        if not passphrase:
            log_message("⚠️ Please enter your passphrase.")
            return

        user_data = load_user_profile(USERNAME)
        if not user_data:
            log_message("❌ No user enrolled. Please enroll first.")
            return

        log_message("🎤 Recording voice for authentication...")
        record_audio(VOICE_PATH_AUTH)

        log_message("🔊 Reducing background noise...")
        reduce_noise(VOICE_PATH_AUTH, VOICE_PATH_AUTH)

        log_message("🧠 Matching voice...")
        similarity, voice_ok = match_voice(VOICE_PATH_AUTH, user_data["voice_path"])
        log_message(f"🎙️ Voice match similarity: {similarity:.2f}")

        log_message("🧾 Matching passphrase...")
        spoken_text = transcribe_audio(VOICE_PATH_AUTH)
        log_message(f"🗣️ You said: {spoken_text}")
        text_ok = match_text(spoken_text, user_data["sentence"])

        if voice_ok and text_ok:
            log_message("✅ Authentication successful! 🎉")
        else:
            log_message("❌ Authentication failed. Please try again.")

    threading.Thread(target=process).start()

# GUI setup
root = tk.Tk()
root.title("🎙️ SecureVoice Authenticator")
root.geometry("440x400")
root.resizable(False, False)

tk.Label(root, text="Enter your passphrase:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Enroll", command=enroll, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Authenticate", command=authenticate, bg="#2196F3", fg="white").pack(pady=5)

log_text = tk.Text(root, height=15, width=55, state='disabled', bg="#F0F0F0")
log_text.pack(pady=10)

root.mainloop()

####################################################################################################3
###################################################################################################33

