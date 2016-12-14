from .context import goal_light

class MockLight:
    def __init__(self):
        self.duration = None

    def trigger(self, duration):
        self.duration = float(duration)

class MockHorn:
    def __init__(self):
        self.horn = None
        
    def trigger(self, horn):
        self.horn = "horn/" + horn + ".mp3"

def test_construct_button_actions():
    button_actions = goal_light.ButtonActions()

def test_update_config():
    button_actions = goal_light.ButtonActions()
    button_actions.update_config({'3h': '5', '3l': '6.0', '2l': '4.0', '1h': '1', '2h': '3', '1l': '2.0'})

def test_trigger_button():
    light = MockLight()
    horn = MockHorn()
    button_actions = goal_light.ButtonActions(light, horn)
    button_actions.update_config({'3h': '5', '3l': '6.0', '2l': '4.0', '1h': '1', '2h': '3', '1l': '2.0'})

    button_actions.trigger('1')
    assert 2.0 == light.duration
    assert "horn/1.mp3" == horn.horn

    button_actions.trigger('2')
    assert 4.0 == light.duration
    assert "horn/3.mp3" == horn.horn

    button_actions.trigger('3')
    assert 6.0 == light.duration
    assert "horn/5.mp3" == horn.horn