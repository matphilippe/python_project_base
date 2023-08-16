from your_package.a_subpackage import goodbye

def test_goodbye():
    assert goodbye.goodbye("world") == "goodbye world"