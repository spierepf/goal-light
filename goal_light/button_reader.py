class ButtonReader:
    def __init__(self, actions=None):
        self.actions = actions
        self.pins = {
            11 : '1',
            7  : '2',
            12 : '3',
            3  : '4'
        }
        for pin, action in pins.iteritems():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=300, callback=lambda: self.actions.trigger(action))
