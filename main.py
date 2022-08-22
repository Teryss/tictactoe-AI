import pygame as p
from tictactoe import Game
import minimax as m
import time

WIDTH, HEIGHT = 300, 300
FPS = 30

def checkForWin(game):
    if m.areMovesLeft(game.board) is False:
        print("Draw!")
        return False
    score = m.eval(game.board, game.getChrs())
    if score != 0:
        print("You won!" if score == 10 else "You lost!")
        return False
    return True

def moveAI(game):
    move = m.getBestMove(
        game.board, game.getChrs(), True
    )
    game.aiMove(move)

def run_ai(who_starts):
    window = p.display.set_mode(size = (WIDTH, HEIGHT))
    clock = p.time.Clock()
    t = Game(window, HEIGHT, WIDTH)
    t.setChrs(who_starts)

    run = True
    moved = False if who_starts == 'player' else True
    while run:
        if moved:
            moveAI(t)
            moved = False
            run = checkForWin(t)

        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if t.playerMove(p.mouse.get_pos()):
                    moved = True
                    run = checkForWin(t)
        t.draw()
        p.display.update()
        clock.tick(FPS)
    
    time.sleep(2)

if __name__ == "__main__":
    run_ai('player')