import body


def test_simple_body_attributes():
    simple_body = body.SimpleBody()
    assert simple_body.name == 'Simple Body'
    assert simple_body.hp == 2
    assert isinstance(simple_body, body.Body)


def test_hard_body_attributes():
    hard_body = body.HardBody()
    assert hard_body.name == 'Hard Body'
    assert hard_body.hp == 5
    assert isinstance(hard_body, body.Body)
