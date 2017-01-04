import goal_light
import logging
import sys
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting...")

source = goal_light.HttpJsonSource('http://www.meetcweb.com/goal/light.php')

light = goal_light.Light()
horn = goal_light.Horn()
horn.trigger("0")

actions = goal_light.ButtonActions(light, horn)
actions.update_config({'3h': '0', '3l': '0.0', '2l': '4.0', '1h': '999', '2h': '999', '1l': '2.0'})

downloader = goal_light.Downloader()
interpreter = goal_light.JsonInterpreter(light, horn, downloader, actions)

reader = goal_light.KeyboardReader(actions)
reader.start()

button_reader = goal_light.ButtonReader(actions)

wifi_thread = goal_light.WifiThread()
wifi_thread.start()

GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)
try:
    while reader.isAlive():
        try:
            json = source.read()
            delay = interpreter.interpret(json)
            GPIO.output(15, GPIO.HIGH)
        except:
            logging.exception('')
            GPIO.output(15, GPIO.LOW)
            delay = 120

        logging.info("Sleeping for: " + str(delay) + " seconds")
        time.sleep(delay)

except KeyboardInterrupt:
    pass

wifi_thread.stop()
GPIO.cleanup()
