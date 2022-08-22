def areMovesLeft(b):
    for r in range(3):
        for c in range(3):
            if b[r][c] == '':
                return True
    return False

def eval(b, players):
    #if==ai
    #elif==player
    for r in range(3):
        if b[r][0] == b[r][1] and b[r][1] == b[r][2]:
            if b[r][0] == players[0]:
                return -10
            elif b[r][0] == players[1]:
                return 10
    for c in range(3):
        if b[0][c] == b[1][c] and b[1][c] == b[2][c]:
            if b[0][c] == players[0]:
                return -10
            elif b[0][c] == players[1]:
                return 10
    
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == players[0]:
            return -10
        elif b[0][0] == players[1]:
            return 10
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == players[0]:
            return -10
        elif b[0][2] == players[1]:
            return 10
    return 0

def minimax(b, players, depth, ismax):
    score = eval(b, players)
    if score == 10 or score == -10:
        return score
    if areMovesLeft(b) is False or depth == 0:
        return 0

    if ismax:
        score = -1000
        for r in range(3):
            for c in range(3):
                if b[r][c] == '':
                    b[r][c] = players[1] #player
                    score = max(score, minimax(b, players, depth - 1, False))
                    b[r][c] = ''
        return score
    else:
        score = 1000
        for r in range(3):
            for c in range(3):
                if b[r][c] == '':
                    b[r][c] = players[0] #ai
                    score = min(score, minimax(b, players, depth - 1, True))
                    b[r][c] = ''
        return score

def getBestMove(board, players,ismax):
    b_score = 1000
    b_move = [-1,-1]

    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                
                board[r][c] = players[0] #player_chr
                score = minimax(board, players, 9, ismax)
                board[r][c] = ''

                if score < b_score:
                    b_score = score
                    b_move = [r,c]
    return b_move
