class MusicTracker:
    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def return_list(self):
        return self.track_list