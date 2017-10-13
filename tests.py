from animeultime import animeultime
import unittest

class AUTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def test_get_episode(self):
        austream = animeultime.AnimeUltime.get_episode(52081)
        stream = 'http://www.anime-ultime.net/stream-83611.mp4'
        self.assertEqual(austream, stream)

    def test_get_id_by_link(self):
        au_id = animeultime.AnimeUltime.get_id_by_link('http://www.anime-ultime.net/info-0-1/52081/Ballroom-e-Youkoso-14-vostfr')
        episode_id = 52081
        self.assertEqual(au_id, episode_id)    

    def test_get_title(self):
        au_title = animeultime.AnimeUltime.get_title('http://www.anime-ultime.net/info-0-1/52081/Ballroom-e-Youkoso-14-vostfr')
        title = 'Ballroom e Youkoso 14'
        self.assertEqual(au_title, title)

unittest.main()