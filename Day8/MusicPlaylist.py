# Music Playlist Creator

playlist = []

def show_menu():
    print("\n🎶 Music Playlist Creator")
    print("1. Add a song")
    print("2. Remove a song")
    print("3. Display playlist")
    print("4. Repeat playlist")
    print("5. Search for a song")
    print("6. Exit")

def add_song():
    song = input("Enter song name to add: ").strip()
    playlist.append(song)
    print(f"✅ '{song}' added to playlist.")

def remove_song():
    song = input("Enter song name to remove: ").strip()
    if song in playlist:
        playlist.remove(song)
        print(f"❌ '{song}' removed from playlist.")
    else:
        print(f"⚠️ '{song}' not found in playlist.")

def display_playlist():
    if playlist:
        print("\n🎵 Current Playlist:")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song}")
    else:
        print("📭 Playlist is empty.")

def repeat_playlist():
    times = input("How many times to repeat the playlist? Enter a number: ").strip()
    if times.isdigit():
        repeated = playlist * int(times)
        print("\n🔁 Repeated Playlist:")
        for i, song in enumerate(repeated, 1):
            print(f"{i}. {song}")
    else:
        print("❌ Invalid number.")

def search_song():
    song = input("Enter song name to search: ").strip()
    if song in playlist:
        print(f"🔍 '{song}' is in the playlist.")
    else:
        print(f"❌ '{song}' not found in the playlist.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_song()
    elif choice == "2":
        remove_song()
    elif choice == "3":
        display_playlist()
    elif choice == "4":
        repeat_playlist()
    elif choice == "5":
        search_song()
    elif choice == "6":
        print("👋 Exiting Music Playlist Creator. Enjoy your music!")
        break
    else:
        print("❌ Invalid choice, try again.")
