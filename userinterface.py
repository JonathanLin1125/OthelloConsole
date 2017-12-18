'''
Created on May 17, 2017

@author: jonathanlin
'''
import othello

def get_user_info()->tuple:
    """
    Gets initial information from user to create board
    Returns a tuple of input information
    """
    try:
        rows = int(input()) - 1
        columns = int(input()) - 1
        turn = input().strip()
        mode = input().strip()
        
        start_board = []
        for y in range(rows + 1):
            piece = input()
            start_board.append(piece)
    
        return rows, columns, turn, mode, start_board
    except:
        pass
    
def get_move(othello_game:othello.Othello)->(int,int):
    """
    Function makes sure that each move is valid
    Once input is valid, function returns the row/col inputs
    """
    move = input()
    move_list = move.split()
    row_input = int(move_list[0]) - 1
    col_input = int(move_list[1]) - 1
    
    while(row_input > othello_game.row) or (col_input > othello_game.col):
        print("INVALID")
        move = input()
        move_list = move.split()
        row_input = int(move_list[0]) - 1
        col_input = int(move_list[1]) - 1
    return(row_input, col_input)
        
def play_game(othello_game:othello.Othello):
    """
    While the game is not over, play_game reprompts for move, and keeps playing the game
    """
    if(othello_game.check_end() == True):
        othello_game.change_turn()
        
    while(othello_game.check_end() == False):
        othello_game.count_disks()
        print("B: " + str(othello_game.bcount) + "  W: " + str(othello_game.wcount))
        othello_game.print_board()
        print("TURN: " + othello_game.turn)
        
        move = get_move(othello_game)
        row_input = move[0]
        col_input = move[1]
        othello_game.get_list_moves(row_input, col_input)
        
        while(othello_game.check_valid() == False):
            print("INVALID")
            move = get_move(othello_game)
            row_input = move[0]
            col_input = move[1]
            othello_game.get_list_moves(row_input, col_input)

        print("VALID")
        
        othello_game.turn_disks(row_input, col_input)
        othello_game.change_turn()
    
    othello_game.count_disks()
    print("B: " + str(othello_game.bcount) + "  W: " + str(othello_game.wcount))
    othello_game.print_board()
    othello_game.print_winner()

if __name__ == "__main__":
    print("FULL")
    try:
        rows, columns, turn, mode, start_board = get_user_info()
        othello_game = othello.Othello(rows, columns, turn, mode, start_board)
        play_game(othello_game)
    except:
        pass
        
