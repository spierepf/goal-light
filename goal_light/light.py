import logging
import threading

import RPi.GPIO as GPIO

class Light:
    def __init__(self):
        self.cv = threading.Condition()

    def thread_body(self, duration):
        self.cv.acquire()

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)

        self.cv.wait(duration)

        GPIO.output(16, GPIO.LOW)
        GPIO.cleanup()

        self.cv.release()

    def trigger(self, duration):
        if duration == None or duration == 0.0:
            logging.info("Extinguishing light because duration zero")
            self.cv.acquire()
            self.cv.notify()
            self.cv.release()
        else:
            threading.Thread(target=self.thread_body, args=(duration,)).start()
