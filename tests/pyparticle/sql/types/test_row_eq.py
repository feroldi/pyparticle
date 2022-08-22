from hypothesis import assume, given
from hypothesis import strategies as st

from pyparticle.sql.types import Row


def st_field_names():
    return st.from_regex(r"[_a-zA-Z][_0-9a-zA-Z]*", fullmatch=True)


def st_basic_values():
    return st.one_of(
        st.none(),
        st.booleans(),
        st.text(),
        st.integers(),
        st.floats(),
    )


@given(
    st.dictionaries(
        keys=st_field_names(), values=st_basic_values(), min_size=1
    )
)
def test_rows_with_same_fields_are_equal(dictionary):
    assert Row(**dictionary) == Row(**dictionary)


@st.composite
def st_same_fields_with_distinct_values(draw):
    fields = draw(st.lists(st_field_names(), min_size=1, unique=True))

    value_lists = st.lists(
        st_basic_values(), min_size=len(fields), max_size=len(fields)
    )
    values_a = draw(value_lists)
    values_b = draw(value_lists)

    assume(values_a != values_b)

    return (
        {f: v for f, v in zip(fields, values_a)},
        {f: v for f, v in zip(fields, values_b)},
    )


@given(st_same_fields_with_distinct_values())
def test_rows_with_same_fields_but_different_values_are_not_equal(
    dicts,
):
    dict_a, dict_b = dicts

    assert Row(**dict_a) != Row(**dict_b)


@given(
    dict_a=st.dictionaries(
        keys=st_field_names(), values=st_basic_values(), min_size=1
    ),
    dict_b=st.dictionaries(
        keys=st_field_names(), values=st_basic_values(), min_size=1
    ),
)
def test_rows_with_different_fields_are_not_equal(dict_a, dict_b):
    assume(list(dict_a.keys()) != list(dict_b.keys()))

    assert Row(**dict_a) != Row(**dict_b)


@st.composite
def same_fields_with_same_values_but_in_distinct_order(draw):
    import random

    dictionary = draw(
        st.dictionaries(
            keys=st_field_names(), values=st_basic_values(), min_size=1
        )
    )

    seed = draw(st.integers(min_value=0))
    rng = random.Random(seed)

    fields_a = list(dictionary.keys())
    fields_b = list(dictionary.keys())

    rng.shuffle(fields_a)
    rng.shuffle(fields_b)

    assume(fields_a != fields_b)

    return (
        {f: v for f, v in zip(fields_a, dictionary.values())},
        {f: v for f, v in zip(fields_b, dictionary.values())},
    )


@given(dicts=same_fields_with_same_values_but_in_distinct_order())
def test_rows_with_same_fields_but_in_different_order_are_not_equal(dicts):
    dict_a, dict_b = dicts

    assert Row(**dict_a) != Row(**dict_b)
