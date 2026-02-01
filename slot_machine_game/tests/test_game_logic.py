import pytest
from slot_machine.game_logic import SYMBOLS, spin_reels, check_win, SlotMachine

def test_spin_returns_three_symbols():
    result = spin_reels()
    assert len(result) == 3

def test_symbols_are_valid():
    result = spin_reels()
    for symbol in result:
        assert symbol in SYMBOLS

def test_three_matching_symbols_wins():
    assert check_win(["Cherry", "Cherry", "Cherry"]) is True

def test_different_symbols_loses():
    assert check_win(["Cherry", "Lemon", "Orange"]) is False

def test_machine_starts_with_correct_balance():
    machine = SlotMachine(starting_balance=100)
    assert machine.balance == 100

def test_spin_deducts_bet_and_adds_winnings():
    machine = SlotMachine(starting_balance=100)
    machine.spin()
    assert machine.balance == 100 - 1 + machine.last_winnings

def test_no_balance_raises_error():
    machine = SlotMachine(starting_balance=0)
    with pytest.raises(ValueError):
        machine.spin()
