import goal_light
import logging
import sys
import time

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting...")

source = goal_light.JsonSource("data.json")

light = goal_light.Light()
horn = goal_light.Horn()
actions = goal_light.ButtonActions(light, horn)
actions.update_config({'3h': '5', '3l': '6.0', '2l': '4.0', '1h': '1', '2h': '3', '1l': '2.0'})

interpreter = goal_light.JsonInterpreter(light, horn, None, actions)

reader = goal_light.ButtonReader(actions)
reader.start()

while reader.isAlive():
    json = source.read()
    delay = interpreter.interpret(json)
    logging.info("Sleeping for: " + str(delay) + " seconds")
    time.sleep(delay)

# import poller_thread
# import time

# pt = poller_thread.PollerThread()

# while True:
#   json = pt.receiveJson()
#   print json
#   pt.interpretJson(json)
#   pt.trigger_light()
#   pt.trigger_horn()
#   time.sleep(pt.poll_delay)
