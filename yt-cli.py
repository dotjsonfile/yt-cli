#!/usr/bin/env python3

import subprocess
import yt_dlp
import argparse


def search_and_play(query):
    ydl_opts = {
        'quiet': True,
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch5:{query}", download=False)['entries']

        if not search_results:
            print("No results found!")
            return

        print("Top 5 results:")
        for i, result in enumerate(search_results):
            print(f"{i + 1}. {result['title']} ({result['url']})")

        try:
            choice = int(input("\nSelect a video number to play: ")) - 1
            if choice < 0 or choice >= len(search_results):
                print("Invalid selection.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        video_url = search_results[choice]['url']
        print(f"\nPlaying: {search_results[choice]['title']}")

        subprocess.run(["mpv", video_url])


def main():
    parser = argparse.ArgumentParser(description="Search and play YouTube videos from the terminal.")
    parser.add_argument("query", help="Search query for YouTube (e.g., 'How to code in Python')")

    args = parser.parse_args()

    print("yt-cli\n")
    search_and_play(args.query)


if __name__ == "__main__":
    main()
