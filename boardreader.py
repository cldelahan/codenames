# takes in a String fileName
# and returns a String[] of the words in it
def readBoard(fileName):
    words = []
    fileObject = open(fileName, "r")
    words = fileObject.read().split()
    return words

# takes in a String fileName
# and returns a char[] of the keys
def readKeycard(fileName):
    fileObject = open(fileName, "r")
    keyString = fileObject.read()
    print(keyString)
    key = []
    for i in range (len(keyString)-1):
        if (keyString[i] != "\n"):
            key.append(keyString[i])
    return key

# takes in two arrays and a char,
# the board (String[]), keys(char[]), and what item (char) to search for
# and returns all words of that type
def getWords(board, keys, type):
    if (len(board) != len(keys)):
        raise ValueError("Board size is not equal to Key size")
    output = []
    for i in range (0, len(board), 1):
        if (keys[i] == type):
            output.append(board[i])
    return output

'''board = readBoard("board.txt")
keycard = readKeycard("keycard.txt")
blueWords = getWords(board, keycard, 'B')
redWords = getWords(board, keycard, 'R')
loseWords = getWords(board, keycard, 'X')
print(blueWords)
print(redWords)
print(loseWords)'''
