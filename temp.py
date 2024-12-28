from utils.video_utils import open_video, add_days_to_video

video = open_video("input_video.mp4")

video_with_text = add_days_to_video(video, 3)

video_with_text.write_videofile("output_video.mp4", codec="libx264", fps=24)