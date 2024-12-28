from moviepy import AudioFileClip, CompositeVideoClip, VideoFileClip
from moviepy.video import fx as vfx

def overlay_transparent_video(original_video, overlay_video_path, color = (0, 254, 0), position=("center", "top"), overlay_size=None):
    overlay_video = VideoFileClip(overlay_video_path)
    overlay_video = overlay_video.with_effects([vfx.MaskColor(color,threshold=50,stiffness=100)])

    if overlay_size:
        overlay_video = overlay_video.resized(overlay_size)

    overlay_video = overlay_video.with_position(position)

    composite_video = CompositeVideoClip([original_video, overlay_video])

    return composite_video