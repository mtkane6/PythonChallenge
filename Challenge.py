import string

"""
This program accepts as input a grid of letters of any size, and a list of words.
In this case the list of words is the full text of Shakespeare's "Love Labour's Lost."
The list of words has been stripped of white space and punctuation.

First, I turn the grid into a very long list of characters, and create a dictionary of
all the words in the word list, mapped word.upper() : len(word) (all uppercase words).
I then utillize a zip() function to find the longest word remaining in the dictionary, 
and compare it to my very long list of letters to ensure the grid even comprises all 
the letters of this word, if not it is removed from the dictionary and we move on to the 
next word.

Once I find a word whose letters exist in the grid in some form, I begin a iterative search
through the grid for the first letter of that word to use as a starting point.  From there 
I begin a recursive search for the next remaining letters in the pattern depicted below.

 ----- Example of valid knight-moves -----

        [-,-,T,-,A,-,-,-],
        [-,E,-,-,-,R,-,-],
        [-,-,-,A,-,-,-,-], <-- starting from this "A"
        [-,W,-,-,-,A,-,-],
        [-,-,R,-,U,-,-,-],

This program assumes the most recent letter found represents the "A" 
in the center of the grid above.  The progam will examine all 8 locations
in a clockwise fashion, beginning with the very top-most "A" in the 
above grid.  The search will continue recursively until the last letter
of the current word is found. 
If ever the next letter cannot be found via a legal knight-move, the next logest 
word will be searched for. 
In the end, the longest word found in the grid will be returned.

"""


# accepts a 2D grid of letters, and a word list
def Wordsearch(grid, wordList):
    if len(wordList) == 0:
        return False
    # turn grid into one large list, to see if current word letters all exist
    entireGrid = []
    [entireGrid.extend(i) for i in grid]

    # turn word list into dict, mapping word to length, w/ no duplicates
    wordDict = {i.upper():len(i) for i in wordList}
    # print(wordDict)

    #starting with longest word, if all letters in grid, begin finding them, else remove from dictionary.
    for i in range(len(wordDict)):
        _,nextLongestWord = max(zip(wordDict.values(),wordDict.keys()))
        nextWordAsList = list(nextLongestWord)
        presenceCheck = all(elem in entireGrid for elem in nextWordAsList)
        if presenceCheck: # if all letters of word are in the grid:
            if (findFirstLetter(nextWordAsList, grid)): #go to first helper function to find instances of first letter of word
                return nextLongestWord #FOUND the longest word in the grid
        del wordDict[nextLongestWord]


# searches iteratively for all instances of first letter of current word (currWord).
def findFirstLetter(currWord, grid): # currWord is a list of letters
    for row in range(len(grid)): #search rows
        for col in range(len(grid[row])): #search columns
            if currWord[0] == grid[row][col]:
                if(findNextLetter(1, currWord, row, col, grid)):
                    return True # FOUND all letters of this word
    return False #did not complete word

# wordIndex == index of current letter searching for in word; currWord == list of letters
# knight-moves are: up/down 2/1, over 1/2
def findNextLetter(wordIndex, currWord, row, col, grid):
    while wordIndex < len(currWord):
        if upperR(wordIndex, currWord, row, col, grid):
            break
        if rUpper(wordIndex, currWord, row, col, grid):
            break
        if rLower(wordIndex, currWord, row, col, grid):
            break
        if lowerR(wordIndex, currWord, row, col, grid):
            break
        if lowerL(wordIndex, currWord, row, col, grid):
            break
        if lLower(wordIndex, currWord, row, col, grid):
            break
        if lUpper(wordIndex, currWord, row, col, grid):
            break
        if upperL(wordIndex, currWord, row, col, grid):
            break
        return False
    return True

    
def upperR(wordIndex, currWord, row, col, grid):
    if (row-2) >= 0 and (col+1) < len(grid[0]): # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row-2][col+1]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord)-1: # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row-2, col+1, grid)
    return  False # didn't find letter, go back to findNextLetter()


def rUpper(wordIndex, currWord, row, col, grid):
    if (row-1) >= 0 and (col+2) < len(grid[0]): # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row-1][col+2]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row-1, col+2, grid)
    return  False # didn't find letter, go back to findNextLetter()
            
def rLower(wordIndex, currWord, row, col, grid):
    if (row+1) < len(grid) and (col+2) < len(grid[0]): # if knight-move would stay w/in grid
        # x = currWord[wordIndex]
        # y = grid[row+1][col+2]
        if currWord[wordIndex] == grid[row+1][col+2]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row+1, col+2, grid)
    return  False# didn't find letter, go back to findNextLetter()

def lowerR(wordIndex, currWord, row, col, grid):
    if (row+2) < len(grid) and (col+1) < len(grid[0]): # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row+2][col+1]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row+2, col+1, grid)
    return  False # didn't find letter, go back to findNextLetter()

def lowerL(wordIndex, currWord, row, col, grid):
    if (row+2) < len(grid) and (col-1) >= 0: # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row+2][col-1]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row+2, col-1, grid)
    return  False # didn't find letter, go back to findNextLetter()

def lLower(wordIndex, currWord, row, col, grid):
    if (row+1) < len(grid) and (col-2) >= 0: # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row+1][col-2]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row+1, col-2, grid)
    return  False # didn't find letter, go back to findNextLetter()

def lUpper(wordIndex, currWord, row, col, grid):
    if (row-1) < len(grid) and (col-2) >= 0: # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row-1][col-2]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row-1, col-2, grid)
    return  False # didn't find letter, go back to findNextLetter()

def upperL(wordIndex, currWord, row, col, grid):
    if (row-2) < len(grid) and (col-1) >= 0: # if knight-move would stay w/in grid
        if currWord[wordIndex] == grid[row-2][col-1]: # if next letter is at this knight-move
            if wordIndex+1 == len(currWord): # if this was the last letter of the word
                return True
            return findNextLetter(wordIndex+1, currWord, row-2, col-1, grid)
    return  False # didn't find letter, go back to findNextLetter()



# import text file
f = open("Shakespeare.txt", "r")
# create a list split on spaces
words = list(f.read().split())
# remove any punctuation like ,."')
words = [item.strip(string.punctuation) for item in words]

# provided grid of letters for this challenge
grid = [["E","X","T","R","A","H","O","P"],
        ["N","E","T","W","O","R","K","S"],
        ["Q","I","H","A","C","I","Q","T"],
        ["B","W","D","I","L","A","T","V"],
        ["L","F","U","N","U","R","X","B"],
        ["O","S","S","Y","N","A","C","K"],
        ["Q","W","O","P","M","T","C","P"],
    [   "K","I","P","A","C","K","E","T"]]

# call to solution, prints longest word found in the grid using legal knigh-moves
print(Wordsearch(grid, words))

