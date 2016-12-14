import logging

class Light:
    def __init__(self):
        pass

    def trigger(self, duration):
        logging.info("Triggering light for " + str(duration) + " seconds")
