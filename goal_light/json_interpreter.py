import logging
import simplejson

class JsonInterpreter:
    def __init__(self, light=None, horn=None):
        self.light = light
        self.horn = horn

    def interpret(self, json):
        dict = simplejson.loads(json)
        logging.info("Received: " + str(dict))
        if 'l' in dict:
            self.light.trigger(float(dict['l']))
        if 'h' in dict:
            self.horn.trigger("horn/"+dict['h']+".mp3")