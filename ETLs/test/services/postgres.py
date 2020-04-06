from etl_src.services.postgres import PostGresRowInserter


def test_create_item_string():
    test_cols = ["col1", "col2"]
    expected = '"col1", "col2"'
    actual = PostGresRowInserter.create_item_string(test_cols)
    print(actual)
    assert (expected == actual)

def test_create_upsert_set_string():
    test_cols = ["col1", "col2"]
    test_vals = ["Bernie", 1]
    expected = '"col1" = "Bernie", "col2" = "1"'
    assert(expected == PostGresRowInserter.create_upsert_set_string(test_cols, test_vals))