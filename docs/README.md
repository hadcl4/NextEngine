# Documentation

If you want to see how NextEngine works before trying it out, or if you need to know how to do a specific thing, you can read these docs. In the engine itself, you can also access this documentation at any time from the "Documentation" button in the menu.

## The Basics
Every game you write in NextEngine will begin this way:
```
from nextlib import *
```
If you're okay with putting `nextlib.` before every nextlib function you call, you can just put
```
import nextlib
```
However, during this tutorial, we'll use the first method (the first method is also the default).
### Getting Everything Ready
Before we get into putting stuff on the screen, you'll need to get everything set up first. You can write down the "init" part of your script after you've imported `nextlib`.
```
global x
x = 0
global xx
xx = 0
global position_x
position_x = 0
global position_y
position_y = 0

init = 0

if init == 0:
    next_init(1280,720)
    SetWindowIcon("player_idle")
    SetWindowTitle("NextEngine Example")
    dir = "idle"
    init = 1
```
This is the "init" section of the included example. First, global variables will be set, then, under `if init == 0:`, there's some more important stuff, and this will be needed for pretty much any NextEngine game. 

First is `next_init()`. This will handle initializing everything, and you'll be able to set the game's resolution from here. The first argument is the window's width, and the second is the window's height. The recommended resolution in NextEngine is `1280x720`, as the coordinate plane is suited well for this resolution.

After this is `SetWindowIcon()`. This will change the icon that shows up on the dash, taskbar, or whatever your OS calls it, and technically isn't required, but is recommended. It only needs one argument. The argument is the name of a sprite located in your project's "sprites" folder (it MUST be `.png`!).

Finally is `SetWindowTitle()`. Like `SetWindowIcon()`, this is optional, but recommended. It also only needs one argument. This argument will be the text you want your window's title to be.

The two things after this just have to do with the example, so I won't go over them.
### The Game Loop
```
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
```
Now we're to the exciting part! This is where tha majority of the game's code will be. You begin the loop with `while True:`, making it run continuously, since `True` is always `True`. Since this part is so long, I'll divide it up.
#### Keyboard
All games need to track input in some way, and in this case, it's using keyboard for input. You'll most likely be using keyboard input for your game, so I'll go over it here.

It's quite easy to figure out how to check keyboard input. `if Key(<key>) == True:` will check if a key is currently pressed. If it is pressed, it will return `True`. And if it's not pressed, it'll return `False`. It takes one argument: the name of the key you want to check. For a list of key names, refer to pygame's list [here](https://www.pygame.org/docs/ref/key.html). Just scroll down a little ways until you find the list. In `nextlib`, always use the key names listed under "Description". Under the `if` statement, you can put the code you want executed when the key is pressed.
#### Backdrop
In `nextlib`, you'll always* need a backdrop to be displayed. Try to use a sprite that fits well with the size of the screen. Keep in mind, if you need to change `x` or `y`, you can just display a large sprite on top of the backdrop, so you don't see it at all.

You can draw a backdrop by running `DrawBackdrop()`. It only needs one argument. This argument is the name of a sprite stored in your project's "sprites" folder (it MUST be `.png`!).

###### *See "Advanced Drawing Functions" for information on an alternative method that doesn't require a sprite.

#### Sprite(s)
After drawing a backdrop, you can display sprites on top of it. Sprites are more versatile, since you can change their `x` and `y`.

You can display a sprite by running `DrawSprite()`. It needs 3 arguments. The first is the name of a sprite stored in your project's "sprites" folder (it MUST be `.png`!), next is the `x` position, and finally is the `y` position. If you want your sprites to move, make sure to use variables in place of just numbers.
#### Text
It's often useful to display text on the screen, often to show the user a stat, such as how much HP they have, or their score.

You can display text by running `DrawText()`. It needs 4 arguments. First is the text you need to display. Second is the color of the text (enclosed in `()`), in RGB. Next is the text size. Finally is positioning. You can put `"auto"` if you want `nextlib` to automatically place it in the upper-left corner of the screen, or you can position it manually by passing a list (e.g. `[250,150]`, first is `x`, then `y`) containing the coordinates. Unlike sprites, text uses Pygame's normal coordinate system.
#### Tracking Distance
You're most likely going to need to track collision in your game. Unlike quite a few game engines, `nextlib` comes with a method to track collision built-in. Handy, right?

The function `Distance()` will return the distance between two sets of `x` and `y` coordinates. It needs 4 arguments. The first two are `x` and `y` values for one sprite, and the the last two are the `x` and `y` values for the sprite you're seeing if it's collided with. To be able to use this function, you'll most likely need to use it in an `if` statement, unless you set a variable to the data it returns (e.g. `data = Distance(a_x,a_y,b_x,b_y)`).
#### Looping
To wrap up the loop, there are two functions you need to be aware of:
```
Draw()
Wait()
```
`Draw()` is an absolute requirement at the end of your loop. It will draw everything onto the screen, and if it detects the window's red X button (or whatever your windowing system has for closing an app) is pressed, it will exit.

`Wait()` is technically optional, but to make things go smoothly, is required. It takes one argument. This will be how many seconds to wait until the loop will be repeated. In the example, it's 1/180th of a second.

#### Fullscreen
This isn't listed in the example at all, but I'll go over it anyway. You can set your game's window to fullscreen by running `FullScreenToggle()`. No arguments at all, just the function by itself.

#### Exiting
If your game is fullscreen, or you want another way to exit the game besides the red X button, you can use the function `next_quit()`. In the example, this is used when the user presses `ESCAPE`.

## The More Complicated Stuff

If you've read through "The Basics", you're now ready to move on to more complex stuff in NextEngine! These will all be covered in their own markdown files:

- [Playing Audio](AUDIO.md)
- [Controller Input](CONTROLLERS.md)
- [Advanced Drawing Functions](ADVANCED_DRAWING.md)
- [Getting Info about the Surface/Screen](NEXT_INFO.md)
- [Mouse Input](MOUSE.md)
