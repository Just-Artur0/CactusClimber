from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYAXISMOTION, joystick, time, key, display, K_a, K_LEFT
from assets import money_image, medium_font, large_font
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, game_surface, render_to_screen
from data import data_shop, save_data
from vid import vid_preview
from sys import exit
def win():
    global window, is_fullscreen
    Money = button(1030, 600, 250, 100, money_image)
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
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                if io == -1: #left
                    vid_preview(1)
                    from menus import mainmenu
                    return mainmenu()
        #text
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        main_text = medium_font.render("Press A or Left key to Go Back Down", 1, (0, 0, 255))
        win_text = medium_font.render("You Reached the Top!", 1, (0, 0, 255))
        win1_text = medium_font.render("but at what Cost?", 1, (255, 0, 0))
        game_surface.blit(win_text, (500, 0))
        game_surface.blit(win1_text, (550, 50))
        game_surface.blit(main_text, (360, 600))
        #keyboard input
        keys = key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            vid_preview(1)
            from menus import mainmenu
            return mainmenu()
        #displaying on screen
        game_surface.blit(money_text, ((game_surface.get_width() - money_text.get_width() - 225), 600))
        game_surface.blit(Money.image, (Money.x, Money.y))
        render_to_screen()