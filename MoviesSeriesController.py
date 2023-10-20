import os
from MovieModel import Movie
from SeriesModel import Series
from consts import ROOT_PATH, MOVIES_AND_SERIES_FILE


class MoviesSeriesController:
    def __init__(self) -> None:
        self._movie = Movie()
        self._series = Series()

    def __save_movie_series(self, movie_series: list[str]) -> None:
        if (movie_series[1] == "pelicula"):
            self._movie.save(movie_series)
            return

        self._series.save(movie_series)

    def load_movies_and_series(self):
        try:
            movie_and_series_file = open(os.path.abspath(
                f"{ROOT_PATH}\{MOVIES_AND_SERIES_FILE}"), "r", encoding="utf-8")

            for movie_series in movie_and_series_file:
                movie_series = movie_series.rstrip("\n").split(",")
                self.__save_movie_series(movie_series)

            movie_and_series_file.close()

        except FileNotFoundError:
            print(f"Sorry, the file {MOVIES_AND_SERIES_FILE} does not exist.")

    def delete_movie(self, movie):
        self._movie.delete(movie)
