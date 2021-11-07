"""Concrete quote ingestor class for pdf files."""

from .IngestorInterface import IngestorInterface, QuoteModel
from .IngestorTXT import IngestorTXT
import subprocess
import random
import os


class IngestorPDF(IngestorInterface):
    """Concrete quote ingestor class for pdf files.

    The quotes must be in the following format. One quote per line, each line of the form '{body} - {author}.
    """

    supported_formats = {'pdf'}

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes.

        Use a subprocess to call pdftotext to convert the pdf to a random temp text file.
        Then call the pre-written IngestorTXT to ingest the resulting txt file.
        Remove the temp text file.
        """
        if not cls.can_ingest(path):
            raise Exception(f'unsupported file format: requires{cls.supported_formats}')

        tmp_code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        tmp_file = f"temp_file_{tmp_code}.txt"

        subprocess.run(['pdftotext', path, tmp_file])

        quotes = IngestorTXT.parse(tmp_file)

        os.remove(tmp_file)

        return quotes


# # testing code
# path = 'DogQuotesPDF.pdf'
#
# ing = IngestorPDF()
#
# quotes = ing.parse(path)
#
# for quote in quotes:
#     print(quote)


# Example code use of subprocess. We will need to use it on pdftotext
# import subprocess
# import random
