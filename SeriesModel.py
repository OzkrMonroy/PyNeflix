class Series:
    _series = []

    def save(self, series_properties: list[str]) -> None:
        series_obj = {
            "id": len(self._series),
            "name": series_properties[0],
            "seasons": series_properties[2],
            "rating": series_properties[3],
            "genre": series_properties[4],
            "release_date": series_properties[5]
        }
        self._series.append(series_obj)

    def get_series(self):
        return self._series

    def delete(self, series):
        self._series.remove(series)

    def update(self, series: list[str]):
        index = self.__get_element_index(series)
        if (bool(index)):
            self._series[index] = series

    def __get_element_index(self, series: list[str]):
        index = None
        for i, element in enumerate(self._series):
            if element["id"] == series[0]:
                index = i
        return index
