from src import body


def test_simple_body_attributes():
    simple_body = body.SimpleBody()
    assert simple_body.name == 'SIMPLE BODY'
    assert simple_body.hp == 2
    assert isinstance(simple_body, body.Body)


def test_hard_body_attributes():
    hard_body = body.HardBody()
    assert hard_body.name == 'HARD BODY'
    assert hard_body.hp == 5
    assert isinstance(hard_body, body.Body)


def test_light_body_attributes():
    light_body = body.LightBody()
    assert light_body.name == 'LIGHT BODY'
    assert light_body.hp == 3
    assert light_body.movement == 1


def test_battle_body_attributes():
    battle_body = body.BattleBody()
    assert battle_body.name == 'BATTLE BODY'
    assert battle_body.hp == 2
    assert battle_body.extra_slot
