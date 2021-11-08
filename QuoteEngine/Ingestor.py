"""Main interface class for quote ingestor, to find and apply file-specific ingestor."""

# import the currently available ingestors
from .IngestorInterface import IngestorInterface
from .IngestorCSV import IngestorCSV
from .IngestorPDF import IngestorPDF
from .IngestorTXT import IngestorTXT
from .IngestorDOCX import IngestorDOCX


class Ingestor(IngestorInterface):
    """
    Encapsulate the different quote ingestor classes for each file type.

    ingestors: The set of ingestors currently written, each for a file type.
    """

    ingestors = {IngestorCSV, IngestorPDF, IngestorDOCX, IngestorTXT}

    @classmethod
    def parse(cls, path):
        """Attempt to ingest the file with each of the ingestors."""
        for ing in cls.ingestors:
            if ing.can_ingest(path):
                return ing.parse(path)
