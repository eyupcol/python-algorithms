from find_max import find_max


def test_find_max():
    """
    Checks if the number real max number in a list
    """
    sample_list = [2, 0, 30, 55, 60, -66]
    assert find_max(sample_list) == 60
