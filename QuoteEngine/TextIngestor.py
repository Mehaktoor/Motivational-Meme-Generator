from typing import List
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        txt_file = f'./data/SimpleLines.txt'
        file_ref = open(txt_file, "r")

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(txt_file)
        return quotes
