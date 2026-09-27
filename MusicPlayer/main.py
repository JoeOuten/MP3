import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)

    if not os.path.exists(file_path):
        print("File not found!")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top")

    while True:
        command = input("> ").upper()
        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid command!")


def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed:", e)
        return

    folder = "MP3"

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' does not exist")
        return

    #How to get MP3 files
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    while True:
        print("***** MP3 PLAYER *****")
        print("My Song List")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        choice_input = input("\n Enter the song # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("GoodBye!")
            break

        if not choice_input.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice_input) - 1 #Because the computer starts @ 0 this will play the correct choice

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()