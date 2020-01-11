class Movie:
    def __init__(self, id, title, rate, *keywords):
        self.title = title
        self.id = id
        self.rate = rate
        self.keywords = keywords

    @classmethod
    def parse_json(self, movie, keywords):
        return Movie(movie['id'], movie['title'], movie['vote_average'], keywords)

    def printMe(self):
        print("=======================")
        print("Movie:")
        print("Title: ", self.title)
        print("Id: ", self.id)
        print("Rate: ", self.rate)
        print("Keywords: ", self.keywords)
        print("=======================")
