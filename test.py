import speech_recognition as sr
from googletrans import Translator
import moviepy.editor as mp
import os

class HinglishCaptioner:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()

    def extract_audio(self, video_path):
        """Extract audio from video file"""
        video = mp.VideoFileClip(video_path)
        audio_path = "extracted_audio.wav"
        video.audio.write_audiofile(audio_path)
        return audio_path

    def transcribe_audio(self, audio_path):
        """Transcribe Hinglish audio to text"""
        with sr.AudioFile(audio_path) as source:
            audio = self.recognizer.record(source)
            try:
                # Using Google's speech recognition for Hinglish
                transcript = self.recognizer.recognize_google(audio, language='hi-IN')
                return transcript
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError:
                print("Error with speech recognition service")
                return None

    def generate_short_caption(self, transcript, max_words=15):
        """Generate a short caption by translation and truncation"""
        if not transcript:
            return None
        
        # Translate to English if needed
        translation = self.translator.translate(transcript, dest='en').text
        
        # Truncate to max words
        words = translation.split()
        short_caption = ' '.join(words[:max_words])
        
        return short_caption + '...' if len(words) > max_words else short_caption

    def process_video(self, video_path):
        """Main method to process video and generate caption"""
        # Extract audio
        audio_path = self.extract_audio(video_path)
        
        # Transcribe audio
        transcript = self.transcribe_audio(audio_path)
        
        # Generate short caption
        short_caption = self.generate_short_caption(transcript)
        
        # Clean up temporary audio file
        os.remove(audio_path)
        
        return short_caption

# Example usage
def main():
    captioner = HinglishCaptioner()
    video_path = "input_video.mp4"  # Replace with your video path
    caption = captioner.process_video(video_path)
    print("Short Caption:", caption)

if __name__ == "__main__":
    main()

# Required dependencies:
# pip install SpeechRecognition
# pip install googletrans==3.1.0a0
# pip install moviepy