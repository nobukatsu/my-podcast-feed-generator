from abc import ABC
from abc import abstractmethod


class Podcast(ABC):

    @abstractmethod
    def has_new_episode(self, target_date) -> bool:
        pass

    @abstractmethod
    def generate(self, target_date):
        pass
