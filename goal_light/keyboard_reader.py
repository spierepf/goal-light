import threading
import time
import logging
import sys

class KeyboardReader(threading.Thread):
    def __init__(self, actions=None):
        threading.Thread.__init__(self)
        self.daemon = True
        self.actions = actions
        
    def run(self):
        logging.info("ButtonReader starting")
        while True:
            k = sys.stdin.read(1)
            while k not in set(['1', '2', '3', '4']):
                time.sleep(0)
                k = sys.stdin.read(1)
            logging.info("Button " + k + " pressed")
            if self.actions != None:
                self.actions.trigger(k)
        logging.info("ButtonReader stopping")

if __name__ == '__main__':
    ButtonReader().start()
