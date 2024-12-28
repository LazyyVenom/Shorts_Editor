import os
from moviepy import AudioFileClip, TextClip, CompositeVideoClip, VideoFileClip

def remove_audio_from_video(video):
    video_without_audio = video.without_audio()
    return video_without_audio


def add_audio_to_video(video: CompositeVideoClip, audio_path: str, start_time: float) -> CompositeVideoClip:
    audio = AudioFileClip(audio_path).with_start(start_time)
    video = video.with_audio(audio)
    return video

def get_video_duration(video):
    return video.duration

def get_audio_duration(audio):
    return audio.duration

def open_video(video_path):
    return VideoFileClip(video_path)

def crop_video(video, start_time, end_time):
    return video.subclipped(start_time, end_time)

def merge_videos(video1, video2):
    final_video = CompositeVideoClip([video1, video2.with_start(video1.duration)])
    return final_video

def add_days_to_video(video, days):
    text_clip = TextClip(
            font="static\Coolvetica Rg.otf",
            text=f"Day {days} / 100",
            font_size=90,
            color='black',
            size=video.size,
            duration=video. duration,
            text_align="center",
            margin=(None, 50),
            stroke_color="white",
            stroke_width=10,
            vertical_align="top",
        ).with_start(0)
    video_with_text = CompositeVideoClip([video, text_clip])
    return video_with_text