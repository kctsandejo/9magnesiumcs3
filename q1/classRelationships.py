class MusicTaste:
    """
    Encapsulates an individual's musical interests, tracking details 
    about their favorite song, artist, music library, and artist popularity.
    """
    def __init__(self, listener_name: str, favorite_song: str, favorite_artist: str, artist_popularity: int):
        self.listener_name = listener_name
        self.favorite_song = favorite_song
        self.favorite_artist = favorite_artist
        self.artist_popularity = artist_popularity  # Scale out of 100

    def update_popularity(self, new_popularity: int):
        """Updates the popularity score of the favorite artist."""
        self.artist_popularity = new_popularity

    def __str__(self):
        return f"[{self.listener_name}'s Taste] Song: '{self.favorite_song}' by {self.favorite_artist} (Popularity: {self.artist_popularity}/100)"


class PlayList:
    """
    Organizes lists of audio, songs, or digital media files (MusicTaste profiles)
    that play back in a specific order or on a loop.
    """
    def __init__(self, name: str):
        self.name = name
        # Implements Multiplicity (*) by using an ordered Python list to hold object references
        self._tracks = []

    def add_music_taste(self, music_taste: MusicTaste):
        """Adds a MusicTaste object reference to the playlist."""
        if isinstance(music_taste, MusicTaste):
            self._tracks.append(music_taste)
            print(f"Added {music_taste.listener_name}'s preferences to playlist '{self.name}'.")
        else:
            raise TypeError("Only MusicTaste object instances can be added.")

    def remove_music_taste(self, listener_name: str):
        """Removes a MusicTaste profile from the playlist by listener name."""
        for track in self._tracks:
            if track.listener_name == listener_name:
                self._tracks.remove(track)
                print(f"Removed {listener_name}'s preferences from playlist '{self.name}'.")
                return
        print(f"Listener '{listener_name}' not found in playlist.")

    def display_playlist(self):
        """Prints the ordered tracking items within the playlist."""
        print(f"\n--- PlayList: {self.name} ---")
        if not self._tracks:
            print("  (Playlist is empty)")
        for index, track in enumerate(self._tracks, start=1):
            print(f"  {index}. {track}")
        print("-" * (14 + len(self.name)))


# ==========================================
# TEST RUN DEMONSTRATION
# ==========================================
if __name__ == "__main__":
    print("=== Step 1: Creating MusicTaste Objects ===")
    user1_taste = MusicTaste("Alice", "Blinding Lights", "The Weeknd", 95)
    user2_taste = MusicTaste("Bob", "Bohemian Rhapsody", "Queen", 88)
    user3_taste = MusicTaste("Charlie", "Shape of You", "Ed Sheeran", 91)
    
    print(user1_taste)
    print(user2_taste)
    print(user3_taste)

    print("\n=== Step 2: Creating PlayList & Establishing Association (A-PlayList) ===")
    my_party_playlist = PlayList("Weekend Vibe Share")
    
    # Associating multiple (*) MusicTaste items into one PlayList
    my_party_playlist.add_music_taste(user1_taste)
    my_party_playlist.add_music_taste(user2_taste)
    my_party_playlist.add_music_taste(user3_taste)

    # Show initial list configuration
    my_party_playlist.display_playlist()

    print("\n=== Step 3: Demonstrating Object Reference Value ===")
    print("Modifying Alice's artist popularity score directly via her original object...")
    # Updating the original object reference proves data integrity across associations
    user1_taste.update_popularity(99) 
    
    # Notice that the playlist reflects this change seamlessly because it points to the object reference
    print("Displaying playlist again to verify changes:")
    my_party_playlist.display_playlist()

    print("\n=== Step 4: Removing an Element ===")
    my_party_playlist.remove_music_taste("Bob")
    my_party_playlist.display_playlist()
