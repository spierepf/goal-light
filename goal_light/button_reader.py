import RPi.GPIO as GPIO

class ButtonReader:
    def __init__(self, actions=None):
        self.actions = actions
        self.pins = {
            11 : '1',
            7  : '2',
            12 : '3',
            3  : '4'
        }
        for pin, action in self.pins.iteritems():
            if pin in [2, 3]:
                GPIO.setup(pin, GPIO.IN)
            else:
                GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

            GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=300, callback=lambda: self.actions.trigger(action))
