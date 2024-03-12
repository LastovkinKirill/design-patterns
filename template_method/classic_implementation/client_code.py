# pdf data process
import logging

from template_method.classic_implementation.module import DataProcessor


class PdfDataProcessor(DataProcessor):
    def getter(self):
        return "pdf data"

    def encoder(self, data: str) -> bytes:
        return data.encode("utf-8")

    def saver(self, data: bytes) -> None:
        print(f"[SAVE PDF] {data} to db")


class CsvDataProcessor(DataProcessor):
    log: logging.Logger

    def __init__(self):
        log = logging.getLogger('csv')
        log.setLevel(logging.DEBUG)
        log.addHandler(logging.StreamHandler())
        self.log = log

    def getter(self):
        return "csv data"

    def encoder(self, data: str) -> bytes:
        return data.encode("utf-8")

    def saver(self, data: bytes) -> None:
        print(f"[SAVE CSV] {data} to db")

    def logger(self, message: str) -> None:
        self.log.info(message)
