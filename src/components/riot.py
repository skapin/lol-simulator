from riotwatcher import RiotWatcher

from config.settings import SETTINGS


class Riot(RiotWatcher):
    def __init__(self):
        RiotWatcher.__init__(self, SETTINGS['RIOT_API_KEY'])

    @staticmethod
    def get_image_url(riot_data, obj):
        return '/'.join([riot_data['cdn'],
                         riot_data['v'],
                         'img',
                         obj['image']['group'],
                         obj['image']['full']
                         ])
