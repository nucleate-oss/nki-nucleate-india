from scraper.base import BaseScraper


def test_base_scraper_is_abstract():
    assert getattr(BaseScraper.scrape, "__isabstractmethod__", False)
