import logging
import simplejson

class JsonInterpreter:
    def __init__(self, light=None, horn=None, downloader=None, button_actions=None):
        self.light = light
        self.horn = horn
        self.downloader = downloader
        self.button_actions = button_actions

    def interpret(self, json):
        dict = {}
        try:
            dict = simplejson.loads(json)
            logging.info("Interpreting: " + str(dict))
        except:
            raise

        if 'l' in dict and dict['l'] != "0.0":
            self.light.trigger(float(dict['l']))
        if 'h' in dict and dict['h'] != "0":
            self.horn.trigger(dict['h'])
        if 'dl' in dict and dict['dl'] != "0":
            logging.info("Downloading: " + str(dict['dl']))
            self.downloader.trigger(dict['dl'])
        if 'b' in dict and dict['b'] != "0":
            self.button_actions.update_config(dict['b'])

        return int(dict['d']) if 'd' in dict else 300
