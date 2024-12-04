# Required Libraries

from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx import Painting

video = VideoFileClip(filename="input_video.mp4")

text = TextClip(
    font="static\Coolvetica Rg.otf", text="Your Text Here", font_size=50, color="white",duration=video.duration
)

video_with_text = CompositeVideoClip([video, text])

video_with_text.write_videofile("output_video.mp4", codec="libx264", fps=video.fps)


# This is gonna take some time as the code is updated and chat gpt don't gets the updated one

#OK IT IS TAKING TIME TO PROCESS THE VIDEO  
# GOOD THING - We can set the time duration for texts easily Let's Go

#NGL Text looking good need to make some good functions and A class to make it usable