"""
NextLib

A simple yet usable library for coding games in Python that runs on top of pygame.
"""

import pygame as pg
import pygame._sdl2.controller
import time
import sys as system
import math
import os

global working_path
working_path = os.path.dirname(os.path.abspath(__file__))+"/"
global sprites
sprites = list()
global bg_init
bg_init = 0
global sprite_init
sprite_init = 0
global backdrops
backdrops = list()
global bi
bi = 0
global dbi
dbi = 0
global bg
bg = 0
global si
si = 0
global sprite
sprite = 0
global surface
surface = 0
global bg_data
bg_data = 0
global sprite_data
sprite_data = 0
global sprites_len
sprites_len = 0
global bg_len
bg_len = 0
global last_used_sprite
last_used_sprite = 0

def get_next_surface():
    global surface
    return surface

def get_next_screen():
    global screen
    global screen_width
    global screen_height
    output = [screen,screen_width,screen_height]
    return output

def DrawText(text,color,size,pos):
    global surface
    if surface != 0:
        font = pg.font.Font(None, size)
        output = font.render(text, 1, color)
        if pos == "auto":
            outpus = output.get_rect()
        else:
            outpus = (pos[0],pos[1],size,size)
        surface.blit(output,outpus)

def Distance(xa,ya,xb,yb):
    a = xa - xb
    b = ya - yb
    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
    return c

def Key(key_to_check):
    pg.key.set_repeat(1,1)
    key = pg.key.key_code(key_to_check)
    output = pg.key.get_pressed()
    if output[key] == True:
        return True
    else:
        return False

# Internal
def load_image(path):
    file = path
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise ValueError("Failed to load image! Make sure you've correctly entered the path, and that the file exists.")
    return surface.convert()

def RenderSprite(sprite_name,x,y):
    global screen
    global surface
    global last_used_sprite
    global working_path
    sprite = working_path+"sprites/"+sprite_name+".png"
    if last_used_sprite != sprite_name:
        sprite_init = 0
    if sprite != 0 and surface != 0:
        if sprite_init == 0:
            sprite_data = load_image(sprite)
            sprite_init = 1
        if sprite_init == 1:
            surface.blit(sprite_data,(x,y))
            pg.display.flip()
            last_used_sprite = sprite_name

def DrawSprite(sprite_name,x,y):
    global sprites
    global si
    global screen
    global screen_height
    global screen_width
    global surface
    global sprite
    global sprite_init
    global sprite_data
    global last_used_sprite
    global working_path
    if last_used_sprite != sprite_name:
        sprite_init = 0
    sprite_x = 0
    sprite_y = 0
    sprite = working_path+"sprites/"+sprite_name+".png"
    sprite_init = 0
    if sprite != 0 and surface != 0:
        if sprite_init == 0:
            sprite_data = load_image(sprite)
            center_x = (screen_width/2)-(sprite_data.get_width())/2
            center_y = (screen_height/2)-(sprite_data.get_height())/2
            sprite_x = center_x+x
            sprite_y = center_y+y
            sprite_init = 1
        if sprite_init == 1 and sprite_x != 0 and sprite_y != 0:
            surface.blit(sprite_data,(sprite_x,sprite_y))
            pg.display.flip()
            last_used_sprite = sprite_name

def Draw():
    global screen
    global surface
    if surface != 0:
        screen.blit(surface,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            next_quit()

# Initialize
def next_init(data_in,data_out):
    global surface_size
    global screen
    global screen_height
    screen_height = data_out
    global screen_width
    screen_width = data_in
    SCREENRECT = pg.Rect(0,0,data_in,data_out)
    surface_size = SCREENRECT.size
    pg.init()
    fullscreen = False
    winstyle = 0
    bestdepth = pg.display.mode_ok(surface_size, winstyle, 32)
    screen = pg.display.set_mode(surface_size, winstyle, bestdepth)

def FullScreenToggle():
    pg.display.toggle_fullscreen()

def SetWindowIcon(img):
    global working_path
    icon = working_path+"sprites/"+img+".png"
    if icon != 0:
        data = load_image(icon)
        pg.display.set_icon(data)

def SetWindowTitle(title):
    pg.display.set_caption(title)

def next_quit():
    pg.quit()
    system.exit()

def SetTransparency(value):
    global surface
    if value <= 255 and value >= 0:
        if surface != 0:
            pg.Surface.set_alpha(surface,value)
    else:
        raise ValueError("The inputted number must be between 0 and 255!")

def RenderBlank():
    global screen
    global screen_height
    global screen_width
    global surface
    surface = pg.Surface(surface_size)
    pg.display.flip()

# Draw a Backdrop
def DrawBackdrop(bg_name):
    global backdrops
    global dbi
    global bg
    global screen
    global screen_height
    global screen_width
    global surface
    global bg_init
    global bg_data
    global bg_len
    global working_path
    center_x = (screen_width/2)-(screen_width/2)
    center_y = (screen_height/2)-(screen_height/2)
    bg = working_path+"sprites/"+bg_name+".png"
    if bg != 0:
        bg_data = load_image(bg)
        surface = pg.Surface(surface_size)
        surface.blit(bg_data,(center_x,center_y))
        pg.display.flip()

def PlayMusic(music_file):
    global working_path
    pg.mixer.music.load(working_path+"music/"+music_file+".ogg")
    pg.mixer.music.play(-1,0.0,0)

def StopMusic():
    pg.mixer.music.stop()
    pg.mixer.music.unload()

def PlaySound(sound_file):
    global working_path
    pg.mixer.Sound(working_path+"music/"+sound_file+".ogg").play()

def PadCount():
    return pg._sdl2.controller.get_count()

def Pad(int):
    pad_init = pg._sdl2.controller.get_init()
    if pad_init != True:
        pg._sdl2.controller.init()
    npad = pg._sdl2.controller.Controller(int)
    return npad

# Pause execution for <sec> seconds
def Wait(sec):
    time.sleep(sec)

def MouseClick():
    return pg.mouse.get_pressed()[0]

def MousePosition():
    global screen_height
    global screen_width
    position = pg.mouse.get_pos()
    center_x = (screen_width)/2
    center_y = (screen_height)/2
    outpos = [0-(center_x-position[0]),0-(center_y-position[1])]
    return outpos
