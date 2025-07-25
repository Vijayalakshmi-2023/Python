class CircularPlaylist:
    def __init__(self, songs):
        if not songs:
            raise ValueError("Playlist cannot be empty.")
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        song = self.songs[self.index]
        self.index = (self.index + 1) % len(self.songs)  # wrap around
        return song
