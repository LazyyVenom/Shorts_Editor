import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

def get_word_timestamps(audio_file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_file_path)
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

    word_timestamps = []
    current_time = 0

    for chunk in chunks:
        chunk_duration = len(chunk) / 1000.0
        with sr.AudioFile(chunk.export(format="wav")) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language='en-IN')
                words = text.split()
                for word in words:
                    word_duration = chunk_duration / len(words)
                    word_timestamps.append({
                        "word": word,
                        "start_time": current_time,
                        "duration": word_duration
                    })
                    current_time += word_duration
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("Could not request results; check your network connection")

    return word_timestamps

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