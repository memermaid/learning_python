board = [' ' for i in range(10)]

def main():
    intro()
    pl1_letter = player1_letter()
    pl2_letter = player2_letter(pl1_letter)
    print('Player 2, you play "' + pl2_letter + '".\n')
    while not boardisfull(board):
        print('Player 1')
        player1 = int(player_move())
        place_letter(player1, pl1_letter)
        if iswinner(board, pl1_letter):
            print('Player 1 won!')
            break
        if boardisfull(board):
            print('It is a draw!')
            break
        print('Player 2')
        player2 = int(player_move())
        place_letter(player2, pl2_letter)
        if iswinner(board, pl2_letter):
            print('Player 2 won!')
            break
        if boardisfull(board):
            print('It is a draw!')

def player1_letter(): # First player letter choice
    letter = input('Player 1, what letter do you choose? X or O? ').capitalize()
    print()
    while letter != 'X' and letter != 'O':
        print("Wrong input!\n")
        letter = input('Player 1, what letter do you choose? X or O? ').capitalize()
    return letter
    
def player2_letter(pl1): # Assigns a letter to 2nd player
    return 'X' if pl1 == 'O' else 'O'

def player_move(): # Asks a player for a move
    isvalid = False
    while not isvalid:
        move = input("What is your move? ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if position_is_open(move):
                    break
                else:
                    print('This position is taken!\n')
            else:
                print('Please choose a position within a range 1-9.\n')
        except ValueError:
                print("Invalid input.\n")
                continue
    return move

def position_is_open(move): # Checks if position is available
    return board[move-1] == ' '

def place_letter(move, letter): # Fills position with a letter
    board[move-1] = letter
    printboard()


def printboard(): # Print the board
    print ('\n   |   |   \n', board[0], '|', board[1], '|', board[2], '\n   |   |   \n-----------\n   |   |   \n',board[3], '|', board[4], '|', board[5], '\n   |   |   \n-----------\n   |   |   \n',board[6], '|', board[7], '|', board[8], '\n   |   |   \n')

def iswinner(board, letter): # Checks if a player is a winner
    return (board[0] == board[1] == board[2] == letter) or (board[3] == board[4] == board[5] == letter) or (board[6] == board[7] == board[8] == letter) or (board[0] == board[3] == board[6]== letter) or (board[1] == board[4] == board[7] == letter) or (board[2] == board[5] == board[8] == letter) or (board[0] == board[4] == board[8] == letter) or (board[2] == board[4] == board[6] == letter) 

def intro():
    print("Welcome to Tic Tac Toe Game.\nThe board is positioned 1-9 starting at the top left.\nTo win the game, you need to fill a row, column or diagonal with you letter.")
    printboard()

def boardisfull(board): # Checks if the board is full
    return board.count(' ') == 1

if __name__ == '__main__':
    main()