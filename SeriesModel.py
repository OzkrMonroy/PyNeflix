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
