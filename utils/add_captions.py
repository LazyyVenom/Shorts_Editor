# Required Libraries

from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx import Painting

video = VideoFileClip("input_video.mp4")

text = TextClip("Your Text Here", fontsize=50, color='white')

text = text.set_duration(video.duration).set_position(("center", "bottom"))

video_with_text = CompositeVideoClip([video, text])

video_with_text.write_videofile("output_video.mp4", codec="libx264", fps=video.fps)


#This is gonna take some time as the code is updated and chat gpt don't gets the updated one
