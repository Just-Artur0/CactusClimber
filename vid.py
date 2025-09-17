from moviepy.editor import VideoFileClip
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, time
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, render_to_screen
from data import save_data
from sys import exit
def vid_preview(video=0):
    global window, is_fullscreen
    run = True
    clockyy = time.Clock()
    if video == 0:
        clip = VideoFileClip("Videos/begin.mp4")
    elif video == 1:
        clip = VideoFileClip("Videos/end.mp4")
    elif video == 2:
        clip = VideoFileClip("Videos/birddeath.mp4")
    elif video == 3:
        clip = VideoFileClip("Videos/fireballdeath.mp4")
    elif video >= 4:
        clip = VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(15)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                exit()
                run = False
            elif e.type == VIDEORESIZE:
                handle_resize(e.w, e.h)
            elif e.type == KEYDOWN:
                if e.key == K_F11:
                    toggle_fullscreen()
                elif e.key == K_ESCAPE and is_fullscreen:
                    toggle_fullscreen()
        clip.preview()
        render_to_screen()
        clip.close()
        if video > 1 and video < 4:
            from menus import mainmenu
            return mainmenu()
        if video == 4:
            from game import game
            return game(1)
        elif video == 5:
            from game import game
            return game(2)
        elif video == 6:
            from game import game
            return game(3)