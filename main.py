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
# print(id2word)

# # Now that we have the corpus (term-document matrix) and id2word (dictionary of location: term),
# # we need to specify two other parameters as well - the number of topics and the number of passes
# lda = models.LdaModel(corpus=corpus, id2word=id2word, num_topics=2, passes=10)
# print(lda.print_topics())



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


# import time
# import const
# import os.path as path
# import db.db_builder as db_builder

# from api.tmdb import tmdb
from db.repo import movies_repo
from topic_modeling.builder import TopicsBuilder

def convert_tuples_to_dir(movies_data):
    data = {}
    for (movie_name, keyword_name) in movies_data:
        if not movie_name in data:
            data[movie_name] = []
        data[movie_name].append(keyword_name)
    return data

def filter_data(movies_data):
    new_data = {}
    for movie_name in movies_data.keys():
        if (len(movies_data[movie_name]) >= 5):
            new_data[movie_name] = movies_data[movie_name]
    return new_data

# filtering movies maybe
movies_data = movies_repo.get_movies_and_their_keywords()
movies_data = convert_tuples_to_dir(movies_data)
movies_data = filter_data(movies_data)
print(len(movies_data))

topics_builder = TopicsBuilder(movies_data)
topics_builder.run_diagnose(10, 80)
prob = topics_builder.get_probablities()
topics = topics_builder.get_topics()



# if not path.isfile(const.API_PAGE_FILE_NAME):
#     with open(const.API_PAGE_FILE_NAME, "w+") as page_file:
#         page_file.write("0")

# # make api call and store in db every 20 seconds until target
# while movies_repo.count_movies() < const.TOTAL_MOVIES:
#     db_builder.build_movies_keywords_database(tmdb, movies_repo, 1)
#     time.sleep(20)

# topics_builder.build_document_term_matrix(movies_repo)
# topics_builder.run_diagnose(const.NUM_OF_TOPICS, const.NUM_OF_ITER)

# prob = topics_builder.get_probablities()
# topics = topics_builder.get_topics()

























# import re
# import pandas as pd
# import string

# from sklearn.feature_extraction.text import CountVectorizer


# def clean_text(text):
#     '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
#     text = text.lower()
#     text = re.sub('\\[.*?\\]', '', text)
#     text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#     text = re.sub('\\w*\\d\\w*', '', text)
#     text = re.sub('[‘’“”…]', '', text)
#     text = re.sub('\n', '', text)
#     return text


# def combine_text(list_of_text):
#     '''Takes a list of text and combines them into one large chunk of text.'''
#     combined_text = ' '.join(list_of_text)
#     return combined_text

# # array of all movies names
# comedians = ['louis', 'dave', 'ricky', 'bo', 'bill', 'jim', 'john', 'hasan', 'ali', 'anthony', 'mike', 'joe']

# # dict {keyword: ['hello','goodbye']}
# data = {}
# for i, c in enumerate(comedians):
#     with open("nlp-in-python-tutorial/transcripts/" + c + ".txt", "rb") as file:
#         data[c] = pickle.load(file)

# # dict {keyword: ['hello goodbye']}
# data_combined = {key: [combine_text(value)] for (key, value) in data.items()}

# # 
# pd.set_option('max_colwidth',150)

# data_df = pd.DataFrame.from_dict(data_combined).transpose()
# data_df.columns = ['transcript']
# data_df = data_df.sort_index()

# # should clean all keywords and movies 
# data_clean = pd.DataFrame(data_df.transcript.apply(clean_text))

# # document term matrix
# cv = CountVectorizer(stop_words='english')
# data_cv = cv.fit_transform(data_clean.transcript)
# data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
# data_dtm.index = data_clean.index


# # One of the required inputs is a term-document matrix
# tdm = data_dtm.transpose()
# tdm.head()

# # We're going to put the term-document matrix into a new gensim format, from df --> sparse matrix --> gensim corpus
# sparse_counts = scipy.sparse.csr_matrix(tdm)
# corpus = matutils.Sparse2Corpus(sparse_counts)


# # Gensim also requires dictionary of the all terms and their respective location in the term-document matrix
# id2word = dict((v, k) for k, v in cv.vocabulary_.items())

# # Now that we have the corpus (term-document matrix) and id2word (dictionary of location: term),
# # we need to specify two other parameters as well - the number of topics and the number of passes
# lda = models.LdaModel(corpus=corpus, id2word=id2word, num_topics=2, passes=10)
# print(lda.print_topics())