from assets import bottom_cactus, mid_cactus, top_cactus, bg, fireball_image, bird_image, dodgemusic, firesound, birdsound, maintheme, money_image, small_font, medium_font, large_font
from assets import cowboy_hat_image, thinking_hat_image, top_hat_image, red_cap_image, party_hat_image, witch_hat_image, mexican_hat_image, king_hat_image
from resize import game_surface, window, is_fullscreen, handle_resize, toggle_fullscreen, render_to_screen
from data import data_easy, data_normal, data_hard, data_options, data_shop, data_achievements, save_data
from Player import player
from Button import button
from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, JOYAXISMOTION, joystick, time, key, transform, Rect, display, K_a, K_d, K_LEFT, K_RIGHT, image
from random import choice, randint
from vid import vid_preview
from os.path import join
from sys import exit
def game(difficulty=0):
    global data_easy, data_normal, data_hard, data_options, data_shop, data_achievements, window, is_fullscreen
    if data_options['play_music'] == True:
        maintheme.play(-1)
    fireballs_dodged = 0
    meters_up = 0
    birds_dodged = 0
    flap = False
    flap2 = True
    player1 = player(590, 300, 50, 100)
    bird1 = button(0, 720, 100, 100, bird_image)
    fireball1 = button(760, player1.y - 1000, 25, 25, fireball_image)
    bird_rac1 = button(0, 300, 740, 100, bottom_cactus)
    Money = button(1030, 600, 250, 100, money_image)
    run = True
    bgy = 0
    cactusy = -500
    clock = time.Clock()
    while run:
        clock.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                run = False
                quit()
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
                if io == 1: #right 
                    if flap2 == True:
                        data_shop['money'] += 1
                        if difficulty == 1:
                            data_easy['meters_up'] += 1
                        elif difficulty == 2:
                            data_normal['meters_up'] += 1
                        elif difficulty == 3:
                            data_hard['meters_up'] += 1
                        meters_up += 1
                        player1.img = image.load(join('Images', 'player', 'player.png')).convert_alpha()
                        player1.img = transform.scale(player1.img, (player1.width, player1.height))
                        player1.x += 150
                        if data_achievements['first_steps'] == False:
                            data_achievements['first_steps'] = True
                        save_data()
                        cactusy += 50
                        bgy += 50
                        bird1.y += 150
                        fireball1.y += 150
                        flap2 = False
                        flap = True
                elif io == -1: #left
                    if flap == True:
                        data_shop['money'] += 1
                        if difficulty == 1:
                            data_easy['meters_up'] += 1
                        elif difficulty == 2:
                            data_normal['meters_up'] += 1
                        elif difficulty == 3:
                            data_hard['meters_up'] += 1
                        meters_up += 1
                        player1.img = image.load(join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                        player1.img = transform.scale(player1.img, (player1.width, player1.height))
                        player1.x -= 150
                        save_data()
                        cactusy += 50
                        bgy += 50
                        bird1.y += 150
                        fireball1.y += 150
                        flap = False
                        flap2 = True
        Cowboy_Hat = button(player1.x, player1.y - 20, 40, 30, cowboy_hat_image)
        Thinking_Hat = button(player1.x, player1.y - 20, 40, 30, thinking_hat_image)
        Top_Hat = button(player1.x, player1.y - 20, 40, 30, top_hat_image)
        Red_Cap = button(player1.x, player1.y - 20, 40, 30, red_cap_image)
        Party_Hat = button(player1.x, player1.y - 20, 40, 30, party_hat_image)
        Witch_Hat = button(player1.x, player1.y - 20, 40, 30, witch_hat_image)
        Mexican_Hat = button(player1.x, player1.y - 20, 40, 30, mexican_hat_image)
        King_Hat = button(player1.x, player1.y - 20, 40, 30, king_hat_image)
        fireball_rect = Rect(fireball1.x, fireball1.y, fireball1.width, fireball1.height)
        bird_rect = Rect(bird1.x, bird1.y, bird1.width, bird1.height)
        bird_rac_rect = Rect(bird_rac1.x, bird_rac1.y, bird_rac1.width, bird_rac1.height)
        player_rect = Rect(player1.x, player1.y, player1.width, player1.height)
        if difficulty == 1:
            top_cactus_rect = Rect(640, cactusy - 2800, 100, 800)
        elif difficulty == 2:
            top_cactus_rect = Rect(640, cactusy - 5800, 100, 800)
        elif difficulty == 3:
            top_cactus_rect = Rect(640, cactusy - 10800, 100, 800)
        if player_rect.colliderect(fireball_rect):
            if data_achievements['catch_on_fire'] == False:
                data_achievements['catch_on_fire'] = True
            save_data()
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            return vid_preview(3)
        elif player_rect.colliderect(bird_rect):
            if data_achievements['get_hit'] == False:
                data_achievements['get_hit'] = True
            save_data()
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            return vid_preview(2)
        keys = key.get_pressed()
        if keys[K_a] and keys[K_d]:
            maintheme.stop()
            from menus import mainmenu
            mainmenu()
        elif keys[K_LEFT] and keys[K_RIGHT]:
            maintheme.stop()
            from menus import mainmenu
            mainmenu()
        elif keys[K_a] and keys[K_RIGHT]:
            maintheme.stop()
            from menus import mainmenu
            mainmenu()
        elif keys[K_LEFT] and keys[K_d]:
            maintheme.stop()
            from menus import mainmenu
            mainmenu()
        if keys[K_a] or keys[K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                if difficulty == 1:
                    data_easy['meters_up'] += 1
                elif difficulty == 2:
                    data_normal['meters_up'] += 1
                elif difficulty == 3:
                    data_hard['meters_up'] += 1
                meters_up += 1
                player1.img = image.load(join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                player1.img = transform.scale(player1.img, (player1.width, player1.height))
                player1.x -= 150
                save_data()
                cactusy += 50
                bgy += 50
                bird1.y += 150
                fireball1.y += 150
                flap = False
                flap2 = True
        elif keys[K_d] or keys[K_RIGHT]:
            if flap2 == True:
                data_shop['money'] += 1
                if difficulty == 1:
                    data_easy['meters_up'] += 1
                elif difficulty == 2:
                    data_normal['meters_up'] += 1
                elif difficulty == 3:
                    data_hard['meters_up'] += 1
                meters_up += 1
                player1.img = image.load(join('Images', 'player', 'player.png')).convert_alpha()
                player1.img = transform.scale(player1.img, (player1.width, player1.height))
                player1.x += 150
                if data_achievements['first_steps'] == False:
                    data_achievements['first_steps'] = True
                save_data()
                cactusy += 50
                bgy += 50
                bird1.y += 150
                fireball1.y += 150
                flap2 = False
                flap = True
        if difficulty != 3:
            fireball1.y += 10
        elif difficulty == 3:
            fireball1.y += 25
        if fireball1.y >= game_surface.get_height():
            fireball1.y = -1000
            fireball1.x = choice([585, 760])
            data_easy['fireballs_dodged'] += 1
            save_data()
            fireballs_dodged += 1
        if difficulty != 3:
            bird1.x += 10
        elif difficulty == 3:
            bird1.x += 25
        if bird1.x >= game_surface.get_width():
            bird1.x = -1000
            data_easy['birds_dodged'] += 1
            save_data()
            birds_dodged += 1
        elif bird1.y >= game_surface.get_height():
            bird1.x = -1000
            bird1.y = randint(300, 800)
            data_easy['birds_dodged'] += 1
            save_data()
            birds_dodged += 1
        dodge_text_red = small_font.render("dodge!", 1, (255, 0, 0))
        dodge_text = small_font.render("dodge!", 1, (255, 255, 255))
        #show dogde text when fireball above player
        if fireball1.y >= 0 and fireball1.x == 585 and player1.x == 590 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            game_surface.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.flip()
        elif fireball1.y >= 0 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            game_surface.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.flip()
        if bird_rect.colliderect(bird_rac_rect):   
            game_surface.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.flip()
            game_surface.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.flip()
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
        if bird_rac_rect.colliderect(top_cactus_rect):
            if data_achievements['climb_the_top'] == False:
                data_achievements['climb_the_top'] = True
            if difficulty == 1:
                data_shop['money'] += 50
            elif difficulty == 2:
                data_shop['money'] += 100
            elif difficulty == 3:
                data_shop['money'] += 200
            save_data()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            from win import win
            return win()
        high_score_text = medium_font.render("High Scores", 1, (255, 255, 255))
        if difficulty == 1:
            total_fireballs_dodged_text = medium_font.render(f"Total Fireballs Dodged: {data_easy['fireballs_dodged']}", 1, (255, 255, 255))
            highest_meter_text = medium_font.render(f"Total Meters Climbed: {data_easy['meters_up']}", 1, (255, 255, 255))
            total_birds_dodged_text = medium_font.render(f"Total Birds Dodged: {data_easy['birds_dodged']}", 1, (255, 255, 255))
        elif difficulty == 2:
            total_fireballs_dodged_text = medium_font.render(f"Total Fireballs Dodged: {data_normal['fireballs_dodged']}", 1, (255, 255, 255))
            highest_meter_text = medium_font.render(f"Total Meters Climbed: {data_normal['meters_up']}", 1, (255, 255, 255))
            total_birds_dodged_text = medium_font.render(f"Total Birds Dodged: {data_normal['birds_dodged']}", 1, (255, 255, 255))
        elif difficulty == 3:
            total_fireballs_dodged_text = medium_font.render(f"Total Fireballs Dodged: {data_hard['fireballs_dodged']}", 1, (255, 255, 255))
            highest_meter_text = medium_font.render(f"Total Meters Climbed: {data_hard['meters_up']}", 1, (255, 255, 255))
            total_birds_dodged_text = medium_font.render(f"Total Birds Dodged: {data_hard['birds_dodged']}", 1, (255, 255, 255))
        score_text = medium_font.render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = medium_font.render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = medium_font.render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = medium_font.render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        game_surface.fill((204, 102, 0))
        if difficulty == 1:
            game_surface.blit(top_cactus, (640, cactusy - 2000))
            game_surface.blit(mid_cactus, (640, cactusy - 1000))
            game_surface.blit(bottom_cactus, (640, cactusy))
        elif difficulty == 2:
            game_surface.blit(top_cactus, (640, cactusy - 5000))
            game_surface.blit(mid_cactus, (640, cactusy - 4000))
            game_surface.blit(mid_cactus, (640, cactusy - 3000))
            game_surface.blit(mid_cactus, (640, cactusy - 2000))
            game_surface.blit(mid_cactus, (640, cactusy - 1000))
            game_surface.blit(bottom_cactus, (640, cactusy))
        elif difficulty == 3:
            game_surface.blit(top_cactus, (640, cactusy - 10000))
            game_surface.blit(mid_cactus, (640, cactusy - 9000))
            game_surface.blit(mid_cactus, (640, cactusy - 8000))
            game_surface.blit(mid_cactus, (640, cactusy - 7000))
            game_surface.blit(mid_cactus, (640, cactusy - 6000))
            game_surface.blit(mid_cactus, (640, cactusy - 5000))
            game_surface.blit(mid_cactus, (640, cactusy - 4000))
            game_surface.blit(mid_cactus, (640, cactusy - 3000))
            game_surface.blit(mid_cactus, (640, cactusy - 2000))
            game_surface.blit(mid_cactus, (640, cactusy - 1000))
            game_surface.blit(bottom_cactus, (640, cactusy))
        game_surface.blit(bg, (0, bgy))
        game_surface.blit(score_text, (1100, 0))
        game_surface.blit(fireballs_dodged_text, (game_surface.get_width() - fireballs_dodged_text.get_width() - 10, 200))
        game_surface.blit(birds_dodged_text, (game_surface.get_width() - birds_dodged_text.get_width() - 10, 150))
        game_surface.blit(meters_text, (game_surface.get_width() - meters_text.get_width() - 10, 100))
        game_surface.blit(high_score_text, (50, 0))
        game_surface.blit(total_fireballs_dodged_text, (0, 200))
        game_surface.blit(total_birds_dodged_text, (0, 150))
        game_surface.blit(highest_meter_text, (0, 100))
        game_surface.blit(money_text, ((game_surface.get_width() - money_text.get_width() - 225), 600))
        game_surface.blit(player1.img, (player1.x, player1.y))
        if data_shop['cowboy_hat_equipped'] == True:
            if player1.x == 740:
                Cowboy_Hat.x = 755
            elif player1.x == 590:
                Cowboy_Hat.x = 585
            game_surface.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            elif player1.x == 590:
                Thinking_Hat.x = 585
            game_surface.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            elif player1.x == 590:
                Top_Hat.x = 585
            game_surface.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            elif player1.x == 590:
                Red_Cap.image = transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            game_surface.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            elif player1.x == 590:
                Party_Hat.x = 585
            game_surface.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            elif player1.x == 590:
                Witch_Hat.x = 585
            game_surface.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            elif player1.x == 590:
                Mexican_Hat.x = 585
            game_surface.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            elif player1.x == 590:
                King_Hat.x = 585
            game_surface.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        game_surface.blit(bird1.image, (bird1.x, bird1.y))
        game_surface.blit(fireball1.image, (fireball1.x, fireball1.y))
        game_surface.blit(Money.image, (Money.x, Money.y))
        render_to_screen()