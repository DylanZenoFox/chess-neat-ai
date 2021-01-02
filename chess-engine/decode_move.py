import chess

def generate_all_moves():
    # Generate moves in pure coordinate notation by using the cartesian product of all squares
    moves = [source + target for source, target in itertools.product(chess.SQUARE_NAMES, chess.SQUARE_NAMES) if source is not target]
    # Generate all moves that result in pawn promotions, which can occur through both forward moves and diagonal captures
    promotionMoves = [source + target + promotion for source, target, promotion in itertools.product(chess.SQUARE_NAMES, chess.SQUARE_NAMES, ['q','r','b','n']) \
        if ((source[1] is '2' and target[1] is '1') or (source[1] is '7' and target[1] is '8')) \
        and ((ord(target[0]) - ord(source[0])) in [-1,0,1])]

    moves += promotionMoves

    return moves
