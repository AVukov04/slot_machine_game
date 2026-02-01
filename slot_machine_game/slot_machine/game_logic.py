import random

SYMBOLS = ["Cherry", "Lemon", "Orange", "Seven"]

def spin_reels():
    return [random.choice(SYMBOLS) for _ in range(3)]

def check_win(symbols):
    if symbols[0] == symbols[1] == symbols[2]:
        return True
    return False

class SlotMachine:
    def __init__(self, starting_balance=100):
        self.balance = starting_balance
        self.bet = 1
        self.last_symbols = []
        self.last_winnings = 0

    def spin(self):
        if self.balance < self.bet:
            raise ValueError("Not enough balance!")

        self.balance -= self.bet
        self.last_symbols = spin_reels()

        if check_win(self.last_symbols):
            self.last_winnings = self.bet * 10
            self.balance += self.last_winnings
        else:
            self.last_winnings = 0

        return self.last_symbols, self.last_winnings
