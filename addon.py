from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "http://feeds.soundcloud.com/users/soundcloud:users:126685326/sounds.rss"

@plugin.route('/')
def main_menu():
    items = [
      {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "http://i1.sndcdn.com/avatars-000118968396-6x0y94-original.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "http://i1.sndcdn.com/avatars-000118968396-6x0y94-original.jpg"},
   ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
