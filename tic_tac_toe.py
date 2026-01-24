# Simple tic-tac-toe game (terminal-based)
# Author: Ifthekar Rahat
# Logic style: function-based

'''features:
1.can play as long as you want
2.level based[easy and hard]
3.smart opponent [simple ai]..
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
    print('These blocks are available:', available)


# =========================
# PLAYER LOGIC
# =========================

def game_play():
    """Handle player input and move."""
    global quit, turn_num, ai_play_case1, ai_play_case2, toss

    while True:
        try:
            playr_input = input("Play your block (1-9) or 'q' to quit --> ").strip()
            if playr_input not in available :
                if playr_input != 'q':
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
        
        if level == 'h':
            if toss == 'won':
                if playr_input in ai_play_case2:
                    ai_play_case2.remove(playr_input)
            else:
                if playr_input in ai_play_case1:
                    ai_play_case1.remove(playr_input)
            
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
    comp_input = random.choice(available)
    bot_ai_call(comp_input)


def ai_play():
    global toss , comp_play_1 ,ai_play_case1 , ai_play_case2, comp_input
    if smart_play(AI) or smart_play(PLAYER):
        pass
    else:
        if toss == 'won':
            if comp_play_1 == True and '5' in available: #just a gaming way,nothing code related
                bot_ai_call('5')
                comp_play_1 = False
                return None
            else:
                if ai_play_case2:
                    comp_input = random.choice(ai_play_case2)   
                    ai_play_case2.remove(comp_input)
                else:
                    comp_input = random.choice(available)
        else :
            if ai_play_case1:
                    comp_input = random.choice(ai_play_case1)   
                    ai_play_case1.remove(comp_input)
            else:
                comp_input = random.choice(available)
        bot_ai_call(comp_input)           
        
        
def smart_play(sign):
    global turn_num
    '''before third play two block being same cant be possible'''
    if turn_num <= 2:
        return False

    for i in range(3):
        if board_main[i][0] == board_main[i][1] == sign and board_main[i][2] == EMPTY:
            bot_ai_call(str(i*3 + 2 + 1))
            return True
        elif board_main[i][0] == board_main[i][2] == sign and board_main[i][1] == EMPTY:
            bot_ai_call(str(i*3 + 1 + 1))
            return True
        elif board_main[i][1] == board_main[i][2] == sign and board_main[i][0] == EMPTY:
            bot_ai_call(str(i*3 + 0 + 1))
            return True
        elif board_main[0][i] == board_main[1][i] == sign and board_main[2][i] == EMPTY:
            bot_ai_call(str(2*3 + i + 1))
            return True
        elif board_main[0][i] == board_main[2][i] == sign and board_main[1][i] == EMPTY:
            bot_ai_call(str(1*3 + i + 1))
            return True
        elif board_main[1][i] == board_main[2][i] == sign and board_main[0][i] == EMPTY:
            bot_ai_call(str(0*3 + i + 1))
            return True

    if board_main[0][0] == board_main[1][1] == sign and board_main[2][2] == EMPTY:
        bot_ai_call(str(2*3 + 2 + 1))
        return True
    elif board_main[0][0] == board_main[2][2] == sign and board_main[1][1] == EMPTY:
        bot_ai_call(str(1*3 + 1 + 1))
        return True
    elif board_main[1][1] == board_main[2][2] == sign and board_main[0][0] == EMPTY:
        bot_ai_call(str(0*3 + 0 + 1))
        return True

    if board_main[0][2] == board_main[1][1] == sign and board_main[2][0] == EMPTY:
        bot_ai_call(str(2*3 + 0 + 1))
        return True
    elif board_main[0][2] == board_main[2][0] == sign and board_main[1][1] == EMPTY:
        bot_ai_call(str(1*3 + 1 + 1))
        return True
    elif board_main[1][1] == board_main[2][0] == sign and board_main[0][2] == EMPTY:
        bot_ai_call(str(0*3 + 2 + 1))
        return True

    return False


def bot_ai_call(comp_input):
    global turn_num, available, unavailable
    turn_num += 1

    # Update game state
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
    
    global toss, quit
    while True:
        try:
            toss_local = input("Choose 'h' for head or 't' for tail and 'q' to quit --> ").lower().strip()
            if toss_local not in ('h', 't', 'q'):
                raise ValueError
        except ValueError:
            print("Invalid value, try again.")
            continue
        break
    if toss_local == 'q':
        quit = True
        print("Match quit by player.")
        return None
    
    print("Block positions:")
    block_num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in block_num:
        print(row)

    if toss_local == random.choice(['h', 't']):
        print("You won the toss. You play first.")
        toss = 'won'
        game_play()
    else:
        print("You lost the toss. Computer will play first.")
        toss = 'lost'


def level_choose():
    while True:
        try:
            level = input("Choose 'h' for hard mode or 'e' for easy mode --> ").lower().strip()
            if level not in ('h', 'e'):
                raise ValueError
        except ValueError:
            print("Invalid value, try again.")
            continue
        break
    return level




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
            if board_main[i][0] == board_main[i][1] == board_main[i][2] != EMPTY:
                declare_winner(board_main[i][0], 'row', i)
                return

            if board_main[0][i] == board_main[1][i] == board_main[2][i] != EMPTY:
                declare_winner(board_main[0][i], 'col', i)
                return

        # Check diagonals
        if board_main[0][0] == board_main[1][1] == board_main[2][2] != EMPTY:
            declare_winner(board_main[0][0], 'diag1')
            return

        if board_main[0][2] == board_main[1][1] == board_main[2][0] != EMPTY:
            declare_winner(board_main[0][2], 'diag2')
            return

    if not win_cond and turn_num == 9:
        print("Match is a draw.")
        quit = True


def declare_winner(symbol, mode, index=None):
    """Print winner and mark winning line."""
    global quit, win_cond

    if symbol == PLAYER:
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

    board_main[row][column] = PLAYER if identity == 'playr' else AI


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
    global quit , turn_num, win_cond, board_main, available, unavailable
    global toss, comp_input, ai_play_case1, ai_play_case2
    board_main = [row[:] for row in board_cpy]
    turn_num = 0
    quit = False
    win_cond = False
    toss = None
    comp_input = None
    available = available_cpy.copy() 
    unavailable = []
    ai_play_case1 = ai_play_case1_cpy.copy()
    ai_play_case2 = ai_play_case2_cpy.copy()
  
  
# =========================
# CONSTANTS
# =========================

EMPTY = '_'
PLAYER = 'O'
AI = 'X'
  
    
    
# =========================
# INITIAL STATE (SAFE COPIES)
# =========================

board_cpy = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]


#deep copy (not shallow)
board_main = [row[:] for row in board_cpy]

turn_num = 0
quit = False
win_cond = False
comp_play_1 = True
toss = None
comp_input = None

available_cpy = ['1','2','3','4','5','6','7','8','9']
available = available_cpy.copy()        # safe copy
unavailable = []

ai_play_case1_cpy = ['1','3','7','9']
ai_play_case1 = ai_play_case1_cpy.copy()

ai_play_case2_cpy = ['2','4','6','8'] 
ai_play_case2 = ai_play_case2_cpy.copy()

# =========================
# GAME START             
# =========================
while True:
    level = level_choose()
    toss_play()

    while not quit:
        if level == 'e':
            print("you're currently on easy mode,",end=" ")
            bot_play()
        else:
            print("you're currently on hard mode,",end=" ")
            ai_play()
            
        if quit:
            break
        game_play()
    if not play_again():
        print("you're out of the game...")
        break
    else:
        print("you're playing again...")
        restart()
