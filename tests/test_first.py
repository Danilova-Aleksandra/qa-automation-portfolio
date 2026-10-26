def test_numbers_are_equal():
    actual = 2 + 3
    expected = 5

    assert actual == expected


def test_numbers_are_not_equal():
    actual = 10
    expected = 5

    assert actual != expected


def test_string_contains_text():
    actual = "QA Automation"

    assert "Automation" in actual
