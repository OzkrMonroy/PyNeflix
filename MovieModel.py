class Movie:
    _movies = []

    def save(self, movie_properties: list) -> None:
        movie_ob = {
            "id": len(self._movies),
            "name": movie_properties[0],
            "duration": movie_properties[2],
            "rating": movie_properties[3],
            "genre": movie_properties[4]
        }
        self._movies.append(movie_ob)

    def get_movies(self) -> list:
        return self._movies

    def delete(self, movie):
        self._movies.remove(movie)
