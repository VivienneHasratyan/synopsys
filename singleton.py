class MusicPlayer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._current_song = None
        return cls._instance

    def play(self, song):
        self._current_song = song
        print(f"Playing: {song}")

    def stop(self):
        print(f"Stopped: {self._current_song}")
        self._current_song = None

player1 = MusicPlayer()
player2 = MusicPlayer()

player1.play("Imagine - John Lennon")
player2.stop()

print(player1 is player2)