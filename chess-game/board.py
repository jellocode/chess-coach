import chess
from chess import Board

from random import random
from typing import List

try:
    from config import BOARD_SCORES, END_SCORES
except ModuleNotFoundError:
    from .config import BOARD_SCORES, END_SCORES