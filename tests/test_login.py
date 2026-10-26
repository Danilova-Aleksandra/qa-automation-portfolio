import pytest

from app.login import login


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("qa_user", "secret123", True),
        ("qa_user", "wrong_password", False),
        ("wrong_user", "secret123", False),
        ("", "secret123", False),
        ("qa_user", "", False),
    ],
)
def test_login(username, password, expected):
    result = login(username, password)

    assert result is expected