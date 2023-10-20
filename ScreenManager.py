from tkinter import Tk
from MovieFrame import MovieFrame
from SeriesFrame import SeriesFrame


class ScreenManager:
    def __init__(self, root: Tk) -> None:
        self._root = root
        self.show_home_page()

    def show_home_page(self):
        MovieFrame(self._root)
        SeriesFrame(self._root)
