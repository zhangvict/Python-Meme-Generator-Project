"""MemeEngine class using Pillow."""

import random

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """
    Instances of this class generated memes to a given directory.

    Supported image file types: This module supports image file type supported by Pillow, including jpg/png.
    However, code to further restrict file types can be activated by commenting out the '#' below.

    attributes:
        various formatting options for memes, including width, font, fill color.

    methods:
        can_make: tests whether a image path is of a supported file type
        make_meme: makes a meme from image path, saves it, and returns the meme file path
    """

    # supported_file_types={'jpg','png'}
    meme_width = 500  # set the width of the meme
    meme_font = './LilitaOne-Regular.ttf'  # truetype font of the meme
    meme_fill = 'white'  # fill color for meme text
    meme_factor = 18  # how much smaller the font size is relative to width

    def __init__(self, meme_dir: str):
        """Create a MemeEngine that saves meme images to path directory.

        meme_dir: directory to store the created memes
        """
        self.mem_dir = meme_dir

    # @classmethod
    # def can_make(cls, img: str) -> bool:
    #     """Check whether img is of a supported file type."""
    #     extension = img.split('.')[-1]
    #     return extension in cls.supported_file_types

    def make_meme(self, img: str, body: str, author: str) -> str:
        """Make a meme and return the file path of the meme.

        Arguments:
            img: image path string
            body: meme body string
            author: author body string

        return: meme path string

        Meme specifications:
            Image is resized to width exactly 500px while maintaining original aspect ratio.
            Meme is placed in a random location in the image
            Font size is automatically set to 12 times less than width
        """
        # if not self.can_make(img):
        #     raise Exception('unsupported image type')

        caption = f'{body}, {author}'  # caption text to put on image

        with Image.open(img) as meme:
            # resize image
            old_width, old_height = meme.size
            scale = self.meme_width/old_width
            new_size = new_width, new_height = self.meme_width, int(scale*old_height)
            meme = meme.resize(new_size)

            # caption image to a random location on the left half of the image, depending on font size
            draw = ImageDraw.Draw(meme)
            font_size = self.meme_width//self.meme_factor
            x, y = 10, random.randint(font_size, new_height-font_size)
            font = ImageFont.truetype(font=self.meme_font, size=font_size)
            draw.text((x, y), caption, fill=self.meme_fill, font=font)

            # save meme to out path determined by MemeEngine object
            meme_name = f'meme_{img.split("/")[-1]}'
            out_path = f'{self.mem_dir}/{meme_name}'
            meme.save(out_path)

        return out_path
