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

