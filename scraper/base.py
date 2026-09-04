"""Base class for per-source scrapers."""

from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """Inherit from this for each data source."""

    @abstractmethod
    def scrape(self):
        """Return raw records from this source. TODO: implement per source."""
