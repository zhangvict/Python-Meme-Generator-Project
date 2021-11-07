"""Command Line Interface for meme generator."""

import os
import random
import argparse

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path: str = None, body: str = None, author: str = None):
    """Generate a meme."""
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make a meme')
    parser.add_argument('--path', type=str)
    parser.add_argument('--body', type=str)
    parser.add_argument('--author', type=str)
    args = parser.parse_args()

    _meme = generate_meme(args.path, args.body, args.author)
    print(f'your meme is at {_meme}')
