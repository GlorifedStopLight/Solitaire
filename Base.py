from random import *
from kandinsky import *


# class of playing cards
class Card:
    def __init__(self, type, number, showInfo):

        # type of card (spades hearts etc)
        self.type = type

        if type == "D":
            self.cardColor = (0, 0, 90)

        elif type == "S":
            self.cardColor = (0, 90, 0)

        elif type == "C":
            self.cardColor = (255, 100, 0)

        elif type == "H":
            self.cardColor = (255, 100, 0)

        # number of card 1-13
        self.number = number

        # true -> shows the card information
        self.showInfo = showInfo


# holds the information on the board
class Board:
    def __init__(self):

        # deck of cards at the top right corner
        self.deck = None

        # slots where the aces go
        self.aceSlots = [None, None, None, None]

        # columns that hold stacks of cards
        self.columns = [None, None, None, None, None, None, None]

    # creates a new game
    def newGame(self):

        # get a deck of cards
        self.deck = getNewDeck()

        # shuffle the deck
        shuffle(self.deck)

        # iterate through the columns
        for cardsInEachStack in range(1, 8):

            # contains the cards from this column
            thisColumn = []

            # add cards for the amount needed in each stack (column)
            for singleCard in range(cardsInEachStack):

                # remove a card from the deck and add it to the column
                thisColumn.append(self.deck.pop(0))

            # flip the card on the top of the pile so you can see what it says
            thisColumn[-1].showInfo = True

            # add the stack of cards to the columns on the board
            self.columns[cardsInEachStack-1] = thisColumn

    # starts the game
    def startGame(self):

        while True:
            pass


# returns a list of new cards
def getNewDeck():

    # initialize the new deck
    newDeck = []

    # loop through each card type
    for type in ["H", "D", "C", "S"]:

        # loop though the card numbers
        for number in range(1, 14):

            # add new card to deck
            newDeck.append(Card(type, number, False))

    # return filled deck
    return newDeck


# displays a stack
def displaySingleStack(x, y, stackData):

    # loop through each card in the stack
    for cardIndex in range(len(stackData)):

        # the information should be displayed
        if stackData[cardIndex].showInfo:

            # display information
            fill_rect(x, y+(cardIndex * verticalSpacing), horizontalWidthOfCard, verticalHeightOfCard, stackData[cardIndex].cardColor)

        # just show the back of the card instead
        else:
            # display information
            fill_rect(x, y + (cardIndex * verticalSpacing), horizontalWidthOfCard, verticalHeightOfCard, (0, 0, 255))


# displays all stacks
def displayAllStacks(allStacks):

    # loop through each stack
    for stackIndex in range(len(allStacks)):

        # display the single stack
        displaySingleStack(startX + (stackIndex * horizontalSpacing), startY, allStacks[stackIndex])


# displays the draw pile and the cards flipped next to it
def displayDrawPile():
    pass


# displays the piles just for aces
def displayAcePiles():
    pass


# displays everything on board
def displayBoard():
    pass


# creates an outline
def outLine(columnIndex, fromRow, toRow, c):

    # x coordinate where we start drawing
    x = startX + (horizontalSpacing * columnIndex)

    # y coordinate (top left)
    y1 = startY + (verticalSpacing * fromRow)

    yDistance = verticalSpacing * (abs(fromRow - toRow) + 1)

    # left side outline
    fill_rect(x-outLineWidth, y1-outLineWidth, outLineWidth, yDistance, c)

    # right side outline
    fill_rect(x + horizontalWidthOfCard, y1, outLineWidth, yDistance, c)

    # top outline
    fill_rect(x, y1-outLineWidth, horizontalWidthOfCard + outLineWidth, outLineWidth, c)

    # bottom outline
    fill_rect(x - outLineWidth, y1 + yDistance - outLineWidth, horizontalWidthOfCard + outLineWidth, outLineWidth, c)


startX = 10
startY = 10

verticalSpacing = 17
horizontalSpacing = 32

horizontalWidthOfCard = 30
verticalHeightOfCard = 15

outLineWidth = 2


game = Board()
game.newGame()

displayAllStacks(game.columns)
outLine(3, 0, 3, (0, 0, 0))
tk.mainloop()