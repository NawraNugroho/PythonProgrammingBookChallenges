#-----------------------------------------------------------------------Challenges Chapter 6-----------------------------------------------------------------------------------------------
#1) Improve the function ask_number()

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question).lower())
        
        if response != None:          
            if response >= high:
                print("Your number is too high")
            elif response < low:
                print("Your number it too low")
            elif response%step != 0:
                print("Your number isn't divisible by", step)
                
    return response


def list_number(high):
    num = []
    for i in range(0, high, 5):
        num.append(i)
    return num


def val(question):
    response1 = None
    while response1 == 5 or response1 == None:
        response1 = int(input(question))
    return response1


value = val("Value other than 5: ")
high = int(input("Highest number in range: "))
number = ask_number("Number to test with: ", value, high, step = value)


if number in list_number(high):
    print(number, "is divisible by both 5 and", value)
else:
    print(number, "isn't divisible by 5, but divisible by", value)

input("\nPress enter to continue.")
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2 and #3) Modifying Guess My Number

#Pseudo Code
#Choose number from 1 to 16 randomly
#Ask for number in range 1 to 16
#While player gueses not correct
#   print number that're left to guess
#   ask for number in range var minimum to var maximum
#   var guesses increase by one   
#   if player guess lower than the number
#       say higher
#       var minimum is player quess + 1
#   if player guess higher than the number
#       say lower
#       var maximum is player guess

print("--------------------------------------------------------------------------------")
import random


def ask_number(question, minimum, maximum):
    """Answer question for range"""
    response = None

    print("\n")
    for i in range(minimum, maximum):
        print(i, end=" ")
        
    while response not in range(minimum, maximum):
        response = int(input(question))

        if response != None:
            if response < minimum:
                print("Too low from range")
            elif response >= maximum:
                print("Too high from range")

    return response


def main():
    low = 1
    high = 101
    number = random.randint(low, high)
    guesses = 0
    print("\nGuess my number from", low, "to", high - 1)

    guess = 0
    
    while guess != number:
        guess = ask_number("\n\nNumber: ", low, high)
        guesses += 1
        if guess > number:
            print("Lower")
            high = guess
        elif guess < number:
            print("Higher")
            low = guess + 1
        elif guess == number:
            print("Correct")
            print("\nYou take", guesses, "guess")
        else:
            print("Wrong input.. try again")

main()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#4) Modify Tic-Tac-Toe
print("--------------------------------------------------------------------------------")

#Tic-Tac-Toe pseudocode
#Display game instruction
#Determine who goes first (computer or human)
#Display Tic-Tac-Toe board
#switch turn
#While nobody's win or tie:
#   if human turn,
#       human make moves
#       display the moves in the board
#   if computer turn,
#       computer make moves
#       display the moves in the board
#Congratulate a winner or declare a tie

import random

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Instruction"""
    print(
        """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0-8. The number
    will correspond to the board position as illustrated:

                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yoursel, human. The ultimate battles is about to begin. \n
    """
    )


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question).lower())
    return response


def pieces():
    """Determine who goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Create new board."""
    board = [] #list
    
    #input " " to the list of board
    for square in range(NUM_SQUARES): 
        board.append(EMPTY)
    return board


def display_board(board):
    """Display game board on a screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """Create list of legal moves."""
    moves = [] #list
    
    #for every EMPTY place in the board, add that (place) index number to the list of moves
    for square in range(NUM_SQUARES): 
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    #To check if there's any winner
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:                        #board[row[1]]
            winner = board[row[0]]                                                          #      -     -    
            return winner                                                                   #       -   -
    #if it's a tie                                                                          #        - -
    if EMPTY not in board:                                                                  #         -                                                            
            return TIE                                                                      #    represent the index number list of board         
    #if there's no winner yet and not a tie                                                                                       
    return None

def first_move(board):
    FIRST = ((0, 4),
             (2, 4),
             (6, 4),
             (8, 4))

    #if index 4 is not empty
    if board[4] != EMPTY:
        option = random.randrange(0, 4)
        goes = FIRST[option][0]
        return goes
    
    #if index 4 is empty
    else:
        for row in FIRST:
            if board[row[0]] != EMPTY:
                goes = row[1]
                return goes
        
        #If everything is empty    
        option = random.randrange(0, 4)
        goes = FIRST[option][0]
        return goes

def second_move(board):
    SECOND = ((0, 1, 2),
              (0, 3, 6),
              (2, 5, 8),
              (6, 7, 8))

def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("\nWhere will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another. \n")
    print("Fine...")
    return move



def computer_move(board, computer, human, tried):
    """Make computer move."""
    #make a copy to work with since function will be changing list
    board = board[:]
    #the best position to have in order
    BEST_MOVES = (0, 2, 6, 8, 4, 1, 3, 5, 7)

    print("I shall take square number", end=" ")
    

    #if computer can win, take that move
    #------------------------------------------------------------
    #To check one by one move, if computer can win the next move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY


    #if human can win, block that move
    #------------------------------------------------------------
    #To check one by one move, if human can win the next move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

        
    #first move
    if tried <= 1:  
        move = first_move(board)
        print(move)
        return move
    else:
        #Since no one can win on the next move, pick best open square
        #option = random.randrange(0, 4)
        #move = BEST_MOVES[option]
        for move in BEST_MOVES:
            if move in legal_moves(board):
                print(move)
                return move
            else:
                for move in BEST_MOVES:
                    if move in legal_moves(board):
                        print(move)
                        return move


def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Congratulate the winner"""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more. \n" \
              "Proof that computer are superior to human in all regards.")

    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" \
              "But never again! I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" \
              "Celebrate today... for this is the best you will ever achieve.")


def main():
    display_instruct()
    computer, human = pieces() #who goes first
    tried = 0
    turn = X 
    board = new_board() #list of moves #Example: ["X", "O", "X", " ", " ", "O", " ", " "]
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
            tried += 1
            print("Tried =", tried)
            print("winner(board) =", winner(board))
        else:
            move = computer_move(board, computer, human, tried)
            board[move] = computer
            tried += 1
            print("Tried =", tried)
            print("winner(board) =", winner(board))
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


#start the program
main()
input("\n\nPress the enter key to quit.")
    
    

