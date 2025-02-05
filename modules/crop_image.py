from PIL import Image
from rich import print

async def crop_image():
    image = Image.open(".thumbnail.jpg")
    width, height = image.size
    square_size = min(width, height)
    left = (width - square_size) // 2
    top = (height - square_size) // 2
    image = image.crop((left, top, left + square_size, top + square_size))
    image.save(".thumbnail.jpg")
    print("[green bold]Thumbnail cropped successfully.[/green bold]")