import os
from moviepy import AudioFileClip, CompositeAudioClip, CompositeVideoClip

def remove_audio_from_video(video):
    video_without_audio = video.without_audio()

    return video_without_audio


def add_audio_to_video(video: CompositeVideoClip, audio_path: str, start_time: float) -> CompositeVideoClip:
    audio = AudioFileClip(audio_path).with_start(start_time)
    
    if video.audio is None:
        video = video.with_audio(audio)
        return video
    
    new_audio = CompositeAudioClip([video.audio, audio])
    
    video_with_new_audio = video.with_audio(new_audio)

    return video_with_new_audio