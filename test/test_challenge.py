from lib.challenge import *

def test_music_tracker():
    music_tracker = MusicTracker()
    music_tracker.add("Yesterday")
    music_tracker.add("Coco Melon")
    music_tracker.add("Dancing Queen")

    result = music_tracker.return_list()
    assert result == ["Yesterday", "Coco Melon", "Dancing Queen"]