from tkinter import Tk, Label, Frame, Button, font
from utils import Utils
from MovieItem import MovieItem
from MoviesSeriesController import MoviesSeriesController
from consts import APP_COLS


class MovieFrame:
    controller = MoviesSeriesController()

    def __init__(self, root: Tk, navigation_callback) -> None:
        self._root = root
        self._navigation_callback = navigation_callback
        self.init_frame()

    def init_frame(self):
        utils = Utils()
        label_font = font.Font(family="Arial", size=20, weight="bold")
        movies = self.controller.get_movies()

        movies_frame_container = Frame(self._root)
        movies_frame_container.columnconfigure((0, 1), weight=1)
        movies_frame_container.rowconfigure((0, 1), weight=1)
        movies_frame_container.pack(fill="x")

        movie_section_title = Label(
            movies_frame_container, text="Películas", anchor="w", font=label_font)
        movie_section_title.grid(padx=10, pady=10, column=0, row=0)
        add_button = Button(movies_frame_container,
                            text="Agregar", command=self.__navigate_to_add_movie)
        add_button.grid(padx=10, pady=10, column=1, row=0)

        movie_list = Frame(movies_frame_container)
        utils.config_list_cols(movie_list)
        utils.config_list_row(movies_frame_container, len(movies))
        movie_list.grid(row=1, column=0, columnspan=2)

        col = 1
        row = 1

        for movie in movies:
            MovieItem(movie_list, movie, row, col,
                      lambda card_reference: self.__delete_card(card_reference), self._navigation_callback)
            if (col == APP_COLS):
                col = 1
                row += 1
            else:
                col += 1

    def __delete_card(self, card_reference: Frame):
        card_reference.destroy()

    def __navigate_to_add_movie(self):
        self.controller.set_element_type("película")
        self.controller.set_is_to_update(False, None)
        self._navigation_callback()
