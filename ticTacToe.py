import random

board = {"top-l":" ","top-m":" ","top-r":" ",
         "mid-l":" ","mid-m":" ","mid-r":" ",
         "bot-l":" ","bot-m":" ","bot-r":" "}

def printBoard(b):
    print(b["top-l"] + " | " + b["top-m"] + " | " + b["top-r"])
    print("---------")
    print(b["mid-l"] + " | " + b["mid-m"] + " | " + b["mid-r"])
    print("---------")
    print(b["bot-l"] + " | " + b["bot-m"] + " | " + b["bot-r"])



print("X or O ?") #Player joga sempre primeiro
token = input()

def play(b, t):
    while True:
        print("Pick a move: top-l, top-m, top-r, mid..., bot...")
        move = input()
        b.update({move: t})
        
        if not checkVictory(b):
            computerMove(b,t)

        printBoard(board)
        
        if checkVictory(b):
            print("\nThe End")
            break   
    
def checkVictory(b):
    if b["top-l"] == b["top-m"] == b["top-r"] and b["top-l"]!=" ":
        return True
    if b["mid-l"] == b["mid-m"] == b["mid-r"] and b["mid-l"]!=" ":
        return True
    if b["bot-l"] == b["bot-m"] == b["bot-r"] and b["bot-l"]!=" ":
        return True

    if b["top-l"] == b["mid-m"] == b["bot-r"] and b["top-l"]!=" ":
        return True
    if b["top-r"] == b["mid-m"] == b["bot-l"] and b["top-r"]!=" ":
        return True    

    if b["top-l"] == b["mid-l"] == b["bot-l"] and b["top-l"]!=" ":
        return True
    if b["top-m"] == b["mid-m"] == b["bot-m"] and b["top-m"]!=" ":
        return True    
    if b["top-r"] == b["mid-r"] == b["bot-r"] and b["top-r"]!=" ":
        return True
    
    list_values = list(b.values())
    if " " not in list_values: #parar quando n ha mais moves
        return True
    
    return False

def computerMove(b,t):
    computerT = " "
    if t=="X":
        computerT = "O"
    else:
        computerT = "X"

    list_keys = list(b.keys())
    r = random.randint(0,8)

    while b[list_keys[r]] != " " : #para nao jogar em lugares ocupados
        r = random.randint(0,8)
    b.update({list_keys[r]: computerT})


play(board, token)
