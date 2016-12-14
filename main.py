import poller_thread
import time

pt = poller_thread.PollerThread()

while True:
  json = pt.receiveJson()
  print json
  pt.interpretJson(json)
  pt.trigger_light()
  pt.trigger_horn()
  time.sleep(pt.poll_delay)
