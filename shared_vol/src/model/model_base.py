from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self) -> None:
        super().__init__()
        pass

    @abstractmethod
    def predict(self):
        pass
