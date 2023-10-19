import os
from tkinter import Tk, Frame, Scrollbar, ttk
from Movie import Movie
from Series import Series

ROOT_PATH = "C:\Archivos"
MOVIES_AND_SERIES_FILE = "CargaSerie_Pelicula.txt"


def init_window() -> None:
    window = Tk()
    window.title("PyNetflix")
    window.geometry("768x1024")

    frame = Frame(window)
    frame.pack(fill="both", expand=True)

    scrollbar = Scrollbar(frame, orient="vertical")
    movies_table = ttk.Treeview(frame, columns=(
        "Id", "Name", "Duration", "Rating", "Genre"), show="headings")
    scrollbar.config(command=movies_table.yview)

    scrollbar.pack(side="right", fill="y")
    movies_table.pack(fill="both", expand=True)

    movies_table.heading("#1", text="Id")
    movies_table.heading("#2", text="Name")
    movies_table.heading("#3", text="Duration")
    movies_table.heading("#4", text="Rating")
    movies_table.heading("#5", text="Genre")

    movies = Movie().get_movies()
    for movie in movies:
        movies_table.insert("", "end", values=(
            movie["id"], movie["name"], movie["duration"], movie["rating"], movie["genre"]))

    window.mainloop()


def save_movie_series(movie_series: list[str]) -> None:
    if (movie_series[1] == "pelicula"):
        movie = Movie()
        movie.save(movie_series)
        return
    series = Series()
    series.save(movie_series)


def main() -> None:
    try:
        movie_and_series_file = open(os.path.abspath(
            f"{ROOT_PATH}\{MOVIES_AND_SERIES_FILE}"), "r", encoding="utf-8")

        for movie_series in movie_and_series_file:
            movie_series = movie_series.rstrip("\n").split(",")
            save_movie_series(movie_series)

        movie_and_series_file.close()
        init_window()

    except FileNotFoundError:
        print(f"Sorry, the file {MOVIES_AND_SERIES_FILE} does not exist.")


main()
