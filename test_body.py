import body


def test_simple_body_attributes():
    simple_body = body.SimpleBody()
    assert simple_body.name == 'Simple Body'
    assert simple_body.hp == 2
    assert isinstance(simple_body, body.Body)
