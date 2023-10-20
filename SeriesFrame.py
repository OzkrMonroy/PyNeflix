from tkinter import Tk, Label, Frame, font
from utils import Utils
from Series import Series
from SeriesItem import SeriesItem
from consts import APP_COLS


class SeriesFrame:
    def __init__(self, root: Tk) -> None:
        self._root = root
        self.__init_frame()

    def __init_frame(self):
        utils = Utils()
        series = Series().get_series()
        label_font = font.Font(family="Arial", size=20, weight="bold")

        series_frame_container = Frame(self._root)
        series_frame_container.pack(fill="x")
        series_section_title = Label(
            series_frame_container, text="Series", anchor="w", font=label_font)
        series_section_title.pack(padx=10, pady=10, fill="x")
        series_list = Frame(series_frame_container)
        utils.config_list_cols(series_list)
        utils.config_list_row(series_frame_container, len(series))
        series_list.pack(fill="x")

        col = 1
        row = 1

        for movie in series:
            SeriesItem(series_list, movie, row, col)
            if (col == APP_COLS):
                col = 1
                row += 1
            else:
                col += 1
