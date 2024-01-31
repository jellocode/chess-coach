import pandas as pd
from chess import Board
from itertools import count
from time import sleep, time # create delay and time since epoch
from random import choice

# for notebook
from tqdm.notebook import tqdm # progress bar of loop
from IPython.display import display, clear_output, HTML

try:
    from board import game_over, check_tie, check_win, eval_board_state
    from config import BOARD_SCORES
except ModuleNotFoundError:
    from .board import  game_over, check_tie, check_win, eval_board_state
    from .config import BOARD_SCORES
    
class Game:
    def __init__(self, board: Board=None):
    # for games with specific starting point (board)
        if board:
            self.board = Board
        else:
            self.board = Board()
        
def _game(self, white_p, black_p, visual = False, pause=1):
    board = self.board.copy()
    result = None
    start_time = time()
    
    try:
        for i in count():
            if visual:
                display(board)
                
                white_score = eval_board_state(board, True, BOARD_SCORES)
                black_score = eval_board_state(board, False, BOARD_SCORES)
                display(HTML(f'<div> WHITE: {white_p.solver} SCORE: {white_p.score}</div'))
                display(HTML(f'<div> BLACK: {black_p.solver} SCORE: {black_p.score}</div'))
                sleep(pause)
                
            if game_over(board, claim_draw=True):
                break
            
            if board.turn:
                move = white_p.move(board)
            else:
                move = black_p.move(board)
                
            board.push_uci(move)
            if visual:
                clear_output(wait=True)
                
    except KeyboardInterrupt:
        print('Game stopped')
        
    if check_tie(board, claim_draw= True):
        result = -1
    else:
        result = int(check_win(board, True))
        
    if visual:
        display(HTML(f'<div>RESULT:{result}</div>'))
        
    result_stat = {
        'white' : white_p.solver,
        'black' : black_p.solver,
        'FEN' : board.fen(),
        'last_move' : board.peek(),
        'moves_history' : [move.uci() for move in board.move_stack],
        'moves' : i, 'time': round(time() - )
    }