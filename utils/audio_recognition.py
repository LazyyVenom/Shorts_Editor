import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import io
from faster_whisper import WhisperModel
from typing import List

def detect_leading_silence(sound, silence_threshold=-40.0, chunk_size=10):
    trim_ms = 0

    assert chunk_size > 0
    while trim_ms < len(sound) and sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size

    return trim_ms

def get_word_timestamps(audio_file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_file_path)
    
    leading_silence_duration = detect_leading_silence(audio) / 1000.0
    current_time = leading_silence_duration

    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40, keep_silence=500)

    word_timestamps = []

    for chunk in chunks:
        chunk_duration = len(chunk) / 1000.0
        chunk_leading_silence_duration = detect_leading_silence(chunk) / 1000.0  # duration in seconds
        current_time += chunk_leading_silence_duration

        with io.BytesIO() as wav_buffer:
            chunk.export(wav_buffer, format="wav")
            wav_buffer.seek(0)
            with sr.AudioFile(wav_buffer) as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data, language='en-IN')
                    words = text.split()
                    for word in words:
                        word_duration = (chunk_duration - chunk_leading_silence_duration) / len(words)
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

model_size = "medium"
model = WhisperModel(model_size, device='cpu')

def get_word_timestamps_faster_whisper(audio_file_path):
    segments, info = model.transcribe(audio_file_path, language='hi', word_timestamps=True)
    segments = list(segments)
    for segment in segments:
        for word in segment.words:
            print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))

    wordlevel_info = []

    for segment in segments:
        for word in segment.words:
            wordlevel_info.append({'word':word.word,'start':word.start,'end':word.end})

    return wordlevel_info

def hindi_to_hinglish(captions : List[str]) -> List[str]:
    return text


if __name__ == "__main__":
    # audio_path = "temp_processing.wav"
    # word_timestamps = get_word_timestamps(audio_path)

    # texts = [word_info['word'] for word_info in word_timestamps]
    # start_times = [word_info['start_time'] for word_info in word_timestamps]
    # durations = [word_info['duration'] for word_info in word_timestamps]

    # for word_info in word_timestamps:
    #     print(f"Word: {word_info['word']}, Start Time: {word_info['start_time']:.2f} seconds, Duration: {word_info['duration']:.2f} seconds")

    # print("Texts:", texts)
    # print("Start Times:", start_times)
    # print("Durations:", durations)

    print(get_word_timestamps_faster_whisper("input_audio.wav"))