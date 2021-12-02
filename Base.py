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
        self.columns = [[], [], [], [], [], [], []]

    # creates a new game
    def newGame(self):

        # get a deck of cards
        self.deck = getNewDeck()

        # shuffle the deck
        self.deck = shuffleDeck(self.deck)

        # iterate through the columns
        for cardsInEachStack in range(1, 8):

            # contains the cards from this column
            thisColumn = []

            # add cards for the amount needed in each stack (column)
            for singleCard in range(cardsInEachStack):

                # remove a card from the deck and add it to the column
                thisColumn.append(self.deck.pop(0))

            # flip the card on the top of the pile so you can see what it says
            thisColumn[-1][2] = True

            # add the stack of cards to the columns on the board
            self.columns[cardsInEachStack-1] = thisColumn

    # starts the game
    def startGame(self):

        # saves what is selected
        selected = None

        # the coordinates of outline/cursor
        cursorCoordinates = [0, 0]

        # game loop
        while True:

            # pressed OK
            if keydown("KEY_OK"):

                # you are selecting something
                if selected is None:

                    # save selected
                    selected = self.columns[cursorCoordinates[0]][cursorCoordinates[1]:]

                    # remember where the selection is
                    selectedCoordinates = cursorCoordinates.copy()

                    # outline what you have selected
                    outLine(cursorCoordinates[0], cursorCoordinates[1], len(self.columns[cursorCoordinates[0]]) - 1, selectedColor)

                # you are trying to move what you have selected to the current location
                else:

                    # can move "selected" to that location
                    if selected[0].cardColor[0] > 150 > self.columns[cursorCoordinates[0]][cursorCoordinates[1]:][0].cardColor[0] \
                            or selected[0].cardColor[0] < 150 < self.columns[cursorCoordinates[0]][cursorCoordinates[1]:][0].cardColor[0]:

                        # remove selected outline
                        outLine(selectedCoordinates[0], selectedCoordinates[1],
                                len(self.columns[cursorCoordinates[0]]) - 1, gameBackgroundColor)

                        # remove the card(s) that you have selected
                        fill_rect(startX + (selectedCoordinates[0] * horizontalSpacing), startY + (selectedCoordinates[1] * verticalSpacing),
                                  horizontalWidthOfCard, 222, gameBackgroundColor)

                        # add the cards in the spot where you selected
                        displaySingleStack(startX + (cursorCoordinates[0] * horizontalSpacing), startY + (cursorCoordinates[1] * verticalSpacing), selected)

                        # remove the selected cards from the columns
                        del self.columns[selectedCoordinates[0]][selectedCoordinates[1]:]

                        # add selected cards to the appropriate location in columns
                        for item in selected:
                            self.columns[cursorCoordinates[0]].append(item)

                        # stop selecting
                        selected = None

            # wants to move cursor down
            elif keydown("KEY_DOWN"):

                # not already at the bottom of current stack
                if len(self.columns[cursorCoordinates[0]]) - 1 != cursorCoordinates[1]:

                    # remove old outline
                    outLine(cursorCoordinates[0], cursorCoordinates[1],
                            len(self.columns[cursorCoordinates[0]]) - 1, gameBackgroundColor)

                    # move cursor down
                    cursorCoordinates[1] -= 1

                    # create new outline
                    outLine(cursorCoordinates[0], cursorCoordinates[1],
                            len(self.columns[cursorCoordinates[0]]) - 1, notSelectedOutlineColor)

            # wants to move cursor up
            elif keydown("KEY_UP"):

                # not already at the top of current stack
                if cursorCoordinates[1] != 0:

                    # remove old outline
                    outLine(cursorCoordinates[0], cursorCoordinates[1],
                            len(self.columns[cursorCoordinates[0]]) - 1, gameBackgroundColor)

                    # move cursor up
                    cursorCoordinates[1] += 1

                    # create new outline
                    outLine(cursorCoordinates[0], cursorCoordinates[1],
                            len(self.columns[cursorCoordinates[0]]) - 1, notSelectedOutlineColor)

            # wants to move cursor right
            elif keydown("KEY_RIGHT"):

                # not already at the far right
                if cursorCoordinates[0] != 6:

                    # at least one column to the right has cards
                    if self.columns[cursorCoordinates[0]][cursorCoordinates[1] + 1:].count([])\
                            != len(self.columns[cursorCoordinates[0]][cursorCoordinates[1] + 1:]):

                        # remove old outline
                        outLine(cursorCoordinates[0], cursorCoordinates[1],
                                len(self.columns[cursorCoordinates[0]]) - 1, gameBackgroundColor)

                        # what is added to the x axis index of cursorCoordinates
                        addToXIndex = 1

                        # find the closest column (going right) that has cards
                        while self.columns[cursorCoordinates[0]+addToXIndex][cursorCoordinates[1]] is []:

                            # next column over
                            addToXIndex += 1

                        # move cursor over to the right
                        cursorCoordinates[0] += addToXIndex

                        # create new outline
                        outLine(cursorCoordinates[0], cursorCoordinates[1],
                                len(self.columns[cursorCoordinates[0]]) - 1, notSelectedOutlineColor)

            # wants to move cursor to the left
            elif keydown("KEY_LEFT"):

                # not already at the far left
                if cursorCoordinates[0] != 0:

                    # at least one column to the left has cards
                    if self.columns[cursorCoordinates[0]][:cursorCoordinates[1]].count([]) \
                            != len(self.columns[cursorCoordinates[0]][:cursorCoordinates[1]]):

                        # remove old outline
                        outLine(cursorCoordinates[0], cursorCoordinates[1],
                                len(self.columns[cursorCoordinates[0]]) - 1, gameBackgroundColor)

                        # what is added to the x axis index of cursorCoordinates
                        addToXIndex = -1

                        # find the closest column (going left) that has cards
                        while self.columns[cursorCoordinates[0] + addToXIndex][cursorCoordinates[1]] is []:

                            # next column over
                            addToXIndex -= 1

                        # move cursor over to the left
                        cursorCoordinates[0] += addToXIndex

                        # create new outline
                        outLine(cursorCoordinates[0], cursorCoordinates[1],
                                len(self.columns[cursorCoordinates[0]]) - 1, notSelectedOutlineColor)


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
        if stackData[cardIndex][2]:

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


# shuffles a list and returns the shuffled one
def shuffleDeck(mixMe):

    # the cards that haven't been added to the new list
    haveNotPicked = mixMe.copy()

    # list of shuffled cards
    shuffledList = []

    # at least one card hasn't been used yet
    while haveNotPicked:

        # pick a random card from those that haven't already been picked, remove that card from the list of not been picked
        shuffledList.append(haveNotPicked.pop(randint(0, len(haveNotPicked)-1)))

    # return the shuffled deck
    return shuffledList


# a place holder function until we put it on the calculator
def keydown(string):
    pass


startX = 10
startY = 10

drawPileX = 265
drawPileY = 10

aceSpacingY = 80

verticalSpacing = 17
horizontalSpacing = 32

horizontalWidthOfCard = 30
verticalHeightOfCard = 15

outLineWidth = 2

xSpaceForIcons = 20
ySpaceForIcons = 3

cardNotFlippedColor = (92, 177, 243)
gameBackgroundColor = (72, 176, 74)

diamondsColor = (239, 80, 80)
heartsColor = (187, 45, 38)
spadesColor = (47, 58, 87)
clubsColor = (22, 22, 36)

selectedColor = (0, 255, 0)
notSelectedOutlineColor = (0, 0, 0)

baseCardColor = (200, 200, 200)


game = Board()
game.newGame()

displayBoard(game)
outLine(3, 0, 3, (0, 0, 0))
tk.mainloop()