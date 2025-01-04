from utils.add_captions import add_captions
from utils.video_utils import add_audio_to_video
from utils.audio_recognition import get_word_timestamps
from moviepy import VideoFileClip

if __name__ == "__main__":
    video_path = r"C:\Users\Anubhav Choubey\AppData\Local\CapCut\Videos\Day8(1).mp4"
    audio_path = r"C:\Users\Anubhav Choubey\AppData\Local\CapCut\Videos\Day8.WAV"

    word_timestamps = get_word_timestamps(audio_path)
    captions = [word_info['word'] for word_info in word_timestamps]
    captions = list(map(str.upper, captions))
    start_times = [word_info['start_time'] for word_info in word_timestamps]
    durations = [word_info['duration'] for word_info in word_timestamps]

    print(captions)

    video = VideoFileClip(video_path)

    # video.with_audio()

    video = add_captions(video, captions, start_times, durations)

    # video_with_audio = add_audio_to_video(video, audio_path, 0)
    video.write_videofile("output_video.mp4", codec="libx264", audio = True)