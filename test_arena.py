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

