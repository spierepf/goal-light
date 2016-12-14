class JsonSource:
    def __init__(self, filename):
        self.filename = filename
        
    def read(self):
        with open(self.filename, 'r') as content_file:
            return content_file.read()
