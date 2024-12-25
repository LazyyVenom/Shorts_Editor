from utils import add_captions as capt
from utils import audio_recognition as reco
import streamlit as st
from utils import video_utils

st.title("Video Captioning")

st.write("This is a simple web app to add captions to a video based on the audio of the video.")

primary_video = st.file_uploader("Upload a Primary Video", type=["mp4"])
print(primary_video)
secondary_video =  st.file_uploader("Upload a Secondary Video", type=["mp4"])

st.file_uploader("Upload an audio file", type=["wav"])