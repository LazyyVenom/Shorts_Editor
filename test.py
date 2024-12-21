from utils.add_captions import AddCaptions
from utils.video_utils import add_audio_to_video
from utils.audio_recognition import get_word_timestamps

if __name__ == "__main__":
    video_path = "input_video.mp4"
    audio_path = "input_audio.wav"

    word_timestamps = get_word_timestamps(audio_path)
    captions = [word_info['word'] for word_info in word_timestamps]
    start_times = [word_info['start_time'] for word_info in word_timestamps]
    durations = [word_info['duration'] for word_info in word_timestamps]

    addCaptions = AddCaptions(video_path, captions, start_times, durations)
    addCaptions.add_captions()
    video = addCaptions.video

    video_with_audio = add_audio_to_video(video, audio_path, 0)
    video_with_audio.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")