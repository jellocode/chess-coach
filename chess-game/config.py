# constants

# chess piece scoring
BOARD_SCORES = {
    'PAWN' : 1,
    'BISHOP' : 3,
    'KNIGHT' : 3,
    'ROOK' : 5,
    'QUEEN' : 9,
    'KING' : 0
}

# max board score for player == 39 < win
END_SCORES = {
    'WIN' : 100,
    'LOSE' : -100,
    'TIE' : 0,
}

# giving value to pieces
PIECES = {
    1 : 'PAWN',
    2 : 'KNIGHT',
    3 : 'BISHOP',
    4 : 'ROOK',
    5 : 'QUEEN',
    6 : 'KING'
}