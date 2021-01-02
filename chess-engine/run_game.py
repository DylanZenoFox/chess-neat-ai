import chess
import chess.svg
import random
import itertools
from encode_board import encode_board

def play_game(agent1, agent2):
    board = chess.Board()

    board.turn = chess.WHITE

    while (not board.is_game_over()):
        
        makeMove(agent1 if board.turn is chess.WHITE else agent2, board)
        
        if(board.is_game_over()):
            if(board.is_checkmate()):
                print("Checkmate")
            elif(board.is_stalemate()):
                print("Stalemate")
            elif(board.is_insufficient_material()):
                print("Insufficient Material")
            elif(board.is_seventyfive_moves()):
                print("Draw by Seventy-Five Moves")
            elif(board.is_fivefold_repetition()):
                print("Draw by Fivefold Repetition")
        else:
            pass


# Make move
def makeMove(agent, board):

    firstMove = random.choice(list(board.legal_moves))
    board.push(firstMove)
    x = chess.svg.board(board, lastmove=firstMove)
    #print(board.fen())
    #print(encode_board(board))
    #print(board.fullmove_number)
    #print(firstMove)
    print(board)
    print("-----------------")

if __name__ == '__main__':
    play_game("foo", "bar")


