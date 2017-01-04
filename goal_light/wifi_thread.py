import logging
import threading
import os

import RPi.GPIO as GPIO

class WifiThread:
    def __init__(self):
        self.thread = None
        self.cv = threading.Condition()
        self.running = False

    def thread_body(self):
        logging.info("Starting wifi_thread.")
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)

        while self.running:
            if os.system("ping -c 1 24.222.0.94 >/dev/null 2>&1") == 0:
                GPIO.output(13, GPIO.HIGH)
            else:
                GPIO.output(13, GPIO.LOW)

            self.cv.acquire()
            self.cv.wait(30)
            self.cv.release()

        GPIO.output(13, GPIO.LOW)

    def start(self):
        if self.thread == None:
            self.running = True
            self.thread = threading.Thread(target=self.thread_body)
            self.thread.start()

    def stop(self):
        if self.thread != None:
            self.cv.acquire()
            self.running = False
            self.cv.notify()
            self.cv.release()
            self.thread.join()
            self.thread = None
