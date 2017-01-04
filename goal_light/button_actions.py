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
        if button == "4":
            self.light.trigger(0.0)
            self.horn.silence_horn()
        else:
            self.light.trigger(float(self.config[button + "l"]))
            self.horn.trigger(str(self.config[button + "h"]))
