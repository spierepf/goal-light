import goal_light
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting...")

light = goal_light.Light()
horn = goal_light.Horn()
actions = goal_light.ButtonActions(light, horn)
actions.update_config({'3h': '5', '3l': '6.0', '2l': '4.0', '1h': '1', '2h': '3', '1l': '2.0'})

reader = goal_light.ButtonReader(actions)
reader.start()

while reader.isAlive():
    pass

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
