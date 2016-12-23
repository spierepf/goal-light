from .context import goal_light

def test_construct_downloader():
    downloader = goal_light.Downloader()

def test_trigger_downloader():
    downloader = goal_light.Downloader()
    downloader.trigger("501")
