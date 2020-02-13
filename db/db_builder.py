TOTAL_MOVIES = 3000

def build_movies_keywords_database(tmdb, movies_repo):    
    while movies_repo.count_movies() < TOTAL_MOVIES:
        movies = tmdb.discover_movies()
        keywords = tmdb.get_keywords(movies)
        movies_repo.insert_movies(movies)
        movies_repo.insert_keywords(keywords)
        movies_ids = [movie.id for movie in movies]
        movies_repo.insert_movies_keywords(zip(movies_ids, keywords))