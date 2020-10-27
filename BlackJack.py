from random import shuffle
inf = 9999999999

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card() :
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) :
        return self.rank + ' of ' + self.suit


class Deck() :
    def __init__(self) :
        self.deck = []
        for suit in suits :
            for rank in ranks :
                self.deck.append(Card(suit, rank))
    
    def shuffleDeck(self) :
        shuffle(self.deck)

    def dealCard(self) :
        topCard = self.deck.pop()
        return topCard


class Hand():
    def __init__(self) :
        self.cards = []
        self.sum = 0
        self.aceCount = 0

    def addCard(self, card) :
        self.cards.append(card)
        self.sum += values[card.rank]
        if card.rank == 'Ace':
            self.aceCount += 1

    def aceAdjustment(self) :
        while self.sum > 21 and self.aceCount :
            self.sum -= 10
            self.aceCount -= 1


class playerChips() :
    def __init__(self, chips) :
        self.chips = chips
        self.bet = 0

    def wonChips(self) :
        self.chips += self.bet

    def lostChips(self) :
        self.chips -= self.bet


def makeBet(playerChips) :
    print("hello")
    while(playerChips.bet>0 and playerChips.bet > playerChips.chips) :
        playerChips.bet = int(input("\nEnter the chips you would like to bet:\n"))


def hitCard(hand, deck) :
    hand.addCard(deck.dealCard())
    hand.aceAdjustment()


def hitOrStand(hand, deck, player) :
    res = ''
    while res not in ['h', 's'] :
        res = input("\nWould you like to hit or stand? (h/s)\n")

        if res == 'h' :
            print(f"\n{player} says hit!")
            hitCard(hand, deck)
            return True
        else :
            print(f"\n{player} stands!")
            return False


def showCard(player, dealer, playerName) :
    # printing dealer's cards
    print("\nDealer's Hand:")
    print(f"{dealer.cards[0]}")
    print("Hidden Card!")
    
    # printing player's cards
    print(f"\n{playerName} Hand:")
    print(f"{player.cards[0]}\n{player.cards[1]}")


def showHand(player, dealer, playerName):
    # printing dealer's cards
    print("\nDealer's Hand:")
    print(f"{dealer.cards[0]}\n{dealer.cards[1]}")
    print(f"Dealer's Hand = {dealer.sum}")
    
    # printing player's cards
    print(f"\n{playerName}'s Hand:")
    print(f"{player.cards[0]}\n{player.cards[1]}")
    print(f"{playerName}'s Hand = {player.sum}")

    
def main() :
    print("\nWelcome to BlackJack!")

    player = input("\nEnter your name:\n")
    x = int(input("\nEnter the amount of chips you have:\n"))

    print(f"\nHello {player}! All the best!")

    # creating a deeck of cards
    deck = Deck()
    deck.shuffleDeck()

    # deal cards to player
    playerHand = Hand()
    playerHand.addCard(deck.dealCard())
    playerHand.addCard(deck.dealCard())

    # deal cards to dealer
    dealerHand = Hand()
    dealerHand.addCard(deck.dealCard())
    dealerHand.addCard(deck.dealCard())

    # setting the player chips
    chips = playerChips(x)

    while True :
        # player bets
        while chips.bet == 0 or chips.bet > chips.chips :
            chips.bet = int(input("\nEnter the amount of chips you would like to bet:\n"))

        # showing cards
        showCard(playerHand, dealerHand, player)

        isHit = True
        while isHit :
            isHit = hitOrStand(playerHand, deck, player)
            
            showCard(playerHand, dealerHand, player)

            if playerHand.sum > 21:
                print(f"\n{player} busts! Dealer wins!!!")
                chips.chips -= chips.bet
                break

        if playerHand.sum <= 21 :
            while dealerHand.sum < 17 :
                hitCard(dealerHand, deck)
                # showHand(playerHand, dealerHand, player)

            showHand(playerHand, dealerHand, player)

            if dealerHand.sum > 17 :
                print(f"\nDealer busts! {player} wins!!!")
                chips.chips += chips.bet
        
            elif dealerHand.sum > playerHand.sum :
                print("\nDealer wins!!!")
                chips.chips -= chips.bet

            elif dealerHand.sum < playerHand.sum :
                print(f"\n{player} wins!!!")
                chips.chips += chips.bet

            else :
                print("\nIt's a Tie!!!")

        # chips left
        print(f"\nPlayer chips left: {chips.chips}")
        chips.bet = 0

        if chips.chips == 0:
            print(f"{player} out of chips!")
            break

        res = input("Do you want to continue? (y/n)\n")
        if res == 'n' :
            break


if __name__ == '__main__':
    main()