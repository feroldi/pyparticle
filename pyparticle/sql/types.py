from typing import Any


class Row:
    def __init__(self, **fields: dict[str, Any]):
        self._index_by_columns = {
            key: i for i, key in enumerate(fields.keys())
        }
        self._values = tuple(fields.values())

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Row)
            and self._index_by_columns == other._index_by_columns
            and self._values == other._values
        )


    def __getitem__(self, item: str) -> Any:
        return self._values[self._index_by_columns[item]]

    # TODO(feroldi): Test.
    def __repr__(self) -> str:
        columns_and_values = ", ".join(
            f"{column}={value}"
            for column, value in zip(
                self._index_by_columns.keys(), self._values
            )
        )
        return f"Row({columns_and_values})"
