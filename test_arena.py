from arena import Arena


def test_arena_is_square_6x6():
    arena = Arena()
    assert len(arena.board) == 6
    for row in arena.board:
        assert len(row) == 6
