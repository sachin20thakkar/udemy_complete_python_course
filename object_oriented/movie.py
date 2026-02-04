class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def get_info(self):
        return f"{self.title} ({self.year}), directed by {self.director}"
    
border = Movie("Border", "J.P. Dutta", 1997)
print(border.get_info())  # Output: Border (1997), directed by J.P. Dutta
