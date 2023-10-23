import os
from Models import MoviesModel, SeriesModel

ROOT_PATH = "C:\Archivos"
MOVIES_AND_SERIES_FILE = "CargaSerie_Pelicula.txt"


class MoviesSeriesController:
    # propiedades o atributos
    _element_type = ""
    _is_update = False
    _element_to_update = {}

    _movie = MoviesModel()
    _series = SeriesModel()

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

    def update_series(self, series):
        self._series.update(series)

    def update_movie(self, movie):
        self._movie.update(movie)

    def get_series(self):
        return self._series.get_series()

    def get_movies(self):
        return self._movie.get_movies()

    @classmethod
    def set_element_type(cls, value):
        cls._element_type = value

    @classmethod
    def get_element_type(cls):
        return cls._element_type

    @classmethod
    def set_is_to_update(cls, is_to_update, element):
        cls._is_update = is_to_update
        cls._element_to_update = element

    @classmethod
    def get_is_to_update(cls):
        return cls._is_update

    @classmethod
    def get_element_to_update(cls):
        return cls._element_to_update
