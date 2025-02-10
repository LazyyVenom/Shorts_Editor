from moviepy import VideoFileClip, CompositeVideoClip
from moviepy.video import fx as vfx
from utils.video_utils import add_days_to_video
from utils.vfx_utils import overlay_transparent_video

if __name__ == "__main__":
    video = VideoFileClip(r"temp_video.mp4")
    # video = add_days_to_video(video, '3')

    # video = overlay_transparent_video(video, r"static\videos\Starting_Notification.mp4",color=(255,49,49),position=("center","top"), overlay_size=(623,180))
    # video = overlay_transparent_video(video, r"static\videos\Like_Badge.webm",color=(0,0,0),position=("center","bottom"), overlay_size=(180,180),start=5)
    # video = overlay_transparent_video(video, r"static\videos\Subscribe.mp4",color=(0,254,0),position=("center","bottom"), overlay_size=(380,180),start=10)
    
    video.write_videofile("temp_video.mp4", codec="libx264", audio_codec="aac") 