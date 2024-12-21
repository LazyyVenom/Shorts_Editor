import os
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

def remove_audio_from_video(input_video_path : str, output_video_path : str):
    video = VideoFileClip(input_video_path)
    video_without_audio = video.without_audio()

    # video_without_audio.write_videofile(output_video_path, codec="libx264")
    

def add_audio_to_video(video_path, audio_path, start_time):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path).set_start(start_time)
    
    new_audio = CompositeAudioClip([video.audio, audio])
    
    video_with_new_audio = video.set_audio(new_audio)

    return video_with_new_audio
    
    # video_with_new_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")