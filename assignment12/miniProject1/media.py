
class Media:
    def __init__(self, id, name, director, IMDB_score, url, duration, casts):
        self.id = id
        self.name = name
        self.director = director
        self.IMDB_score = IMDB_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def show_info(self):
        ...
    
    def download(self):
        ...
    
