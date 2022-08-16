from pyparticle.sql.types import Row


class DataFrame:
    def __init__(self, rows: list[Row]):
        self._rows = rows

    def select(self, *columns: list[str]):
        return DataFrame(
            [
                Row(**{column: row[column] for column in columns})
                for row in self._rows
            ]
        )


    def collect(self) -> list[Row]:
        # TODO(feroldi): Deep-copy list.
        return self._rows

