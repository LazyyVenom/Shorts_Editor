# Required Libraries

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
        for text, start_time, duration in zip(self.texts, self.start_times, self.durations):
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
        video_with_text.write_videofile(output_path, codec="libx264", fps=self.video.fps)


# Example usage
video_path = "input_video.mp4"
texts = ["Sample Caption 1", "Sample Caption 2"]
start_times = [0, 5]
durations = [2, 3]

add_captions = AddCaptions(video_path, texts, start_times, durations)
add_captions.add_captions("output_video.mp4")
