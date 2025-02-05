from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from rich import print

async def set_cover(title):
    audio_file = f".{title}.mp3"
    audio = MP3(audio_file, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        pass
    with open(".thumbnail.jpg", "rb") as f:
        audio.tags.add(APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            desc="Cover",
            data=f.read(),
        ))
    audio.save()
    print(f"[green bold]Cover image added to '{audio_file}'.[/green bold]")