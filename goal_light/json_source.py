import logging

class JsonSource:
    def __init__(self, filename):
        self.filename = filename
        
    def read(self):
        with open(self.filename, 'r') as content_file:
            content = content_file.read()
            logging.info("Received json: " + content)
            return content
