from pyparticle.sql import DataFrame, Row


def test_select_all_columns_in_same_order_from_dataframe_should_return_untouched_dataframe():
    df = DataFrame(
        [
            Row(a=1, b=2, c=3),
            Row(a=4, b=5, c=6),
            Row(a=7, b=8, c=9),
        ]
    )

    output = df.select("a", "b", "c").collect()

    assert output == [
        Row(a=1, b=2, c=3),
        Row(a=4, b=5, c=6),
        Row(a=7, b=8, c=9),
    ]


def test_select_subset_of_columns_from_dataframe_should_return_dataframe_with_only_those_columns():
    df = DataFrame(
        [
            Row(a=1, b=2, c=3),
            Row(a=4, b=5, c=6),
            Row(a=7, b=8, c=9),
        ]
    )

    output = df.select("a", "c").collect()

    assert output == [
        Row(a=1, c=3),
        Row(a=4, c=6),
        Row(a=7, c=9),
    ]


def test_select_reordered_columns_from_dataframe_should_return_dataframe_with_same_column_ordering():
    df = DataFrame(
        [
            Row(a=1, b=2, c=3),
            Row(a=4, b=5, c=6),
            Row(a=7, b=8, c=9),
        ]
    )

    output = df.select("b", "c", "a").collect()

    assert output == [
        Row(b=2, c=3, a=1),
        Row(b=5, c=6, a=4),
        Row(b=8, c=9, a=7),
    ]


def test_select_reordered_subset_of_columns_from_dataframe_should_return_dataframe_with_only_those__columns_in_the_same_order():
    df = DataFrame(
        [
            Row(b=2, c=3, a=1),
            Row(b=5, c=6, a=4),
            Row(b=8, c=9, a=7),
        ]
    )

    output = df.select("c", "b").collect()

    assert output == [
        Row(c=3, b=2),
        Row(c=6, b=5),
        Row(c=9, b=8),
    ]
