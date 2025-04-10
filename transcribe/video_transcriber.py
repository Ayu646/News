
import tempfile
import moviepy.editor as mp
from transcribe.audio_transcriber import transcribe_audio

def transcribe_video(file):
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=True) as temp_video:
        file.save(temp_video.name)
        clip = mp.VideoFileClip(temp_video.name)
        temp_audio = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        clip.audio.write_audiofile(temp_audio.name)
        with open(temp_audio.name, 'rb') as f:
            return transcribe_audio(f)
