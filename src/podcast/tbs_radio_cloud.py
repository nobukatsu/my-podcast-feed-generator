from podcast.abstract_podcast import Podcast
from typing import NamedTuple


class TbsRadioCloud(Podcast):

    def __init__(self, key: str, top_url: str, channel_title: str, folder_name: str):
        self.key = key
        self.top_url = top_url
        self.channel_title = channel_title
        self.folder_name = folder_name

    def has_new_episode(self, target_date) -> bool:
        pass

    def generate(self, target_date):
        pass


    def __create_channel(self):
        return Channel(self.key, self.top_url, self.channel_title, self.folder_name)


class Channel(NamedTuple):
    key: str
    top_url: str
    title: str
    folder_name: str
