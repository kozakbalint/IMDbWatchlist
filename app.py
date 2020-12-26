"""imports"""
from os import path, remove
import random
import webbrowser
import csv
import requests

FILE_URL = "https://www.imdb.com/list/ls045750802/export"
FILE_PATH = "watchlist.csv"
ITEM_LIST = []


class Item:
    """A movie or a TV show information."""

    def __init__(self, imdb_id, title, rating, url):
        self.imdb_id = imdb_id
        self.title = title
        self.rating = rating
        self.url = url


def main():
    """The main function."""
    get_watchlist()
    fill_list()
    pick_random()


def get_watchlist():
    """Get the watchlist from IMDb."""
    if path.exists(FILE_PATH):
        remove(FILE_PATH)
    response = requests.get(FILE_URL)
    open("watchlist.csv", "wb").write(response.content)
    print("Watchlist updated.")


def fill_list():
    """Fill a list with films and Tv shows from my IMDb watchlist."""
    with open("watchlist.csv", "r", encoding="ISO-8859-1") as data:
        data = csv.reader(data)
        for row in data:
            ITEM_LIST.append(Item(row[0], row[5], row[8], row[6]))


def pick_random():
    """Pick a random item (movie or TV show) from the list."""
    random_id = random.randrange(len(ITEM_LIST) + 1)
    for items in ITEM_LIST:
        if items.imdb_id == str(random_id):
            print(f"Picked item: {items.title}")
            webbrowser.open(items.url)


if __name__ == "__main__":
    main()
