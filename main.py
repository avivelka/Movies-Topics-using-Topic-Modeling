import pandas as pd
import pickle
import scipy.sparse
from gensim import matutils, models
from urllib import request
from urllib import parse

# pickle_dir = './nlp-in-python-tutorial/pickle/'

# # Let's read in our document-term matrix
# data = pd.read_pickle(pickle_dir + 'dtm_stop.pkl')

# # One of the required inputs is a term-document matrix
# tdm = data.transpose()
# tdm.head()

# # We're going to put the term-document matrix into a new gensim format, from df --> sparse matrix --> gensim corpus
# sparse_counts = scipy.sparse.csr_matrix(tdm)
# corpus = matutils.Sparse2Corpus(sparse_counts)

# # Gensim also requires dictionary of the all terms and their respective location in the term-document matrix
# cv = pickle.load(open(pickle_dir + "cv_stop.pkl", "rb"))
# id2word = dict((v, k) for k, v in cv.vocabulary_.items())

# # Now that we have the corpus (term-document matrix) and id2word (dictionary of location: term),
# # we need to specify two other parameters as well - the number of topics and the number of passes
# lda = models.LdaModel(corpus=corpus, id2word=id2word, num_topics=2, passes=10)
# # print(lda.print_topics())



# # api call 
# # Get all movies published on 2015 sorted by popularity
# # https://api.themoviedb.org/3/discover/movie?api_key=f02638035efb39331179c63490f34c4c&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&year=2015

# from urllib import request
# from urllib import parse
# import json

# apiKey = "f02638035efb39331179c63490f34c4c"
# params = {
#     "api_key": apiKey,
#     "language": "en-US",
#     "sort_by": "popularity.desc",
#     "include_adult": "false",
#     "include_video": "false",
#     "page": "1",
#     "year": "2019",
#     "vote_average.lte":"10",
#     "vote_average.gte":"9"
# }


# queryString = parse.urlencode(params)
# moviesIn2015Url = "https://api.themoviedb.org/3/discover/movie?" + queryString
# response = request.urlopen(moviesIn2015Url)
# moviesInBytes = response.read()
# moviesInStr = moviesInBytes.decode()
# moviesDict = json.loads(moviesInStr)
# moviesDict = moviesDict["results"]

# for movie in moviesDict:
#     print(movie["title"])
#     print(movie["vote_average"])
#     print(movie["id"])

# getMoviesFromYear(year) : Movie[]

# Movie:
# movie.getKeywords()
# movie.getTitle()
# movie.getId()
# movie.getPopularity()
# movie.getRevenue()

# from movie import Movie
# from movie_repo import MovieRepo


# keywords = ["comedy", "airplane"]
# m = Movie("Check", 1, 4.6, *keywords)
# m.printMe()

# repo = Repo()
# movies = movies_repo.get_movies()
# keywords = movies_repo.union_movies_keywords(movies)
# movies_sorted_by_rate = movies_repo.sort_movies_by_rate(movies)

# # topic modeling
# dtm = ai_repo.build_dtm(movies, keywords)
# topics = ai_repo.get_topics()
# movies_to_topics = ai_repo.get_movies_to_topics()


# movie_repo = MovieRepo()
# movies = movie_repo.get_movies(pages=1)
# # movies = movie_repo.get_page(1, 2019)

# for movie in movies:
#     movie.printMe()

# print(len(movies))
# print(movie.keywords)
# keywords = movie_repo.union_keywords(movies)


# movies = movie_repo.request_movies_from_api(1, 2019)
# print(movies)

# print("=================")

# keywords = movie_repo.get_keywords(419704)
# print(keywords)


from db.db_builder import db_builder
from api.tmdb import tmdb
from db.repo import movies_repo
from topic_modeling.builder import topics_builder

NUM_OF_TOPICS = 4
NUM_OF_ITER = 10

db_builder.build_movies_keywords_database(tmdb, movies_repo)

topics_builder.build_document_term_matrix(movies_repo)
topics_builder.run_diagnose(NUM_OF_TOPICS, NUM_OF_ITER)

prob = topics_builder.get_probablities()
topics = topics_builder.get_topics()