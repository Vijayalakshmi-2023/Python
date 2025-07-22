# movie_ops.py

def add_movie(movies, title, year, genres, actors):
    movie_id = (title, year)
    movie = {
        "id": movie_id,
        "genre": set(genres),
        "actors": list(actors)
    }
    movies.append(movie)
    return f"✅ Movie added: {title} ({year})"

def remove_movie(movies, title, year):
    for movie in movies:
        if movie["id"] == (title, year):
            movies.remove(movie)
            return f"🗑️ Movie removed: {title} ({year})"
    return "❌ Movie not found."
