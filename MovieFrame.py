from tkinter import Tk, Label, Frame, font
from utils import Utils
from Movie import Movie
from MovieItem import MovieItem
from consts import APP_COLS


class MovieFrame:
    def __init__(self, root: Tk) -> None:
        self._root = root
        self.__init_frame()

    def __init_frame(self):
        utils = Utils()
        movies = Movie().get_movies()
        label_font = font.Font(family="Arial", size=20, weight="bold")

        movies_frame_container = Frame(self._root)
        movies_frame_container.pack(fill="x")
        movie_section_title = Label(
            movies_frame_container, text="Películas", anchor="w", font=label_font)
        movie_section_title.pack(padx=10, pady=10, fill="x")
        movie_list = Frame(movies_frame_container)
        utils.config_list_cols(movie_list)
        utils.config_list_row(movies_frame_container, len(movies))
        movie_list.pack(fill="x")

        col = 1
        row = 1

        for movie in movies:
            MovieItem(movie_list, movie, row, col)
            if (col == APP_COLS):
                col = 1
                row += 1
            else:
                col += 1
