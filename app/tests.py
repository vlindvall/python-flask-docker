import pytest
# comment
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


@pytest.mark.parametrize(
'''note, is_equal, expected_output
''',
    [
       (1, 1, True),
       (1, 2, False),
    ]
)
def test_pytest2(note, is_equal, expected_output):
    equal = (is_equal == note)
    assert equal == expected_output



@pytest.mark.parametrize(
'''note, is_equal, expected_output
''',
    [
       (2, 2, True),
       (2, 2, True),
    ]
)
def test_pytest2(note, is_equal, expected_output):
    equal = (is_equal == note)
    assert equal == expected_output

