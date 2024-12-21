from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from typing import List


class AddCaptions:
    def __init__(
        self,
        video,
        texts: List[str],
        start_times: List[float],
        durations: List[float],
        font_size: int = 50,
        font: str = "static\Coolvetica Rg.otf",
    ):
        self.video = video
        self.font = font
        self.font_size = font_size
        self.texts = texts
        self.start_times = start_times
        self.durations = durations

    def add_captions(self):
        clips = [self.video]
        for text, start_time, duration in zip(
            self.texts, self.start_times, self.durations
        ):
            text_clip = TextClip(
                font=self.font,
                text=text,
                font_size=self.font_size,
                color="white",
                method="caption",
                size=self.video.size,
                duration=duration,
                text_align="center",
            ).with_start(start_time)
            clips.append(text_clip)

        video_with_text = CompositeVideoClip(clips)
        self.video = video_with_text


if __name__ == "__main__":
    video_path = "input_video.mp4"
    texts =  ['hello', 'to', 'aaj', 'ke', 'din', 'maine', 'apne', 'speech', 'recognition', 'wale', 'aap', 'Mein', 'Hi', 'Kam', 'Kiya', 'Hai', 'Taki', 'short', 'editing', 'Aasan', 'ho', 'sake', 'aur', 'automatic', 'kar', 'Sakun', 'Main', 'To', 'Aaj', 'Ke', 'Din', 'Maine', 'ISI', 'Mein', 'kam', 'Kiya', 'dekhte', 'hain', 'aage', 'kya', 'karte', 'hain']
    start_times = [0, 0.2973571428571429, 0.5947142857142858, 0.8920714285714286, 1.1894285714285715, 1.4867857142857144, 1.7841428571428573, 2.0815, 2.378857142857143, 2.676214285714286, 2.9735714285714288, 3.2709285714285716, 3.5682857142857145, 3.8656428571428574, 4.163, 4.460357142857143, 4.757714285714286, 5.055071428571429, 5.352428571428572, 5.649785714285715, 5.9471428571428575, 6.2445, 6.541857142857143, 6.839214285714286, 7.136571428571429, 7.433928571428572, 7.731285714285715, 8.028642857142858, 8.326, 8.623357142857143, 8.920714285714286, 9.21807142857143, 9.515428571428572, 9.812785714285715, 10.110142857142858, 10.4075, 10.704857142857144, 11.002214285714286, 11.29957142857143, 11.596928571428572, 11.894285714285715, 12.191642857142858]
    durations = [0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429, 0.2973571428571429]

    texts = list(map(str.upper, texts))

    add_captions = AddCaptions(video_path, texts, start_times, durations)
    video_with_text = add_captions.add_captions()
    video_with_text.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac") 
