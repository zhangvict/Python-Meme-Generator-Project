"""Concrete quote ingestor class for docx files."""

from .IngestorInterface import IngestorInterface, QuoteModel
from docx import Document


class IngestorDOCX(IngestorInterface):
    """Concrete quote ingestor class for docx files.

    The quotes must be in the following format. One quote per line, each line of the form '{body} - {author}.
    """

    supported_formats = {'docx'}

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes."""
        if not cls.can_ingest(path):
            raise Exception(f'unsupported file format: requires{cls.supported_formats}')
        quotes_docx = Document(path)
        quotes = []
        for par in quotes_docx.paragraphs:
            par_words = par.text.split(' - ')
            if len(par_words) == 2:
                quote = QuoteModel(par_words[0], par_words[1])
                quotes.append(quote)
        return quotes
#
# #testing code
# path='DogQuotesDOCX.docx'
#
# ing=IngestorDOCX()
#
# quotes=ing.parse(path)
#
# for quote in quotes:
#     print(quote)
