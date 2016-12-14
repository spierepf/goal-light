import simplejson
import time
import RPi.GPIO as GPIO
from threading import Thread
import urllib
import urllib2
import vlc

class PollerThread:
  def __init__(self):
    self.light_gpio = 16
    self.horn_sound = None

  def receiveJson(self):
    return urllib2.urlopen('http://www.meetcweb.com/goal/light.php').read()

  def illuminate_light(self, duration):
    print "Turn the light on"
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.light_gpio, GPIO.OUT)
    GPIO.output(self.light_gpio, 1)
    time.sleep(duration)
    GPIO.output(self.light_gpio, 0)
    GPIO.cleanup()
    print "Turn the light off"

  def silence_horn(self):
    if self.horn_sound != None:
      self.horn_sound.stop()
      self.horn_sound = None

  def sound_horn(self, filename):
    self.silence_horn()
    self.horn_sound = vlc.MediaPlayer(filename)
    self.horn_sound.play()

  def trigger_light(self):
    if self.light_duration != None and self.light_duration != 0.0:
      thread = Thread(target=self.illuminate_light, args=(self.light_duration,))
      thread.start()
      return thread
    return None

  def trigger_horn(self):
    if self.horn != None:
      self.sound_horn(self.horn)

  def interpretJson(self, json):
    try:
      dict = simplejson.loads(json)
      self.poll_delay = int(dict["d"])
      self.light_duration = float(dict["l"])
      self.horn = None if dict["h"] == "0" else "horn/" + dict["h"] + ".mp3"
      self.download = None if dict["dl"] == "0" else dict["dl"] + ".mp3"
      self.button_config = None
    except Exception as err:
      print err
