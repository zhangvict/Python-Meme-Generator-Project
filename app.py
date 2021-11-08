"""Flask interface for the meme generator."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []

    for file in os.listdir(images_path):
        if file.endswith('.jpg'):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form["image_url"]
    tmp = f'./tmp/random_{random.randint(0, 10000)}.jpg'
    req = requests.get(img_url)
    try:
        with open(tmp, 'wb') as open_file:
            open_file.write(req.content)
            body = request.form["body"]
            author = request.form["author"]
            path = meme.make_meme(tmp, body, author)
        os.remove(tmp)
        return render_template('meme.html', path=path)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run()
