from moviepy import VideoFileClip, CompositeVideoClip
from moviepy.video import fx as vfx

def overlay_transparent_video(original_video_path, overlay_video_path, output_video_path, position=("center", "bottom"), overlay_size=None):
    original_video = VideoFileClip(original_video_path)
    print(original_video.size)

    overlay_video = VideoFileClip(overlay_video_path)
    overlay_video = overlay_video.with_mask().fx(vfx.MaskColor, 1.0, 0.192, 0.192)
    print(overlay_video.size)

    if overlay_size:
        overlay_video = overlay_video.resized(overlay_size)

    overlay_video = overlay_video.with_position(position)

    composite_video = CompositeVideoClip([original_video, overlay_video])

    composite_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    original_video_path = "input_video.mp4"
    overlay_video_path = "overlay_video.mp4"
    output_video_path = "output_video.mp4"
    overlay_size = (320, 180)

    overlay_transparent_video(original_video_path, overlay_video_path, output_video_path, overlay_size=overlay_size)