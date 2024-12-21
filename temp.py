import speech_recognition as sr
from pydub import AudioSegment
from aeneas.executetask import ExecuteTask
from aeneas.task import Task
import os

def get_word_timestamps(audio_file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_file_path)
    duration = len(audio) / 1000.0  # total duration in seconds

    # Recognize the entire audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-IN')
        except sr.UnknownValueError:
            print("Could not understand audio")
            return []
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return []

    # Save the recognized text to a temporary file
    temp_text_path = "temp_text.txt"
    with open(temp_text_path, "w") as f:
        f.write(text)

    # Create aeneas task to align text with audio
    config_string = "task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = os.path.abspath(audio_file_path)
    task.text_file_path_absolute = os.path.abspath(temp_text_path)
    task.sync_map_file_path_absolute = os.path.abspath("temp_syncmap.json")

    # Execute the task
    ExecuteTask(task).execute()

    # Read the sync map
    word_timestamps = []
    with open(task.sync_map_file_path_absolute, "r") as f:
        sync_map = json.load(f)
        for fragment in sync_map["fragments"]:
            word_timestamps.append({
                "word": fragment["lines"][0],
                "start_time": float(fragment["begin"]),
                "duration": float(fragment["end"]) - float(fragment["begin"])
            })

    # Clean up temporary files
    os.remove(temp_text_path)
    os.remove(task.sync_map_file_path_absolute)

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