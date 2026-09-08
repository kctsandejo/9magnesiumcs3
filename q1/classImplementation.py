class MusicTaste:
    def __init__(self, title: str, artist: str, songs: int, listeners: int):
       
        self.title = title
        self.artist = artist
       
        self.__songs = max(0, songs)
        self.__listeners = max(0, listeners)

    def play_songs(self) -> str:
        
        return f"Now playing '{self.title}' by {self.artist}..."

    def update_listeners(self, count: int) -> None:
        
        if count >= 0:
            self.__listeners = count
            print(f"--> Updated {self.artist}'s monthly listeners to {self.__listeners:,}.")
        else:
            print("--> Error: Listener count cannot be negative.")

    def pin_interests(self) -> str:
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
 
    print("Performing action on Object 1...")
    music1.update_listeners(100000)
    print()

    print("Object 1:", music1.pin_interests())
    print("Object 2:", music2.pin_interests())

 just the general blueprint showing attribute names, data types, and methods. Meanwhile, the object diagram shows the actual state of instances during runtime. Instead of listing data types, the object diagram shows the exact values stored inside music1 and music2 at that moment.