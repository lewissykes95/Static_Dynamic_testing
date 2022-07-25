import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("spades", 1)
        self.card2 = Card("hearts", 10)
        self.card3 = Card("diamonds", 6)
        self.card_game  = CardGame()
        self.cards = [self.card1, self.card2, self.card3]

    
    def test_check_ace(self):
        value = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, value)

    def test_check_highest_card(self): 
        highest_card = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, highest_card)

    def test_cards_total(self):
        total = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 17", total)

