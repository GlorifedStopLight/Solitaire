from random import *
from kandinsky import *


# class of playing cards
class Card:
    def __init__(self, type, number, showInfo):

        # type of card (spades hearts etc)
        self.type = type

        if type == "D":
            self.cardColor = diamondsColor

        elif type == "S":
            self.cardColor = spadesColor

        elif type == "C":
            self.cardColor = clubsColor

        elif type == "H":
            self.cardColor = heartsColor

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
        self.aceSlots = [[Card("H", "", True)], [Card("D", "", True)], [Card("C", "", True)], [Card("S", "", True)]]

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
            fill_rect(x, y+(cardIndex * verticalSpacing), horizontalWidthOfCard, verticalHeightOfCard, baseCardColor)

            # display heart icon
            if stackData[cardIndex].type == "H":
                displayHeart(x, y + (cardIndex * verticalSpacing))

            # display diamond icon
            elif stackData[cardIndex].type == "D":
                displayDiamond(x, y + (cardIndex * verticalSpacing))

            # display club icon
            elif stackData[cardIndex].type == "C":
                displayClub(x, y + (cardIndex * verticalSpacing))

            # display spade icon
            elif stackData[cardIndex].type == "S":
                displaySpade(x, y + (cardIndex * verticalSpacing))

        # just show the back of the card instead
        else:
            # display information
            fill_rect(x, y + (cardIndex * verticalSpacing), horizontalWidthOfCard, verticalHeightOfCard, cardNotFlippedColor)


# displays the ace piles
def displayAceStacks(stackData):

    x = drawPileX
    y = drawPileY + aceSpacingY

    displaySingleStack(x, y, [stackData[0][0], stackData[1][0], stackData[2][0], stackData[3][0]])


# displays all stacks
def displayAllStacks(allStacks):

    # loop through each stack
    for stackIndex in range(len(allStacks)):

        # display the single stack
        displaySingleStack(startX + (stackIndex * horizontalSpacing), startY, allStacks[stackIndex])


# displays the draw pile and the cards flipped next to it
def displayDrawPile(pile):

    # pile isn't empty
    if len(pile) > 0:

        #
        fill_rect(drawPileX, drawPileY, horizontalWidthOfCard, verticalHeightOfCard, cardNotFlippedColor)

    # pile is empty
    else:

        fill_rect(drawPileX, drawPileY, horizontalWidthOfCard, verticalHeightOfCard, gameBackgroundColor)


# displays everything on board
def displayBoard(gameInfo):

    # color the background
    fill_rect(0, 0, 320, 222, gameBackgroundColor)

    # display draw pile
    displayDrawPile(gameInfo.deck)

    # display stacks of cards
    displayAllStacks(gameInfo.columns)

    # display the ace piles
    displayAceStacks(gameInfo.aceSlots)


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


# heart icon for cards
def displayHeart(x, y):
    x += xSpaceForIcons
    y += ySpaceForIcons

    # layer 0
    fill_rect(x+1, y, 2, 1, heartsColor)
    fill_rect(x+6, y, 2, 1, heartsColor)

    # layer 1
    fill_rect(x, y+1, 4, 1, heartsColor)
    fill_rect(x+5, y+1, 4, 1, heartsColor)

    # layer 2
    fill_rect(x, y+2, 9, 1, heartsColor)

    # layer 3
    fill_rect(x, y+3, 9, 1, heartsColor)

    # layer 4
    fill_rect(x, y+4, 9, 1, heartsColor)

    # layer 5
    fill_rect(x+1, y+5, 7, 1, heartsColor)

    # layer 6
    fill_rect(x+2, y+6, 5, 1, heartsColor)

    # layer 7
    fill_rect(x+3, y+7, 3, 1, heartsColor)

    # layer 8
    fill_rect(x+4, y+8, 1, 1, heartsColor)


# diamond icon for cards
def displayDiamond(x, y):
    x += xSpaceForIcons
    y += ySpaceForIcons

    # layer 0
    fill_rect(x+4, y, 1, 1, diamondsColor)

    # layer 1
    fill_rect(x+3, y+1, 3, 1, diamondsColor)

    # layer 2
    fill_rect(x+2, y+2, 5, 1, diamondsColor)

    # layer 3
    fill_rect(x+1, y+3, 7, 1, diamondsColor)

    # layer 4
    fill_rect(x, y+4, 9, 1, diamondsColor)

    # layer 5
    fill_rect(x+1, y+5, 7, 1, diamondsColor)

    # layer 6
    fill_rect(x+2, y+6, 5, 1, diamondsColor)

    # layer 7
    fill_rect(x+3, y+7, 3, 1, diamondsColor)

    # layer 8
    fill_rect(x+4, y+8, 1, 1, diamondsColor)


# club icon for cards
def displayClub(x, y):
    x += xSpaceForIcons
    y += ySpaceForIcons

    # layer 0
    fill_rect(x+2, y, 5, 1, clubsColor)

    # layer 1
    fill_rect(x+2, y+1, 5, 1, clubsColor)

    # layer 2
    fill_rect(x, y+2, 2, 1, clubsColor)
    fill_rect(x+3, y+2, 3, 1, clubsColor)
    fill_rect(x+7, y+2, 2, 1, clubsColor)

    # layer 3
    fill_rect(x, y + 3, 3, 1, clubsColor)
    fill_rect(x+4, y + 3, 1, 1, clubsColor)
    fill_rect(x+6, y + 3, 3, 1, clubsColor)

    # layer 4
    fill_rect(x, y + 4, 9, 1, clubsColor)

    # layer 5
    fill_rect(x, y + 5, 3, 1, clubsColor)
    fill_rect(x + 4, y + 5, 1, 1, clubsColor)
    fill_rect(x + 6, y + 5, 3, 1, clubsColor)

    # layer 6
    fill_rect(x, y + 6, 2, 1, clubsColor)
    fill_rect(x + 4, y + 6, 1, 1, clubsColor)
    fill_rect(x + 7, y + 6, 2, 1, clubsColor)

    # layer 7
    fill_rect(x+4, y + 7, 1, 1, clubsColor)

    # layer 8
    fill_rect(x+3, y + 8, 3, 1, clubsColor)


# spade icon for cards
def displaySpade(x, y):
    x += xSpaceForIcons
    y += ySpaceForIcons

    # layer 0
    fill_rect(x+4, y, 1, 1, spadesColor)

    # layer 1
    fill_rect(x+3, y+1, 3, 1, spadesColor)

    # layer 2
    fill_rect(x+2, y+2, 5, 1, spadesColor)

    # layer 3
    fill_rect(x + 1, y + 3, 7, 1, spadesColor)

    # layer 4
    fill_rect(x, y + 4, 9, 1, spadesColor)

    # layer 5
    fill_rect(x, y + 5, 9, 1, spadesColor)

    # layer 6
    fill_rect(x, y + 6, 9, 1, spadesColor)

    # layer 7
    fill_rect(x+1, y + 7, 2, 1, spadesColor)
    fill_rect(x + 4, y + 7, 1, 1, spadesColor)
    fill_rect(x + 6, y + 7, 2, 1, spadesColor)

    # layer 8
    fill_rect(x + 3, y + 8, 3, 1, spadesColor)


startX = 10
startY = 10

drawPileX = 265
drawPileY = 10

aceSpacingY = 50

verticalSpacing = 17
horizontalSpacing = 32

horizontalWidthOfCard = 30
verticalHeightOfCard = 15

outLineWidth = 2

xSpaceForIcons = 20
ySpaceForIcons = 3

cardNotFlippedColor = (92, 177, 243)
gameBackgroundColor = (72, 176, 74)

diamondsColor = (187, 45, 38)
heartsColor = (239, 80, 80)
spadesColor = (47, 58, 87)
clubsColor = (22, 22, 36)

baseCardColor = (200, 200, 200)


game = Board()
game.newGame()

displayBoard(game)
outLine(3, 0, 3, (0, 0, 0))
tk.mainloop()