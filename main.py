from letterboxdpy.user import User
from letterboxdpy.watchlist import Watchlist
import random

USERNAME = "convlict"

def main():
  print("Random movie generator")
  print(f"Loading {USERNAME}'s watchlist")
  titles = []
  watchlist = Watchlist(USERNAME)
  movies = watchlist.movies
  for key, value in movies.items():
    for title in value:
      if title == "name":
        titles.append(value[title])

  movie_choice = random.choice(titles)

  print(f"\nYou got: \n\n\"{movie_choice}\"\n\nHave fun!")


if __name__ == "__main__":
  main()
