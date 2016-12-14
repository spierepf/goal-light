import os
from .context import goal_light

def test_construct_json_source():
    source = goal_light.JsonSource('data.json')

def test_trigger_light():
    source = goal_light.JsonSource('data.json')
    with open('data.json', "w") as text_file:
        text_file.write("text")
    assert "text" == source.read()
    os.remove('data.json')