from your_package import hello


def test_goodbye():
    assert hello.hello("world") == "hello world"
