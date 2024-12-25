from utils import add_captions as capt
from utils import audio_recognition as reco
import streamlit as st
from utils import video_utils
import os

st.title("Video Captioning")

st.write("This is a simple web app to add captions to a video based on the audio of the video.")

primary_video_path = st.text_input("Enter the Path of the primary video")
primary_video_path = primary_video_path.replace('"','')

if os.path.exists(primary_video_path):
    primary_video = video_utils.open_video(primary_video_path)
    primary_video_duration = video_utils.get_video_duration(primary_video)

    st.write("Cropping Section")
    start_time, end_time = st.slider("Select the start and end time of the video", 0.0, primary_video_duration, (0.0, primary_video_duration))
    
    if start_time < end_time:
        st.write(f"Selected video segment from {start_time} to {end_time}")
    else:
        st.write("Error: Start time must be less than end time")

else:
    st.write("The file don't exists: ", primary_video_path)

secondary_video = st.text_input("Enter the Path of the secondary video")

st.file_uploader("Upload an audio file", type=["wav"])