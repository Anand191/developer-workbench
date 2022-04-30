import string
import random
from loguru import logger
from src.model.model_base import BaseModel


class SampleModel(BaseModel):
    def __init__(self, num_suggestions=10) -> None:
        super().__init__()
        self.num = num_suggestions
        logger.info(f"Ready to provide {self.num} suggestions!!")

    def predict(self, query):
        return ([''.join(random.choices(string.ascii_lowercase, k=10)) for i in range(self.num)])
