import chess
from chess import Board

from random import random
from typing import List

# import from config
try:
    from config import BOARD_SCORES, END_SCORES
except ModuleNotFoundError:
    from .config import BOARD_SCORES, END_SCORES

# dictionary of squares corrosponding square names
NAME_TO_SQUARE = dict(zip(chess.SQUARE_NAMES, chess.SQUARES))

# get uci notation of move
def square_name(move):
    return move.uci()[:2]

# determine player side is white/black
def turn_side(board):
    side = 'white' if board.turn == True else 'black'
    return side

# checks if game ended and returns boolean
def game_over(board: Board, claim_draw: bool= False) -> bool:
    if board.is_game_over(claim_draw= claim_draw):
        return True
    return False
    
def check_win(board: Board, player_colour: bool) -> bool:
    if board.is_checkmate() and board.turn == (not player_colour):
        return True
    return False

# function to calculate if board is draw; stalemate, insuff pieces, repetition
def check_tie(board: Board, claim_draw: bool= False) -> bool:
    tie = (board.is_stalemate() or
           board.is_fivefold_repetition() or
           board.is_insufficient_material())
    
    if claim_draw:
        tie = tie or board.can_claim_draw()
        
    if tie:
        return True
    
    return False
            
# calculate game score
def game_score(board, player_colour, end_scores_policy = END_SCORES, board_scores_policy = BOARD_SCORES) -> float:
    score = None,
    
    if check_tie(board):
        score = end_scores_policy['TIE']
    elif check_win(board, player_colour):
        score = end_scores_policy['WIN']
    elif check_win(board, not player_colour):
        score = end_scores_policy['LOSE']
    else:
        score = eval_board_state(board, player_colour, board_scores_policy)
        
    return score
