import logging
import os

class FileJsonSource:
    def __init__(self, filename):
        self.filename = filename
        
    def read(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as content_file:
                content = content_file.read()
                logging.info("Received json: " + content)
                os.remove(self.filename)
                return content
        return ""
