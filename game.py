import math
import time
from player import HumanPlayer, RandomComputerPlayer, IntelligentComputerPlayer


class TicTacToe:
    def __init__(self):
        #Using single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # Keep track of winner
        
    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # function used to clear board (same as __init__ function)
    def clear_board(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # Keep track of winner
      
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (what numbers correspond to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print()
    
    # function to find all available moves
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    
    # function to find empty squares
    def empty_squares(self):
        return ' ' in self.board
    
    # function to find the number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')
    
    # function to make each move and change ' ' to player's letter
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # if move is a winning move, change winner to player's letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # function to check if a move is a winning move
    def winner(self, square, letter):
        # winner if 3 in a row
        # first check row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        # can only be diagonal win if square is even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diag.
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diag.
            if all([spot == letter for spot in diagonal2]):
                return True
            
        # if all checks fail, move was not a winning move
        return False

# function to play game
def play(game, x_player, o_player, print_game = True):

    # at beginning of game, clear the board
    game.clear_board()
    
    # if print_game == True, print the current board
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #starting letter
    while game.empty_squares(): #while there are still empty squares
        # get players move
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        #Function to make a move
        if game.make_move(square, letter):
            # print that player has moved to a square, and also print board
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')
            
            # if there's a winner, print which player won
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                    
            #after move is made, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
        
        # short time delay for readability when running
        time.sleep(.8)
            
    # if no more empty squares and function has not returned a winner, print that the game was a tie
    if print_game:
        print("It's a tie!")
