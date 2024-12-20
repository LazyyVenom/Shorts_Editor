import speech_recognition as sr

def recognize_hinglish_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-IN')
            return text
        except sr.UnknownValueError:
            return "Audio not clear"
        except sr.RequestError:
            return "Could not request results; check your network connection"

if __name__ == "__main__":
    audio_path = "input_audio.wav"
    recognized_text = recognize_hinglish_audio(audio_path)
    print("Recognized Text:", recognized_text)