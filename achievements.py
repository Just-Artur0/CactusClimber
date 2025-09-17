from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYBUTTONDOWN, MOUSEBUTTONDOWN, Rect, joystick, time
from assets import back_image, first_steps_image, climb_the_top_image, cactus_climber_image, catch_on_fire_image, climb_image, dont_catch_on_fire_image, dont_get_hit_image, expert_image
from assets import get_hit_image, the_true_cactus_climber_image, hat_collector_image, checked_off_image, checked_image, large_font, medium_font
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, game_surface, render_to_screen, scale_mouse_pos
from data import data_achievements, data_easy, data_normal, data_hard, data_shop, save_data
from json import dump
from os.path import join
from sys import exit
def achievements():
    global data_achievements, data_easy, data_hard, data_normal, data_shop, window, is_fullscreen
    Back = button(0, 670, 100, 50, back_image)
    First_Steps = button(10, 100, 250, 100, first_steps_image)
    Checked_off = button(280, 100, 100, 100, checked_off_image)
    Checked = button(10760, 100, 100, 100, checked_image)
    Climb_The_Top = button(460, 100, 250, 100, climb_the_top_image)
    Checked_off1 = button(730, 100, 100, 100, checked_off_image)
    Checked1 = button(10760, 100, 100, 100, checked_image)
    Cactus_Climber = button(10, 400, 250, 100, cactus_climber_image)
    Checked_off2 = button(280, 400, 100, 100, checked_off_image)
    Checked2 = button(10760, 400, 100, 100, checked_image)
    Catch_On_Fire = button(910, 250, 250, 100, catch_on_fire_image)
    Checked_off3 = button(1180, 250, 100, 100, checked_off_image)
    Checked3 = button(10760, 250, 100, 100, checked_image)
    Climb = button(10, 250, 250, 100, climb_image)
    Checked_off4 = button(280, 250, 100, 100, checked_off_image)
    Checked4 = button(10760, 250, 100, 100, checked_image)
    Dont_Catch_On_Fire = button(910, 550, 250, 100, dont_catch_on_fire_image)
    Checked_off5 = button(1180, 550, 100, 100, checked_off_image)
    Checked5 = button(10760, 550, 100, 100, checked_image)
    Dont_Get_Hit = button(460, 550, 250, 100, dont_get_hit_image)
    Checked_off6 = button(730, 550, 100, 100, checked_off_image)
    Checked6 = button(10760, 550, 100, 100, checked_image)
    Expert = button(460, 250, 250, 100, expert_image)
    Checked_off7 = button(730, 250, 100, 100, checked_off_image)
    Checked7 = button(10760, 250, 100, 100, checked_image)
    Get_Hit = button(910, 400, 250, 100, get_hit_image)
    Checked_off8 = button(1180, 400, 100, 100, checked_off_image)
    Checked8 = button(10760, 400, 100, 100, checked_image)
    Hat_Collector = button(910, 100, 250, 100, hat_collector_image)
    Checked_off9 = button(1180, 100, 100, 100, checked_off_image)
    Checked9 = button(10760, 100, 100, 100, checked_image)
    The_True_Cactus_Climber = button(460, 400, 250, 100, the_true_cactus_climber_image)
    Checked_off10 = button(730, 400, 100, 100, checked_off_image)
    Checked10 = button(10760, 400, 100, 100, checked_image)
    if data_easy['meters_up'] + data_normal['meters_up'] + data_hard['meters_up'] >= 500:
        data_achievements['climb'] = True
        with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
            dump(data_achievements, save_data_achievements)
    if data_easy['meters_up'] + data_normal['meters_up'] + data_hard['meters_up'] >= 1000:
        data_achievements['cactus_climber'] = True
        with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
            dump(data_achievements, save_data_achievements)
    if data_easy['meters_up'] + data_normal['meters_up'] + data_hard['meters_up'] >= 10000:
        data_achievements['the_true_cactus_climber'] = True
        with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
            dump(data_achievements, save_data_achievements)
    if data_easy['fireballs_dodged'] + data_normal['fireballs_dodged'] + data_hard['fireballs_dodged'] >= 500:
        data_achievements['dont_catch_on_fire'] = True
        with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
            dump(data_achievements, save_data_achievements)
    if data_easy['birds_dodged'] + data_normal['birds_dodged'] + data_hard['birds_dodged'] >= 500:
        data_achievements['dont_get_hit'] = True
        with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
            dump(data_achievements, save_data_achievements)
    if data_shop['red_cap_unlocked'] == True and data_shop['thinking_hat_unlocked'] == True and data_shop['top_hat_unlocked'] == True and data_shop['cowboy_hat_unlocked'] == True and data_shop['party_hat_unlocked'] == True and data_shop['witch_hat_unlocked'] == True and data_shop['mexican_hat_unlocked'] == True and data_shop['king_hat_unlocked'] == True:
        data_achievements['hat_collector'] = True
        with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
            dump(data_achievements, save_data_achievements)
    if data_achievements['first_steps'] == True:
        if data_achievements['achievement_1'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off.x = 10760
        Checked.x = 280
        data_achievements['achievement_1'] = False
    if data_achievements['climb_the_top'] == True:
        if data_achievements['achievement_2'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off1.x = 10760
        Checked1.x = 730
        data_achievements['achievement_2'] = False
    if data_achievements['cactus_climber'] == True:
        if data_achievements['achievement_3'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off2.x = 10760
        Checked2.x = 280
        data_achievements['achievement_3'] = False
    if data_achievements['catch_on_fire'] == True:
        if data_achievements['achievement_4'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off3.x = 10760
        Checked3.x = 1180
        data_achievements['achievement_4'] = False
    if data_achievements['climb'] == True:
        if data_achievements['achievement_5'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off4.x = 10760
        Checked4.x = 280
        data_achievements['achievement_5'] = False
    if data_achievements['dont_catch_on_fire'] == True:
        if data_achievements['achievement_6'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off5.x = 10760
        Checked5.x = 1180
        data_achievements['achievement_6'] = False
    if data_achievements['dont_get_hit'] == True:
        if data_achievements['achievement_7'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off6.x = 10760
        Checked6.x = 730
        data_achievements['achievement_7'] = False
    if data_achievements['expert'] == True:
        if data_achievements['achievement_8'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off7.x = 10760
        Checked7.x = 730
        data_achievements['achievement_8'] = False
    if data_achievements['get_hit'] == True:
        if data_achievements['achievement_9'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off8.x = 10760
        Checked8.x = 1180
        data_achievements['achievement_9'] = False
    if data_achievements['hat_collector'] == True:
        if data_achievements['achievement_10'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off9.x = 10760
        Checked9.x = 1180
        data_achievements['achievement_10'] = False
    if data_achievements['the_true_cactus_climber'] == True:
        if data_achievements['achievement_11'] == True:
            data_achievements['achievements_complete'] += 1
        Checked_off10.x = 10760
        Checked10.x = 730
        data_achievements['achievement_11'] = False
    with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
        dump(data_achievements, save_data_achievements)
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
                if joystick.Joystick(0).get_button(1):
                    from menus import start
                    return start()
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = scale_mouse_pos(*e.pos)
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                if back_rect.collidepoint(mousex, mousey):
                    from menus import start
                    return start()
        title_text = large_font.render("ACHIEVEMENTS", 1, (255, 0, 0))
        achievements_complete_text = medium_font.render(str(data_achievements['achievements_complete']) + "/11 Complete", 1, (255, 255, 255))
        game_surface.fill((204, 102, 25))
        game_surface.blit(Back.image, (Back.x, Back.y))
        game_surface.blit(First_Steps.image, (First_Steps.x, First_Steps.y))
        game_surface.blit(Back.image, (Back.x, Back.y))
        game_surface.blit(Checked.image, (Checked.x, Checked.y))
        game_surface.blit(Checked_off.image, (Checked_off.x, Checked_off.y))
        game_surface.blit(Climb_The_Top.image, (Climb_The_Top.x, Climb_The_Top.y))
        game_surface.blit(Checked1.image, (Checked1.x, Checked1.y))
        game_surface.blit(Checked_off1.image, (Checked_off1.x, Checked_off1.y))
        game_surface.blit(Cactus_Climber.image, (Cactus_Climber.x, Cactus_Climber.y))
        game_surface.blit(Checked2.image, (Checked2.x, Checked2.y))
        game_surface.blit(Checked_off2.image, (Checked_off2.x, Checked_off2.y))
        game_surface.blit(Catch_On_Fire.image, (Catch_On_Fire.x, Catch_On_Fire.y))
        game_surface.blit(Checked3.image, (Checked3.x, Checked3.y))
        game_surface.blit(Checked_off3.image, (Checked_off3.x, Checked_off3.y))
        game_surface.blit(Climb.image, (Climb.x, Climb.y))
        game_surface.blit(Checked4.image, (Checked4.x, Checked4.y))
        game_surface.blit(Checked_off4.image, (Checked_off4.x, Checked_off4.y))
        game_surface.blit(Dont_Catch_On_Fire.image, (Dont_Catch_On_Fire.x, Dont_Catch_On_Fire.y))
        game_surface.blit(Checked5.image, (Checked5.x, Checked5.y))
        game_surface.blit(Checked_off5.image, (Checked_off5.x, Checked_off5.y))
        game_surface.blit(Dont_Get_Hit.image, (Dont_Get_Hit.x, Dont_Get_Hit.y))
        game_surface.blit(Checked6.image, (Checked6.x, Checked6.y))
        game_surface.blit(Checked_off6.image, (Checked_off6.x, Checked_off6.y))
        game_surface.blit(Expert.image, (Expert.x, Expert.y))
        game_surface.blit(Checked7.image, (Checked7.x, Checked7.y))
        game_surface.blit(Checked_off7.image, (Checked_off7.x, Checked_off7.y))
        game_surface.blit(Get_Hit.image, (Get_Hit.x, Get_Hit.y))
        game_surface.blit(Checked8.image, (Checked8.x, Checked8.y))
        game_surface.blit(Checked_off8.image, (Checked_off8.x, Checked_off8.y))
        game_surface.blit(Hat_Collector.image, (Hat_Collector.x, Hat_Collector.y))
        game_surface.blit(Checked9.image, (Checked9.x, Checked9.y))
        game_surface.blit(Checked_off9.image, (Checked_off9.x, Checked_off9.y))
        game_surface.blit(The_True_Cactus_Climber.image, (The_True_Cactus_Climber.x, The_True_Cactus_Climber.y))
        game_surface.blit(Checked10.image, (Checked10.x, Checked10.y))
        game_surface.blit(Checked_off10.image, (Checked_off10.x, Checked_off10.y))
        game_surface.blit(title_text, (370, 0))
        game_surface.blit(achievements_complete_text, (0, 600))
        render_to_screen()