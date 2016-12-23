import logging
import urllib

class Downloader:
    def __init__(self):
        pass

    def trigger(self, id):
        url = "http://www.meetcweb.com/goal/horns/" + id + ".mp3"
        destination = "horn/" + id + ".mp3"
        logging.info("Downloading " + url + " to " + destination)
        urllib.urlretrieve(url, destination)
