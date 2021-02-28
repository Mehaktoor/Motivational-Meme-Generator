from typing import List
import os
import subprocess

from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = './pdf_ref.txt'
        command = f"pdftotext {path} {tmp}"

        subprocess.call(command, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(tmp)

        os.remove(tmp)
        return quotes
