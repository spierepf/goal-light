import logging
import vlc

class Horn:
    def __init__(self):
        self.horn_sound = None

    def silence_horn(self):
        if self.horn_sound != None:
            self.horn_sound.stop()
            self.horn_sound = None

    def sound_horn(self, filename):
        self.silence_horn()
        self.horn_sound = vlc.MediaPlayer(filename)
        self.horn_sound.play()

    def trigger(self, id):
        logging.info("Triggering horn: " + id)
        self.sound_horn("horn/" + str(id) + ".mp3")
