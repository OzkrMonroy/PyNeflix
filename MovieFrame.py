from tkinter import Tk, Label, Frame, font
from utils import Utils
from MovieModel import Movie
from MovieItem import MovieItem
from consts import APP_COLS


class MovieFrame:
    def __init__(self, root: Tk, navigation_callback) -> None:
        self._root = root
        self._navigation_callback = navigation_callback
        self.init_frame()

    def __delete_card(self, card_reference: Frame):
        card_reference.destroy()

    def __create_items(self, root: Frame, movies: list):
        col = 1
        row = 1

        for movie in movies:
            MovieItem(root, movie, row, col,
                      lambda card_reference: self.__delete_card(card_reference), self._navigation_callback)
            if (col == APP_COLS):
                col = 1
                row += 1
            else:
                col += 1

    def init_frame(self):
        utils = Utils()
        label_font = font.Font(family="Arial", size=20, weight="bold")
        movies = Movie().get_movies()

        movies_frame_container = Frame(self._root)
        movies_frame_container.pack(fill="x")
        movie_section_title = Label(
            movies_frame_container, text="Películas", anchor="w", font=label_font)
        movie_section_title.pack(padx=10, pady=10, fill="x")
        movie_list = Frame(movies_frame_container)
        utils.config_list_cols(movie_list)
        utils.config_list_row(movies_frame_container, len(movies))
        movie_list.pack(fill="x")

        self.__create_items(movie_list, movies)
