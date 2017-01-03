from .context import goal_light

def test_construct_horn():
    horn = goal_light.Horn()

def test_trigger_horn():
    horn = goal_light.Horn()
    horn.trigger("0")
