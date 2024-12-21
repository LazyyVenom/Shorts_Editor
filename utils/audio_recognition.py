import speech_recognition as sr
from pydub import AudioSegment

def get_word_timestamps(audio_file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_file_path)
    duration = len(audio) / 1000.0  # total duration in seconds

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-IN')
            words = text.split()
            word_durations = duration / len(words)  # average duration per word

            word_timestamps = []
            current_time = 0

            for word in words:
                word_timestamps.append({
                    "word": word,
                    "start_time": current_time,
                    "duration": word_durations
                })
                current_time += word_durations

            return word_timestamps

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results; check your network connection")

    return []

if __name__ == "__main__":
    audio_path = "input_audio.wav"
    word_timestamps = get_word_timestamps(audio_path)

    texts = [word_info['word'] for word_info in word_timestamps]
    start_times = [word_info['start_time'] for word_info in word_timestamps]
    durations = [word_info['duration'] for word_info in word_timestamps]

    for word_info in word_timestamps:
        print(f"Word: {word_info['word']}, Start Time: {word_info['start_time']:.2f} seconds, Duration: {word_info['duration']:.2f} seconds")

    print("Texts:", texts)
    print("Start Times:", start_times)
    print("Durations:", durations)