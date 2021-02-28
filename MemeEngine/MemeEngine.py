from PIL import Image, ImageDraw, ImageFont
from time import time
from random import randrange
import os

class MemeEngine:
    def __init__(self, out_path):
        self.out_path = out_path

        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def generate_meme(self, in_path, text, author, width = 500) -> str:
        """Meme will be generated here using image, text and author."""
        img = Image.open(in_path)
        # resizing the image
        w, h = img.size
        width = min(500, width)
        r = width / w
        height = int(r * h)
        img = img.resize((width, height), Image.NEAREST)

        # put the text on top of the image
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/Fonts/LilitaOne-Regular.ttf', size=20)

        # put the quote on 'random' position on the image
        row_text = randrange(30, height - 50)
        draw.text((50, row_text), text, font= font, fill= 'white')
        draw.text((50, row_text + 20), f'- {author}', font= font, fill= 'white')

        out_dir = os.path.join(self.out_path, f'tmp-{time()}.png')
        img.save(out_dir)
        print(f'Image saved to {out_dir}.')
        return out_dir