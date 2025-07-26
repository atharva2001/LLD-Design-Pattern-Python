class OldSong:
    def golden_songs(self, text):
        return f"Some Old Lyrics: {text}"
    

class RockMusic:
    def new_song(self, text):
        pass 

class GenZ(RockMusic):
    def __init__(self, old_songs: OldSong):
        self.old_songs  = old_songs

    def new_song(self, text):
        return self.old_songs.golden_songs(text)


old_song = OldSong()
adapter = GenZ(old_song)

print(adapter.new_song("with some new Rock music"))
