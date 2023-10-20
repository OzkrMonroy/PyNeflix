from tkinter import Tk
from utils import Utils
from ScreenManager import ScreenManager
from MoviesSeriesController import MoviesSeriesController


def main() -> None:
    utils = Utils()
    controller = MoviesSeriesController()
    controller.load_movies_and_series()

    window = Tk()
    window.title("PyNeflix")
    window.geometry("1024x600")
    utils.center_window(window, 1024, 600)
    ScreenManager(window)
    window.mainloop()


main()
