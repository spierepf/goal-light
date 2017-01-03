import logging
import threading

import RPi.GPIO as GPIO

class Light:
    def __init__(self):
        self.thread = None
        self.cv = threading.Condition()

    def thread_body(self, duration):
        self.cv.acquire()

        logging.info("Triggering light for up to: " + str(duration) + " seconds.")
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)

        self.cv.wait(duration)

        GPIO.output(16, GPIO.LOW)
        GPIO.cleanup()
        logging.info("Light extinguished")

        self.cv.release()

    def trigger(self, duration):
        if self.thread:
            self.cv.acquire()
            self.cv.notify()
            self.cv.release()
            self.thread.join()
            self.thread = None
            
        if duration != None and duration != 0.0:
            self.thread = threading.Thread(target=self.thread_body, args=(duration,))
            self.thread.start()
