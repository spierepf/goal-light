import unittest
import poller_thread
import RPi.GPIO as GPIO

class TestPollerThread(unittest.TestCase):
  def test_interpretJson(self):
    object_under_test = poller_thread.PollerThread()
    json = '''{"d":"300","l":"0.0","h":"0","dl":"5","b":0}'''
    object_under_test.interpretJson(json)

    self.assertEqual(300, object_under_test.poll_delay)
    self.assertEqual(0.0, object_under_test.light_duration)
    self.assertEqual(None, object_under_test.horn)
    self.assertEqual("5.mp3", object_under_test.download)
    self.assertEqual(None, object_under_test.button_config)

#  def test_illuminate_light(self):
#    object_under_test = poller_thread.PollerThread()
#    object_under_test.illuminate_light(5.0)

  def test_interpretJson(self):
    object_under_test = poller_thread.PollerThread()
    object_under_test.light_duration = 5.0
    object_under_test.trigger_light()

if __name__ == '__main__':
  unittest.main()
