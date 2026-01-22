# Simple tic-tac-toe game (terminal-based)
# Author: Ifthekar Rahat
# Logic style: function-based

'''features:
1.can play as long as you want
2.level based[easy and hard] (future)
3.smart opponent [simple ai]..(future)
'''

import random

# =========================
# DISPLAY FUNCTIONS
# =========================

def show():
    """Display the current game board."""
    for r in range(3):
        for c in range(3):
            print(board_main[r][c], end=' ')
        print()


def unavl():
    """Show available and unavailable blocks."""
    print('These blocks are not available:', unavailable)
    print('These blocks are available:', bot_available)


# =========================
# PLAYER LOGIC
# =========================

def game_play():
    """Handle player input and move."""
    global quit, turn_num

    while True:
        try:
            playr_input = input("Play your block (1-9) or 'q' to quit --> ").strip()
            if playr_input not in available:
                raise ValueError
        except ValueError:
            print("Invalid value, try again.")
            continue
        break

    if playr_input.isdigit():
        quit = False
        turn_num += 1

        # Update game state
        unavailable.append(playr_input)
        available.remove(playr_input)
        bot_available.remove(playr_input)

        edit(int(playr_input), "playr")
        show()
        checking()

    elif playr_input == 'q':
        quit = True
        print("Match quit by player.")


# =========================
# COMPUTER LOGIC
# =========================

def bot_play():
    """Computer selects a random valid move."""
    global turn_num

    comp_input = random.choice(bot_available)
    turn_num += 1

    # Update game state
    bot_available.remove(comp_input)
    available.remove(comp_input)
    unavailable.append(comp_input)

    edit(int(comp_input), "comptr")
    print("Computer played:")
    show()
    checking()

    if not win_cond and turn_num != 9:
        unavl()


# =========================
# GAME FLOW
# =========================

def toss_play():
    """Decide who starts the game using a coin toss."""
    while True:
        try:
            toss = input("Choose 'h' for head or 't' for tail --> ").lower().strip()
            if toss not in ('h', 't'):
                raise ValueError
        except ValueError:
            print("Invalid value, try again.")
            continue
        break

    print("Block positions:")
    block_num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in block_num:
        print(row)

    if toss == random.choice(['h', 't']):
        print("You won the toss. You play first.")
        game_play()
    else:
        print("You lost the toss. Computer will play first.")


# =========================
# WIN CHECKING
# =========================

def checking():
    """Check rows, columns, diagonals for a win or draw."""
    global quit, turn_num, win_cond
    min_turns_win = 4
    if turn_num > min_turns_win:
        # Check rows and columns
        for i in range(3):
            if board_main[i][0] == board_main[i][1] == board_main[i][2] != '_':
                declare_winner(board_main[i][0], 'row', i)
                return

            if board_main[0][i] == board_main[1][i] == board_main[2][i] != '_':
                declare_winner(board_main[0][i], 'col', i)
                return

        # Check diagonals
        if board_main[0][0] == board_main[1][1] == board_main[2][2] != '_':
            declare_winner(board_main[0][0], 'diag1')
            return

        if board_main[0][2] == board_main[1][1] == board_main[2][0] != '_':
            declare_winner(board_main[0][2], 'diag2')
            return

    if not win_cond and turn_num == 9:
        print("Match is a draw.")
        quit = True


def declare_winner(symbol, mode, index=None):
    """Print winner and mark winning line."""
    global quit, win_cond

    if symbol == 'O':
        print("Congratulations! You won!")
    else:
        print("Computer won. Better luck next time.")

    # Visual highlight
    if mode == 'row':
        board_main[index] = ['—', '—', '—']
    elif mode == 'col':
        for r in range(3):
            board_main[r][index] = '|'
    elif mode == 'diag1':
        for i in range(3):
            board_main[i][i] = '\\'
    elif mode == 'diag2':
        board_main[0][2] = board_main[1][1] = board_main[2][0] = '/'

    show()
    win_cond = True
    quit = True


# =========================
# BOARD UPDATE
# =========================

def edit(game_input, identity):
    """Convert block number into board position."""
    row = (game_input - 1) // 3
    column = (game_input - 1) % 3

    board_main[row][column] = 'O' if identity == 'playr' else 'X'


#====================
# RESTART game
#====================

def play_again():
    """Decides if user wants to play again."""
    while True:
        try:
            play = input("Choose 'y' for yes or 'n' for no, to play again --> ").lower().strip()
            if play not in ('y', 'n'):
                raise ValueError
        except ValueError:
            print("Invalid value, try again.")
            continue
        break
    if play == 'y':
        return True
    else:
        return False


def restart():
    """restarts the game."""
    global quit , turn_num , win_cond , board_main , available , unavailable , bot_available
    board_main = [row[:] for row in board_cpy]
    turn_num = 0
    quit = False
    win_cond = False
    available = available_cpy.copy() 
    unavailable = []
    bot_available = bot_available_cpy.copy()
    
    
# =========================
# INITIAL STATE (SAFE COPIES)
# =========================

board_cpy = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

#deep copy (not shallow)
board_main = [row[:] for row in board_cpy]

turn_num = 0
quit = False
win_cond = False

available_cpy = ['1','2','3','4','5','6','7','8','9','q']
available = available_cpy.copy()        # safe copy

unavailable = []

bot_available_cpy = ['1','2','3','4','5','6','7','8','9']
bot_available = bot_available_cpy.copy() # safe copy


# =========================
# GAME START             
# =========================
while True:
    toss_play()

    while not quit:
        bot_play()
        if quit:
            break
        game_play()
    if not play_again():
        print("you're out of the game...")
        break
    else:
        print("you're playing again...")
        restart()
