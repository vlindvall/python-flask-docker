import pytest

@pytest.mark.parametrize(
'''note, is_equal, expected_output
''',
    [
       ('correct', 1, True),
       ('incorrect', 2, False),
    ]
)
def test_pytest(note, is_equal, expected_output):
    number = 1
    equal = (is_equal == number)
    assert equal == expected_output
