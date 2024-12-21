from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from typing import List


class AddCaptions:
    def __init__(
        self,
        video_path: str,
        texts: List[str],
        start_times: List[int],
        durations: List[int],
        font_size: int = 50,
        font: str = "static\Coolvetica Rg.otf",
    ):
        self.video = VideoFileClip(filename=video_path)
        self.font = font
        self.font_size = font_size
        self.texts = texts
        self.start_times = start_times
        self.durations = durations

    def add_captions(self, output_path: str):
        clips = [self.video]
        for text, start_time, duration in zip(
            self.texts, self.start_times, self.durations
        ):
            text_clip = TextClip(
                font=self.font,
                text=text,
                font_size=self.font_size,
                color="white",
                method="caption",
                size=self.video.size,
                duration=duration,
                text_align="center",
            ).with_start(start_time)
            clips.append(text_clip)

        video_with_text = CompositeVideoClip(clips)
        video_with_text.write_videofile(
            output_path, codec="libx264", fps=self.video.fps
        )


if __name__ == "__main__":
    video_path = "input_video.mp4"
    texts = [
        "hello",
        "to",
        "aaj",
        "ke",
        "din",
        "speech",
        "recognition",
        "Nahin",
        "kam",
        "Kiya",
        "Taki",
        "short",
        "editing",
        "Aasan",
        "ho",
        "sakeshort",
        "editing",
        "Aasan",
        "ho",
        "sake",
        "aur",
        "to",
        "Aaj",
    ]
    start_times = [
        0,
        0.2578,
        0.5156,
        0.7733999999999999,
        1.0312,
        1.289,
        1.8445,
        2.4,
        2.7236666666666665,
        3.047333333333333,
        3.3709999999999996,
        3.7757142857142854,
        4.180428571428571,
        4.5851428571428565,
        4.989857142857142,
        5.394571428571427,
        5.799285714285713,
        6.203999999999998,
        6.701499999999998,
    ]
    durations = [
        0.2578,
        0.2578,
        0.2578,
        0.2578,
        0.2578,
        0.5555,
        0.5555,
        0.32366666666666666,
        0.32366666666666666,
        0.32366666666666666,
        0.40471428571428575,
        0.40471428571428575,
        0.40471428571428575,
        0.40471428571428575,
        0.40471428571428575,
        0.40471428571428575,
        0.40471428571428575,
        0.4975,
        0.4975,
    ]

    add_captions = AddCaptions(video_path, texts, start_times, durations)
    add_captions.add_captions("output_video.mp4")
