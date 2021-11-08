"""Abstract base class for ingesting quotes from files of various file types.

Child classes will be ingestor classes for specific file types.
"""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """Abstract base class for an ingestor."""

    supported_formats = {'csv', 'docx', 'pdf', 'txt'}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if a file path is an extension of one of the supported formats."""
        ext = path.split('.')[-1]
        return ext in cls.supported_formats

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes."""
        pass
