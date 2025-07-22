# search_ops.py

def search_by_actor(movies, actor_name):
    return [m for m in movies if actor_name in m["actors"]]

def search_by_genre(movies, genre):
    return [m for m in movies if genre in m["genre"]]

def group_by_genre(movies):
    genre_map = {}
    for m in movies:
        for genre in m["genre"]:
            genre_map.setdefault(genre, []).append(m)
    return genre_map

def get_unique_genres(movies):
    return {genre for m in movies for genre in m["genre"]}

def get_unique_actors(movies):
    return {actor for m in movies for actor in m["actors"]}
