class songs:
    def __init__(self, name, album, artist, length, year):
        self.name=name
        self.album=album
        self.artist=artist
        self.length=length
        self.year=year
    def show_info(self):
        print("track", self.name, "-", self.artist, "length", self.length//60,":", self.length%60)
song1=songs("I_stay", "Nezha - Single", "Ars", 183, 2026)
song2=songs("I_stay (Instrumental)", "Nezha - Single", "Ars", 183, 2026)
song3=songs("KILLA (Face the other me)", "CRACK CODE - EP", "Kep1er", 176, 2026)
class media:
    def __init__(self):
        self.songs=[]
    def add_songs(self, songs):
        self.songs.append(songs)
        print(songs.name, "была добавлена!")
    def show_all_songs(self):
        for i in self.songs:
            i.show_info()

streaming=media()
streaming.add_songs(song1)
streaming.add_songs(song2)
streaming.add_songs(song3)
streaming.show_all_songs()