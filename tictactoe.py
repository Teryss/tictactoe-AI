import pygame as p

class Game():
    def __init__(self, screen, height, width):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.WHITE, self.RED = (255,255,255), (255,0,0)
        self.sqrSize = height//3
        self.turns = 0
        self.gamesPlayed = 0
        self.board = [['','',''],['','',''],['','','']]
        self.grid = (
            ((0, self.sqrSize), (self.HEIGHT, self.sqrSize)),
            ((0, 2 * self.sqrSize), (self.HEIGHT, 2 * self.sqrSize)),
            ((self.sqrSize,0), (self.sqrSize, self.WIDTH)),
            ((2 * self.sqrSize, 0), (2 * self.sqrSize, self.WIDTH))
        )
        self.margin = 10
    
    def setChrs(self, who_starts):
        if who_starts == 'player':
            self.player = 'x'
            self.ai = 'o'
        else:
            self.player = 'o'
            self.ai = 'x'
    
    def getChrs(self):
        return self.ai, self.player
    
    def aiMove(self, pos):
        self.board[pos[0]][pos[1]] = self.ai

    def playerMove(self, pos):
        x,y = pos[0] // self.sqrSize, pos[1] // self.sqrSize
        if self.board[x][y] == '':
            self.board[x][y] = self.player
            return True
        return False

    def draw(self):
        self.screen.fill(self.WHITE)
        for point in self.grid:
            p.draw.lines(self.screen, (0,0,0), False, point, width = 4)
        for r in range(3):
            for c in range(3):
                if self.board[r][c] != '':
                    if self.board[r][c][0] == 'x':
                        leftTopPos = (r * self.sqrSize, c * self.sqrSize)
                        p.draw.line(
                            self.screen, 
                            self.RED,   
                            (leftTopPos[0] + self.margin, leftTopPos[1] +self. margin),
                            (leftTopPos[0] + self.sqrSize - self.margin, leftTopPos[1] + self.sqrSize - self.margin),
                            width=5
                        )
                        p.draw.line(
                            self.screen, 
                            self.RED,
                            (leftTopPos[0] + self.sqrSize - self.margin, leftTopPos[1] + self.margin),
                            (leftTopPos[0] +self. margin, leftTopPos[1] + self.sqrSize - self.margin ),
                            width=5
                        )
                    else:
                        p.draw.circle(
                            self.screen, 
                            self.RED, 
                            (r * self.sqrSize + self.sqrSize * 0.5,  c * self.sqrSize + self.sqrSize * 0.5),
                            self.sqrSize * 0.5 - self.margin
                            )