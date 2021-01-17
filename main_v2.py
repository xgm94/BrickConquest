
import pygame
import random

import math

colors = [
    (10, 10, 10),
    (255, 0, 0), #red
    (100, 100, 100),#white
]

class Figure:
    x = 0
    y = 0
    figures = [
            [[12]], #taver 0
            [[7,12],[13,12],[17,12],[11,12]],   #stable   1   
            [[7,12,13],[13,12,17],[17,12,11],[11,12,7]],   #inn     2
            [[7,12,17],[13,12,11]],   #bridge   3
            [[6,7,11,12]],   #square    4
            [[7,12,13,18],[13,12,17,16],[17,12,11,6],[11,12,7,8]],   #abey  5      
            [[7,11,12,13],[7,12,17,13],[11,12,13,17],[7,12,17,11]],   #manon    6
            [[8,12,16,13,17],[6,12,18,11,17],[8,12,16,7,11],[6,12,18,7,13]],   #tower 7        
            [[7,12,17,11,13]],   #infirmary 8
            [[6,11,12,13,8],[8,7,12,17,18],[11,12,13,16,18],[7,12,17,6,16]],  #castle 9
            [[7,12,17,11,18],[11,12,13,7,16],[7,12,17,6,13],[11,12,13,17,8]],  #academy 10
            [[7,12,17,22,11,13],[10,11,12,13,7,17],[3,7,12,17,11,13],[11,12,13,14,7,17]],  #cathedral 11
        ]
        
    def __init__(self, x, y,fig_type,color):
        self.x = x
        self.y = y
        self.type = fig_type
        self.color =color
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

class Player:
    team = 0
    color = None
    figures = [
        {"used": False, "type": 0, "id":0,"name":"tavern"},
        {"used": False, "type": 0, "id":1,"name":"tavern"},
        {"used": False, "type": 1, "id":2,"name":"stable"},
        {"used": False, "type": 1, "id":3,"name":"stable"},
        {"used": False, "type": 2, "id":4,"name":"inn"},
        {"used": False, "type": 2, "id":5,"name":"inn"},
        {"used": False, "type": 3, "id":6,"name":"bridge"},
        {"used": False, "type": 4, "id":7,"name":"square"},
        {"used": False, "type": 5, "id":8,"name":"abey"},
        {"used": False, "type": 6, "id":9,"name":"manon"},
        {"used": False, "type": 7, "id":10,"name":"tower"},
        {"used": False, "type": 8, "id":11,"name":"infirmary"},
        {"used": False, "type": 9, "id":12,"name":"castle"},
        {"used": False, "type": 10, "id":13,"name":"academy"},
    ]
    def __init__(self, team,color):
        self.team = team
        self.color = color
        for figure in self.figures:
            figure["used"] = False
            figure["figure"] = Figure(3,0,figure["type"],color)

    def place(self,fig_id):
        for figure in self.figures:
            if not figure["used"] and figure["used"]== fig_id:
                figure["used"] = True

    def getFigure(self):
        figure = None
        while figure == None:
            fig_id = random.randint(0,13)
            if not self.figures[fig_id]["used"]:
                return self.figures[fig_id]["figure"]
                
class Tetris:
    
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None
    players = []
    tourn = 0
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        self.init_players()
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def init_players(self):
        self.players.append(Player(0, 0))
        self.players.append(Player(1, 1))
            

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(5):
            for j in range(5):
                if i * 5 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def intersects_walls(self):
        intersection = False
        for i in range(5):
            for j in range(5):
                if i * 5 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            i + self.figure.y < 0 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 :
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        

    def place(self):
        if not self.intersects():
            self.freeze()
            self.next_tourn()

    def go_vertical(self,dy):
        old_y = self.figure.y
        self.figure.y += dy
        if self.intersects_walls():
            self.figure.y = old_y

    def freeze(self):
        for i in range(5):
            for j in range(5):
                if i * 5 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects_walls():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()

    def next_tourn(self):
        self.tourn += 1
        game.figure = None

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Cathedral beta")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(10, 10)
game.tourn = 0
#initialize cathedral
while not done:
    #who should move:
    if game.figure is None:
        if game.tourn % 2 == 0:
            #white
            game.figure = game.players[0].getFigure() 
        else:
            #red
            game.figure = game.players[1].getFigure()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.go_vertical(-1)
            if event.key == pygame.K_DOWN:
                game.go_vertical(1)
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.place()
            if event.key == pygame.K_r:
                game.rotate()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(5):
            for j in range(5):
                p = i * 5 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.players[game.tourn%2].color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
