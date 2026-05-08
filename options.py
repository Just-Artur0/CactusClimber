from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYBUTTONDOWN, JOYAXISMOTION, MOUSEBUTTONDOWN, Rect, joystick, time, transform
from assets import back_image, checked_off_image, checked_image, music_image, sfx_image
from assets import controller_vibration_image, select_box_image, denied_sound, equipped_sound
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, game_surface, render_to_screen, scale_mouse_pos
from data import data_options, save_data
from json import dump
from os.path import join
from sys import exit
def options():
    global data_options, window, is_fullscreen
    show_select_box = False
    move_delay = 250  # milliseconds
    last_move_time = time.get_ticks()
    move_delay2 = 250  # milliseconds
    last_move_time2 = time.get_ticks()
    Select_Box = button(760, 400, 250, 100, select_box_image)
    Back = button(0, 600, 250, 100, back_image)
    Checked_off = button(10000, 400, 250, 100, checked_off_image)
    Checked_off2 = button(10000, 300, 250, 100, checked_off_image)
    Checked_off3 = button(10000, 200, 250, 100, checked_off_image)
    Checked = button(760, 400, 250, 100, checked_image)
    Checked2 = button(760, 300, 250, 100, checked_image)
    Checked3 = button(760, 200, 250, 100, checked_image)
    Music = button(500, 400, 250, 100, music_image)
    SFX = button(500, 300, 250, 100, sfx_image)
    Controller_Vibration = button(500, 200, 250, 100, controller_vibration_image)
    if data_options['play_music'] == False: 
        Checked.image = transform.scale(checked_image, (0, 0))
        Checked.x = 10000
        Checked_off.image = transform.scale(checked_off_image, (250, 100))
        Checked_off.x = 760
    elif data_options['play_music'] == True:
        Checked.image = transform.scale(checked_image, (250, 100))
        Checked.x = 760
        Checked_off.image = transform.scale(checked_off_image, (0, 0))
        Checked_off.x = 10000
    if data_options['play_sfx'] == False:
        Checked2.image = transform.scale(checked_image, (0, 0))
        Checked2.x = 10000
        Checked_off2.image = transform.scale(checked_off_image, (250, 100))
        Checked_off2.x = 760
    elif data_options['play_sfx'] == True:
        Checked2.image = transform.scale(checked_image, (250, 100))
        Checked2.x = 760
        Checked_off2.image = transform.scale(checked_off_image, (0, 0))
        Checked_off2.x = 10000
    if data_options['controller_vibration'] == False:
        Checked3.image = transform.scale(checked_image, (0, 0))
        Checked3.x = 10000
        Checked_off3.image = transform.scale(checked_off_image, (250, 100))
        Checked_off3.x = 760
    elif data_options['controller_vibration'] == True:
        Checked3.image = transform.scale(checked_image, (250, 100))
        Checked3.x = 760
        Checked_off3.image = transform.scale(checked_off_image, (0, 0))
        Checked_off3.x = 10000
    run = True
    clockyy = time.Clock()
    while run:  
        clockyy.tick(15)
        current_time = time.get_ticks()
        current_time2 = time.get_ticks()
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
                elif joystick.Joystick(0).get_button(3):
                    show_select_box = True
                elif joystick.Joystick(0).get_button(0):
                    if Select_Box.y == Checked.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_options['play_music'] = False
                        with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                            dump(data_options, save_data_options)
                        Checked.image = transform.scale(checked_image, (0, 0))
                        Checked.x = 10000
                        Checked_off.image = transform.scale(checked_off_image, (250, 100))
                        Checked_off.x = 760
                        last_move_time = current_time
                    elif Select_Box.y == Checked_off.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_options['play_music'] = True
                        with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                            dump(data_options, save_data_options)
                        Checked.image = transform.scale(checked_image, (250, 100))
                        Checked.x = 760
                        Checked_off.image = transform.scale(checked_off_image, (0, 0))
                        Checked_off.x = 10000
                        last_move_time = current_time
                    elif Select_Box.y == Checked2.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_options['play_sfx'] = False
                        with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                            dump(data_options, save_data_options)
                        Checked2.image = transform.scale(checked_image, (0, 0))
                        Checked2.x = 10000
                        Checked_off2.image = transform.scale(checked_off_image, (250, 100))
                        Checked_off2.x = 760
                        last_move_time = current_time
                    elif Select_Box.y == Checked_off2.y and current_time - last_move_time > move_delay:
                        data_options['play_sfx'] = True
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                            dump(data_options, save_data_options)
                        Checked2.image = transform.scale(checked_image, (250, 100))
                        Checked2.x = 760
                        Checked_off2.image = transform.scale(checked_off_image, (0, 0))
                        Checked_off2.x = 10000
                        last_move_time = current_time
                    elif Select_Box.y == Checked3.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_options['controller_vibration'] = False
                        with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                            dump(data_options, save_data_options)
                        Checked3.image = transform.scale(checked_image, (0, 0))
                        Checked3.x = 10000
                        Checked_off3.image = transform.scale(checked_off_image, (250, 100))
                        Checked_off3.x = 760
                        last_move_time = current_time
                    elif Select_Box.y == Checked_off3.y and current_time - last_move_time > move_delay:
                        data_options['controller_vibration'] = True
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                            dump(data_options, save_data_options)
                        Checked3.image = transform.scale(checked_image, (250, 100))
                        Checked3.x = 760
                        Checked_off3.image = transform.scale(checked_off_image, (0, 0))
                        Checked_off3.x = 10000
                        last_move_time = current_time
            elif e.type == JOYAXISMOTION:
                io2 = round(joystick.Joystick(0).get_axis(1))
                if io2 == -1 and Select_Box.y >= 300 and current_time2 - last_move_time2 > move_delay2: #up
                    Select_Box.y -= 100
                    last_move_time2 = current_time2
                elif io2 == 1 and Select_Box.y < 400 and current_time2 - last_move_time2 > move_delay2: #down
                    Select_Box.y += 100
                    last_move_time2 = current_time2
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = scale_mouse_pos(*e.pos)
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                checked_off_rect = Rect(Checked_off.x, Checked_off.y, Checked_off.width, Checked_off.height)
                checked_rect = Rect(Checked.x, Checked.y, Checked.width, Checked.height)
                checked_off2_rect = Rect(Checked_off2.x, Checked_off2.y, Checked_off2.width, Checked_off2.height)
                checked2_rect = Rect(Checked2.x, Checked2.y, Checked2.width, Checked2.height)
                checked_off3_rect = Rect(Checked_off3.x, Checked_off3.y, Checked_off3.width, Checked_off3.height)
                checked3_rect = Rect(Checked3.x, Checked3.y, Checked3.width, Checked3.height)
                if back_rect.collidepoint(mousex, mousey):
                    from menus import start
                    return start()
                elif checked_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_options['play_music'] = False
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Checked.image = transform.scale(checked_image, (0, 0))
                    Checked.x = 10000
                    Checked_off.image = transform.scale(checked_off_image, (250, 100))
                    Checked_off.x = 760
                elif checked_off_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_options['play_music'] = True
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Checked.image = transform.scale(checked_image, (250, 100))
                    Checked.x = 760
                    Checked_off.image = transform.scale(checked_off_image, (0, 0))
                    Checked_off.x = 10000
                elif checked2_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_options['play_sfx'] = False
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Checked2.image = transform.scale(checked_image, (0, 0))
                    Checked2.x = 10000
                    Checked_off2.image = transform.scale(checked_off_image, (250, 100))
                    Checked_off2.x = 760
                elif checked_off2_rect.collidepoint(mousex, mousey):
                    data_options['play_sfx'] = True
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Checked2.image = transform.scale(checked_image, (250, 100))
                    Checked2.x = 760
                    Checked_off2.image = transform.scale(checked_off_image, (0, 0))
                    Checked_off2.x = 10000
                elif checked3_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_options['controller_vibration'] = False
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Checked3.image = transform.scale(checked_image, (0, 0))
                    Checked3.x = 10000
                    Checked_off3.image = transform.scale(checked_off_image, (250, 100))
                    Checked_off3.x = 760
                elif checked_off3_rect.collidepoint(mousex, mousey):
                    data_options['controller_vibration'] = True
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
                        dump(data_options, save_data_options)
                    Checked3.image = transform.scale(checked_image, (250, 100))
                    Checked3.x = 760
                    Checked_off3.image = transform.scale(checked_off_image, (0, 0))
                    Checked_off3.x = 10000
        game_surface.fill((204, 102, 25))
        game_surface.blit(Back.image, (Back.x, Back.y))
        game_surface.blit(Music.image, (Music.x, Music.y))
        game_surface.blit(SFX.image, (SFX.x, SFX.y))
        game_surface.blit(Controller_Vibration.image, (Controller_Vibration.x, Controller_Vibration.y))
        game_surface.blit(Checked.image, (Checked.x, Checked.y))
        game_surface.blit(Checked_off.image, (Checked_off.x, Checked_off.y))
        game_surface.blit(Checked2.image, (Checked2.x, Checked2.y))
        game_surface.blit(Checked_off2.image, (Checked_off2.x, Checked_off2.y))
        game_surface.blit(Checked3.image, (Checked3.x, Checked3.y))
        game_surface.blit(Checked_off3.image, (Checked_off3.x, Checked_off3.y))
        if show_select_box == True:
            game_surface.blit(Select_Box.image, (Select_Box.x, Select_Box.y))
        render_to_screen()