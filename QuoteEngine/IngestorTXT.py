"""Concrete quote ingestor class for txt files."""

from .IngestorInterface import IngestorInterface, QuoteModel


class IngestorTXT(IngestorInterface):
    """Concrete quote ingestor class for txt files.

    The quotes must be in the following format. One quote per line, each line of the form '{body} - {author}.'
    """

    supported_formats = {'txt'}

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes."""
        if not cls.can_ingest(path):
            raise Exception(f'unsupported file format: requires{cls.supported_formats}')
        quotes = []
        with open(path, encoding='utf-8-sig') as txt_file:
            for row in txt_file:
                line = row.split(' - ')
                if len(line) == 2:
                    body, author = line[0].strip(), line[1].strip()
                    quote = QuoteModel(body, author)
                    quotes.append(quote)
        return quotes

#
# # testing code
# path = 'DogQuotesTXT.txt'
#
# ing = IngestorTXT()
#
# quotes = ing.parse(path)
#
# for quote in quotes:
#     print(quote)
#
