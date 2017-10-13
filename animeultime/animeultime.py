import requests
import re


class AnimeUltime():
    base_url = 'http://www.anime-ultime.net'

    @classmethod
    def get_episode(self, episode_id):
        episode_page = requests.get(
            '{}/info-0-1/{}'.format(
                self.base_url,
                episode_id
            )
        ).text
        url = re.findall(
            'og:video\"\ content=\"(http:\/\/www.anime-ultime.net\/stream-[0-9]+\.mp4)',
            episode_page
        )[0]
        return url

    @classmethod
    def get_id_by_link(self, url):
        return int(re.findall(
            '(?:file|info)-0-1\/([0-9]+)',
            url
        )[0])

    @classmethod
    def get_title(self, link):
        return re.findall(
            'info-0-1\/[^\/]+\/(.*)-vostfr',
            link
        )[0].replace('-', ' ')

    @classmethod
    def get_all_episodes(self, serie_id):
        episodes = {}
        playlist = requests.get(
            '{}/file-0-1/{}'.format(self.base_url, serie_id)
        ).text
        episode_list = re.findall(
            '<a\ href=\"info-0-1/([0-9]+)/([^\"]+)-vostfr\"',
            playlist
        )
        for episode in episode_list:
            episode_id, title = episode
            title = title.replace('-', ' ')
            episodes[title] = self.get_episode(episode_id)
        return episodes
