from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process_data(self) -> None:
        data = self.getter()
        self.logger(f"Got `{data}`")

        encoded_data = self.encoder(data)
        self.saver(encoded_data)

        self.logger(f"`{data}` was processed")

    @abstractmethod
    def getter(self):
        ...

    @abstractmethod
    def encoder(self, data: str) -> bytes:
        ...

    @abstractmethod
    def saver(self, data: bytes) -> None:
        ...

    # default implementation
    def logger(self, message: str) -> None:
        print(message)
