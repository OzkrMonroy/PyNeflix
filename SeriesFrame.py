from tkinter import Tk, Label, Frame, font, Button
from utils import Utils
from SeriesItem import SeriesItem
from MoviesSeriesController import MoviesSeriesController
from consts import APP_COLS


class SeriesFrame:
    controller = MoviesSeriesController()

    def __init__(self, root: Tk, navigation_callback) -> None:
        self._root = root
        self._navigation_callback = navigation_callback
        self.__init_frame()

    def __init_frame(self):
        utils = Utils()
        series = self.controller.get_series()
        label_font = font.Font(family="Arial", size=20, weight="bold")

        series_frame_container = Frame(self._root)
        series_frame_container.columnconfigure((0, 1), weight=1)
        series_frame_container.rowconfigure((0, 1), weight=1)
        series_frame_container.pack(fill="x")

        series_section_title = Label(
            series_frame_container, text="Series", anchor="w", font=label_font)
        series_section_title.grid(padx=10, pady=10, column=0, row=0)
        add_button = Button(series_frame_container,
                            text="Agregar", command=self.__navigate_to_add_series)
        add_button.grid(padx=10, pady=10, column=1, row=0)

        series_list = Frame(series_frame_container)
        utils.config_list_cols(series_list)
        utils.config_list_row(series_frame_container, len(series))
        series_list.grid(row=1, column=0, columnspan=2)

        col = 1
        row = 1

        for movie in series:
            SeriesItem(series_list, movie, row, col,
                       lambda card_reference: self.__delete_card(card_reference), self._navigation_callback)
            if (col == APP_COLS):
                col = 1
                row += 1
            else:
                col += 1

    def __delete_card(self, card_reference: Frame):
        card_reference.destroy()

    def __navigate_to_add_series(self):
        self.controller.set_is_to_update(False, None)
        self.controller.set_element_type("serie")
        self._navigation_callback()
