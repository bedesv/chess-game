import chess
import chess.svg

def save_image(board):
    image = chess.svg.board(
        board,
        size=350,
    ) 

    with open("output.svg", "w+") as output:
        output.write(image)

def get_all_moves(board, colour):
    moves = []
    # possible_squares = [square for square in chess.SQUARES if square.con]
        

def main():
    board = chess.Board()
    print(board.)
    if board.turn == chess.WHITE:
        # Maximise White
        pass

    else:
        # Maximise Black
        pass


    
 

if __name__ == "__main__":
    main()