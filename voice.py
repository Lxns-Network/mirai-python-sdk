from pathlib import Path
from abc import ABCMeta, abstractmethod

class InternalVoice(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def render(self) -> bytes:
        pass


class LocalVoice(InternalVoice):
    path: Path

    def __init__(self, path):
        if isinstance(path, str):
            self.path = Path(path)
        elif isinstance(path, Path):
            self.path = path

    def render(self) -> bytes:
        return self.path.read_bytes()
