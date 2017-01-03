import logging

class ButtonActions:
    def __init__(self, light=None, horn=None):
        self.light = light
        self.horn = horn
        self.config = None

    def update_config(self, config):
        logging.info("Updated config: " + str(config))
        self.config = config

    def trigger(self, button):
        self.light.trigger(float(self.config[button + "l"]))
        self.horn.trigger(str(self.config[button + "h"]))
