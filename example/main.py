from nextlib import *

global x
x = 0
global xx
xx = 0
global position_x
position_x = 0
global position_y
position_y = 0
next_init(1280,720)
SetWindowIcon("player_idle")
SetWindowTitle("NextEngine Example")
dir = "idle"

while True:
    if Key("right") == True:
        position_x += 10
        dir = "right"
    elif Key("left") == True:
        position_x -= 10
        dir = "left"
    elif Key("up") == True:
        position_y -= 10
        dir = "up"
    elif Key("down") == True:
        position_y += 10
        dir = "down"
    elif Key("escape") == True:
        next_quit()
    else:
        dir = "idle"
    x += 10
    if x > 690:
        x = -690
    xx -= 10
    if xx < -690:
        xx = 690
    DrawBackdrop("player_0")
    DrawSprite("player_right",x,180)
    DrawSprite("player_left",xx,-180)
    DrawSprite("player_"+dir,position_x,position_y)
    DrawSprite("player_idle",180,0)
    DrawText("NextEngine Example",(255,255,255),50,"auto")
    if Distance(position_x,position_y,180,0) < 128:
        DrawSprite("collide",position_x+32,position_y-64)
    Draw()
    Wait(1/180)

