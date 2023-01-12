import random

class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        rows = [self.board[3*i:3*i+3] for i in range(3)]
        for row in rows:
            print(' | '.join(row))

    def make_move(self, letter, square):
        self.board[square] = letter

        if self.is_win(letter, square):
            self.current_winner = letter

    @property
    def available_squares(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def is_win(self, letter, square):
        '''
        There are 8 possible win conditions - 3 horizontal & veritcal, 2 diagonal
        '''

        row_ind = square // 3
        row = [row_ind*3+i for i in range(3)]
        if all(letter==self.board[i] for i in row):
            return True

        # Column win
        col_ind = square % 3
        col = [col_ind + i*3 for i in range(3)]
        if all(letter==self.board[i] for i in col):
            return True

        # Diagonal win
        diagonal1 = [0,4,8]
        if all(letter==self.board[i] for i in diagonal1):
            return True

        diagonal2 = [2,4,6]
        if all(letter==self.board[i] for i in diagonal2):
            return True
        
        return False

class Computer():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        move = random.choice(game.available_squares)
        return move

class Human():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        move = int(input("Enter a valid move: "))
        while move not in game.available_squares:
            move = int(input("Invalid move! Enter a valid move: "))
        return move

class GeniusComputer():
    def __init__(self, letter):
        self.letter = letter

    

def play(game, x_player, o_player, print_game=True):
    
    letter = 'x'

    while ' ' in game.board:
        if letter == 'x':
            move = x_player.get_move(game)
        else:
            move = o_player.get_move(game)

        game.make_move(letter, move)

        if print_game and letter == 'x':
            game.print_board()

        if game.current_winner:
            print(f"{letter} wins!")
            if print_game:
                game.print_board()
            return letter

        letter = 'x' if letter == 'o' else 'o'

    print("It's a tie!")

x_player = Computer('x')
o_player = Human('o')

t = TicTacToe()
letter = play(t, x_player, o_player)


# board = ['','','3','','','a','b','2']
# print([i for i, spot in enumerate(board) if spot == ''])