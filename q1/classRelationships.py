class MusicTaste:
   # Encapsulates an individual's musical interests, tracking details about their favorite song, artist, music library, and artist popularity.
  
    def __init__(self, listener_name: str, favorite_song: str, favorite_artist: str, artist_popularity: int):
        self.listener_name = listener_name
        self.favorite_song = favorite_song
        self.favorite_artist = favorite_artist
        self.artist_popularity = artist_popularity  # out of 100

    def update_popularity(self, new_popularity: int):
        #popularity score
        self.artist_popularity = new_popularity

    def __str__(self):
        return f"[{self.listener_name}'s Taste] Song: '{self.favorite_song}' by {self.favorite_artist} (Popularity: {self.artist_popularity}/100)"


class PlayList:
    """
    organizes lists of audio, songs, or digital media files
    """
    def __init__(self, name: str):
        self.name = name
        self._tracks = []

    def add_music_taste(self, music_taste: MusicTaste):
        if isinstance(music_taste, MusicTaste):
            self._tracks.append(music_taste)
            print(f"Added {music_taste.listener_name}'s preferences to playlist '{self.name}'.")
        else:
            raise TypeError("Only MusicTaste object instances can be added.")
#checks for errors, only musictaste

    def remove_music_taste(self, listener_name: str):
        for track in self._tracks:
            if track.listener_name == listener_name:
                self._tracks.remove(track)
                print(f"Removed {listener_name}'s preferences from playlist '{self.name}'.")
                return
        print(f"Listener '{listener_name}' not found in playlist.")

    def display_playlist(self):
        print(f"\n--- PlayList: {self.name} ---")
        if not self._tracks:
            print("  (Playlist is empty)")
        for index, track in enumerate(self._tracks, start=1):
            print(f"  {index}. {track}")
        print("-" * (14 + len(self.name)))
#Test run     
if __name__ == "__main__":
    print("Step 1: Creating MusicTaste Objects")
    user1_taste = MusicTaste("Alice", "Circles", "Post Malone", 95)
    user2_taste = MusicTaste("Bob", "Bohemian Rhapsody", "Queen", 88)
    user3_taste = MusicTaste("Guo", "Shape of You", "Ed Sheeran", 91)

    print(user1_taste)
    print(user2_taste)
    print(user3_taste)

    print(" Step 2: Creating PlayList & Establishing Association (A-PlayList)")
    my_party_playlist = PlayList("Weekendz")

    # multiple MusicTaste into 1 playlist
    my_party_playlist.add_music_taste(user1_taste)
    my_party_playlist.add_music_taste(user2_taste)
    my_party_playlist.add_music_taste(user3_taste)

    # initial config
    my_party_playlist.display_playlist()

    print("\n=== Step 3: Demonstrating Object Reference Value ===")
    print("Modifying Alice's artist popularity score directly via her original object")
    # proves data integrity and consistency across associations
    user1_taste.update_popularity(99) 
  
    #  playlist reflects change from object reference 
    print("Displaying playlist again to verify changes:")
    my_party_playlist.display_playlist()

    print(" Step 4: Removing an Element")
    my_party_playlist.remove_music_taste("Bob")
    my_party_playlist.display_playlist()