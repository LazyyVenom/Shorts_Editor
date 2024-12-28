from moviepy import VideoFileClip, CompositeVideoClip

def overlay_transparent_video(original_video_path, overlay_video_path, output_video_path, position=("center", "bottom")):
    original_video = VideoFileClip(original_video_path)

    overlay_video = VideoFileClip(overlay_video_path, has_mask=True)

    overlay_video = overlay_video.with_position(position)

    composite_video = CompositeVideoClip([original_video, overlay_video])

    composite_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    original_video_path = "input_video.mp4"
    overlay_video_path = "overlay_video.webm"
    output_video_path = "output_video.mp4"

    overlay_transparent_video(original_video_path, overlay_video_path, output_video_path)