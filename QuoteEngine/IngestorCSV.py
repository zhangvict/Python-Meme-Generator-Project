"""Concrete quote ingestor class for csv files."""

from .IngestorInterface import IngestorInterface, QuoteModel
import pandas as pd


class IngestorCSV(IngestorInterface):
    """Concrete quote ingestor class for csv files.

    The csv file have a header and be of 2 columns, first column labelled 'body' and second column labelled 'author'.
    """

    supported_formats = {'csv'}

    @classmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes."""
        if not cls.can_ingest(path):
            raise Exception(f'unsupported file format: requires{cls.supported_formats}')
        quotes = []
        df = pd.read_csv(path, header=0)
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes

# #testing code
# path='DogQuotesCSV.csv'
#
# ing=IngestorCSV()
#
# quotes=ing.parse(path)
#
# for quote in quotes:
#     print(quote)
