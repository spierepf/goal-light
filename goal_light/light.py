import logging
import RPi.GPIO as GPIO

class Light:
    def __init__(self):
        GPIO.setup(self.light_gpio, GPIO.OUT)

    def trigger(self, duration):
        logging.info("Triggering light for " + str(float(duration)) + " seconds")
        GPIO.output(self.light_gpio, 1)
        time.sleep(duration)
        GPIO.output(self.light_gpio, 0)
