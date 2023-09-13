import math
import random


# Team: Hunter Termo (alone)
# Date: 9/13/2023
# Assignment: 1

# Source code referenced:
# Author: Kylie Ying
# Title: Tic-Tac-Toe AI
# Type: Source code
# Web Address: https://github.com/kying18/tic-tac-toe

# Player class
class Player():
    def __init__(self, letter):
        # letter is 'x' or 'o'
        self.letter = letter
    
    def get_move(self, game):
        pass

# Random computer player class (will select a random available spot)
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

# Human player class (user)
class HumanPlayer(Player):
    # assign letter to human player
    def __init__(self, letter):
        super().__init__(letter)
    
    # ask user which space they'd like to move
    def get_move(self, game):
        # initialize valid_square and value variable
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8):")
            # try block will test for error (user tries to go in square already taken)
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        # if no error, return value
        return val

# Intelligent computer player class (AI)
class IntelligentComputerPlayer(Player):
    # assign letter to computer player
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # if board is empty, randomly choose spot (only occurs when computer makes first move)
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # if not first move of the game, get square based of minimax alg
            square = self.minimax(game, self.letter)['position']
        return square
    
    # minimax algorithm to find best possible move
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        # first we check if previous move is a winner (base case)
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1*(state.num_empty_squares() + 1)
                   }
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
        
        # initalize best move dictionary
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        # algorithm to create game states and test possible moves
        for possible_move in state.available_moves():
            #step 1: make a move, try that spot
            state.make_move(possible_move, player)
            #step 2: recurse using minimax to simulate the game after making said move
            sim_score = self.minimax(state, other_player) # alternate players
            
            #step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            #step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                    
        return best # return best move