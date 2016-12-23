import logging
import urllib

class HttpJsonSource:
    def __init__(self, url):
        self.url = url
        
    def read(self):
        try:
            content = urllib.urlopen(self.url).read()
            logging.info("Received: " + content)
            return content
        except:
            logging.exception('While trying to read ' + str(self.url))
            raise
