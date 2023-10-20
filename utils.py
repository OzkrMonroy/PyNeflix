from tkinter import Tk, Frame
from consts import APP_COLS


class Utils:
    def center_window(self, window: Tk, width: int, height: int):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = int((screen_width/2) - (width / 2))
        y = int((screen_height/2) - (height / 2))

        return window.geometry(f"{width}x{height}+{x}+{y}")

    def config_list_cols(self, frame: Frame):
        for col in range(APP_COLS):
            frame.columnconfigure(col, weight=1)

    def config_list_row(self, frame: Frame, row_quantity: int):
        for row in range(row_quantity):
            frame.rowconfigure(row, weight=1)
