# Implementation of classic arcade game Pong

import simplegui
import random

#GLOBAL VARIABLES
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel=[0,0]
ball_pos=[300,200]
paddle1_pos=100
paddle2_pos=100
paddle1_vel=0
score1=0
score2=0
paddle2_vel=0

def spawn_ball(canvas):
    global ball_pos, ball_vel # these are vectors stored as lists
    canvas.draw_circle(ball_pos,20,10,"Green")



def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    spawn_ball(canvas)
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if(ball_pos[1]+20>HEIGHT):
        ball_vel[1]=-ball_vel[1]
    if(ball_pos[1]-20<0):
        ball_vel[1]=-ball_vel[1]
    # DRAWINGS
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line((0,paddle1_pos+HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT),PAD_HEIGHT,"RED")
    canvas.draw_line((WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT),(WIDTH,paddle2_pos+HALF_PAD_HEIGHT),PAD_HEIGHT,"RED")
    canvas.draw_text("P1: "+str(score1),[20,20],30,"Blue")
    canvas.draw_text("P2: "+str(score2),[520,20],30,"Blue")
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    # ENDS OF PADDLES
    if(paddle1_pos<0):
        paddle1_pos=0
    if(paddle1_pos+PAD_HEIGHT>HEIGHT):
        paddle1_pos=HEIGHT-PAD_HEIGHT
    if(paddle2_pos<0):
        paddle2_pos=0
    if(paddle2_pos+PAD_HEIGHT>HEIGHT):
        paddle2_pos=HEIGHT-PAD_HEIGHT

    #PADDLE BOUNCING, SCORE UPDATE, GUTTER AND RESET
    if(ball_pos[0]-BALL_RADIUS<PAD_WIDTH):
        if(ball_pos[1]>paddle1_pos and ball_pos[1]<paddle1_pos+PAD_HEIGHT):

            ball_vel[0]=-ball_vel[0]
            if(ball_vel[0]>0):
                 ball_vel[0]+=1
            if(ball_vel[0]<0):
                 ball_vel[0]-=1
        else:
            score2+=1
            ball_pos=[350,200]
            ball_vel=[-2,-2]
    if(ball_pos[0]+BALL_RADIUS>WIDTH-PAD_WIDTH):
        if(ball_pos[1]>paddle2_pos and ball_pos[1]<paddle2_pos+PAD_HEIGHT):

                ball_vel[0]=-ball_vel[0]
                if(ball_vel[0]>0):
                    ball_vel[0]+=1
                if(ball_vel[0]<0):
                    ball_vel[0]-=1
        else:
                score1+=1
                ball_pos=[200,300]
                ball_vel=[2,-2]

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -3
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 3
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 3
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -3

def start():
    global ball_vel,ball_pos,score1,score2
    ball_pos=[300,250]
    ball_vel=[2,-2]
    score1=0
    score2=0

#FRAME
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.add_label("This is the classic 2-person arcade game Pong. The rules are pretty simple. P1 uses 'W' and 'S' key to move up and down while P2 uses 'Up' and 'Down' keys to move up and down.Stop the ball to reach screen ends by paddles. Game away to ultimate Pong glory!!",200)
frame.add_button("Start",start,200)
frame.start()

#full implementation at:http://www.codeskulptor.org/#user44_8aii4y1zuS_25.py
