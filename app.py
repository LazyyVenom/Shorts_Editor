from utils import add_captions as capt
from utils import audio_recognition as reco
from utils import audio_utils as audio_utils
import streamlit as st
from utils import video_utils
import os

def get_video_segment(video_path_label):
    video_path = st.text_input(f"Enter the Path of the {video_path_label} video")
    video_path = video_path.replace('"', '')
    start_time = 0.0
    end_time = 0.0

    if os.path.exists(video_path):
        video = video_utils.open_video(video_path)
        video_duration = video_utils.get_video_duration(video)
        video.close()

        st.write("Cropping Section")
        start_time, end_time = st.slider(f"Select the start and end time of the {video_path_label} video", 0.0, video_duration, (0.0, video_duration))

        if start_time < end_time:
            st.write(f"Selected video segment from {start_time} to {end_time}")
        else:
            st.write("Error: Start time must be less than end time")

        st.video(video_path, start_time=start_time, end_time=end_time)
    else:
        st.write(f"The file doesn't exist: {video_path}")

    return video_path, start_time, end_time

st.title("Video Captioning")
st.write("This is a simple web app to add captions to a video based on the audio of the video.")

with st.expander("Primary Video"):
    primary_video_path, primary_start_time, primary_end_time = get_video_segment("primary")

with st.expander("Secondary Video"):
    secondary_video_path, secondary_start_time, secondary_end_time = get_video_segment("secondary")

with st.expander("Audio File"):
    audio_file = st.text_input("Enter the Path of the audio file")
    audio_file = audio_file.replace('"', '')

    if os.path.exists(audio_file):
        audio_duration = audio_utils.get_audio_duration(audio_file)

        st.write("Cropping Section for Audio File")
        audio_start_time, audio_end_time = st.slider("Select the start and end time of the audio file", 0.0, audio_duration, (0.0, audio_duration))
        
        if audio_start_time < audio_end_time:
            st.write(f"Selected audio segment from {audio_start_time} to {audio_end_time}")
            st.audio(audio_file, start_time=audio_start_time, end_time=audio_end_time)
        else:
            st.write("Error: Start time must be less than end time")

    else:
        st.write(f"The file doesn't exist: {audio_file}")


# Audio Processing Stuff Here
audio_utils.reduce_noise(audio_file, "temp_processing.wav")
audio_utils.audio_speed_increase("temp_processing.wav", "temp_processing.wav", 1.25)

# Video Processing Stuff Here