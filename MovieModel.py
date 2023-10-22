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

    def update(self, series: list[str]):
        index = self.__get_element_index(series)
        if (bool(index)):
            self._movies[index] = series

    def __get_element_index(self, series: list[str]):
        index = None
        for i, element in enumerate(self._movies):
            if element["id"] == series[0]:
                index = i
        return index
