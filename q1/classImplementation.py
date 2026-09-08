class MusicTaste:
    def __init__(self, title: str, artist: str, songs: int, listeners: int):
        # Public attributes: Accessible freely by external code for display purposes
        self.title = title
        self.artist = artist
        
        # Private attributes: Prefixed with two underscores (__) to prevent 
        # direct modification and protect data integrity
        self.__songs = max(0, songs)
        self.__listeners = max(0, listeners)

    def play_songs(self) -> str:
        """Simulates playing the selected song (Reads/Returns object state)."""
        return f"Now playing '{self.title}' by {self.artist}..."

    def update_listeners(self, count: int) -> None:
        """
        Receives a parameter and safely modifies a private changing attribute.
        Includes a safety check to ensure listener values cannot be negative.
        """
        if count >= 0:
            self.__listeners = count
            print(f"--> Updated {self.artist}'s monthly listeners to {self.__listeners:,}.")
        else:
            print("--> Error: Listener count cannot be negative.")

    def pin_interests(self) -> str:
        """Safely reads and formats summary info including private attributes."""
        return (f"Title: '{self.title}' | Artist: {self.artist} | "
                f"Saved Songs: {self.__songs} | Monthly Listeners: {self.__listeners:,}")


if __name__ == "__main__":
    # Step 6: Instantiate two independent objects from the same class blueprint
    music1 = MusicTaste("Bohemian Rhapsody", "Queen", 45, 50000)
    music2 = MusicTaste("Piledriver Waltz", "Arctic Monkeys", 120, 85000000)

    # Step 8: Display the initial state of both objects before making any changes
    print("--- BEFORE ---")
    print("Object 1:", music1.pin_interests())
    print("Object 2:", music2.pin_interests())
    print()

    # Step 7: Modify state for Object 1 ONLY using its state-changing method
    print("Performing action on Object 1...")
    music1.update_listeners(100000)
    print()

    # Step 8: Display updated states to prove Object 1 changed while Object 2 remained untouched
    print("--- AFTER ---")
    print("Object 1:", music1.pin_interests())
    print("Object 2:", music2.pin_interests())