from pyparticle.sql.types import Row


def test_access_column_by_index():
    row = Row(one=42, two="hello", three=None)

    assert (row[0], row[1], row[2]) == (42, "hello", None)


def test_access_column_by_str():
    row = Row(one=42, two="hello", three=None)

    assert (row["one"], row["two"], row["three"]) == (42, "hello", None)


def test_access_column_by_field():
    row = Row(one=42, two="hello", three=None)

    assert (row.one, row.two, row.three) == (42, "hello", None)
