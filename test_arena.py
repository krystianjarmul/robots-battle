from arena import Arena


def test_arena_is_square_6x6():
    arena = Arena()
    assert len(arena.board) == 6
    for row in arena.board:
        assert len(row) == 6


def test_arena_default_has_all_fields_fill_with_zeros():
    arena = Arena()
    assert any([field == 0 for row in arena.board for field in row])


def test_arena_object_symbol():
    arena = Arena()
    assert arena.robot == 'x'
    assert arena.item == '*'


def test_sets_a_blue_team_robot_its_starting_area():
    arena = Arena()

    arena.set_blue_team()

    assert 'x' in arena.board[0]


def test_sets_a_red_team_robot_in_its_starting_area():
    arena = Arena()

    arena.set_red_team()

    assert 'x' in arena.board[-1]


def test_sets_8_deactivated_robots_in_battleground():
    arena = Arena()

    arena.set_deactivated_robots()

    assert sum([row.count('x') for row in arena.board]) == 8


def test_init_sets_all_robots_on_board():
    arena = Arena()

    arena.init()

    assert sum([row.count('x') for row in arena.board]) == 10
