#!/usr/bin/env python3

import requests
import sys

def fetch_characters(movie_id):
    """
    Fetch and print character names from the specified Star Wars movie ID.

    Args:
        movie_id (int): The ID of the Star Wars movie.
    """
    # Star Wars API URL for films
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data for movie ID {movie_id}")
        return

    movie_data = response.json()
    characters = movie_data.get("characters", [])

    for character_url in characters:
        char_response = requests.get(character_url)
        if char_response.status_code == 200:
            char_data = char_response.json()
            print(char_data.get("name"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./starwars_characters.py <movie_id>")
        sys.exit(1)

    try:
        movie_id = int(sys.argv[1])
    except ValueError:
        print("Movie ID must be an integer")
        sys.exit(1)

    fetch_characters(movie_id)

