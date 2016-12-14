from .context import goal_light

class MockLight:
    def __init__(self):
        self.duration = None

    def trigger(self, duration):
        self.duration = duration

class MockHorn:
    def __init__(self):
        self.horn = None
        
    def trigger(self, horn):
        self.horn = "horn/" + horn + ".mp3"

class MockDownloader:
    def __init__(self):
        self.url = None
        self.destination = None
        
    def trigger(self, id):
        self.url = "http://lh.meetcweb.com/goal/horns/" + id + ".mp3"
        self.destination = "horn/" + id + ".mp3"

class MockButtonActions:
    def __init__(self):
        self.config = None

    def update_config(self, config):
        print "Updated config: " + str(config)
        self.config = config

def test_construct_json_interpreter():
    interpreter = goal_light.JsonInterpreter()

def test_poll_delay():
    interpreter = goal_light.JsonInterpreter()
    assert 100 == interpreter.interpret('{"d":"100"}')

def test_no_poll_delay():
    interpreter = goal_light.JsonInterpreter()
    assert 300 == interpreter.interpret('{}')

def test_trigger_light():
    light = MockLight()
    interpreter = goal_light.JsonInterpreter(light)
    interpreter.interpret('{"l":"5.0"}')
    assert light.duration == 5.0

def test_no_trigger_light():
    light = MockLight()
    interpreter = goal_light.JsonInterpreter(light)
    interpreter.interpret('{"l":"0.0"}')
    assert light.duration == None

def test_trigger_horn():
    horn = MockHorn()
    interpreter = goal_light.JsonInterpreter(None, horn)
    interpreter.interpret('{"h":"8"}')
    assert horn.horn == "horn/8.mp3"

def test_no_trigger_horn():
    horn = MockHorn()
    interpreter = goal_light.JsonInterpreter(None, horn)
    interpreter.interpret('{"h":"0"}')
    assert horn.horn == None

def test_trigger_download():
    downloader = MockDownloader()
    interpreter = goal_light.JsonInterpreter(None, None, downloader)
    interpreter.interpret('{"dl":"82"}')
    assert downloader.url == "http://lh.meetcweb.com/goal/horns/82.mp3"
    assert downloader.destination == "horn/82.mp3"

def test_no_trigger_download():
    downloader = MockDownloader()
    interpreter = goal_light.JsonInterpreter(None, None, downloader)
    interpreter.interpret('{"dl":"0"}')
    assert downloader.url == None
    assert downloader.destination == None

def test_configure_buttons():
    button_actions = MockButtonActions()
    interpreter = goal_light.JsonInterpreter(None, None, None, button_actions)
    interpreter.interpret('{"b":{"3h":"5","3l":"6.0","2l":"4.0","1h":"1","2h":"3","1l":"2.0"}}')
    assert button_actions.config != None

def test_no_configure_buttons():
    button_actions = MockButtonActions()
    interpreter = goal_light.JsonInterpreter(None, None, None, button_actions)
    interpreter.interpret('{"b":"0"}')
    assert button_actions.config == None
