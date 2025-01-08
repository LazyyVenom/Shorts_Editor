from utils import add_captions as capt
from utils import audio_recognition as reco
from utils import audio_utils as audio_utils
import streamlit as st
from utils import video_utils
from faster_whisper import WhisperModel
import os
from moviepy import AudioFileClip, CompositeVideoClip, VideoFileClip
from utils.vfx_utils import overlay_transparent_video

def get_video_segment(video_path_label):
    video_path = st.text_input(f"Enter the Path of the {video_path_label} video")
    video_path = video_path.replace('"', "")
    start_time = 0.0
    end_time = 0.0

    if os.path.exists(video_path):
        video = video_utils.open_video(video_path)
        video_duration = video_utils.get_video_duration(video)
        video.close()

        st.write("Cropping Section")
        start_time, end_time = st.slider(
            f"Select the start and end time of the {video_path_label} video",
            0.0,
            video_duration,
            (0.0, video_duration),
        )

        if start_time < end_time:
            st.write(f"Selected video segment from {start_time} to {end_time}")
        else:
            st.write("Error: Start time must be less than end time")

        st.video(video_path, start_time=start_time, end_time=end_time)
    else:
        st.write(f"The file doesn't exist: {video_path}")

    return video_path, start_time, end_time


st.title("Video Captioning")
st.write(
    "This is a simple web app to add captions to a video based on the audio of the video."
)

day_count = st.text_input("Enter the day count")
day_count = int(day_count) if day_count.isnumeric() else 0

with st.expander("Primary Video"):
    primary_video_path, primary_start_time, primary_end_time = get_video_segment(
        "primary"
    )

with st.expander("Secondary Video"):
    secondary_video_path, secondary_start_time, secondary_end_time = get_video_segment(
        "secondary"
    )

with st.expander("Audio File"):
    audio_file = st.text_input("Enter the Path of the audio file")
    audio_file = audio_file.replace('"', "")

    if os.path.exists(audio_file):
        audio_duration = audio_utils.get_audio_duration(audio_file)

        st.write("Cropping Section for Audio File")
        audio_start_time, audio_end_time = st.slider(
            "Select the start and end time of the audio file",
            0.0,
            audio_duration,
            (0.0, audio_duration),
        )

        if audio_start_time < audio_end_time:
            st.write(
                f"Selected audio segment from {audio_start_time} to {audio_end_time}"
            )
            st.audio(audio_file, start_time=audio_start_time, end_time=audio_end_time)
        else:
            st.write("Error: Start time must be less than end time")

    else:
        st.write(f"The file doesn't exist: {audio_file}")

# Audio Processing Stuff Here
if st.button("Start Processing"):
    # audio_file = audio_utils.reduce_noise(audio_file, "temp_processing.wav")
    # audio_utils.audio_speed_increase(audio_file, "temp_processing.wav", 1)
    # audio_duration = audio_utils.get_audio_duration("temp_processing.wav")

    # Video Processing Stuff Here
    primary_video = video_utils.open_video(primary_video_path)
    primary_video_path = video_utils.crop_video(
        primary_video, primary_start_time, primary_end_time
    )

    if len(secondary_video_path) > 0:
        secondary_video = video_utils.open_video(secondary_video_path)
        secondary_video_path = video_utils.crop_video(
            secondary_video, secondary_start_time, secondary_end_time
        )

        video = video_utils.merge_videos(primary_video_path, secondary_video)

    else:
        video = primary_video

    # Audio Recognition Stuff Here
    model_size = "medium"
    model = WhisperModel(model_size, device='cpu')
    word_timestamps = reco.get_word_timestamps_faster_whisper(audio_file, model=model)

    # Captioning Stuff Here
    captions = [word_info['word'] for word_info in word_timestamps]
    captions = list(map(str.upper, captions))
    captions = list(map(str.strip, captions))

    print('------------------------------------------------------------')
    print(captions)
    print('------------------------------------------------------------')
    
    start_times = [word_info['start'] for word_info in word_timestamps]
    durations = [word_info['end'] - word_info['start'] for word_info in word_timestamps]
 
    # input_hinglish_captions = input("Enter the hinglish captions: ")

    # captions = input_hinglish_captions.split(",")

    # captions = list(map(str.upper, captions))

    video : CompositeVideoClip | VideoFileClip = video_utils.crop_video(video, 0, audio_duration)
 
    video = capt.add_captions(video, captions, start_times, durations)
    # video = video_utils.add_days_to_video(video, day_count)

    # video = overlay_transparent_video(video, r"static\videos\Starting_Notification.mp4",color=(255,49,49),position=("center","top"), overlay_size=(623,180))
    # video = overlay_transparent_video(video, r"static\videos\Like_Badge.webm",color=(0,0,0),position=("center","bottom"), overlay_size=(180,180),start=5)
    # video = overlay_transparent_video(video, r"static\videos\Subscribe.mp4",color=(0,254,0),position=("center","bottom"), overlay_size=(180,180),start=10)

    # audio = AudioFileClip(audio_file).with_start(0)
    # video = video.with_audio(audio)

    video.write_videofile("temp_video.mp4", codec="libx264", audio_codec="aac")

    st.video("temp_video.mp4")

    video.close()