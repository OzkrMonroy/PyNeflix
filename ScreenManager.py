from tkinter import Tk, Frame, Label, Button, messagebox, font
from AddElement import AddElement
from MoviesSeriesController import MoviesSeriesController

APP_COLS = 5


class ListItem:
    controller = MoviesSeriesController()

    def __init__(self, root: Frame, element, row: int, col: int, delete_callback, navigation_callback, is_movie) -> None:
        self._element = element
        self._row = row
        self._col = col
        self._root = root
        self._delete_callback = delete_callback
        self._navigation_callback = navigation_callback
        self._is_movie = is_movie
        self._element_type = "pelicula" if is_movie else "serie"
        self.__build_item()

    def __edit_series(self):
        self.controller.set_element_type(self._element_type)
        self.controller.set_is_to_update(True, self._element)
        self._navigation_callback()

    def __delete_series(self, card_reference: Frame):
        response = messagebox.askyesno(
            "Eliminar", f"¿Esta seguro que quiere eliminar la {self._element_type}: {self._element.name}?")
        if (response):
            if (self._is_movie):
                self.controller.delete_movie(self._element)
            else:
                self.controller.delete_series(self._element)
            self._delete_callback(card_reference)

    def __build_item(self):
        frame = Frame(self._root, width=200, height=200,
                      borderwidth=2, relief="groove")
        frame.grid(row=self._row, column=self._col,
                   padx=10, pady=10, sticky="we")

        card = Frame(frame)
        card.columnconfigure((0, 1), weight=1)
        card.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        card.pack(padx=10, pady=10)

        card_title = Label(card, text=self._element.name)
        card_title.grid(row=0, column=0, sticky="ew", columnspan=2)

        duration_title = "Duración:" if self._is_movie else "Temporadas:"
        card_duration_label = Label(card, text=duration_title)
        card_duration_label.grid(row=1, column=0, sticky="w")
        card_duration = Label(card, text=self._element.duration)
        card_duration.grid(row=1, column=1, sticky="e")

        card_duration_label = Label(card, text="Clasificación:")
        card_duration_label.grid(row=2, column=0, sticky="w")
        card_duration = Label(card, text=self._element.rating)
        card_duration.grid(row=2, column=1, sticky="e")

        card_duration_label = Label(card, text="Género:")
        card_duration_label.grid(row=3, column=0, sticky="w")
        card_duration = Label(card, text=self._element.genre)
        card_duration.grid(row=3, column=1, sticky="e")

        if (not self._is_movie):
            card_duration_label = Label(card, text="Fecha de lanzamiento:")
            card_duration = Label(card, text=self._element.release_date)
            card_duration_label.grid(row=4, column=0, sticky="w")
            card_duration.grid(row=4, column=1, sticky="e")

        row_index = 4 if self._is_movie else 5
        edit_button = Button(card, text="Editar", command=self.__edit_series)
        edit_button.grid(row=row_index, column=1, sticky="e", pady=8)
        delete_button = Button(card, text="Eliminar",
                               command=lambda: self.__delete_series(frame))
        delete_button.grid(row=row_index, column=0, sticky="w", pady=8)


class ListFrame:
    controller = MoviesSeriesController()

    def __init__(self, root: Tk, navigation_callback, is_movie) -> None:
        self._root = root
        self._navigation_callback = navigation_callback
        self._is_movie = is_movie
        self.__init_frame()

    def __init_frame(self):
        elements = []
        if (self._is_movie):
            elements = self.controller.get_movies()
        else:
            elements = self.controller.get_series()
        label_font = font.Font(family="Arial", size=20, weight="bold")

        series_frame_container = Frame(self._root)
        series_frame_container.columnconfigure((0, 1), weight=1)
        series_frame_container.rowconfigure((0, 1), weight=1)
        series_frame_container.pack(fill="x")

        title = "Películas" if self._is_movie else "Series"
        series_section_title = Label(
            series_frame_container, text=title, anchor="w", font=label_font)
        series_section_title.grid(padx=10, pady=10, column=0, row=0)
        add_button = Button(series_frame_container,
                            text="Agregar", command=self.__navigate_to_add_series)
        add_button.grid(padx=10, pady=10, column=1, row=0)

        series_list = Frame(series_frame_container)
        self.config_list_cols(series_list)
        self.config_list_row(series_frame_container, len(elements))
        series_list.grid(row=1, column=0, columnspan=2)

        col = 1
        row = 1

        for movie in elements:
            ListItem(series_list, movie, row, col,
                     lambda card_reference: self.__delete_card(card_reference), self._navigation_callback, self._is_movie)
            if (col == APP_COLS):
                col = 1
                row += 1
            else:
                col += 1

    def __delete_card(self, card_reference: Frame):
        card_reference.destroy()

    def __navigate_to_add_series(self):
        type_element = "pelicula" if self._is_movie else "serie"
        self.controller.set_is_to_update(False, None)
        self.controller.set_element_type(type_element)
        self._navigation_callback()

    def config_list_cols(self, frame: Frame):
        for col in range(APP_COLS):
            frame.columnconfigure(col, weight=1)

    def config_list_row(self, frame: Frame, row_quantity: int):
        for row in range(row_quantity):
            frame.rowconfigure(row, weight=1)


class ScreenManager:
    current_page: Tk | None = None

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
        window.geometry("1024x768")
        self.center_window(window, 1024, 768)
        ListFrame(window, self.show_add_page, True)
        ListFrame(window, self.show_add_page, False)
        self.current_page = window
        window.mainloop()

    def show_add_page(self):
        self.__destroy_current_page()
        window = Tk()
        window.title("PyNeflix - Add")
        window.geometry("1024x768")
        self.center_window(window, 1024, 768)
        AddElement(window, self.show_home_page)
        self.current_page = window
        window.mainloop()

    def center_window(self, window: Tk, width: int, height: int):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = int((screen_width/2) - (width / 2))
        y = int((screen_height/2) - (height / 2))

        return window.geometry(f"{width}x{height}+{x}+{y}")
