import random
card_symbols = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
card_face_value=[2,3,4,5,6,7,8,9,10,10,10,10,11]
values=dict(zip(cards,card_face_value))
print("print values zip",(values))

playing=True
class Card:

    def __init__(self, card_symbols, cards):
        self.card_symbols = card_symbols
        self.cards = cards

    def __str__(self):
        return (self.cards+ " of " + self.card_symbols)

class Deck:

    def __init__(self):
        self.deck = []
        for i in card_symbols:
            for j in cards:
                self.deck.append(Card(i, j))

    def __str__(self):
        deck_com = ''
        for card in self.deck:
            deck_com += "\n" + card.__str__()

        return deck_com
    def move_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card



class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.cards]
        if card.cards == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Cash:

    def __init__(self):
        self.total = 52  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    def take_bet(self, betamt):
        self.bet = betamt

def take_bet(Cashs):

        while True:
            try:
                Cashs.bet = int(input('Cashs would you like to bet? '))
            except ValueError:
                print('bet must be an integer!')
            else:
                if Cashs.bet > Cashs.total:
                    print("your bet can't exceed", Cashs.total)
                else:
                    break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):


    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x == 'h':
            hit(deck, hand)

        elif x == 's':
            print("Player stands. Dealer is playing.")
            return False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_one_card(player, dealer):
    print("\nDealer's Hand:")
    print(" card hidden")
    print(dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, Cashs):
    print("Player busts!, Dealer wins")
    Cashs.lose_bet()
    print("\nPlayer's Total cash after loss: ", player_Cashs.total)
    print("your bet was:", player_Cashs.bet)


def player_wins(player, dealer, Cashs):
    print("Player wins!")
    #print("\nPlayer's Total cash after win: ", player_Cashs.total)
    Cashs.win_bet()
    print("\nPlayer's Total cash after win: ", player_Cashs.total)
    print("your bet was:", player_Cashs.bet)


def dealer_busts(player, dealer, Cashs):
    print("Dealer busts!, Player wins")
    Cashs.win_bet()
    print("\nPlayer's Total cash after win: ", player_Cashs.total)
    print("your bet was:", player_Cashs.bet)


def dealer_wins(player, dealer, Cashs):
    print("Dealer wins!")
    Cashs.lose_bet()
    print("\nPlayer's Total cash after loss: ", player_Cashs.total)
    print("your bet was:",player_Cashs.bet)


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")
    print("your bet was:", player_Cashs.bet)


while True:
    test_deck = Deck()
    test_deck.move_deck()

    player_hand = Hand()
    player_hand.add_card(test_deck.deal())
    player_hand.add_card(test_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(test_deck.deal())
    dealer_hand.add_card(test_deck.deal())


    player_Cashs = Cash()


    take_bet(player_Cashs)


    show_one_card(player_hand, dealer_hand)

    while playing:


        playing = hit_or_stand(test_deck, player_hand)


        show_one_card(player_hand, dealer_hand)


        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_Cashs)
            break


    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(test_deck, dealer_hand)


        show_all(player_hand, dealer_hand)


        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_Cashs)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_Cashs)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_Cashs)

        else:
            push(player_hand, dealer_hand)


    #print("\nPlayer's Total cash after win: ", player_Cashs.total)


    want_play_again = input("Do you want play another round? Enter 'y' or 'n' ")

    if want_play_again == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break