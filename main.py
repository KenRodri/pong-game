import pygame, random, sys

from pygame.constants import KEYDOWN, K_DOWN, K_UP
pygame.init()#initializing pygame
clock = pygame.time.Clock()#clock variable for making game stay at 60fps

win_width = 800#width of game window
win_height = 600#height of game window
win = pygame.display.set_mode((win_width,win_height))#initializing game window
pygame.display.set_caption('Pong')#changing window name
#creating game objects
ball = pygame.Rect(win_width/2-15,win_height/2-15,30,30)
computer = pygame.Rect(20,win_height/2-60,30,150)
player = pygame.Rect(win_width-50,win_height/2-60,30,150)
white = (255,255,255)
#drawing game objects on the screen
def rect_draw():
    
    pygame.draw.ellipse(win,white,ball)
    pygame.draw.rect(win,white,player)
    pygame.draw.rect(win,white,computer)
    pygame.draw.aaline(win,white,(win_width/2,0),(win_width/2,win_height))
    player_text = game_font.render(f"{player_score}",False,white)
    comp_text = game_font.render(f"{comp_score}",False,white)
    win.blit(player_text,(450,300))
    win.blit(comp_text,(350,300))
score_time = True
player_score = 0#player score variable
comp_score = 0#computer score variable
game_font = pygame.font.Font("freesansbold.ttf",32)#initializing game font
#game logic of the ball
def ball_movement():
        global ball_horizontal_speed,ball_vertical_speed,player_score,comp_score,score_time
        ball.x += ball_horizontal_speed
        ball.y += ball_vertical_speed
        if ball.top <= 0 or ball.bottom >= win_height:
            ball_vertical_speed *= -1
        if ball.left <=0 :
            player_score += 1
            score_time = pygame.time.get_ticks()
        if ball.right >= win_width:
            comp_score += 1
            score_time = pygame.time.get_ticks()
        if ball.colliderect(player):
            ball_horizontal_speed *= -1
            ball_vertical_speed *= -1
        if ball.colliderect(computer):
            ball_horizontal_speed *= -1
            ball_vertical_speed *= -1
#game logic of player
def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= win_height:
        player.bottom = win_height
    
    
#game logic of the computer ai
def computer_movement():
    if computer.top <= ball.y:
        computer.top += comp_speed
    if computer.bottom >= ball.y:
        computer.bottom -= comp_speed
    if computer.top <= 0:
        computer.top = 0
    if computer.bottom >= win_height:
        computer.bottom = win_height
#restarting of ball after every goal and timer
def ball_restart():
    global ball_horizontal_speed,ball_vertical_speed,score_time
    current_time = pygame.time.get_ticks()
    ball.center = (win_width/2,win_height/2)
    if current_time-score_time<700:
        num_three = game_font.render("3",False,white)
        win.blit(num_three,(win_width/2-10,win_height/2+20))
    if 700 < current_time-score_time<1400:
        num_two = game_font.render("2",False,white)
        win.blit(num_two,(win_width/2-10,win_height/2+20))
    if 1400 < current_time-score_time<2100:
        num_one = game_font.render("1",False,white)
        win.blit(num_one,(win_width/2-10,win_height/2+20))
    if current_time-score_time<2100:
        ball_horizontal_speed,ball_vertical_speed = 0,0
    else:
        ball_horizontal_speed = 7*random.choice((1,-1))
        ball_vertical_speed = 7*random.choice((1,-1))
        score_time = None

bg_color = (8,108,108)
ball_vertical_speed = 7#vertical speed of ball
ball_horizontal_speed = 7#horizontal speed of ball
comp_speed = 7#speed of computer ai
player_speed = 0#speed of player
#main loop
def main_loop():
    global player_speed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    player_speed += 7
                if event.key == K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == K_DOWN:
                    player_speed -= 7
                if event.key == K_UP:
                    player_speed += 7
        win.fill((bg_color))
        rect_draw()
        ball_movement()
        
        player_movement()
        computer_movement()
        if score_time:
            ball_restart()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main_loop()