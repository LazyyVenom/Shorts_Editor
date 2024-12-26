from scipy.io import wavfile
import noisereduce as nr
from pydub import AudioSegment

def reduce_noise(input_file_path, output_file_path):
    rate, data = wavfile.read(input_file_path)
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(output_file_path, rate, reduced_noise)

def get_audio_duration(audio_file):
    rate, data = wavfile.read(audio_file)
    return len(data) / rate

def audio_speed_increase(input_file_path, output_file_path, speed_factor):
    if speed_factor < 1.0:
        raise ValueError("Speed factor must be greater than or equal to 1.0")
    
    sound = AudioSegment.from_file(input_file_path)
    sped_up_sound = sound.speedup(playback_speed=speed_factor, chunk_size=150, crossfade=25)
    sped_up_sound.export(output_file_path, format="wav")
