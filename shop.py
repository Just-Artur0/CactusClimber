from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYBUTTONDOWN, JOYAXISMOTION, MOUSEBUTTONDOWN, Rect, joystick, time, transform
from assets import back_image, cowboy_hat_image, thinking_hat_image, top_hat_image, red_cap_image, party_hat_image, witch_hat_image, mexican_hat_image, king_hat_image, money_image, equip_image
from assets import unequip_image, buy_image, select_box_image, denied_sound, buy_sound, equipped_sound, medium_font, large_font
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, game_surface, render_to_screen, scale_mouse_pos
from data import data_shop, data_options, save_data
from json import dump
from os.path import join
from sys import exit
def shop():
    global data_shop, data_options, window, is_fullscreen
    play_denied = True
    play_denied2 = True
    play_denied3 = True
    play_denied4 = True
    play_denied5 = True
    play_denied6 = True
    play_denied7 = True
    play_denied8 = True
    show_select_box = False
    move_delay = 150  # milliseconds
    last_move_time = time.get_ticks()
    Back = button(0, 600, 250, 100, back_image)
    Select_Box = button(50, 200, 100, 50, select_box_image)
    Cowboy_Hat = button(50, 150, 100, 50, cowboy_hat_image)
    Thinking_Hat = button(350, 150, 100, 50, thinking_hat_image)
    Top_Hat = button(650, 150, 100, 50, top_hat_image)
    Red_Cap = button(950, 150, 100, 50, red_cap_image)
    Party_Hat = button(50, 300, 100, 50, party_hat_image)
    Witch_Hat = button(350, 300, 100, 50, witch_hat_image)
    Mexican_Hat = button(650, 300, 100, 50, mexican_hat_image)
    King_Hat = button(950, 300, 100, 50, king_hat_image)
    Money = button(0, 0, 250, 100, money_image)
    Equip = button(10000, 200, 100, 50, equip_image)
    Equip2 = button(10000, 200, 100, 50, equip_image)
    Equip3 = button(10000, 200, 100, 50, equip_image)
    Equip4 = button(10000, 200, 100, 50, equip_image)
    Equip5 = button(10000, 350, 100, 50, equip_image)
    Equip6 = button(10000, 350, 100, 50, equip_image)
    Equip7 = button(10000, 350, 100, 50, equip_image)
    Equip8 = button(10000, 350, 100, 50, equip_image)
    Unequip = button(10000, 200, 100, 50, unequip_image)
    Unequip2 = button(10000, 200, 100, 50, unequip_image)
    Unequip3 = button(10000, 200, 100, 50, unequip_image)
    Unequip4 = button(10000, 200, 100, 50, unequip_image)
    Unequip5 = button(10000, 350, 100, 50, unequip_image)
    Unequip6 = button(10000, 350, 100, 50, unequip_image)
    Unequip7 = button(10000, 350, 100, 50, unequip_image)
    Unequip8 = button(10000, 350, 100, 50, unequip_image)
    Buy = button(50, 200, 100, 50, buy_image)
    Buy2 = button(350, 200, 100, 50, buy_image)
    Buy3 = button(650, 200, 100, 50, buy_image)
    Buy4 = button(950, 200, 100, 50, buy_image)
    Buy5 = button(50, 350, 100, 50, buy_image)
    Buy6 = button(350, 350, 100, 50, buy_image)
    Buy7 = button(650, 350, 100, 50, buy_image)
    Buy8 = button(950, 350, 100, 50, buy_image)
    if data_shop['cowboy_hat_unlocked'] == True:
        Buy.image = transform.scale(buy_image, (0, 0))
        Buy.x = 10000
        Equip.image = transform.scale(equip_image, (100, 50))
        Equip.x = 50
    if data_shop['thinking_hat_unlocked'] == True:
        Buy2.image = transform.scale(buy_image, (0, 0))
        Buy2.x = 10000
        Equip2.image = transform.scale(equip_image, (100, 50))
        Equip2.x = 350
    if data_shop['top_hat_unlocked'] == True:
        Buy3.image = transform.scale(buy_image, (0, 0))
        Buy3.x = 10000
        Equip3.image = transform.scale(equip_image, (100, 50))
        Equip3.x = 650
    if data_shop['red_cap_unlocked'] == True:
        Buy4.image = transform.scale(buy_image, (0, 0))
        Buy4.x = 10000
        Equip4.image = transform.scale(equip_image, (100, 50))
        Equip4.x = 950
    if data_shop['party_hat_unlocked'] == True:
        Buy5.image = transform.scale(buy_image, (0, 0))
        Buy5.x = 10000
        Equip5.image = transform.scale(equip_image, (100, 50))
        Equip5.x = 50
    if data_shop['witch_hat_unlocked'] == True:
        Buy6.image = transform.scale(buy_image, (0, 0))
        Buy6.x = 10000
        Equip6.image = transform.scale(equip_image, (100, 50))
        Equip6.x = 350
    if data_shop['mexican_hat_unlocked'] == True:
        Buy7.image = transform.scale(buy_image, (0, 0))
        Buy7.x = 10000
        Equip7.image = transform.scale(equip_image, (100, 50))
        Equip7.x = 650
    if data_shop['king_hat_unlocked'] == True:
        Buy8.image = transform.scale(buy_image, (0, 0))
        Buy8.x = 10000
        Equip8.image = transform.scale(equip_image, (100, 50))
        Equip8.x = 950
    if data_shop['cowboy_hat_equipped'] == True:
        Equip.image = transform.scale(equip_image, (0, 0))
        Equip.x = 10000
        Unequip.image = transform.scale(unequip_image, (100, 50))
        Unequip.x = 50
    if data_shop['thinking_hat_equipped'] == True:
        Equip2.image = transform.scale(equip_image, (0, 0))
        Equip2.x = 10000
        Unequip2.image = transform.scale(unequip_image, (100, 50))
        Unequip2.x = 350
    if data_shop['top_hat_equipped'] == True:
        Equip3.image = transform.scale(equip_image, (0, 0))
        Equip3.x = 10000
        Unequip3.image = transform.scale(unequip_image, (100, 50))
        Unequip3.x = 650
    if data_shop['red_cap_equipped'] == True:
        Equip4.image = transform.scale(equip_image, (0, 0))
        Equip4.x = 10000
        Unequip4.image = transform.scale(unequip_image, (100, 50))
        Unequip4.x = 950
    if data_shop['party_hat_equipped'] == True:
        Equip5.image = transform.scale(equip_image, (0, 0))
        Equip5.x = 10000
        Unequip5.image = transform.scale(unequip_image, (100, 50))
        Unequip5.x = 50
    if data_shop['witch_hat_equipped'] == True:
        Equip6.image = transform.scale(equip_image, (0, 0))
        Equip6.x = 10000
        Unequip6.image = transform.scale(unequip_image, (100, 50))
        Unequip6.x = 350
    if data_shop['mexican_hat_equipped'] == True:
        Equip7.image = transform.scale(equip_image, (0, 0))
        Equip7.x = 10000
        Unequip7.image = transform.scale(unequip_image, (100, 50))
        Unequip7.x = 650
    if data_shop['king_hat_equipped'] == True:
        Equip8.image = transform.scale(equip_image, (0, 0))
        Equip8.x = 10000
        Unequip8.image = transform.scale(unequip_image, (100, 50))
        Unequip8.x = 950
    run = True
    clockyy = time.Clock()
    while run:  
        clockyy.tick(15)
        current_time = time.get_ticks()
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
                #press triangle to show select box
                elif joystick.Joystick(0).get_button(3):
                    show_select_box = True
                elif joystick.Joystick(0).get_button(0):
                    if Select_Box.x == Buy.x and Select_Box.y == Buy.y and data_shop['money'] >= 100 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 100
                        data_shop['show_cost'] = False
                        data_shop['cowboy_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy.image = transform.scale(buy_image, (0, 0))
                        Buy.x = 10000
                        Equip.image = transform.scale(equip_image, (100, 50))
                        Equip.x = 50
                        play_denied = False
                        last_move_time = current_time
                    elif Select_Box.x == Buy2.x and Select_Box.y == Buy2.y and data_shop['money'] >= 250 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 250
                        data_shop['show_cost2'] = False
                        data_shop['thinking_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy2.image = transform.scale(buy_image, (0, 0))
                        Buy2.x = 10000
                        Equip2.image = transform.scale(equip_image, (100, 50))
                        Equip2.x = 350
                        play_denied2 = False
                        last_move_time = current_time
                    elif Select_Box.x == Buy3.x and Select_Box.y == Buy3.y and data_shop['money'] >= 500 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 500
                        data_shop['show_cost3'] = False
                        data_shop['top_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy3.image = transform.scale(buy_image, (0, 0))
                        Buy3.x = 10000
                        Equip3.image = transform.scale(equip_image, (100, 50))
                        Equip3.x = 650
                        play_denied3 = False
                        last_move_time = current_time
                    elif Select_Box.x == Buy4.x and Select_Box.y == Buy4.y and data_shop['money'] >= 1000 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 1000
                        data_shop['show_cost4'] = False
                        data_shop['red_cap_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy4.image = transform.scale(buy_image, (0, 0))
                        Buy4.x = 10000
                        Equip4.image = transform.scale(equip_image, (100, 50))
                        Equip4.x = 950
                        play_denied4 = False
                        last_move_time = current_time                        
                    elif Select_Box.x == Buy5.x and Select_Box.y == Buy5.y and data_shop['money'] >= 100 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 100
                        data_shop['show_cost5'] = False
                        data_shop['party_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy5.image = transform.scale(buy_image, (0, 0))
                        Buy5.x = 10000
                        Equip5.image = transform.scale(equip_image, (100, 50))
                        Equip5.x = 50
                        play_denied5 = False
                        last_move_time = current_time
                    elif Select_Box.x == Buy6.x and Select_Box.y == Buy6.y and data_shop['money'] >= 500 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 500
                        data_shop['show_cost7'] = False
                        data_shop['witch_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy6.image = transform.scale(buy_image, (0, 0))
                        Buy6.x = 10000
                        Equip6.image = transform.scale(equip_image, (100, 50))
                        Equip6.x = 350
                        play_denied6 = False
                        last_move_time = current_time
                    elif Select_Box.x == Buy7.x and Select_Box.y == Buy7.y and data_shop['money'] >= 250 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 250
                        data_shop['show_cost6'] = False
                        data_shop['mexican_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy7.image = transform.scale(buy_image, (0, 0))
                        Buy7.x = 10000
                        Equip7.image = transform.scale(equip_image, (100, 50))
                        Equip7.x = 650
                        play_denied7 = False
                        last_move_time = current_time
                    elif Select_Box.x == Buy8.x and Select_Box.y == Buy8.y and data_shop['money'] >= 2000 and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            buy_sound.play()
                        data_shop['money'] -= 2000
                        data_shop['show_cost8'] = False
                        data_shop['king_hat_unlocked'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Buy8.image = transform.scale(buy_image, (0, 0))
                        Buy8.x = 10000
                        Equip8.image = transform.scale(equip_image, (100, 50))
                        Equip8.x = 950
                        play_denied8 = False
                        last_move_time = current_time
                    elif Select_Box.x == Equip.x and Select_Box.y == Equip.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['cowboy_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip.image = transform.scale(equip_image, (0, 0))
                        Equip.x = 10000
                        Unequip.image = transform.scale(unequip_image, (100, 50))
                        Unequip.x = 50
                        last_move_time = current_time
                    elif Select_Box.x == Equip2.x and Select_Box.y == Equip2.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['thinking_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip2.image = transform.scale(equip_image, (0, 0))
                        Equip2.x = 10000
                        Unequip2.image = transform.scale(unequip_image, (100, 50))
                        Unequip2.x = 350
                        last_move_time = current_time
                    elif Select_Box.x == Equip3.x and Select_Box.y == Equip3.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['top_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip3.image = transform.scale(equip_image, (0, 0))
                        Equip3.x = 10000
                        Unequip3.image = transform.scale(unequip_image, (100, 50))
                        Unequip3.x = 650
                        last_move_time = current_time
                    elif Select_Box.x == Equip4.x and Select_Box.y == Equip4.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['red_cap_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip4.image = transform.scale(equip_image, (0, 0))
                        Equip4.x = 10000
                        Unequip4.image = transform.scale(unequip_image, (100, 50))
                        Unequip4.x = 950
                        last_move_time = current_time
                    elif Select_Box.x == Equip5.x and Select_Box.y == Equip5.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['party_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip5.image = transform.scale(equip_image, (0, 0))
                        Equip5.x = 10000
                        Unequip5.image = transform.scale(unequip_image, (100, 50))
                        Unequip5.x = 50 
                        last_move_time = current_time
                    elif Select_Box.x == Equip6.x and Select_Box.y == Equip6.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['witch_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip6.image = transform.scale(equip_image, (0, 0))
                        Equip6.x = 10000
                        Unequip6.image = transform.scale(unequip_image, (100, 50))
                        Unequip6.x = 350
                        last_move_time = current_time
                    elif Select_Box.x == Equip7.x and Select_Box.y == Equip7.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['mexican_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip7.image = transform.scale(equip_image, (0, 0))
                        Equip7.x = 10000
                        Unequip7.image = transform.scale(unequip_image, (100, 50))
                        Unequip7.x = 650
                        last_move_time = current_time
                    elif Select_Box.x == Equip8.x and Select_Box.y == Equip8.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            equipped_sound.play()
                        data_shop['king_hat_equipped'] = True
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip8.image = transform.scale(equip_image, (0, 0))
                        Equip8.x = 10000
                        Unequip8.image = transform.scale(unequip_image, (100, 50))
                        Unequip8.x = 950
                        last_move_time = current_time
                    elif Select_Box.x == Unequip.x and Select_Box.y == Unequip.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['cowboy_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip.image = transform.scale(equip_image, (100, 50))
                        Equip.x = 50
                        Unequip.image = transform.scale(unequip_image, (0, 0))
                        Unequip.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip2.x and Select_Box.y == Unequip2.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['thinking_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip2.image = transform.scale(equip_image, (100, 50))
                        Equip2.x = 350
                        Unequip2.image = transform.scale(unequip_image, (0, 0))
                        Unequip2.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip3.x and Select_Box.y == Unequip3.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['top_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip3.image = transform.scale(equip_image, (100, 50))
                        Equip3.x = 650
                        Unequip3.image = transform.scale(unequip_image, (0, 0))
                        Unequip3.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip4.x and Select_Box.y == Unequip4.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['red_cap_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip4.image = transform.scale(equip_image, (100, 50))
                        Equip4.x = 950
                        Unequip4.image = transform.scale(unequip_image, (0, 0))
                        Unequip4.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip5.x and Select_Box.y == Unequip5.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['party_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip5.image = transform.scale(equip_image, (100, 50))
                        Equip5.x = 50
                        Unequip5.image = transform.scale(unequip_image, (0, 0))
                        Unequip5.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip6.x and Select_Box.y == Unequip6.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['witch_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip6.image = transform.scale(equip_image, (100, 50))
                        Equip6.x = 350
                        Unequip6.image = transform.scale(unequip_image, (0, 0))
                        Unequip6.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip7.x and Select_Box.y == Unequip7.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['mexican_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip7.image = transform.scale(equip_image, (100, 50))
                        Equip7.x = 650
                        Unequip7.image = transform.scale(unequip_image, (0, 0))
                        Unequip7.x = 10000
                        last_move_time = current_time
                    elif Select_Box.x == Unequip8.x and Select_Box.y == Unequip8.y and current_time - last_move_time > move_delay:
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        data_shop['king_hat_equipped'] = False
                        with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            dump(data_shop, save_data_shop)
                        Equip8.image = transform.scale(equip_image, (100, 50))
                        Equip8.x = 950
                        Unequip8.image = transform.scale(unequip_image, (0, 0))
                        Unequip8.x = 10000
                        last_move_time = current_time
            #moving the select box
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                io2 = round(joystick.Joystick(0).get_axis(1))
                if io == 1 and Select_Box.x < 900 and current_time - last_move_time > move_delay: #right
                    Select_Box.x += 300
                    last_move_time = current_time
                elif io == -1 and Select_Box.x > 50 and current_time - last_move_time > move_delay: #left
                    Select_Box.x -= 300
                    last_move_time = current_time
                elif io2 == -1 and Select_Box.y >= 350 and current_time - last_move_time > move_delay: #up
                    Select_Box.y -= 150
                    last_move_time = current_time
                elif io2 == 1 and Select_Box.y < 350 and current_time - last_move_time > move_delay: #down
                    Select_Box.y += 150
                    last_move_time = current_time
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = scale_mouse_pos(*e.pos)
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                equip_rect = Rect(Equip.x, Equip.y, Equip.width, Equip.height)
                unequip_rect = Rect(Unequip.x, Unequip.y, Unequip.width, Unequip.height)
                equip2_rect = Rect(Equip2.x, Equip2.y, Equip2.width, Equip2.height)
                unequip2_rect = Rect(Unequip2.x, Unequip2.y, Unequip2.width, Unequip2.height)
                equip3_rect = Rect(Equip3.x, Equip3.y, Equip3.width, Equip3.height)
                unequip3_rect = Rect(Unequip3.x, Unequip3.y, Unequip3.width, Unequip3.height)
                equip4_rect = Rect(Equip4.x, Equip4.y, Equip4.width, Equip4.height)
                unequip4_rect = Rect(Unequip4.x, Unequip4.y, Unequip4.width, Unequip4.height)
                equip5_rect = Rect(Equip5.x, Equip5.y, Equip5.width, Equip5.height)
                unequip5_rect = Rect(Unequip5.x, Unequip5.y, Unequip5.width, Unequip5.height)
                equip6_rect = Rect(Equip6.x, Equip6.y, Equip6.width, Equip6.height)
                unequip6_rect = Rect(Unequip6.x, Unequip6.y, Unequip6.width, Unequip6.height)
                equip7_rect = Rect(Equip7.x, Equip7.y, Equip7.width, Equip7.height)
                unequip7_rect = Rect(Unequip7.x, Unequip7.y, Unequip7.width, Unequip7.height)
                equip8_rect = Rect(Equip8.x, Equip8.y, Equip8.width, Equip8.height)
                unequip8_rect = Rect(Unequip8.x, Unequip8.y, Unequip8.width, Unequip8.height)
                buy_rect = Rect(Buy.x, Buy.y, Buy.width, Buy.height)
                buy2_rect = Rect(Buy2.x, Buy2.y, Buy2.width, Buy2.height)
                buy3_rect = Rect(Buy3.x, Buy3.y, Buy3.width, Buy3.height)
                buy4_rect = Rect(Buy4.x, Buy4.y, Buy4.width, Buy4.height)
                buy5_rect = Rect(Buy5.x, Buy5.y, Buy5.width, Buy5.height)
                buy6_rect = Rect(Buy6.x, Buy6.y, Buy6.width, Buy6.height)
                buy7_rect = Rect(Buy7.x, Buy7.y, Buy7.width, Buy7.height)
                buy8_rect = Rect(Buy8.x, Buy8.y, Buy8.width, Buy8.height)
                if back_rect.collidepoint(mousex, mousey):
                    from menus import start
                    return start()
                elif buy_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 100:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 100
                    data_shop['show_cost'] = False
                    data_shop['cowboy_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy.image = transform.scale(buy_image, (0, 0))
                    Buy.x = 10000
                    Equip.image = transform.scale(equip_image, (100, 50))
                    Equip.x = 50
                    play_denied = False
                elif buy_rect.collidepoint(mousex, mousey) and data_shop['money'] < 100 and play_denied == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif buy2_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 250:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 250
                    data_shop['show_cost2'] = False
                    data_shop['thinking_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy2.image = transform.scale(buy_image, (0, 0))
                    Buy2.x = 10000
                    Equip2.image = transform.scale(equip_image, (100, 50))
                    Equip2.x = 350
                    play_denied2 = False
                elif buy2_rect.collidepoint(mousex, mousey) and data_shop['money'] < 250 and play_denied2 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif buy3_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 500:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 500
                    data_shop['show_cost3'] = False
                    data_shop['top_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy3.image = transform.scale(buy_image, (0, 0))
                    Buy3.x = 10000
                    Equip3.image = transform.scale(equip_image, (100, 50))
                    Equip3.x = 650
                    play_denied3 = False
                elif buy3_rect.collidepoint(mousex, mousey) and data_shop['money'] < 500 and play_denied3 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif buy4_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 1000:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 1000
                    data_shop['show_cost4'] = False
                    data_shop['red_cap_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy4.image = transform.scale(buy_image, (0, 0))
                    Buy4.x = 10000
                    Equip4.image = transform.scale(equip_image, (100, 50))
                    Equip4.x = 950
                    play_denied4 = False
                elif buy4_rect.collidepoint(mousex, mousey) and data_shop['money'] < 1000 and play_denied4 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif equip_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['cowboy_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip.image = transform.scale(equip_image, (0, 0))
                    Equip.x = 10000
                    Unequip.image = transform.scale(unequip_image, (100, 50))
                    Unequip.x = 50 
                elif unequip_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['cowboy_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip.image = transform.scale(equip_image, (100, 50))
                    Equip.x = 50
                    Unequip.image = transform.scale(unequip_image, (0, 0))
                    Unequip.x = 10000
                elif equip2_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['thinking_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip2.image = transform.scale(equip_image, (0, 0))
                    Equip2.x = 10000
                    Unequip2.image = transform.scale(unequip_image, (100, 50))
                    Unequip2.x = 350
                elif unequip2_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['thinking_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip2.image = transform.scale(equip_image, (100, 50))
                    Equip2.x = 350
                    Unequip2.image = transform.scale(unequip_image, (0, 0))
                    Unequip2.x = 10000
                elif equip3_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['top_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip3.image = transform.scale(equip_image, (0, 0))
                    Equip3.x = 10000
                    Unequip3.image = transform.scale(unequip_image, (100, 50))
                    Unequip3.x = 650
                elif unequip3_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['top_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip3.image = transform.scale(equip_image, (100, 50))
                    Equip3.x = 650
                    Unequip3.image = transform.scale(unequip_image, (0, 0))
                    Unequip3.x = 10000
                elif equip4_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['red_cap_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip4.image = transform.scale(equip_image, (0, 0))
                    Equip4.x = 10000
                    Unequip4.image = transform.scale(unequip_image, (100, 50))
                    Unequip4.x = 950
                elif unequip4_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['red_cap_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip4.image = transform.scale(equip_image, (100, 50))
                    Equip4.x = 950
                    Unequip4.image = transform.scale(unequip_image, (0, 0))
                    Unequip4.x = 10000
                elif buy5_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 100:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 100
                    data_shop['show_cost5'] = False
                    data_shop['party_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy5.image = transform.scale(buy_image, (0, 0))
                    Buy5.x = 10000
                    Equip5.image = transform.scale(equip_image, (100, 50))
                    Equip5.x = 50
                    play_denied5 = False
                elif buy5_rect.collidepoint(mousex, mousey) and data_shop['money'] < 100 and play_denied5 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif buy6_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 500:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 500
                    data_shop['show_cost7'] = False
                    data_shop['witch_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy6.image = transform.scale(buy_image, (0, 0))
                    Buy6.x = 10000
                    Equip6.image = transform.scale(equip_image, (100, 50))
                    Equip6.x = 350
                    play_denied6 = False
                elif buy6_rect.collidepoint(mousex, mousey) and data_shop['money'] < 500 and play_denied6 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif buy7_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 250:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 250
                    data_shop['show_cost6'] = False
                    data_shop['mexican_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy7.image = transform.scale(buy_image, (0, 0))
                    Buy7.x = 10000
                    Equip7.image = transform.scale(equip_image, (100, 50))
                    Equip7.x = 650
                    play_denied7 = False
                elif buy7_rect.collidepoint(mousex, mousey) and data_shop['money'] < 250 and play_denied7 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif buy8_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 2000:
                    if data_options['play_sfx'] == True:
                        buy_sound.play()
                    data_shop['money'] -= 2000
                    data_shop['show_cost8'] = False
                    data_shop['king_hat_unlocked'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Buy8.image = transform.scale(buy_image, (0, 0))
                    Buy8.x = 10000
                    Equip8.image = transform.scale(equip_image, (100, 50))
                    Equip8.x = 950
                    play_denied8 = False
                elif buy8_rect.collidepoint(mousex, mousey) and data_shop['money'] < 2000 and play_denied8 == True:
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                elif equip5_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['party_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip5.image = transform.scale(equip_image, (0, 0))
                    Equip5.x = 10000
                    Unequip5.image = transform.scale(unequip_image, (100, 50))
                    Unequip5.x = 50 
                elif unequip5_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['party_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip5.image = transform.scale(equip_image, (100, 50))
                    Equip5.x = 50
                    Unequip5.image = transform.scale(unequip_image, (0, 0))
                    Unequip5.x = 10000
                elif equip6_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['witch_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip6.image = transform.scale(equip_image, (0, 0))
                    Equip6.x = 10000
                    Unequip6.image = transform.scale(unequip_image, (100, 50))
                    Unequip6.x = 350
                elif unequip6_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['witch_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip6.image = transform.scale(equip_image, (100, 50))
                    Equip6.x = 350
                    Unequip6.image = transform.scale(unequip_image, (0, 0))
                    Unequip6.x = 10000
                elif equip7_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['mexican_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip7.image = transform.scale(equip_image, (0, 0))
                    Equip7.x = 10000
                    Unequip7.image = transform.scale(unequip_image, (100, 50))
                    Unequip7.x = 650
                elif unequip7_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['mexican_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip7.image = transform.scale(equip_image, (100, 50))
                    Equip7.x = 650
                    Unequip7.image = transform.scale(unequip_image, (0, 0))
                    Unequip7.x = 10000
                elif equip8_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        equipped_sound.play()
                    data_shop['king_hat_equipped'] = True
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip8.image = transform.scale(equip_image, (0, 0))
                    Equip8.x = 10000
                    Unequip8.image = transform.scale(unequip_image, (100, 50))
                    Unequip8.x = 950
                elif unequip8_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        denied_sound.play()
                    data_shop['king_hat_equipped'] = False
                    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        dump(data_shop, save_data_shop)
                    Equip8.image = transform.scale(equip_image, (100, 50))
                    Equip8.x = 950
                    Unequip8.image = transform.scale(unequip_image, (0, 0))
                    Unequip8.x = 10000
        cost_text = medium_font.render("100", 1, (64, 255, 25))
        cost2_text = medium_font.render("250", 1, (64, 255, 25))
        cost3_text = medium_font.render("500", 1, (64, 255, 25))
        cost4_text = medium_font.render("1000", 1, (64, 255, 25))
        cost5_text = medium_font.render("100", 1, (64, 255, 25))
        cost6_text = medium_font.render("250", 1, (64, 255, 25))
        cost7_text = medium_font.render("500", 1, (64, 255, 25))
        cost8_text = medium_font.render("2000", 1, (64, 255, 25))
        money_text = large_font.render(f": {data_shop['money']}", 1, (64, 255, 25))
        game_surface.fill((204, 102, 25))
        game_surface.blit(money_text, (250, 0))
        if data_shop['show_cost'] == True:
            game_surface.blit(cost_text, (60, 250))
        if data_shop['show_cost2'] == True:
            game_surface.blit(cost2_text, (360, 250))
        if data_shop['show_cost3'] == True:
            game_surface.blit(cost3_text, (660, 250))
        if data_shop['show_cost4'] == True:
            game_surface.blit(cost4_text, (950, 250))
        if data_shop['show_cost5'] == True:
            game_surface.blit(cost5_text, (60, 400))
        if data_shop['show_cost6'] == True:
            game_surface.blit(cost6_text, (660, 400))
        if data_shop['show_cost7'] == True:
            game_surface.blit(cost7_text, (360, 400))
        if data_shop['show_cost8'] == True:
            game_surface.blit(cost8_text, (950, 400))
        game_surface.blit(Back.image, (Back.x, Back.y))
        game_surface.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        game_surface.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        game_surface.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        game_surface.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        game_surface.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        game_surface.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        game_surface.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        game_surface.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        game_surface.blit(Money.image, (Money.x, Money.y))
        game_surface.blit(Buy.image, (Buy.x, Buy.y))
        game_surface.blit(Buy2.image, (Buy2.x, Buy2.y))
        game_surface.blit(Buy3.image, (Buy3.x, Buy3.y))
        game_surface.blit(Buy4.image, (Buy4.x, Buy4.y))
        game_surface.blit(Buy5.image, (Buy5.x, Buy5.y))
        game_surface.blit(Buy6.image, (Buy6.x, Buy6.y))
        game_surface.blit(Buy7.image, (Buy7.x, Buy7.y))
        game_surface.blit(Buy8.image, (Buy8.x, Buy8.y))
        game_surface.blit(Equip.image, (Equip.x, Equip.y))
        game_surface.blit(Equip2.image, (Equip2.x, Equip2.y))
        game_surface.blit(Equip3.image, (Equip3.x, Equip3.y))
        game_surface.blit(Equip4.image, (Equip4.x, Equip4.y))
        game_surface.blit(Equip5.image, (Equip5.x, Equip5.y))
        game_surface.blit(Equip6.image, (Equip6.x, Equip6.y))
        game_surface.blit(Equip7.image, (Equip7.x, Equip7.y))
        game_surface.blit(Equip8.image, (Equip8.x, Equip8.y))
        game_surface.blit(Unequip.image, (Unequip.x, Unequip.y))
        game_surface.blit(Unequip2.image, (Unequip2.x, Unequip2.y))
        game_surface.blit(Unequip3.image, (Unequip3.x, Unequip3.y))
        game_surface.blit(Unequip4.image, (Unequip4.x, Unequip4.y))
        game_surface.blit(Unequip5.image, (Unequip5.x, Unequip5.y))
        game_surface.blit(Unequip6.image, (Unequip6.x, Unequip6.y))
        game_surface.blit(Unequip7.image, (Unequip7.x, Unequip7.y))
        game_surface.blit(Unequip8.image, (Unequip8.x, Unequip8.y))
        if show_select_box == True:
            game_surface.blit(Select_Box.image, (Select_Box.x, Select_Box.y))
        render_to_screen()