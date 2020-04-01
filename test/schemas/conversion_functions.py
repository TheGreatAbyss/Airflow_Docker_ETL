from functools import partial

from etl_src.schemas.conversion_functions import convert_bool, skip_empty_string


def test_convert_bool():
    assert (True == convert_bool("T"))
    assert (False == convert_bool("F"))
    assert (True == convert_bool("1"))
    assert (False == convert_bool("0"))
    assert (True == convert_bool(1))
    assert (False == convert_bool(0))
    assert (convert_bool(None) is None)


def test_skip_emtpy_string():
    partial_func = partial(skip_empty_string, conversion_func=float)
    assert(1.0 == partial_func(1.0))