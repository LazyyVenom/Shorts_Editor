import os
from moviepy import AudioFileClip, CompositeAudioClip

def remove_audio_from_video(video : str):
    video_without_audio = video.without_audio()

    return video_without_audio

    # video_without_audio.write_videofile(output_video_path, codec="libx264")
    

def add_audio_to_video(video: str, audio_path, start_time):
    audio = AudioFileClip(audio_path).set_start(start_time)
    
    new_audio = CompositeAudioClip([video.audio, audio])
    
    video_with_new_audio = video.set_audio(new_audio)

    return video_with_new_audio
    
    # video_with_new_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")