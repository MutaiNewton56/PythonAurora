

def rookPosibleMoves(rook,knight):
    moves=[]
    top(rook,moves)
    bottom(rook,moves)
    left(rook,moves)
    right(rook,moves)

    for move in moves:
        if move['x']==knight['x'] and move['y']==knight['y']:
            print("Posible capture")

    return moves

def top(rook,moves):
    y=rook['y']
    for i in range(1,8):
        c_y=y+i
        if c_y>=0 and c_y<=7:
            moves.append({"x":rook["x"],"y":c_y})
    return moves

def bottom(rook,moves):
    y=rook['y']
    for i in range(1,8):
        c_y=y-i
        if c_y>=0 and c_y<=7:
            moves.append({"x":rook["x"],"y":c_y})
    return moves

def right(rook,moves):
    x=rook['x']
    for i in range(1,8):
        c_x=x+i
        if c_x>=0 and c_x<=7:
            moves.append({"x":c_x,"y":rook['y']})

def left(rook,moves):
    x=rook['x']
    for i in range(1,8):
        c_x=x-i
        if c_x>=0 and c_x<=7:
            moves.append({"x":c_x,"y":rook['y']})