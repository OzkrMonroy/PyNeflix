import os
from MovieModel import Movie
from SeriesModel import Series
from consts import ROOT_PATH, MOVIES_AND_SERIES_FILE


class MoviesSeriesController:
    # propiedades o atributos
    _element_type = ""
    _movie = Movie()
    _series = Series()

    # métodos
    def load_movies_and_series(self):
        try:
            movie_and_series_file = open(os.path.abspath(
                f"{ROOT_PATH}\{MOVIES_AND_SERIES_FILE}"), "r", encoding="utf-8")

            for movie_series in movie_and_series_file:
                movie_series = movie_series.rstrip("\n").split(",")
                self.save_movie_series(movie_series)

            movie_and_series_file.close()

        except FileNotFoundError:
            print(f"Sorry, the file {MOVIES_AND_SERIES_FILE} does not exist.")

    def save_movie_series(self, movie_series: list[str]) -> None:
        if (movie_series[1] == "pelicula"):
            self._movie.save(movie_series)
            return

        self._series.save(movie_series)

    def delete_movie(self, movie):
        self._movie.delete(movie)

    def delete_series(self, series):
        self._series.delete(series)

    @classmethod
    def set_element_type(cls, value):
        cls._element_type = value

    @classmethod
    def get_element_type(cls):
        return cls._element_type
