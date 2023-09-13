from game import TicTacToe, play
from players import HumanPlayer, RandomComputerPlayer, IntelligentComputerPlayer


# main function
if __name__ == '__main__':
    print('Welcome to my Tic-Tac-Toe game!')
    print('You will face off against a smart AI algorithm, so don\'t get discouraged if you lose.')
    print('You will be playing as the \'X\' character and the computer will be playing as the \'O\' character.')
    # create x_player using HumanPlayer class
    x_player = HumanPlayer('X')
    # create o_player using IntelligentComputerPlayer class
    o_player = IntelligentComputerPlayer('O')
    # create instance of the game
    t = TicTacToe()

    # initialize variable that tells the program whether or not user wants to play
    choice = '1'
    # play the game while choice equals '1'
    while choice == '1':
        play(t, x_player, o_player, print_game = True)
      # after done playing, ask user if they want to play again
        print('Would you like to play again? Enter 1 if so, and anything else if not.')
        choice = input('Enter: ')  # user enters if they want to play again
        if choice != '1':  # if not, print goodbye message
            print('Thanks for playing! See you soon. Maybe you\'ll win next time \U0001F609.')
