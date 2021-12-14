from random import randint
from kandinsky import *
from ion import *


# takes the color of a card returns a card object
def getCard(infoColor):
    # card not displaying info -> (88-104, 180, 244)

    # initialize variable
    cardType = None

    # card is visible (200, 200, 200)
    if infoColor[0] >= 200:

        # color without special info
        normalColor = baseCardColor
        showTheInfo = True

    # card not flipped
    else:

        # color without special info
        normalColor = cardNotFlippedColor
        showTheInfo = False

    # card is red genera
    if (infoColor[0] - normalColor[0]) / 8 > 0:

        # 1 = diamonds (-1) , 2 = hearts (-2)
        cardType = ((infoColor[0] - normalColor[0]) // 8) * -1

    # card is black genera
    elif (infoColor[2] - normalColor[2]) / 8 > 0:

        # 1 = clubs (0), 2 = spades (1)
        cardType = ((infoColor[2] - normalColor[2]) // 8) - 1

    # card has no type
    else:
        print("(card has no type) from getCard()")
        print("color:", infoColor)

    # no number
    if (infoColor[1] - normalColor[1]) / 4 == 0:
        cardNumber = 0

    # card has number
    else:

        # calculate card number based on color
        cardNumber = (infoColor[1] - normalColor[1]) // 4

    # return the card that the color represents
    return [cardType, cardNumber, showTheInfo]


# takes a set of coordinates calls on the getCard to get the card at given cords
def takeCordsGiveCard(setOfCords):
    # get the color of the pixel at setOfCords & return it
    return getCard(get_pixel(startX + (setOfCords[0] * horizontalSpacing), startY + (setOfCords[1] * verticalSpacing)))


# returns a list of new cards
def getNewDeck():
    # initialize the new deck
    newDeck = []

    # loop through each card type
    for type in [-2, -1, 0, 1]:

        # loop though the card numbers
        for number in range(1, 14):
            # add new card to deck
            newDeck.append([type, number, False])

    # list of shuffled cards
    shuffledList = []

    # at least one card hasn't been used yet
    while newDeck:
        # pick a random card from those that haven't already been picked, remove that card from the list of not been picked
        shuffledList.append(newDeck.pop(randint(0, len(newDeck) - 1)))

    # return the shuffled deck
    return shuffledList


# displays a stack
def displaySingleStack(x, y, stackData):
    # loop through each card in the stack
    for cardIndex in range(len(stackData)):
        displaySingleCard(x, y + (cardIndex * verticalSpacing), stackData[cardIndex])


# displays a card
def displaySingleCard(x, y, cardData):
    # the information should be displayed
    if cardData[2]:

        # diamonds
        if cardData[0] == -1:
            cc = diamondsColor

        # spades
        elif cardData[0] == 1:
            cc = spadesColor

        # clubs
        elif cardData[0] == 0:
            cc = clubsColor

        # hearts
        else:
            cc = heartsColor

        # display information
        fill_rect(x, y, horizontalWidthOfCard, verticalHeightOfCard, baseCardColor)
        draw_string(str(cardData[1]), x, y, cc, baseCardColor)
        fill_rect(x, y + verticalHeightOfCard, horizontalWidthOfCard, 3, gameBackgroundColor)

        chosenColor = list(baseCardColor)

        # red -2, -1
        if cardData[0] < 0:
            chosenColor[0] += (abs(cardData[0]) * 8)

        # black 0, 1
        else:
            chosenColor[2] += (abs(cardData[0]) + 1) * 8

        chosenColor[1] += abs(cardData[1]) * 4

        # change color of top left pixel to have special information
        fill_rect(x, y, 1, 1, chosenColor)

        x += xSpaceForIcons
        y += ySpaceForIcons

        # display heart icon
        if cardData[0] == -2:

            # layer 0
            fill_rect(x + 1, y, 2, 1, heartsColor)
            fill_rect(x + 6, y, 2, 1, heartsColor)

            # layer 1
            fill_rect(x, y + 1, 4, 1, heartsColor)
            fill_rect(x + 5, y + 1, 4, 1, heartsColor)

            # layer 2
            fill_rect(x, y + 2, 9, 1, heartsColor)

            # layer 3
            fill_rect(x, y + 3, 9, 1, heartsColor)

            # layer 4
            fill_rect(x, y + 4, 9, 1, heartsColor)

            # layer 5
            fill_rect(x + 1, y + 5, 7, 1, heartsColor)

            # layer 6
            fill_rect(x + 2, y + 6, 5, 1, heartsColor)

            # layer 7
            fill_rect(x + 3, y + 7, 3, 1, heartsColor)

            # layer 8
            fill_rect(x + 4, y + 8, 1, 1, heartsColor)

        # display diamond icon
        elif cardData[0] == -1:

            # layer 0
            fill_rect(x + 4, y, 1, 1, diamondsColor)

            # layer 1
            fill_rect(x + 3, y + 1, 3, 1, diamondsColor)

            # layer 2
            fill_rect(x + 2, y + 2, 5, 1, diamondsColor)

            # layer 3
            fill_rect(x + 1, y + 3, 7, 1, diamondsColor)

            # layer 4
            fill_rect(x, y + 4, 9, 1, diamondsColor)

            # layer 5
            fill_rect(x + 1, y + 5, 7, 1, diamondsColor)

            # layer 6
            fill_rect(x + 2, y + 6, 5, 1, diamondsColor)

            # layer 7
            fill_rect(x + 3, y + 7, 3, 1, diamondsColor)

            # layer 8
            fill_rect(x + 4, y + 8, 1, 1, diamondsColor)

        # display club icon
        elif cardData[0] == 0:

            # layer 0
            fill_rect(x + 2, y, 5, 1, clubsColor)

            # layer 1
            fill_rect(x + 2, y + 1, 5, 1, clubsColor)

            # layer 2
            fill_rect(x, y + 2, 2, 1, clubsColor)
            fill_rect(x + 3, y + 2, 3, 1, clubsColor)
            fill_rect(x + 7, y + 2, 2, 1, clubsColor)

            # layer 3
            fill_rect(x, y + 3, 3, 1, clubsColor)
            fill_rect(x + 4, y + 3, 1, 1, clubsColor)
            fill_rect(x + 6, y + 3, 3, 1, clubsColor)

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
            fill_rect(x + 4, y + 7, 1, 1, clubsColor)

            # layer 8
            fill_rect(x + 3, y + 8, 3, 1, clubsColor)

        # display spade icon
        elif cardData[0] == 1:

            # layer 0
            fill_rect(x + 4, y, 1, 1, spadesColor)

            # layer 1
            fill_rect(x + 3, y + 1, 3, 1, spadesColor)

            # layer 2
            fill_rect(x + 2, y + 2, 5, 1, spadesColor)

            # layer 3
            fill_rect(x + 1, y + 3, 7, 1, spadesColor)

            # layer 4
            fill_rect(x, y + 4, 9, 1, spadesColor)

            # layer 5
            fill_rect(x, y + 5, 9, 1, spadesColor)

            # layer 6
            fill_rect(x, y + 6, 9, 1, spadesColor)

            # layer 7
            fill_rect(x + 1, y + 7, 2, 1, spadesColor)
            fill_rect(x + 4, y + 7, 1, 1, spadesColor)
            fill_rect(x + 6, y + 7, 2, 1, spadesColor)

            # layer 8
            fill_rect(x + 3, y + 8, 3, 1, spadesColor)

    # just show the back of the card instead
    else:

        # display back of card
        fill_rect(x, y, horizontalWidthOfCard, verticalHeightOfCard, cardNotFlippedColor)

        chosenColor = list(cardNotFlippedColor)

        # red -1, -2
        if cardData[0] < 0:
            chosenColor[0] += abs(cardData[0]) * 8

        # black 1, 0
        else:
            chosenColor[2] += (abs(cardData[0]) + 1) * 8

        chosenColor[1] += abs(cardData[1]) * 4
        fill_rect(x, y, 1, 1, chosenColor)


# displays the ace piles
def displayAceStacks(stackData):
    aceSpacingY = 80
    x = drawPileX
    y = drawPileY + aceSpacingY

    displaySingleStack(x, y, stackData)


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


# creates an outline
def outLine(columnIndex, fromRow, toRow, c):
    # x coordinate where we start drawing
    x = startX + (horizontalSpacing * columnIndex)

    # y coordinate (top left)
    y1 = startY + (verticalSpacing * fromRow)

    yDistance = verticalSpacing * (abs(fromRow - toRow) + 1)

    # left side outline
    fill_rect(x - outLineWidth, y1 - outLineWidth, outLineWidth, yDistance, c)

    # right side outline
    fill_rect(x + horizontalWidthOfCard, y1, outLineWidth, yDistance, c)

    # top outline
    fill_rect(x, y1 - outLineWidth, horizontalWidthOfCard + outLineWidth, outLineWidth, c)

    # bottom outline
    fill_rect(x - outLineWidth, y1 + yDistance - outLineWidth, horizontalWidthOfCard + outLineWidth, outLineWidth, c)


# slots where the aces go
aceSlots = [(-2, 0, True), (-1, 0, True), (0, 0, True), (1, 0, True)]

# a list showing how many cards are in each column
cardsInEachColumn = [0, 0, 0, 0, 0, 0, 0]

startX = 10
startY = 10

verticalSpacing = 17
horizontalSpacing = 32

drawPileX = startX + (horizontalSpacing * 8)
drawPileY = startY

horizontalWidthOfCard = 30
verticalHeightOfCard = 15

outLineWidth = 2

xSpaceForIcons = 20
ySpaceForIcons = 3

cardNotFlippedColor = (88, 180, 232)
gameBackgroundColor = (72, 176, 72)
baseCardColor = (200, 200, 200)

diamondsColor = (239, 80, 80)
heartsColor = (187, 45, 38)
spadesColor = (47, 58, 87)
clubsColor = (22, 22, 36)

selectedColor = (0, 255, 0)
notSelectedOutlineColor = (8, 8, 8)


# creates a new game

# change that deck

# get a deck of cards
deck = getNewDeck()

# color the background
fill_rect(0, 0, 320, 222, gameBackgroundColor)

# display draw pile
displayDrawPile(deck)

# display the ace piles
displayAceStacks(aceSlots)

# iterate through the columns
for cardsInEachStack in range(1, 8):

    # add cards for the amount needed in each stack (column)
    for singleCard in range(cardsInEachStack):

        # add a card to the current column
        cardsInEachColumn[cardsInEachStack - 1] += 1

        # last card in this column
        if singleCard + 1 == cardsInEachStack:

            # flip the card at the bottom of the column
            deck[0][2] = True

        # display the card on the screen
        displaySingleCard(startX + (horizontalSpacing * (cardsInEachStack - 1)), startY + (verticalSpacing * singleCard),
                          deck.pop(0))


# coordinates of what is selected
selectedCoordinates = None

# the coordinates of outline/cursor
cursorCoordinates = [6, 3]

# key was down or not
keyOk = keyDown = keyUp = keyRight = keyLeft = keyNewCard = False

# game loop
while True:

    if keydown(KEY_OK):
        keyOk = True
    elif keydown(KEY_UP):
        keyUp = True
    elif keydown(KEY_DOWN):
        keyDown = True
    elif keydown(KEY_RIGHT):
        keyRight = True
    elif keydown(KEY_LEFT):
        keyLeft = True
    if keydown(KEY_SHIFT):
        keyNewCard = True

    # pressed OK
    if not keydown(KEY_OK) and keyOk:

        keyOk = False

        # you are selecting something
        if not selectedCoordinates:

            # trying to select a card that has not been flipped
            if takeCordsGiveCard(cursorCoordinates)[2] is False:
                selectedCoordinates = None
                continue

            # remember where the selection is
            selectedCoordinates = cursorCoordinates.copy()

            # outline what you have selected
            outLine(cursorCoordinates[0], cursorCoordinates[1], cardsInEachColumn[cursorCoordinates[0]] - 1,
                    selectedColor)

        # you are trying to move what you have selected to the current location
        else:

            # trying to put what you have where it is it does nothing, next iteration
            if selectedCoordinates == cursorCoordinates:
                # remove selected outline
                outLine(selectedCoordinates[0], selectedCoordinates[1],
                        cardsInEachColumn[selectedCoordinates[0]] - 1, gameBackgroundColor)

                # stop selecting
                selectedCoordinates = None

                continue

            # can move "selected" to that location based on color
            if int(takeCordsGiveCard(selectedCoordinates)[0] * 0.5 + 1) + int(
                    takeCordsGiveCard(cursorCoordinates)[0] * 0.5 + 1) == 1:

                # can move "selected" based on number
                if takeCordsGiveCard(selectedCoordinates)[1] == takeCordsGiveCard([cursorCoordinates[0],
                                                                                   cardsInEachColumn[
                                                                                       cursorCoordinates[0]] - 1])[
                    1] - 1:

                    # loop through the selected cards
                    for cardIndex in range(cardsInEachColumn[selectedCoordinates[0]] - selectedCoordinates[1]):
                        # display the cards in the new spot
                        displaySingleCard(startX + (cursorCoordinates[0] * horizontalSpacing),
                                          startY + (cardsInEachColumn[cursorCoordinates[0]] * verticalSpacing),
                                          takeCordsGiveCard(
                                              [selectedCoordinates[0], selectedCoordinates[1] + cardIndex]))

                        # add a card to the current column
                        cardsInEachColumn[cursorCoordinates[0]] += 1
                        cardsInEachColumn[selectedCoordinates[0]] -= 1

                    # remove the card(s) that you have selected
                    fill_rect(startX + (selectedCoordinates[0] * horizontalSpacing),
                              startY + (selectedCoordinates[1] * verticalSpacing),
                              horizontalWidthOfCard, 222, gameBackgroundColor)

            # remove selected outline
            outLine(selectedCoordinates[0], selectedCoordinates[1],
                    cardsInEachColumn[selectedCoordinates[0]] - 1, gameBackgroundColor)

            # the selection didn't take the last card in the stack
            if selectedCoordinates[1] > 0:
                cardToFlip = takeCordsGiveCard([selectedCoordinates[0], selectedCoordinates[1] - 1])
                cardToFlip[2] = True

                displaySingleCard(startX + (selectedCoordinates[0] * horizontalSpacing),
                                  startY + (verticalSpacing * (selectedCoordinates[1] - 1)), cardToFlip)

            # stop selecting
            selectedCoordinates = None

    # wants to move cursor down
    elif not keydown(KEY_DOWN) and keyDown:

        keyDown = False

        # not already at the bottom of current stack
        if cardsInEachColumn[cursorCoordinates[0]] - 1 != cursorCoordinates[1]:
            # remove old outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, gameBackgroundColor)

            # move cursor down
            cursorCoordinates[1] += 1

            # create new outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, notSelectedOutlineColor)

    # wants to move cursor up
    elif not keydown(KEY_UP) and keyUp:
        keyUp = False

        # not already at the top of current stack
        if cursorCoordinates[1] != 0:
            # remove old outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, gameBackgroundColor)

            # move cursor up
            cursorCoordinates[1] -= 1

            # create new outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, notSelectedOutlineColor)

    # wants to move cursor right
    elif not keydown(KEY_RIGHT) and keyRight:
        keyRight = False

        # at least one column to the right has cards
        if cursorCoordinates[0] != 6 and any(cardsInEachColumn[cursorCoordinates[0] + 1:]):

            # remove old outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, gameBackgroundColor)

            # what is added to the x axis index of cursorCoordinates
            addToXIndex = 1

            # find the closest column (going right) that has cards
            while cardsInEachColumn[cursorCoordinates[0] + addToXIndex] == 0:
                # next column over
                addToXIndex += 1

            # move cursor over to the right
            cursorCoordinates[0] += addToXIndex

            # there are no cards in that column in the row we are on
            if cardsInEachColumn[cursorCoordinates[0]] - 1 < cursorCoordinates[1]:
                # move down to the top card in the column we moved to
                cursorCoordinates[1] = cardsInEachColumn[cursorCoordinates[0]] - 1

            # create new outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, notSelectedOutlineColor)

    # wants to move cursor to the left
    elif not keydown(KEY_LEFT) and keyLeft:
        keyLeft = False

        # not already at the far left and at least one column has cards
        if cursorCoordinates[0] != 0 and any(cardsInEachColumn[:cursorCoordinates[0]]):

            # remove old outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, gameBackgroundColor)

            # what is added to the x axis index of cursorCoordinates
            addToXIndex = -1

            # find the closest column (going left) that has cards
            while cardsInEachColumn[cursorCoordinates[0] + addToXIndex] == 0:
                # next column over
                addToXIndex -= 1

            # move cursor over to the left
            cursorCoordinates[0] += addToXIndex

            # there are no cards in that column in the row we are on
            if cardsInEachColumn[cursorCoordinates[0]] - 1 < cursorCoordinates[1]:
                # move down to the top card in the column we moved to
                cursorCoordinates[1] = cardsInEachColumn[cursorCoordinates[0]] - 1

            # create new outline
            outLine(cursorCoordinates[0], cursorCoordinates[1],
                    cardsInEachColumn[cursorCoordinates[0]] - 1, notSelectedOutlineColor)

    # flip next card in draw pile
    elif not keydown(KEY_SHIFT) and keyNewCard:

        # reset button state
        keyNewCard = False

        # flip the card
        deck[0][2] = True

        # display the card from the top of the deck
        displaySingleCard(drawPileX, drawPileY+verticalSpacing, deck[0])

        # flip the card again
        deck[0][2] = False

        # move the card from the top of the deck to the bottom of the deck
        deck.append(deck.pop(0))

        # deck is empty
        if not deck:

            # remove the draw pile
            fill_rect(drawPileX, drawPileY, horizontalWidthOfCard, verticalHeightOfCard, gameBackgroundColor)
