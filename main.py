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

interpreter = goal_light.JsonInterpreter(light, horn, None, actions)

reader = goal_light.ButtonReader(actions)
reader.start()

wifi_thread = goal_light.WifiThread()
wifi_thread.start()


try:
    while reader.isAlive():
        json = source.read()
        delay = interpreter.interpret(json)
        logging.info("Sleeping for: " + str(delay) + " seconds")
        time.sleep(delay)

except KeyboardInterrupt:
    pass

wifi_thread.stop()
GPIO.cleanup()
