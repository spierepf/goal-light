from .context import goal_light

import RPi.GPIO as GPIO

def setup_module(module):
    GPIO.setmode(GPIO.BOARD)

def teardown_module(module):
    GPIO.cleanup()

def test_construct_light():
    light = goal_light.Light()

def test_trigger_light():
    light = goal_light.Light()
    light.trigger(5.0)
