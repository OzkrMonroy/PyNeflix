# Parent Classes

class ParentClass:
    def __init__(self, id, name, duration, rating, genre) -> None:
        self.id = id
        self.name = name
        self.duration = duration
        self.rating = rating
        self.genre = genre


class ParentModel:
    def get_element_index(self, list, elements):
        index = None
        for i, element in enumerate(elements):
            if element.id == list[0]:
                index = i
        return index

# Template to create series
# These use herency because series and movies shared almost all their properties


class Series(ParentClass):
    def __init__(self, id, name, duration, rating, genre, release_date) -> None:
        super().__init__(id, name, duration, rating, genre)
        self.release_date = release_date

# Template to create movies


class Movie(ParentClass):
    def __init__(self, id, name, duration, rating, genre) -> None:
        super().__init__(id, name, duration, rating, genre)


# Models
# These use herency because both use a method to get the index of an element selected (for update)
class SeriesModel(ParentModel):
    _series = []

    def save(self, series_properties: list[str]) -> None:
        series = Series(len(self._series), series_properties[0], series_properties[2],
                        series_properties[3], series_properties[4], series_properties[5])
        self._series.append(series)

    def get_series(self):
        return self._series

    def delete(self, series):
        self._series.remove(series)

    def update(self, series):
        index = self.__get_element_index(series)
        if (index != None):
            self._series[index].name = series[1]
            self._series[index].duration = series[2]
            self._series[index].rating = series[3]
            self._series[index].genre = series[4]
            self._series[index].release_date = series[5]

    def __get_element_index(self, series):
        return super().get_element_index(series, self._series)


# For Movies
class MoviesModel(ParentModel):
    _movies = []

    def save(self, movie_properties: list) -> None:
        movie = Movie(len(
            self._movies), movie_properties[0], movie_properties[2], movie_properties[3], movie_properties[4])
        self._movies.append(movie)

    def get_movies(self) -> list:
        return self._movies

    def delete(self, movie):
        self._movies.remove(movie)

    def update(self, movie):
        index = self.__get_element_index(movie)
        if (index != None):
            self._movies[index].name = movie[1]
            self._movies[index].duration = movie[2]
            self._movies[index].rating = movie[3]
            self._movies[index].genre = movie[4]

    def __get_element_index(self, movie):
        return super().get_element_index(movie, self._movies)
