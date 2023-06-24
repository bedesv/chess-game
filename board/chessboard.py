import re
from chesspieces import Pawn, Rook, Knight, Bishop, Queen, King

def check_fen_validity(fen_string):
    """
        Checks the board for validity

        1. Only one king per colour
        2. No pawns in the first or last rows
        3. 
    """
    regexMatch=re.match('\s*^(((?:[rnbqkpRNBQKP1-8]+\/){7})[rnbqkpRNBQKP1-8]+)\s([b|w])\s([K|Q|k|q]{1,4})\s(-|[a-h][1-8])\s(\d+\s\d+)$', fen)
    if regexMatch:
        regexList = regexMatch.groups()
        fen = regexList[0].split("/")
        if len(fen) != 8:
            raise ValueError("expected 8 rows in position part of fen: {0}".format(repr(fen)))

        for fenPart in fen:
            field_sum = 0
            previous_was_digit, previous_was_piece = False,False

            for c in fenPart:
                if c in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    if previous_was_digit:
                        raise ValueError("two subsequent digits in position part of fen: {0}".format(repr(fen)))
                    field_sum += int(c)
                    previous_was_digit = True
                    previous_was_piece = False
                elif c.lower() in ["p", "n", "b", "r", "q", "k"]:
                    field_sum += 1
                    previous_was_digit = False
                    previous_was_piece = True
                else:
                    raise ValueError("invalid character in position part of fen: {0}".format(repr(fen)))

            if field_sum != 8:
                raise ValueError("expected 8 columns per row in position part of fen: {0}".format(repr(fen)))  

    else: raise ValueError("fen doesn`t match follow this example: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 ") 

def generate_starting_board(state):


class ChessBoard:

    def __init__(self, initial_state_fen_string=None):
        self.state = generate_starting_board(initial_state_fen_string)
