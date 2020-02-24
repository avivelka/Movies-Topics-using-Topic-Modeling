from db.repo import movies_repo
from topic_modeling.builder import TopicsBuilder
import const


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

movies_data = movies_repo.get_movies_and_their_keywords()
movies_data = convert_tuples_to_dir(movies_data)
movies_data = filter_data(movies_data)

topics_builder = TopicsBuilder(movies_data)
topics_builder.run_diagnose(10, 50)
prob = topics_builder.get_probablities()
# [(movie_name, topic)]
movies_names_topics = topics_builder.get_topics()

# [(movie, topic)]
movies_topics = [(movies_repo.get_movie_by_name(name)[0], topic) for name, topic in movies_names_topics]
movies_topics_sorted_by_popularity = sorted(movies_topics, key=lambda movie_topic: movie_topic[0][4], reverse=True)

def limit_to_at_most_100_movies_per_year(movies_topics):
    movies_by_year = {}
    for movie, topic in movies_topics:
        year = movie[2][:4]
        if not year in movies_by_year:
            movies_by_year[year] = []
        if len(movies_by_year[year]) < 100:
            movies_by_year[year].append((movie, topic))
    return movies_by_year


movies_by_years = limit_to_at_most_100_movies_per_year(movies_topics_sorted_by_popularity)

def split_movies_to_topics(movies_by_years):
    movies_by_years_and_topics = {}
    for year in movies_by_years:
        if not year in movies_by_years_and_topics:
            movies_by_years_and_topics[year] = {}
        for movie, topic in movies_by_years[year]:
            topic = str(topic)
            if not topic in movies_by_years_and_topics[year]:
                movies_by_years_and_topics[year][topic] = []
            movies_by_years_and_topics[year][topic].append(movie[3])
    return movies_by_years_and_topics

movies_by_years_and_topics = split_movies_to_topics(movies_by_years)


movies_and_topics_arr = movies_names_topics
popularity_arr = []

topics_years = set()

for x in movies_and_topics_arr:
    tmp_movie = movies_repo.get_movie_by_name(x[0])
    tmp_movie = tmp_movie[0]
    year = tmp_movie[2]
    year = year[:4]
    topics_years.add((year, x[1], tmp_movie))
    popularity = tmp_movie[4]
    popularity_arr.append(popularity)

i = 0
movies_topics_popularity = []
for x in movies_and_topics_arr:
    x = x + (popularity_arr[i],)
    i = i+1
    movies_topics_popularity.append(x)

sorted_by_popularity = sorted(movies_topics_popularity, key=lambda tup: tup[2])
sorted_by_popularity.reverse()

years_topics_dict = {}
for year,topic,movie in topics_years:
    topic = str(topic)
    if not year in years_topics_dict:
        years_topics_dict[year] = {}
    if not topic in years_topics_dict[year]:
        years_topics_dict[year][topic] = []
    years_topics_dict[year][topic].append(movie)


hundred_popular_movies = []
i = 0
for x in sorted_by_popularity:
    if i < 100:
        hundred_popular_movies.append(x)
        i = i + 1


# print(hundred_popular_movies)

topic_0 = set()
topic_1 = set()
topic_2 = set()
topic_3 = set()
topic_4 = set()
topic_5 = set()
topic_6 = set()
topic_7 = set()
topic_8 = set()
topic_9 = set()


for x in hundred_popular_movies:
    if x[1] == 0:
        topic_0.add(x)
    elif x[1] == 1:
        topic_1.add(x)
    elif x[1] == 2:
        topic_2.add(x)
    elif x[1] == 3:
        topic_3.add(x)
    elif x[1] == 4:
        topic_4.add(x)  
    elif x[1] == 5:
        topic_5.add(x)
    elif x[1] == 6:
        topic_6.add(x)
    elif x[1] == 7:
        topic_7.add(x)
    elif x[1] == 8:
        topic_8.add(x)
    else:
        topic_9.add(x)

# print("lenght of topic 0: " , len(topic_0))
# print("lenght of topic 1: " , len(topic_1))
# print("lenght of topic 2: " , len(topic_2))
# print("lenght of topic 3: " , len(topic_3))
# print("lenght of topic 4: " , len(topic_4))
# print("lenght of topic 5: " , len(topic_5))
# print("lenght of topic 6: " , len(topic_6))
# print("lenght of topic 7: " , len(topic_7))
# print("lenght of topic 8: " , len(topic_8))
# print("lenght of topic 9: " , len(topic_9))

