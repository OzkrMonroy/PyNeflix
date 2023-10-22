from tkinter import Tk
from MovieFrame import MovieFrame
from SeriesFrame import SeriesFrame
from AddElement import AddElement
from MoviesSeriesController import MoviesSeriesController
from utils import Utils


class ScreenManager:
    current_page: Tk | None = None
    _utils = Utils()

    def __init__(self) -> None:
        controller = MoviesSeriesController()
        controller.load_movies_and_series()

    def __destroy_current_page(self):
        if (self.current_page):
            self.current_page.destroy()

    def show_home_page(self):
        self.__destroy_current_page()
        window = Tk()
        window.title("PyNeflix")
        window.geometry("1024x600")
        self._utils.center_window(window, 1024, 600)
        MovieFrame(window, self.show_add_page)
        SeriesFrame(window, self.show_add_page)
        self.current_page = window
        window.mainloop()

    def show_add_page(self):
        self.__destroy_current_page()
        window = Tk()
        window.title("PyNeflix - Add")
        window.geometry("1024x600")
        self._utils.center_window(window, 1024, 600)
        AddElement(window, self.show_home_page)
        self.current_page = window
        window.mainloop()
