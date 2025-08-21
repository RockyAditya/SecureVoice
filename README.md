# SecureVoice: Dual-Factor Voice and Sentence-Based Authenticator

## 📌 Project Overview
SecureVoice is a Python-based authentication system that verifies users using both **voice identity** and **spoken sentence matching**.  
It provides an additional layer of security by ensuring that only the right person speaking the right passphrase is granted access.  

## 🚀 Features
- User registration with voice sample and chosen passphrase  
- Authentication using both voice similarity and sentence verification  
- GUI built with **Tkinter** for easy interaction  
- Audio recording and processing using **SpeechRecognition** and **Resemblyzer**  
- User data management with **MySQL**  

## 🛠️ Tech Stack
- **Languages**: Python  
- **Libraries**: Tkinter, SpeechRecognition, Resemblyzer  
- **Database**: MySQL  

## 🔑 Process
1. User enrolls by recording their voice and setting a passphrase.  
2. System stores both the voice embedding and the passphrase in the database.  
3. During login, the user speaks the passphrase.  
4. System checks both:
   - Voice similarity against stored voice embedding.  
   - Sentence match against stored passphrase.  
5. Access is granted only if both checks succeed.  

## 📂 Project Structure
SecureVoice/
│── main.py # GUI entry point
│── model/
│ └── voice_auth.py # Core authentication logic
│── utils/
│ ├── audio_processing.py
│ ├── file_storage.py
│ └── voice_match.py
│── recordings/ # Stored user audio samples
│── user_data/ # User profile data
│── requirements.txt
│── README.md


## 📖 Setup Instructions
1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/SecureVoice.git
   cd SecureVoice
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app
   ```bash
   python main.py
  
