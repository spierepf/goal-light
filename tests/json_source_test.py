import os
from .context import goal_light

def test_construct_json_source():
    source = goal_light.JsonSource('data.json')

def test_read_data():
    source = goal_light.JsonSource('data.json')
    with open('data.json', "w") as text_file:
        text_file.write("text")
    assert "text" == source.read()
    try:
        os.remove('data.json')
    except:
        pass

def test_no_data():
    source = goal_light.JsonSource('data.json')
    assert "" == source.read()
