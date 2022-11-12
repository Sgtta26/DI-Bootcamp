#A class is a code template for creating objects
#Instance is an object that belongs to a class
#Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit
#Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user
#Inheritance is a feature that allows us to define a class that inherits all the methods and properties from another class

class Card:
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __repr__(self):
        return f"Card({self.suit},{self.value})"

    def __init__(self, suit, value):
        if not suit in Card.SUITS or not value in Card.VALUES:
            raise Exception("Not valid suit or value")
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        from itertools import product

        cards = product(Card.SUITS, Card.VALUES)

        self.cards = [Card(*card) for card in cards]

    def shuffle(self):
        from random import shuffle as do_shuffle

        if len(self.cards) != 52:
            raise Exception("Not all cards in deck")

        do_shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


def main():
    deck = Deck()
    print(deck.cards)
    deck.shuffle()
    print(deck.cards)
    print(deck.deal())
    print(len(deck.cards))
    deck.shuffle()


main()