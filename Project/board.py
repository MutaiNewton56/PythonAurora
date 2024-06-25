
def printBoard(board):
    for row in board:
        for col in row:
            print(f"{col}",end=" ")
        print("")

def makeMove(board,fr,to):
    fr_x=fr['x']
    fr_y=fr['y']
    to_x=to['x']
    to_y=to['y']
    print(f"from {fr} to {to}")
    from_str=board[fr_y][fr_x]
    to_str=board[to_y][to_x]

    from_str_arr=from_str.split(",")

    print(f"from {from_str} to {to_str}")
    print(from_str_arr)
    board[fr_y][fr_x]=f"{from_str_arr[0]},  "
    board[to_y][to_x]=f"{to_str.strip()}{from_str_arr[1]}"

