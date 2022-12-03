from sord.util import group_items


def test_group_items():
    identifiers = range(10)
    items = (i % 3 for i in identifiers)
    result = group_items(items, identifiers)
    expected_result = {hash(0): [0, 3, 6, 9], hash(1): [1, 4, 7], hash(2): [2, 5, 8]}
    assert result == expected_result
