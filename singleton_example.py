class GameSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}  # Initialize settings dictionary
        return cls._instance

    def set_setting(self, name, value):
        self._settings[name] = value

    def get_setting(self, name):
        return self._settings.get(name)


settings1 = GameSettings()
settings2 = GameSettings()

settings1.set_setting("volume", 80)
settings2.set_setting("difficulty", "hard")

print(settings1.get_setting("volume"))       # Output: 80
print(settings2.get_setting("difficulty"))   # Output: hard
print(settings1 is settings2)                # Output: True
