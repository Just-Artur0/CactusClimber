from pygame import transform, font, joystick, time, event, quit, Rect
from pygame.locals import QUIT, JOYBUTTONDOWN, MOUSEBUTTONDOWN, K_F11, KEYDOWN, K_ESCAPE, VIDEORESIZE
from json import dump
from Button import button
from assets import money_image, back_image, easy_image, normal_image, hard_image, show_stats_image, hide_stats_image, large_font, medium_font, small_font, play_image, options_image, shop_image
from assets import credits_image, quit_image, reset_image, achievements_image, yes_image, no_image, textbox_image, denied_sound, equipped_sound, maintheme
from resize import handle_resize, render_to_screen, scale_mouse_pos, toggle_fullscreen, window, is_fullscreen, game_surface
from data import data_easy, data_normal, data_hard, data_options, data_shop, data_achievements, save_data
from os.path import join
from sys import exit
def mainmenu():
    global data_options, window, is_fullscreen
    Money = button(1030, 0, 250, 100, money_image)
    Back = button(0, 670, 100, 50, back_image)
    Easy = button(50, 300, 350, 200, easy_image)
    Normal = button(450, 300, 350, 200, normal_image)
    Hard = button(850, 300, 350, 200, hard_image)
    Easy_Stats = button(50, 500, 250, 50, show_stats_image)
    Normal_Stats = button(450, 500, 250, 50, show_stats_image)
    Hard_Stats = button(850, 500, 250, 50, show_stats_image)
    Easy_Hide_Stats = button(10050, 500, 250, 50, hide_stats_image)
    Normal_Hide_Stats = button(1450, 500, 250, 50, hide_stats_image)
    Hard_Hide_Stats = button(1850, 500, 250, 50, hide_stats_image)
    if data_options['show_easy'] == True:
        Easy_Stats.image = transform.scale(hide_stats_image, (0, 0))
        Easy_Stats.x = 10000
        Easy_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
        Easy_Hide_Stats.x = 50
    if data_options['show_normal'] == True:
        Normal_Stats.image = transform.scale(hide_stats_image, (0, 0))
        Normal_Stats.x = 10000
        Normal_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
        Normal_Hide_Stats.x = 450
    if data_options['show_hard'] == True:
        Hard_Stats.image = transform.scale(hide_stats_image, (0, 0))
        Hard_Stats.x = 10000
        Hard_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
        Hard_Hide_Stats.x = 850
    maintheme.stop()
    run = True
    clockyy = time.Clock()
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
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(3):
                    from mainspot import mainspot
                    return mainspot(1)
                elif joystick.Joystick(0).get_button(2):
                    from mainspot import mainspot
                    return mainspot(2)
                elif joystick.Joystick(0).get_button(0):
                    from mainspot import mainspot
                    return mainspot(3)
                elif joystick.Joystick(0).get_button(1):
                    start()
                elif joystick.Joystick(0).get_button(4):
                    data_options['show_easy'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Easy_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Easy_Stats.x = 10000
                    Easy_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
                    Easy_Hide_Stats.x = 50
                elif joystick.Joystick(0).get_button(5):
                    data_options['show_normal'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Normal_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Normal_Stats.x = 10000
                    Normal_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
                    Normal_Hide_Stats.x = 450
                elif joystick.Joystick(0).get_button(7):
                    data_options['show_hard'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Hard_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Hard_Stats.x = 10000
                    Hard_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
                    Hard_Hide_Stats.x = 850
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = scale_mouse_pos(*e.pos)
                easy_rect = Rect(Easy.x, Easy.y, Easy.width, Easy.height)
                normal_rect = Rect(Normal.x, Normal.y, Normal.width, Normal.height)
                hard_rect = Rect(Hard.x, Hard.y, Hard.width, Hard.height)
                easy_stats_rect = Rect(Easy_Stats.x, Easy_Stats.y, Easy_Stats.width, Easy_Stats.height)
                normal_stats_rect = Rect(Normal_Stats.x, Normal_Stats.y, Normal_Stats.width, Normal_Stats.height)
                hard_stats_rect = Rect(Hard_Stats.x, Hard_Stats.y, Hard_Stats.width, Hard_Stats.height)
                easy_hide_stats_rect = Rect(Easy_Hide_Stats.x, Easy_Hide_Stats.y, Easy_Hide_Stats.width, Easy_Hide_Stats.height)
                normal_hide_stats_rect = Rect(Normal_Hide_Stats.x, Normal_Hide_Stats.y, Normal_Hide_Stats.width, Normal_Hide_Stats.height)
                hard_hide_stats_rect = Rect(Hard_Hide_Stats.x, Hard_Hide_Stats.y, Hard_Hide_Stats.width, Hard_Hide_Stats.height)
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                if easy_rect.collidepoint(mousex, mousey):
                    from mainspot import mainspot
                    return mainspot(1)
                elif normal_rect.collidepoint(mousex, mousey):
                    from mainspot import mainspot
                    return mainspot(2)
                elif hard_rect.collidepoint(mousex, mousey):
                    from mainspot import mainspot
                    return mainspot(3)
                elif easy_stats_rect.collidepoint(mousex, mousey):   
                    data_options['show_easy'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Easy_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Easy_Stats.x = 10000
                    Easy_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
                    Easy_Hide_Stats.x = 50
                elif easy_hide_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_easy'] = False
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Easy_Stats.image = transform.scale(show_stats_image, (250, 50))
                    Easy_Stats.x = 50
                    Easy_Hide_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Easy_Hide_Stats.x = 10000
                elif normal_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_normal'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Normal_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Normal_Stats.x = 10000
                    Normal_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
                    Normal_Hide_Stats.x = 450
                elif normal_hide_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_normal'] = False
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Normal_Stats.image = transform.scale(show_stats_image, (250, 50))
                    Normal_Stats.x = 450
                    Normal_Hide_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Normal_Hide_Stats.x = 10000
                elif hard_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_hard'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Hard_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Hard_Stats.x = 10000
                    Hard_Hide_Stats.image = transform.scale(hide_stats_image, (250, 50))
                    Hard_Hide_Stats.x = 850
                elif hard_hide_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_hard'] = False
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Hard_Stats.image = transform.scale(show_stats_image, (250, 50))
                    Hard_Stats.x = 850
                    Hard_Hide_Stats.image = transform.scale(hide_stats_image, (0, 0))
                    Hard_Hide_Stats.x = 1850
                elif back_rect.collidepoint(mousex, mousey):
                    return start()
        #text
        full_meter_normal_text = small_font.render("(cactus is 117m)", 1, (255, 255, 255))
        total_fireballs_dodged_normal_text = small_font.render(f"Total Fireballs Dodged: {data_normal['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_normal_text = small_font.render(f"Total Meters Climbed: {data_normal['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_normal_text = small_font.render(f"Total Birds Dodged: {data_normal['birds_dodged']}", 1, (255, 255, 255))
        full_meter_hard_text = small_font.render("(cactus is 217m)", 1, (255, 255, 255))
        total_fireballs_dodged_hard_text = small_font.render(f"Total Fireballs Dodged: {data_hard['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_hard_text = small_font.render(f"Total Meters Climbed: {data_hard['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_hard_text = small_font.render(f"Total Birds Dodged: {data_hard['birds_dodged']}", 1, (255, 255, 255))
        full_meter_easy_text = small_font.render("(cactus is 57m)", 1, (255, 255, 255))
        total_fireballs_dodged_easy_text = small_font.render(f"Total Fireballs Dodged: {data_easy['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_easy_text = small_font.render(f"Total Meters Climbed: {data_easy['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_easy_text = small_font.render(f"Total Birds Dodged: {data_easy['birds_dodged']}", 1, (255, 255, 255))
        title_text = font.SysFont('comicsans', 140).render("Cactus Climber", 1, (64, 255, 25)) 
        version_text = medium_font.render("v1.3.1", 1, (64, 255, 25))
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        game_surface.fill((204, 102, 25))
        if data_options['show_easy'] == True:
            game_surface.blit(total_fireballs_dodged_easy_text, (50, 550))
            game_surface.blit(total_birds_dodged_easy_text, (50, 580))
            game_surface.blit(highest_meter_easy_text, (50, 610))
            game_surface.blit(full_meter_easy_text, (50, 640))
        if data_options['show_normal'] == True:
            game_surface.blit(total_fireballs_dodged_normal_text, (450, 550))
            game_surface.blit(total_birds_dodged_normal_text, (450, 580))
            game_surface.blit(highest_meter_normal_text, (450, 610))
            game_surface.blit(full_meter_normal_text, (450, 640))
        if data_options['show_hard'] == True:
            game_surface.blit(total_fireballs_dodged_hard_text, (850, 550))
            game_surface.blit(total_birds_dodged_hard_text, (850, 580))
            game_surface.blit(highest_meter_hard_text, (850, 610))
            game_surface.blit(full_meter_hard_text, (850, 640))
        game_surface.blit(Easy.image, (Easy.x, Easy.y))
        game_surface.blit(Normal.image, (Normal.x, Normal.y))
        game_surface.blit(Hard.image, (Hard.x, Hard.y))
        game_surface.blit(Easy_Stats.image, (Easy_Stats.x, Easy_Stats.y))
        game_surface.blit(Normal_Stats.image, (Normal_Stats.x, Normal_Stats.y))
        game_surface.blit(Hard_Stats.image, (Hard_Stats.x, Hard_Stats.y))
        game_surface.blit(Easy_Hide_Stats.image, (Easy_Hide_Stats.x, Easy_Hide_Stats.y))
        game_surface.blit(Normal_Hide_Stats.image, (Normal_Hide_Stats.x, Normal_Hide_Stats.y))
        game_surface.blit(Hard_Hide_Stats.image, (Hard_Hide_Stats.x, Hard_Hide_Stats.y))
        game_surface.blit(Back.image, (Back.x, Back.y))
        game_surface.blit(title_text, (150, 90))
        game_surface.blit(version_text, (0, 0))
        game_surface.blit(money_text, ((game_surface.get_width() - money_text.get_width() - 225), 0))
        game_surface.blit(Money.image, (Money.x, Money.y))
        render_to_screen()
def start():
    global data_easy, data_normal, data_hard, data_options, data_shop, data_achievements, window, is_fullscreen
    Play = button(500, 150, 250, 100, play_image)
    Options = button(500, 260, 250, 100, options_image)
    Shop = button(500, 370, 250, 100, shop_image)
    Credits = button(500, 480, 250, 100, credits_image)
    Quit = button(500, 600, 250, 100, quit_image)
    Reset = button(1030, 0, 250, 100, reset_image)
    Achievements = button(0, 50, 250, 100, achievements_image)
    Yes = button(450, 500, 150, 100, yes_image)
    No = button(700, 500, 150, 100, no_image)
    TextBox = button(450, 200, 400, 400, textbox_image)
    show_textbox = False
    show_start = True
    run = True
    clockyy = time.Clock()
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
            elif e.type == JOYBUTTONDOWN:
                if show_textbox == True:
                    if joystick.Joystick(0).get_button(1):
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        show_textbox = False
                        show_start = True
                        return start()
                    elif joystick.Joystick(0).get_button(0):
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['money'] = 0
                        data_shop['red_cap_equipped'] = False
                        data_shop['thinking_hat_equipped'] = False
                        data_shop['top_hat_equipped'] = False
                        data_shop['cowboy_hat_equipped'] = False
                        data_shop['king_hat_equipped'] = False
                        data_shop['mexican_hat_equipped'] = False
                        data_shop['witch_hat_equipped'] = False
                        data_shop['party_hat_equipped'] = False
                        data_shop['red_cap_unlocked'] = False
                        data_shop['thinking_hat_unlocked'] = False
                        data_shop['top_hat_unlocked'] = False
                        data_shop['cowboy_hat_unlocked'] = False
                        data_shop['king_hat_unlocked'] = False
                        data_shop['mexican_hat_unlocked'] = False
                        data_shop['witch_hat_unlocked'] = False
                        data_shop['party_hat_unlocked'] = False
                        data_shop['show_cost'] = True
                        data_shop['show_cost2'] = True
                        data_shop['show_cost3'] = True
                        data_shop['show_cost4'] = True
                        data_shop['show_cost5'] = True
                        data_shop['show_cost6'] = True
                        data_shop['show_cost7'] = True
                        data_shop['show_cost8'] = True
                        data_options['play_sfx'] = True
                        data_options['play_music'] = True
                        data_options['controller_vibration'] = True
                        data_options['show_easy'] = False
                        data_options['show_normal'] = False
                        data_options['show_hard'] = False
                        data_easy['birds_dodged'] = 0
                        data_easy['fireballs_dodged'] = 0
                        data_easy['meters_up'] = 0
                        data_normal['birds_dodged'] = 0
                        data_normal['fireballs_dodged'] = 0
                        data_normal['meters_up'] = 0
                        data_hard['birds_dodged'] = 0
                        data_hard['fireballs_dodged'] = 0
                        data_hard['meters_up'] = 0
                        data_achievements['cactus_climber'] = False
                        data_achievements['catch_on_fire'] = False
                        data_achievements['climb_the_top'] = False
                        data_achievements['climb'] = False
                        data_achievements['dont_catch_on_fire'] = False
                        data_achievements['dont_get_hit'] = False
                        data_achievements['expert'] = False
                        data_achievements['first_steps'] = False
                        data_achievements['get_hit'] = False
                        data_achievements['hat_collector'] = False
                        data_achievements['the_true_cactus_climber'] = False
                        data_achievements['achievements_complete'] = 0
                        data_achievements['achievement_1'] = True
                        data_achievements['achievement_2'] = True
                        data_achievements['achievement_3'] = True
                        data_achievements['achievement_4'] = True
                        data_achievements['achievement_5'] = True
                        data_achievements['achievement_6'] = True
                        data_achievements['achievement_7'] = True
                        data_achievements['achievement_8'] = True
                        data_achievements['achievement_9'] = True
                        data_achievements['achievement_10'] = True
                        data_achievements['achievement_11'] = True
                        save_data()
                        show_start = True
                        return start()
                if show_start == True:
                    if joystick.Joystick(0).get_button(0):
                        return mainmenu()
                    elif joystick.Joystick(0).get_button(6):
                        from achievements import achievements
                        return achievements()
                    elif joystick.Joystick(0).get_button(2):
                        from shop import shop
                        return shop()
                    elif joystick.Joystick(0).get_button(3):
                        from credits import credits
                        return credits()
                    elif joystick.Joystick(0).get_button(4):
                        run = False
                        quit()
                        exit()
                    elif joystick.Joystick(0).get_button(5):
                        show_textbox = True
                        show_start = False
                    elif joystick.Joystick(0).get_button(7):
                        from options import options
                        return options()
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = scale_mouse_pos(*e.pos)
                play_rect = Rect(Play.x, Play.y, Play.width, Play.height)
                options_rect = Rect(Options.x, Options.y, Options.width, Options.height)
                shop_rect = Rect(Shop.x, Shop.y, Shop.width, Shop.height)
                credits_rect = Rect(Credits.x, Credits.y, Credits.width, Credits.height)
                quit_rect = Rect(Quit.x, Quit.y, Quit.width, Quit.height)
                reset_rect = Rect(Reset.x, Reset.y, Reset.width, Reset.height)
                achievements_rect = Rect(Achievements.x, Achievements.y, Achievements.width, Achievements.height)
                yes_rect = Rect(Yes.x, Yes.y, Yes.width, Yes.height)
                no_rect = Rect(No.x, No.y, No.width, No.height)
                if show_start == True:
                    if play_rect.collidepoint(mousex, mousey):
                        return mainmenu()
                    elif quit_rect.collidepoint(mousex, mousey):
                        run = False
                        quit()
                        exit()
                    elif options_rect.collidepoint(mousex, mousey):
                        from options import options
                        return options()
                    elif shop_rect.collidepoint(mousex, mousey):
                        from shop import shop
                        return shop()
                    elif achievements_rect.collidepoint(mousex, mousey):
                        from achievements import achievements
                        return achievements()
                    elif credits_rect.collidepoint(mousex, mousey):
                        from credits import credits
                        return credits()
                if show_textbox == True:
                    if no_rect.collidepoint(mousex, mousey):
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        show_textbox = False
                        show_start = True
                        return start()
                    elif yes_rect.collidepoint(mousex, mousey):
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['money'] = 0
                        data_shop['red_cap_equipped'] = False
                        data_shop['thinking_hat_equipped'] = False
                        data_shop['top_hat_equipped'] = False
                        data_shop['cowboy_hat_equipped'] = False
                        data_shop['king_hat_equipped'] = False
                        data_shop['mexican_hat_equipped'] = False
                        data_shop['witch_hat_equipped'] = False
                        data_shop['party_hat_equipped'] = False
                        data_shop['red_cap_unlocked'] = False
                        data_shop['thinking_hat_unlocked'] = False
                        data_shop['top_hat_unlocked'] = False
                        data_shop['cowboy_hat_unlocked'] = False
                        data_shop['king_hat_unlocked'] = False
                        data_shop['mexican_hat_unlocked'] = False
                        data_shop['witch_hat_unlocked'] = False
                        data_shop['party_hat_unlocked'] = False
                        data_shop['show_cost'] = True
                        data_shop['show_cost2'] = True
                        data_shop['show_cost3'] = True
                        data_shop['show_cost4'] = True
                        data_shop['show_cost5'] = True
                        data_shop['show_cost6'] = True
                        data_shop['show_cost7'] = True
                        data_shop['show_cost8'] = True
                        data_options['play_sfx'] = True
                        data_options['play_music'] = True
                        data_options['controller_vibration'] = True
                        data_options['show_easy'] = False
                        data_options['show_normal'] = False
                        data_options['show_hard'] = False
                        data_easy['birds_dodged'] = 0
                        data_easy['fireballs_dodged'] = 0
                        data_easy['meters_up'] = 0
                        data_normal['birds_dodged'] = 0
                        data_normal['fireballs_dodged'] = 0
                        data_normal['meters_up'] = 0
                        data_hard['birds_dodged'] = 0
                        data_hard['fireballs_dodged'] = 0
                        data_hard['meters_up'] = 0
                        data_achievements['cactus_climber'] = False
                        data_achievements['catch_on_fire'] = False
                        data_achievements['climb_the_top'] = False
                        data_achievements['climb'] = False
                        data_achievements['dont_catch_on_fire'] = False
                        data_achievements['dont_get_hit'] = False
                        data_achievements['expert'] = False
                        data_achievements['first_steps'] = False
                        data_achievements['get_hit'] = False
                        data_achievements['hat_collector'] = False
                        data_achievements['the_true_cactus_climber'] = False
                        data_achievements['achievements_complete'] = 0
                        data_achievements['achievement_1'] = True
                        data_achievements['achievement_2'] = True
                        data_achievements['achievement_3'] = True
                        data_achievements['achievement_4'] = True
                        data_achievements['achievement_5'] = True
                        data_achievements['achievement_6'] = True
                        data_achievements['achievement_7'] = True
                        data_achievements['achievement_8'] = True
                        data_achievements['achievement_9'] = True
                        data_achievements['achievement_10'] = True
                        data_achievements['achievement_11'] = True
                        save_data()
                        show_start = True
                        return start()
                if reset_rect.collidepoint(mousex, mousey):
                    show_textbox = True
                    show_start = False
        title_text = large_font.render("Cactus Climber", 1, (64, 255, 25)) 
        version_text = medium_font.render("v1.3.1", 1, (64, 255, 25))
        game_surface.fill((204, 102, 25))
        game_surface.blit(Play.image, (Play.x, Play.y))
        game_surface.blit(Options.image, (Options.x, Options.y))
        game_surface.blit(Shop.image, (Shop.x, Shop.y))
        game_surface.blit(Credits.image, (Credits.x, Credits.y))
        game_surface.blit(Quit.image, (Quit.x, Quit.y))
        game_surface.blit(Reset.image, (Reset.x, Reset.y))
        game_surface.blit(Achievements.image, (Achievements.x, Achievements.y))
        game_surface.blit(title_text, (350, 0))
        game_surface.blit(version_text, (0, 0))
        if show_textbox == True:
            game_surface.blit(TextBox.image, (TextBox.x, TextBox.y))
            game_surface.blit(No.image, (No.x, No.y))
            game_surface.blit(Yes.image, (Yes.x, Yes.y))
        render_to_screen()