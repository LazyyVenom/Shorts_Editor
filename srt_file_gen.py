from faster_whisper import WhisperModel


def generate_srt(audio_file_path: str, output_srt_path: str, model) -> None:
    segments, info = model.transcribe(
        audio_file_path, language="en", word_timestamps=True
    )
    segments = list(segments)

    subtitle_index = 1
    srt_lines = []

    for segment in segments:
        for word in segment.words:
            start_time = word.start
            end_time = word.end
            text = word.word

            start_srt_time = format_srt_time(start_time)
            end_srt_time = format_srt_time(end_time)

            srt_lines.append(
                f"{subtitle_index}\n{start_srt_time} --> {end_srt_time}\n{text}\n"
            )
            subtitle_index += 1

    with open(output_srt_path, "w", encoding="utf-8") as srt_file:
        srt_file.writelines(srt_lines)


def format_srt_time(seconds: float) -> str:
    milliseconds = int((seconds % 1) * 1000)
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


# Example usage:
model_size = "medium"
model = WhisperModel(model_size, device="cpu")

generate_srt(
    r"C:\Users\Anubhav Choubey\AppData\Local\CapCut\Videos\Day6.WAV",
    r"C:\Users\Anubhav Choubey\Downloads\output_subtitles.srt",
    model,
)
