import csv
import requests
import random
import webbrowser
from os import path
from os import remove
file_url = "https://www.imdb.com/list/ls045750802/export"
file_path = "watchlist.csv"
item_list =[]

class item:
    def __init__(self, id, title, rating, url):
       self.id = id
       self.title = title
       self.rating = rating
       self.url = url 

def main():
    getWatchlist()
    fillList()
    pickRandom()

def getWatchlist():
    if(path.exists(file_path)):
        remove(file_path)
    response = requests.get(file_url)
    open('watchlist.csv','wb').write(response.content)
    print("Watchlist updated.")

def fillList():
    with open('watchlist.csv', 'rt') as d:
        data = csv.reader(d)
        for row in data:
            item_list.append(item(row[0],row[5],row[8],row[6]))

def pickRandom():
    random_id = random.randrange(len(item_list)+1)
    for items in item_list:
        if(items.id == str(random_id)):
            print(f"Picked item: {items.title}")
            webbrowser.open(items.url)

if __name__ == "__main__":
    main()