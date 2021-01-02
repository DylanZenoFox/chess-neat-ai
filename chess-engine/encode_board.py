import chess
import numpy as np

def encode_board(board):
    input_vec = []
    for square in chess.SQUARES:
        square_vec = np.zeros(12)
        
        piece = board.piece_type_at(square)

        # If there is no piece on this square
        if(piece is None):
            input_vec.append(square_vec)
            continue
        
        # If piece is black
        if(not board.color_at(square)):
            piece += 6

        square_vec[piece-1] = 1.0
        input_vec.append(square_vec)
    
    return np.concatenate(input_vec)
            


