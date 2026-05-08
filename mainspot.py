from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYAXISMOTION, joystick, time, key, transform, K_d, K_RIGHT
from assets import bottom_cactus, begin_player, medium_font, bg, cowboy_hat_image, thinking_hat_image, top_hat_image
from assets import red_cap_image, party_hat_image, witch_hat_image, mexican_hat_image, king_hat_image, maintheme
from resize import game_surface, window, is_fullscreen, handle_resize, toggle_fullscreen, render_to_screen
from data import data_shop, save_data
from vid import vid_preview
from sys import exit
def mainspot(diff=0):
    global data_shop, window, is_fullscreen
    Cowboy_Hat = button(175, 380, 40, 30, cowboy_hat_image)
    Thinking_Hat = button(175, 380, 40, 30, thinking_hat_image)
    Top_Hat = button(175, 375, 40, 30, top_hat_image)
    Red_Cap = button(180, 380, 40, 30, red_cap_image)
    Red_Cap.image = transform.flip(Red_Cap.image, 90, 0)
    Party_Hat = button(175, 380, 40, 30, party_hat_image)
    Witch_Hat = button(175, 375, 40, 30, witch_hat_image)
    Mexican_Hat = button(175, 380, 40, 30, mexican_hat_image)
    King_Hat = button(175, 380, 40, 30, king_hat_image)
    maintheme.stop()
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
                if io == 1 and diff == 1: #right
                    vid_preview(4)
                    from game import game
                    game(1)
                elif io == 1 and diff == 2: #right
                    vid_preview(5)
                    from game import game
                    game(2)
                elif io == 1 and diff == 3: #right
                    vid_preview(6)
                    from game import game
                    game(3)
        begin_text = medium_font.render("Press D or Right key to Climb", 1, (0, 0, 255))
        keys = key.get_pressed()
        if keys[K_d] and diff == 1 or keys[K_RIGHT] and diff == 1:
            vid_preview(4)
            from game import game
            game(1)
        elif keys[K_d] and diff == 2 or keys[K_RIGHT] and diff == 2:
            vid_preview(5)
            from game import game
            game(2)
        elif keys[K_d] and diff == 3 or keys[K_RIGHT] and diff == 3:
            vid_preview(6)
            from game import game
            game(3)
        game_surface.fill((204, 102, 0))
        game_surface.blit(bottom_cactus, (640, -500))
        game_surface.blit(bg, (0, 0))
        game_surface.blit(begin_player, (150, 400))
        game_surface.blit(begin_text, (360, 600))
        if data_shop['cowboy_hat_equipped'] == True:
            game_surface.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            game_surface.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            game_surface.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            game_surface.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            game_surface.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            game_surface.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            game_surface.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            game_surface.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        render_to_screen()