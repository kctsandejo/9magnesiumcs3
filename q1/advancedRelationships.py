
# part 1: inheritance (IS-A Relationship)
class MusicTaste:
    """
    Parent Class: Encapsulates basic listener preferences.
    """
    def __init__(self, listener_name: str, favorite_song: str, favorite_artist: str, artist_popularity: int):
        self.listener_name = listener_name
        self.favorite_song = favorite_song
        self.favorite_artist = favorite_artist
        self.artist_popularity = artist_popularity  # Out of 100

    def update_popularity(self, new_popularity: int):
        self.artist_popularity = new_popularity

    def __str__(self):
        return f"[{self.listener_name}'s Taste] Song: '{self.favorite_song}' by {self.favorite_artist} (Popularity: {self.artist_popularity}/100)"


class PremiumMusicTaste(MusicTaste):
    """
    Child Class: Inherits from MusicTaste and adds listening mode.
    """
    def __init__(self, listener_name: str, favorite_song: str, favorite_artist: str, artist_popularity: int, listening_mode: str):
        # reinitializ using super().__init__()
        super().__init__(listener_name, favorite_song, favorite_artist, artist_popularity)
        self.listening_mode = listening_mode

    def __str__(self):
        return f"[PREMIUM - {self.listener_name}] Song: '{self.favorite_song}' by {self.favorite_artist} | Mode: {self.listening_mode}"



# part 2: composition ( Strong HAS-A relationship)
class PlayListInfo:
    # holds playlist created exclusively by PlayList
    
    def __init__(self, created_date: str, genre: str):
        self.created_date = created_date
        self.genre = genre

    def __str__(self):
        return f"Genre: {self.genre} | Created: {self.created_date}"


class PlayList:
   # manages tracks and owns PlayListInfo
    
    def __init__(self, name: str, created_date: str, genre: str):
        self.name = name
        self._tracks = []
        # Composition
        self.info = PlayListInfo(created_date, genre)

    def add_music_taste(self, music_taste: MusicTaste):
        if isinstance(music_taste, MusicTaste):
            self._tracks.append(music_taste)
            print(f"Added {music_taste.listener_name}'s preferences to playlist '{self.name}'.")
        else:
            raise TypeError("Only MusicTaste or PremiumMusicTaste objects can be added.")

    def remove_music_taste(self, listener_name: str):
        for track in self._tracks:
            if track.listener_name == listener_name:
                self._tracks.remove(track)
                print(f"Removed {listener_name}'s preferences from playlist '{self.name}'.")
                return
        print(f"Listener '{listener_name}' not found in playlist.")

    def display_playlist(self):
        print(f" PlayList: {self.name} ({self.info})")
        if not self._tracks:
            print("  (Playlist is empty)")
        for index, track in enumerate(self._tracks, start=1):
            print(f"  {index}. {track}")
        print("-" * 60)


# Test run
if __name__ == "__main__":
    print("=== Step 1: Creating Regular and Premium Objects (Inheritance) ===")
    user1_taste = MusicTaste("Alice", "Circles", "Post Malone", 95)
    user2_taste = MusicTaste("Bob", "Bohemian Rhapsody", "Queen", 88)
    user3_taste = PremiumMusicTaste("Guo", "Shape of You", "Ed Sheeran", 91, listening_mode="Spatial Audio / Lossless")

    print(user1_taste)
    print(user2_taste)
    print(user3_taste)

    print(" Step 2: Creating PlayList with Composition")
    my_party_playlist = PlayList("Weekendz", created_date="2026-09-24", genre="Pop/Hits")

    # add regular and premium objects into the playlist
    my_party_playlist.add_music_taste(user1_taste)
    my_party_playlist.add_music_taste(user2_taste)
    my_party_playlist.add_music_taste(user3_taste)

    # initial display
    my_party_playlist.display_playlist()

    print("Step 3: Demonstrating Object Reference Value")
    print("Modifying Alice's artist popularity score directly via her original object")
    user1_taste.update_popularity(99)

    print("Displaying playlist again to verify changes:")
    my_party_playlist.display_playlist()

    print("Step 4: Removing an Element")
    my_party_playlist.remove_music_taste("Bob")
    my_party_playlist.display_playlist()
