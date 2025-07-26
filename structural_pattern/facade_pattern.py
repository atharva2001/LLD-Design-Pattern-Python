# Subsystems
class DVDPlayer:
    def on(self):
        print("DVD Player ON")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def off(self):
        print("DVD Player OFF")

class Projector:
    def on(self):
        print("Projector ON")

    def off(self):
        print("Projector OFF")

class SoundSystem:
    def on(self):
        print("Sound System ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")

    def off(self):
        print("Sound System OFF")

class Lights:
    def dim(self):
        print("Lights dimmed")

    def on(self):
        print("Lights ON")

# Facade
class HomeTheaterFacade:
    def __init__(self, dvd, projector, sound, lights):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
        self.lights = lights

    def watch_movie(self, movie):
        print("Getting ready to watch a movie...")
        self.lights.dim()
        self.projector.on()
        self.sound.on()
        self.sound.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting down movie theater...")
        self.dvd.off()
        self.sound.off()
        self.projector.off()
        self.lights.on()

# Client code
dvd = DVDPlayer()
projector = Projector()
sound = SoundSystem()
lights = Lights()

home_theater = HomeTheaterFacade(dvd, projector, sound, lights)

home_theater.watch_movie("Inception")
print("\nMovie done!\n")
home_theater.end_movie()
