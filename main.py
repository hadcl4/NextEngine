from guizero import *
import os
import math
import time
import subprocess
import nextlib
import webbrowser

nextlib.pg.mixer.init()

home = os.getenv("HOME")

global mode
mode = 0
global folder
folder = 0
global tab
tab = "Code"
global code_width
code_width = 75
global code_height
code_height = 32
global working_path
working_path = os.path.dirname(os.path.abspath(__file__))+"/"

def edit(loc):
    global app
    global mode
    global codebox
    global editor
    global folder
    code = open(folder+"/main.py","r").read()
    try:
        title = open(folder+"/.title","r").read()
        des = open(folder+"/description.txt","r").read()
    except:
        ttittlle = open(folder+"/.title","w").write("Project Title")
        title = open(folder+"/.title","r").read()
        ddess = open(folder+"/description.txt","w").write("Description")
        des = open(folder+"/description.txt","r").read()
    def return_to_menu():
        global app
        global mode
        return_q = yesno("NextEngine - Return to Home","Are you sure? All changes since your last save will be lost.")
        if return_q == True:
            editor.destroy()
            app.show()
            mode = 0
    def tab_switch():
        global codebox
        global tab
        tab = menu.value
        if tab != "Code":
            codebox.visible = False
            apply_button.visible = False
        if tab == "Code":
            codebox.visible = True
            apply_button.visible = True
        if tab == "Run Game":
            run_button.visible = True
        if tab != "Run Game":
            run_button.visible = False
        if tab == "Information":
            title_box.visible = True
            des_box.visible = True
            save_button.visible = True
        if tab != "Information":
            title_box.visible = False
            des_box.visible = False
            save_button.visible = False
        if tab == "Assets":
            sprite_text.visible = True
            open_sprite.visible = True
            add_sprite.visible = True
            music_text.visible = True
            open_music.visible = True
            add_music.visible = True
        if tab != "Assets":
            sprite_text.visible = False
            open_sprite.visible = False
            add_sprite.visible = False
            music_text.visible = False
            open_music.visible = False
            add_music.visible = False
        editor.update()
    def resize():
        global codebox
        global code_width
        global code_height
        code_width = math.ceil(editor.width/11)
        code_height = math.ceil(editor.height/20)
        codebox.width = code_width
        codebox.height = code_height
        des_box.width = code_width
        des_box.height = code_height-3
        editor.update()
    def fullscreen_toggle():
        global editor
        if editor.full_screen == False:
            editor.full_screen = True
        elif editor.full_screen == True:
            editor.full_screen = False
        editor.update()
        time.sleep(1/4)
        editor.update()
        resize()
    def save_changes():
        try:
            new_code = open(folder+"/main.py","w").write(codebox.value)
            info("NextEngine - Save","Changes have been saved.")
        except:
            editor.error("NextEngine - Project Error","An error occured while saving!")
    def apply_changes():
        try:
            new_des = open(folder+"/description.txt","w").write(des_box.value)
            new_title = open(folder+"/.title","w").write(title_box.value)
            info("NextEngine - Save","Changes have been saved.")
        except:
            editor.error("NextEngine - Project Error","An error occured while saving!")
    def view_sprite():
        sprite_to_view = editor.select_file(title="Select Asset to View",folder=folder+"/sprites",filetypes=[["PNG Files",".png"]])
        if sprite_to_view != "":
            sprite_viewer = Window(editor,bg="darkblue",title="NextEngine - View Asset",height=256,width=256)
            sprite_viewing = Picture(sprite_viewer,image=sprite_to_view)
            sprite_viewer.height = sprite_viewing.height+32
            sprite_viewer.width = sprite_viewing.width+64
    def music_play():
        def music_stop():
            nextlib.StopMusic()
            music_player.destroy()
        music_to_play = editor.select_file(title="Select Asset to Play",folder=folder+"/music",filetypes=[["OGG Files",".ogg"]])
        if music_to_play != "":
            nextlib.pg.mixer.music.load(music_to_play)
            nextlib.pg.mixer.music.play(-1,0.0,0)
            music_player = Window(editor,bg="darkblue",title="NextEngine - Music Player",height=64,width=300)
            PushButton(music_player,text="Stop Playback",command=music_stop).bg = "white"
    def move_sprite():
        sprite_to_add = editor.select_file(title="Select Asset to Add",folder=home,filetypes=[["PNG Files",".png"]])
        if sprite_to_add != "":
            try:
                command = f'cp '+sprite_to_add+' '+folder+'/sprites/'
                subprocess.Popen(command,stdout=True,stderr=True,shell=True)
                time.sleep(3)
                info("NextEngine - Add Asset","Asset has been added.")
            except:
                editor.error("NextEngine - Asset Load","An error occured while adding the asset!")
    def move_music():
        music_to_add = editor.select_file(title="Select Asset to Add",folder=home,filetypes=[["OGG Files",".ogg"]])
        if music_to_add != "":
            try:
                command = f'cp '+music_to_add+' '+folder+'/music/'
                subprocess.Popen(command,stdout=True,stderr=True,shell=True)
                time.sleep(3)
                info("NextEngine - Add Asset","Asset has been added.")
            except:
                editor.error("NextEngine - Asset Load","An error occured while adding the asset!")
    def run_game():
        command = f'cd '+folder+'; python3 '+folder+'/main.py'
        subprocess.Popen(command,stdout=True,stderr=True,shell=True)
        print("Running project...")
    def doc_page_basics():
        webbrowser.open(url="https://github.com/hadcl4/NextEngine/blob/main/docs/README.md",new=2,autoraise=True)
    def doc_page_audio():
        webbrowser.open(url="https://github.com/hadcl4/NextEngine/blob/main/docs/AUDIO.md",new=2,autoraise=True)
    def doc_page_control():
        webbrowser.open(url="https://github.com/hadcl4/NextEngine/blob/main/docs/CONTROLLERS.md",new=2,autoraise=True)
    def doc_page_draw():
        webbrowser.open(url="https://github.com/hadcl4/NextEngine/blob/main/docs/ADVANCED_DRAWING.md",new=2,autoraise=True)
    def doc_page_info():
        webbrowser.open(url="https://github.com/hadcl4/NextEngine/blob/main/docs/NEXT_INFO.md",new=2,autoraise=True)
    def doc_page_mouse():
        webbrowser.open(url="https://github.com/hadcl4/NextEngine/blob/main/docs/MOUSE.md",new=2,autoraise=True)
    app.hide()
    editor = Window(app,bg="darkblue",title="NextEngine - Project",height=650,width=800)
    editor.icon = working_path+"assets/logo_small.png"
    editor.when_closed = return_to_menu
    menu = ButtonGroup(editor,options=["Code","Information","Assets","Run Game"],horizontal=True,command=tab_switch)
    menu.bg = "white"
    # Code Tab
    codebox = TextBox(editor,multiline=True,width=code_width,height=code_height,command=resize,text=code,scrollbar=True)
    codebox.bg = "white"
    apply_button = PushButton(editor,text="Save Changes...",command=save_changes)
    apply_button.bg = "white"
    # Information
    title_box = TextBox(editor,multiline=False,width=25,height=1,text=title,scrollbar=False)
    des_box = TextBox(editor,multiline=True,width=code_width,height=code_height-3,command=resize,text=des,scrollbar=True)
    title_box.bg = "white"
    des_box.bg = "white"
    title_box.visible = False
    des_box.visible = False
    save_button = PushButton(editor,text="Save Changes...",command=apply_changes)
    save_button.bg = "white"
    save_button.visible = False
    # Assets
    sprite_text = Text(editor,text="\nSPRITES",color="white",size=15)
    open_sprite = PushButton(editor,text="View Sprite",command=view_sprite)
    add_sprite = PushButton(editor,text="Add Sprite",command=move_sprite)
    music_text = Text(editor,text="\nAUDIO",color="white",size=15)
    open_music = PushButton(editor,text="Play Audio",command=music_play)
    add_music = PushButton(editor,text="Add Audio",command=move_music)
    open_sprite.bg = "white"
    add_sprite.bg = "white"
    open_music.bg = "white"
    add_music.bg = "white"
    sprite_text.visible = False
    open_sprite.visible = False
    add_sprite.visible = False
    music_text.visible = False
    open_music.visible = False
    add_music.visible = False
    # Run game
    run_button = PushButton(editor,text="Run game...",command=run_game)
    run_button.bg = "white"
    run_button.visible = False
    menubar = MenuBar(editor,
                  toplevel=["Menu","Documentation"],
                  options=[
                      [ ["Toggle Fullscreen",fullscreen_toggle], ["Return to Home", return_to_menu] ],
                      [ ["The Basics",doc_page_basics], ["Playing Audio",doc_page_audio], ["Controller Input",doc_page_control], ["Advanced Drawing Functions",doc_page_draw], ["Mouse Input",doc_page_mouse], ["Surface/Screen Info",doc_page_info] ]
                  ])

def load():
    global mode
    global folder
    mode = 0
    folder = app.select_folder(title="Select Project Folder...", folder=home)
    try:
        open(folder+"/.next","r")
        mode = 1
    except:
        app.error("NextEngine - Project Load Error","An error occured while loading the project.")
    if mode == 1:
        edit(folder)

def create():
    global mode
    global folder
    mode = 0
    fol = app.select_folder(title="Select where to store new project...",folder=home)
    proj_name = question("NextEngine - New Project","Please enter a name for your project.")
    if not proj_name == None:
        try:
            if os.name == "posix":
                command = f'cd '+fol+'; mkdir '+proj_name+'; cp '+working_path+'nextlib.py '+proj_name+'/nextlib.py; mkdir '+proj_name+'/sprites; mkdir '+proj_name+'/music'
            elif os.name == "nt":
                command = f'cd '+fol+'; mkdir '+proj_name+'; Copy-Item '+working_path+'nextlib.py '+proj_name+'/nextlib.py; mkdir '+proj_name+'/sprites; mkdir '+proj_name+'/music'
            else:
                app.error("NextEngine - Project Create Error","Unrecognized operating system!")
            subprocess.Popen(command,stdout=True,stderr=True,shell=True)
            time.sleep(3)
            folder = fol+"/"+proj_name
            open(folder+"/.next","w").write("NEXT")
            open(folder+"/main.py","w").write("from nextlib import *\n\n# Initialize variables and nextlib here...\n\nwhile True:\n# Game loop goes here...")
            mode = 1
        except:
            app.error("NextEngine - Project Create Error","An error occured while creating new project.")
    else:
        app.error("NextEngine - Project Create Error","A name is required!")
    if mode == 1:
        creation_success = info("NextEngine - Project Create Success","The project was successfully created! Open the project with LOAD on the menu to get started.")

global app
app = App(title="NextEngine - Home",bg="darkblue",height=345,width=325)
app.icon = working_path+"assets/logo_small.png"
Picture(app,image=working_path+"assets/logo.png")
PushButton(app,image=working_path+"assets/load.png",command=load)
PushButton(app,image=working_path+"assets/new.png",command=create)
PushButton(app,image=working_path+"assets/quit.png",command=exit)
app.display()
