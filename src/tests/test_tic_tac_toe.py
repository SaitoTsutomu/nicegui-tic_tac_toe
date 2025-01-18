# flake8: noqa: S101
from unittest.mock import Mock

import pytest

from nicegui_tic_tac_toe import Game


@pytest.mark.parametrize(
    ("texts", "messages", "values"),
    [
        ([*"47682"], ["X's", "O's"] * 2 + ["O h"], "..O.O.OXX"),
        ([*"012473586"], ["X's", "O's"] * 4 + ["dra"], "OXOXXOOOX"),
    ],
)
def test_tic_tac_toe(texts, messages, values):
    """終局のテスト"""
    ttt = Game()
    event = Mock()
    for text, message in zip(texts, messages, strict=True):
        event.sender.text = text
        ttt.click(event)
        assert ttt.message[:3] == message
    actual = "".join(square.value or "." for square in ttt.squares)
    assert actual == values
