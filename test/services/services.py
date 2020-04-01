from etl_src.services.postgres import PostGresRowInserter


def test_create_col_and_val_string():
    test_cols = ["col1", "col2"]
    expected = ('"col1", "col2"', '"%s", "%s"')
    assert (expected == PostGresRowInserter.create_col_and_val_string(test_cols))

