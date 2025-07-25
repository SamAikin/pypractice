from pypractice import say_hello


def test_say_hello_says_hello():
    assert "hello" in say_hello().lower()
    