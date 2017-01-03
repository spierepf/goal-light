from .context import goal_light

def test_construct_light():
    light = goal_light.Light()

def test_trigger_light():
    light = goal_light.Light()
    light.trigger(5.0)
