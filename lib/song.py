class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)


    @classmethod
    def add_song_to_count (cls):
        cls.count += 1

    @classmethod
    def add_to_genres (cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        cls.add_to_genre_count(genre)

    @classmethod
    def add_to_artists (cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def add_to_genre_count (cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1