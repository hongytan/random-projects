'''
Game
1. Make Board v/
2. Make move v/
3. Decide winner v/

Player
1. Get move v/
'''

import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        rows = [self.board[3*i:3*i+3] for i in range(3)]
        for row in rows:
            print(' | '.join(row))

    # What does a static function do in python?
    def print_num_board(self):
        rows = [[str(3*i),str(3*i+1),str(3*i+2)] for i in range(3)]
        for row in rows:
            print(' | '.join(row))

    @property
    def avail_spots(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, letter, spot):
        self.board[spot] = letter

        if self.is_win(letter, spot):
            self.winner = letter

    def is_win(self, letter, spot):

        # Row 
        row_index = (spot // 3) * 3
        row = [row_index+i for i in range(3)]
        if all([self.board[i] == letter for i in row]):
            return True

        # Column
        col_index = spot % 3
        col = [3*i+col_index for i in range(3)]
        if all([self.board[i] == letter for i in col]):
            return True

        # Diagonal (left to right)
        dia1 = [0,4,8]
        if all([self.board[i] == letter for i in dia1]):
            return True

        # Diagonal (right to left)
        dia2 = [2,4,6]
        if all([self.board[i] == letter for i in dia2]):
            return True

        return False
    
class Computer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        return random.choice(game.avail_spots)

class Human:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        
        move = int(input('Enter a valid position: '))

        while move not in game.avail_spots:
            move = int(input('Enter a valid position: '))

        return move

class Minimax:
    pass

def play(game, player_x, player_o, print_game=True):

    letter = 'x'

    if print_game:
        print("Welcome! The following shows the positioning for the board.")
        game.print_num_board()

    while ' ' in game.board:

        if letter == 'x':
            move = player_x.get_move(game)
        else:
            move = player_o.get_move(game)

        game.make_move(letter, move)

        if print_game:
            print()
            game.print_board()
            print()
            game.print_num_board()
            print()

        if game.winner:
            return letter

        letter = 'x' if letter == 'o' else 'o'

t = TicTacToe()
player_x = Computer('x')
player_o = Human('o')

winner = play(t,player_x,player_o)

if winner:
    print(f"{winner} wins!")
else:
    print("It's a tie!")

