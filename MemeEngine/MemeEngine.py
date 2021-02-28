from PIL import Image
import os

class MemeEngine:
    def __init__(self, out_path):
        self.out_path = out_path

        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def generate_meme(self, in_path, text, author, width = 500) -> str:
        