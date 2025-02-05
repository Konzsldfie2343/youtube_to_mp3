import os
from rich import print


async def cleanup(title):
          os.remove(".thumbnail.jpg")
          os.remove(f".{title}.mp3")
          print("[green bold]Cleanup completed.[/green bold]")