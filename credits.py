from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYBUTTONDOWN, MOUSEBUTTONDOWN, Rect, joystick, time
from assets import back_image, credits_bg_image
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, game_surface, render_to_screen, scale_mouse_pos
from data import save_data
from sys import exit
def credits():
    global window, is_fullscreen
    Back = button(1030, 600, 250, 100, back_image)
    Credits = button(0, 0, game_surface.get_width(), game_surface.get_height(), credits_bg_image)
    run = True
    clockyy = time.Clock()
    while run:  
        clockyy.tick(15)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                exit()
            elif e.type == VIDEORESIZE:
                handle_resize(e.w, e.h)
            elif e.type == KEYDOWN:
                if e.key == K_F11:
                    toggle_fullscreen()
                elif e.key == K_ESCAPE and is_fullscreen:
                    toggle_fullscreen()
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(1):
                    from menus import start
                    return start()
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = scale_mouse_pos(*e.pos)
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                if back_rect.collidepoint(mousex, mousey):
                    from menus import start
                    return start()
        game_surface.blit(Credits.image, (Credits.x, Credits.y))
        game_surface.blit(Back.image, (Back.x, Back.y))
        render_to_screen()