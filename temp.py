from moviepy import VideoFileClip, CompositeVideoClip
from moviepy.video import fx as vfx

def overlay_transparent_video(original_video, overlay_video_path, color = (0, 254, 0), position=("center", "bottom"), overlay_size=None):
    overlay_video = VideoFileClip(overlay_video_path)
    overlay_video = overlay_video.with_effects([vfx.MaskColor(color,threshold=50,stiffness=100)])

    if overlay_size:
        overlay_video = overlay_video.resized(overlay_size)

    overlay_video = overlay_video.with_position(position)

    composite_video = CompositeVideoClip([original_video, overlay_video])

    return composite_video

if __name__ == "__main__":
    original_video_path = "input_video.mp4"
    overlay_video_path = r"static\videos\Like_Badge.webm"
    output_video_path = "output_video.mp4"
    overlay_size = (180, 180)

    original_video = VideoFileClip(original_video_path)
    video = overlay_transparent_video(original_video, overlay_video_path,color=(0,0,0),position=("center","bottom"), overlay_size=overlay_size)
    video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")