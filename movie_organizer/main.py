# main.py

from movie_ops import add_movie, remove_movie
from search_ops import (
    search_by_actor, search_by_genre,
    group_by_genre, get_unique_genres, get_unique_actors
)

movies = []

# Sample Data
add_movie(movies, "Inception", 2010, ["Sci-Fi", "Thriller"], ["Leonardo DiCaprio", "Joseph Gordon-Levitt"])
add_movie(movies, "The Dark Knight", 2008, ["Action", "Drama"], ["Christian Bale", "Heath Ledger"])
add_movie(movies, "Titanic", 1997, ["Romance", "Drama"], ["Leonardo DiCaprio", "Kate Winslet"])

# Search by actor
print("\n🎭 Movies with Leonardo DiCaprio:")
for m in search_by_actor(movies, "Leonardo DiCaprio"):
    print(f"- {m['id'][0]} ({m['id'][1]})")

# Group by genre
print("\n🎞️ Movies grouped by genre:")
grouped = group_by_genre(movies)
for genre, films in grouped.items():
    print(f"{genre}: {[m['id'][0] for m in films]}")

# Unique genres and actors
print("\n📚 Unique Genres:", ", ".join(sorted(get_unique_genres(movies))))
print("🎬 Unique Actors:", ", ".join(sorted(get_unique_actors(movies))))
