from .context import goal_light

class MockLight:
    def trigger(self, duration):
        self.duration = duration

class MockHorn:
    def trigger(self, horn):
        self.horn = horn

def test_construct_json_interpreter():
    interpreter = goal_light.JsonInterpreter()

def test_trigger_light():
    light = MockLight()
    interpreter = goal_light.JsonInterpreter(light)
    interpreter.interpret('{"l":"5.0"}')
    assert light.duration == 5.0

def test_trigger_horn():
    horn = MockHorn()
    interpreter = goal_light.JsonInterpreter(None, horn)
    interpreter.interpret('{"h":"8"}')
    assert horn.horn == "horn/8.mp3"
