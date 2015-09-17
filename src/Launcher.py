from core import AtrapCrawler
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    crawler = AtrapCrawler.AtrapCrawler()
    crawler.start()
