from moviepy.editor import VideoFileClip
from pygame import display, transform, image, font, mixer, joystick, time, mouse, event, quit, Rect, key
from pygame.locals import QUIT, JOYAXISMOTION, JOYBUTTONDOWN, MOUSEBUTTONDOWN, K_a, K_d, K_LEFT, K_RIGHT
from Player import player
from Button import button
from random import choice, randint
from json import dump, load
from os.path import join
font.init()
mixer.init()
joystick.init()
large_font = font.SysFont('comicsans', 80)
medium_font = font.SysFont('comicsans', 40)
small_font = font.SysFont('comicsans', 20)
screen_width = 1280
screen_height = 720
window = display.set_mode((screen_width, screen_height))
display.set_caption("Cactus Climber")
joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]
bottom_cactus = image.load(join('Images', 'cactus', 'bottom_cactus.png')).convert()
bottom_cactus = transform.scale(bottom_cactus, (100, 1000))
mid_cactus = image.load(join('Images', 'cactus', 'mid_cactus.png')).convert()
mid_cactus = transform.scale(mid_cactus, (100, 1000))
display.set_icon(mid_cactus)
top_cactus = image.load(join('Images', 'cactus', 'top_cactus.png')).convert()
top_cactus = transform.scale(top_cactus, (100, 1000))
easy_image = image.load(join('Images', 'difficulty', 'easy.png')).convert()
normal_image = image.load(join('Images', 'difficulty', 'normal.png')).convert()
hard_image = image.load(join('Images', 'difficulty', 'hard.png')).convert()
show_stats_image = image.load(join('Images', 'difficulty', 'show_stats.png')).convert()
hide_stats_image = image.load(join('Images', 'difficulty', 'hide_stats.png')).convert()
begin_player = image.load(join('Images', 'player', 'begin_player.png')).convert_alpha()
begin_player = transform.scale(begin_player, (100, 200))
fireball_image = image.load(join('Images', 'obstacles', 'fireball.png')).convert_alpha()
bird_image = image.load(join('Images', 'obstacles', 'bird.png')).convert_alpha()
back_image = image.load(join('Images', 'ui', 'back.png')).convert()
checked_off_image = image.load(join('Images', 'ui', 'checked_off.png')).convert()
checked_image = image.load(join('Images', 'ui', 'checked.png')).convert()
credits_image = image.load(join('Images', 'ui', 'credits.png')).convert()
music_image = image.load(join('Images', 'ui', 'music.png')).convert()
options_image = image.load(join('Images', 'ui', 'options.png')).convert()
play_image = image.load(join('Images', 'ui', 'play.png')).convert()
quit_image = image.load(join('Images', 'ui', 'quit.png')).convert()
sfx_image = image.load(join('Images', 'ui', 'sfx.png')).convert()
controller_vibration_image = image.load(join('Images', 'ui', 'controller_vibration.png')).convert()
shop_image = image.load(join('Images', 'ui', 'shop.png')).convert()
reset_image = image.load(join('Images', 'ui', 'reset.png')).convert()
achievements_image = image.load(join('Images', 'ui', 'achievements.png')).convert()
first_steps_image = image.load(join('Images', 'achievements', 'first_steps.png')).convert()
climb_the_top_image = image.load(join('Images', 'achievements', 'climb_the_top.png')).convert()
cactus_climber_image = image.load(join('Images', 'achievements', 'cactus_climber.png')).convert()
catch_on_fire_image = image.load(join('Images', 'achievements', 'catch_on_fire.png')).convert()
climb_image = image.load(join('Images', 'achievements', 'climb.png')).convert()
dont_catch_on_fire_image = image.load(join('Images', 'achievements', 'dont_catch_on_fire.png')).convert()
dont_get_hit_image = image.load(join('Images', 'achievements', 'dont_get_hit.png')).convert()
expert_image = image.load(join('Images', 'achievements', 'expert.png')).convert()
get_hit_image = image.load(join('Images', 'achievements', 'get_hit.png')).convert()
the_true_cactus_climber_image = image.load(join('Images', 'achievements', 'the_true_cactus_climber.png')).convert()
hat_collector_image = image.load(join('Images', 'achievements', 'hat_collector.png')).convert()
select_box_image = image.load(join('Images', 'ui', 'select_box.png')).convert_alpha()
textbox_image = image.load(join('Images', 'ui', 'TextBox.png')).convert()
yes_image = image.load(join('Images', 'ui', 'yes.png')).convert()
no_image = image.load(join('Images', 'ui', 'no.png')).convert()
red_cap_image = image.load(join('Images', 'shop', 'red_cap.png')).convert_alpha()
thinking_hat_image = image.load(join('Images', 'shop', 'thinking_hat.png')).convert_alpha()
top_hat_image = image.load(join('Images', 'shop', 'top_hat.png')).convert_alpha()
cowboy_hat_image = image.load(join('Images', 'shop', 'cowboy_hat.png')).convert_alpha()
king_hat_image = image.load(join('Images', 'shop', 'king_hat.png')).convert_alpha()
mexican_hat_image = image.load(join('Images', 'shop', 'mexican_hat.png')).convert_alpha()
witch_hat_image = image.load(join('Images', 'shop', 'witch_hat.png')).convert_alpha()
party_hat_image = image.load(join('Images', 'shop', 'party_hat.png')).convert_alpha()
money_image = image.load(join('Images', 'shop', 'money.png')).convert()
equip_image = image.load(join('Images', 'shop', 'equip.png')).convert()
unequip_image = image.load(join('Images', 'shop', 'unequip.png')).convert()
buy_image = image.load(join('Images', 'shop', 'buy.png')).convert()
credits_bg_image = image.load(join('Images', 'credits', 'credits_bg.png')).convert()
maintheme = mixer.Sound(join('Music', 'maintheme.mp3'))
dodgemusic = mixer.Sound(join('Music', 'dodge!.mp3'))
firesound = mixer.Sound(join('Music', 'Sounds', 'fire.mp3'))
birdsound = mixer.Sound(join('Music', 'Sounds', 'bird.mp3')) 
buy_sound = mixer.Sound(join('Music', 'Sounds', 'buy.mp3'))
equipped_sound = mixer.Sound(join('Music', 'Sounds', 'equipped.mp3'))
denied_sound = mixer.Sound(join('Music', 'Sounds', 'denied.mp3'))
bg = image.load(join('Images', 'bg.png')).convert_alpha()
diff = 0
show_textbox = False
show_start = True
show_select_box = False
play_denied = True
play_denied2 = True
play_denied3 = True
play_denied4 = True
play_denied5 = True
play_denied6 = True
play_denied7 = True
play_denied8 = True
data_easy = {
    'birds_dodged': 0,
    'fireballs_dodged': 0,
    'meters_up': 0
}
data_normal = {
    'birds_dodged': 0,
    'fireballs_dodged': 0,
    'meters_up': 0
}
data_hard = {
    'birds_dodged': 0,
    'fireballs_dodged': 0,
    'meters_up': 0
}
data_shop = {
    'money': 0,
    'red_cap_equipped': False,
    'thinking_hat_equipped': False,
    'top_hat_equipped': False,
    'cowboy_hat_equipped': False,
    'king_hat_equipped': False,
    'mexican_hat_equipped': False,
    'witch_hat_equipped': False,
    'party_hat_equipped': False,
    'red_cap_unlocked': False,
    'thinking_hat_unlocked': False,
    'top_hat_unlocked': False,
    'cowboy_hat_unlocked': False,
    'king_hat_unlocked': False,
    'mexican_hat_unlocked': False,
    'witch_hat_unlocked': False,
    'party_hat_unlocked': False,
    'show_cost': True,
    'show_cost2': True,
    'show_cost3': True,
    'show_cost4': True,
    'show_cost5': True,
    'show_cost6': True,
    'show_cost7': True,
    'show_cost8': True
}
data_options = {
    'play_sfx': True,
    'play_music': True,
    'controller_vibration': True,
    'show_easy': False,
    'show_normal': False,
    'show_hard': False,
}
data_achievements = {
    'first_steps': False,
    'climb_the_top': False,
    'cactus_climber': False,
    'catch_on_fire': False,
    'climb': False,
    'dont_catch_on_fire': False,
    'dont_get_hit': False,
    'expert': False,
    'get_hit': False,
    'the_true_cactus_climber': False,
    'hat_collector': False,
    'achievements_complete': 0,
    'achievement_1': True,
    'achievement_2': True,
    'achievement_3': True,
    'achievement_4': True,
    'achievement_5': True,
    'achievement_6': True,
    'achievement_7': True,
    'achievement_8': True,
    'achievement_9': True,
    'achievement_10': True,
    'achievement_11': True
}
with open(join('data','save_data_easy.json')) as save_data_easy:
    data_easy = load(save_data_easy)
with open(join('data','save_data_normal.json')) as save_data_normal:
    data_normal = load(save_data_normal)
with open(join('data','save_data_hard.json')) as save_data_hard:
    data_hard = load(save_data_hard)
with open(join('data','save_data_shop.json')) as save_data_shop:
    data_shop = load(save_data_shop)
with open(join('data','save_data_options.json')) as save_data_options:
    data_options = load(save_data_options)
with open(join('data','save_data_achievements.json')) as save_data_achievements:
    data_achievements = load(save_data_achievements)
def save_data():
    with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
        dump(data_easy, save_data_easy)
    with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
        dump(data_normal, save_data_normal)
    with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
        dump(data_hard, save_data_hard)
    with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
        dump(data_shop, save_data_shop)
    with open(join('data', 'save_data_options.json'),'w') as save_data_options:
        dump(data_options, save_data_options)
    with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
        dump(data_achievements, save_data_achievements)
def win():
    Money = button(1030, 600, 250, 100, money_image)
    run = True
    clockyy = time.Clock()
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                if io == -1: #left
                    endvideo()
        #text
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        main_text = medium_font.render("Press A or Left key to Go Back Down", 1, (0, 0, 255))
        win_text = medium_font.render("You Reached the Top!", 1, (0, 0, 255))
        win1_text = medium_font.render("but at what Cost?", 1, (255, 0, 0))
        window.blit(win_text, (500, 0))
        window.blit(win1_text, (550, 50))
        window.blit(main_text, (360, 600))
        #keyboard input
        keys = key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            display.update()
            time.wait(3000)
            endvideo()
        #displaying on screen
        window.blit(money_text, ((screen_width - money_text.get_width() - 225), 600))
        window.blit(Money.image, (Money.x, Money.y))
        display.update()
def credits():
    global data_options, window
    Back = button(1030, 600, 250, 100, back_image)
    Credits = button(0, 0, screen_width, screen_height, credits_bg_image)
    run = True
    clockyy = time.Clock()
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(1):
                    start()
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = mouse.get_pos()
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                if back_rect.collidepoint(mousex, mousey):
                    start()
        window.blit(Credits.image, (Credits.x, Credits.y))
        window.blit(Back.image, (Back.x, Back.y))
        display.update()
def shop():
    global show_select_box, data_shop, data_options, play_denied, play_denied2, play_denied3, play_denied4, play_denied5, play_denied6, play_denied7, play_denied8
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
        clockyy.tick(60)
        current_time = time.get_ticks()
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(1):
                    start()
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
                mousex, mousey = mouse.get_pos()
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
                    start()
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
        window.fill((204, 102, 25))
        window.blit(money_text, (250, 0))
        if data_shop['show_cost'] == True:
            window.blit(cost_text, (60, 250))
        if data_shop['show_cost2'] == True:
            window.blit(cost2_text, (360, 250))
        if data_shop['show_cost3'] == True:
            window.blit(cost3_text, (660, 250))
        if data_shop['show_cost4'] == True:
            window.blit(cost4_text, (950, 250))
        if data_shop['show_cost5'] == True:
            window.blit(cost5_text, (60, 400))
        if data_shop['show_cost6'] == True:
            window.blit(cost6_text, (660, 400))
        if data_shop['show_cost7'] == True:
            window.blit(cost7_text, (360, 400))
        if data_shop['show_cost8'] == True:
            window.blit(cost8_text, (950, 400))
        window.blit(Back.image, (Back.x, Back.y))
        window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(Money.image, (Money.x, Money.y))
        window.blit(Buy.image, (Buy.x, Buy.y))
        window.blit(Buy2.image, (Buy2.x, Buy2.y))
        window.blit(Buy3.image, (Buy3.x, Buy3.y))
        window.blit(Buy4.image, (Buy4.x, Buy4.y))
        window.blit(Buy5.image, (Buy5.x, Buy5.y))
        window.blit(Buy6.image, (Buy6.x, Buy6.y))
        window.blit(Buy7.image, (Buy7.x, Buy7.y))
        window.blit(Buy8.image, (Buy8.x, Buy8.y))
        window.blit(Equip.image, (Equip.x, Equip.y))
        window.blit(Equip2.image, (Equip2.x, Equip2.y))
        window.blit(Equip3.image, (Equip3.x, Equip3.y))
        window.blit(Equip4.image, (Equip4.x, Equip4.y))
        window.blit(Equip5.image, (Equip5.x, Equip5.y))
        window.blit(Equip6.image, (Equip6.x, Equip6.y))
        window.blit(Equip7.image, (Equip7.x, Equip7.y))
        window.blit(Equip8.image, (Equip8.x, Equip8.y))
        window.blit(Unequip.image, (Unequip.x, Unequip.y))
        window.blit(Unequip2.image, (Unequip2.x, Unequip2.y))
        window.blit(Unequip3.image, (Unequip3.x, Unequip3.y))
        window.blit(Unequip4.image, (Unequip4.x, Unequip4.y))
        window.blit(Unequip5.image, (Unequip5.x, Unequip5.y))
        window.blit(Unequip6.image, (Unequip6.x, Unequip6.y))
        window.blit(Unequip7.image, (Unequip7.x, Unequip7.y))
        window.blit(Unequip8.image, (Unequip8.x, Unequip8.y))
        if show_select_box == True:
            window.blit(Select_Box.image, (Select_Box.x, Select_Box.y))
        display.update()
def options():
    global data_options, show_select_box
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
        clockyy.tick(60)
        current_time = time.get_ticks()
        current_time2 = time.get_ticks()
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(1):
                        start()
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
                mousex, mousey = mouse.get_pos()
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                checked_off_rect = Rect(Checked_off.x, Checked_off.y, Checked_off.width, Checked_off.height)
                checked_rect = Rect(Checked.x, Checked.y, Checked.width, Checked.height)
                checked_off2_rect = Rect(Checked_off2.x, Checked_off2.y, Checked_off2.width, Checked_off2.height)
                checked2_rect = Rect(Checked2.x, Checked2.y, Checked2.width, Checked2.height)
                checked_off3_rect = Rect(Checked_off3.x, Checked_off3.y, Checked_off3.width, Checked_off3.height)
                checked3_rect = Rect(Checked3.x, Checked3.y, Checked3.width, Checked3.height)
                if back_rect.collidepoint(mousex, mousey):
                    start()
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
        window.fill((204, 102, 25))
        window.blit(Back.image, (Back.x, Back.y))
        window.blit(Music.image, (Music.x, Music.y))
        window.blit(SFX.image, (SFX.x, SFX.y))
        window.blit(Controller_Vibration.image, (Controller_Vibration.x, Controller_Vibration.y))
        window.blit(Checked.image, (Checked.x, Checked.y))
        window.blit(Checked_off.image, (Checked_off.x, Checked_off.y))
        window.blit(Checked2.image, (Checked2.x, Checked2.y))
        window.blit(Checked_off2.image, (Checked_off2.x, Checked_off2.y))
        window.blit(Checked3.image, (Checked3.x, Checked3.y))
        window.blit(Checked_off3.image, (Checked_off3.x, Checked_off3.y))
        if show_select_box == True:
            window.blit(Select_Box.image, (Select_Box.x, Select_Box.y))
        display.update()
def start():
    global show_textbox, show_start, data_easy, data_normal, data_hard, data_options, data_shop, data_achievements
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
    run = True
    clockyy = time.Clock()
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYBUTTONDOWN:
                if show_textbox == True:
                    if joystick.Joystick(0).get_button(1):
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        show_textbox = False
                        show_start = True
                        start()
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
                        start()
                if show_start == True:
                    if joystick.Joystick(0).get_button(0):
                        mainmenu()
                    elif joystick.Joystick(0).get_button(6):
                        achievements()
                    elif joystick.Joystick(0).get_button(2):
                        shop()
                    elif joystick.Joystick(0).get_button(3):
                        credits()
                    elif joystick.Joystick(0).get_button(4):
                        run = False
                        quit()
                    elif joystick.Joystick(0).get_button(5):
                        show_textbox = True
                        show_start = False
                    elif joystick.Joystick(0).get_button(7):
                        options()
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = mouse.get_pos()
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
                        mainmenu()
                    elif quit_rect.collidepoint(mousex, mousey):
                        run = False
                        quit()
                    elif options_rect.collidepoint(mousex, mousey):
                        options()
                    elif shop_rect.collidepoint(mousex, mousey):
                        shop()
                    elif achievements_rect.collidepoint(mousex, mousey):
                        achievements()
                    elif credits_rect.collidepoint(mousex, mousey):
                        credits()
                if show_textbox == True:
                    if no_rect.collidepoint(mousex, mousey):
                        if data_options['play_sfx'] == True:
                            denied_sound.play()
                        show_textbox = False
                        show_start = True
                        start()
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
                        start()
                if reset_rect.collidepoint(mousex, mousey):
                    show_textbox = True
                    show_start = False
        title_text = large_font.render("Cactus Climber", 1, (64, 255, 25)) 
        version_text = medium_font.render("v1.3.1", 1, (64, 255, 25))
        window.fill((204, 102, 25))
        window.blit(Play.image, (Play.x, Play.y))
        window.blit(Options.image, (Options.x, Options.y))
        window.blit(Shop.image, (Shop.x, Shop.y))
        window.blit(Credits.image, (Credits.x, Credits.y))
        window.blit(Quit.image, (Quit.x, Quit.y))
        window.blit(Reset.image, (Reset.x, Reset.y))
        window.blit(Achievements.image, (Achievements.x, Achievements.y))
        window.blit(title_text, (350, 0))
        window.blit(version_text, (0, 0))
        if show_textbox == True:
            window.blit(TextBox.image, (TextBox.x, TextBox.y))
            window.blit(No.image, (No.x, No.y))
            window.blit(Yes.image, (Yes.x, Yes.y))
        display.update()
def achievements():
    global data_achievements, data_easy, data_hard, data_normal, data_shop
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
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(1):
                    start()
            elif e.type == MOUSEBUTTONDOWN:
                mousex, mousey = mouse.get_pos()
                back_rect = Rect(Back.x, Back.y, Back.width, Back.height)
                if back_rect.collidepoint(mousex, mousey):
                    start()
        title_text = large_font.render("ACHIEVEMENTS", 1, (255, 0, 0))
        achievements_complete_text = medium_font.render(str(data_achievements['achievements_complete']) + "/11 Complete", 1, (255, 255, 255))
        window.fill((204, 102, 25))
        window.blit(Back.image, (Back.x, Back.y))
        window.blit(First_Steps.image, (First_Steps.x, First_Steps.y))
        window.blit(Back.image, (Back.x, Back.y))
        window.blit(Checked.image, (Checked.x, Checked.y))
        window.blit(Checked_off.image, (Checked_off.x, Checked_off.y))
        window.blit(Climb_The_Top.image, (Climb_The_Top.x, Climb_The_Top.y))
        window.blit(Checked1.image, (Checked1.x, Checked1.y))
        window.blit(Checked_off1.image, (Checked_off1.x, Checked_off1.y))
        window.blit(Cactus_Climber.image, (Cactus_Climber.x, Cactus_Climber.y))
        window.blit(Checked2.image, (Checked2.x, Checked2.y))
        window.blit(Checked_off2.image, (Checked_off2.x, Checked_off2.y))
        window.blit(Catch_On_Fire.image, (Catch_On_Fire.x, Catch_On_Fire.y))
        window.blit(Checked3.image, (Checked3.x, Checked3.y))
        window.blit(Checked_off3.image, (Checked_off3.x, Checked_off3.y))
        window.blit(Climb.image, (Climb.x, Climb.y))
        window.blit(Checked4.image, (Checked4.x, Checked4.y))
        window.blit(Checked_off4.image, (Checked_off4.x, Checked_off4.y))
        window.blit(Dont_Catch_On_Fire.image, (Dont_Catch_On_Fire.x, Dont_Catch_On_Fire.y))
        window.blit(Checked5.image, (Checked5.x, Checked5.y))
        window.blit(Checked_off5.image, (Checked_off5.x, Checked_off5.y))
        window.blit(Dont_Get_Hit.image, (Dont_Get_Hit.x, Dont_Get_Hit.y))
        window.blit(Checked6.image, (Checked6.x, Checked6.y))
        window.blit(Checked_off6.image, (Checked_off6.x, Checked_off6.y))
        window.blit(Expert.image, (Expert.x, Expert.y))
        window.blit(Checked7.image, (Checked7.x, Checked7.y))
        window.blit(Checked_off7.image, (Checked_off7.x, Checked_off7.y))
        window.blit(Get_Hit.image, (Get_Hit.x, Get_Hit.y))
        window.blit(Checked8.image, (Checked8.x, Checked8.y))
        window.blit(Checked_off8.image, (Checked_off8.x, Checked_off8.y))
        window.blit(Hat_Collector.image, (Hat_Collector.x, Hat_Collector.y))
        window.blit(Checked9.image, (Checked9.x, Checked9.y))
        window.blit(Checked_off9.image, (Checked_off9.x, Checked_off9.y))
        window.blit(The_True_Cactus_Climber.image, (The_True_Cactus_Climber.x, The_True_Cactus_Climber.y))
        window.blit(Checked10.image, (Checked10.x, Checked10.y))
        window.blit(Checked_off10.image, (Checked_off10.x, Checked_off10.y))
        window.blit(title_text, (370, 0))
        window.blit(achievements_complete_text, (0, 600))
        display.update()
def mainmenu():
    global diff, data_options
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
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYBUTTONDOWN:
                if joystick.Joystick(0).get_button(3):
                    diff = 1
                    mainspot()
                elif joystick.Joystick(0).get_button(2):
                    diff = 2
                    mainspot()
                elif joystick.Joystick(0).get_button(0):
                    diff = 3
                    mainspot()
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
                mousex, mousey = mouse.get_pos()
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
                    diff = 1
                    mainspot()
                elif normal_rect.collidepoint(mousex, mousey):
                    diff = 2
                    mainspot()
                elif hard_rect.collidepoint(mousex, mousey):
                    diff = 3
                    mainspot()
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
                    start()
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
        window.fill((204, 102, 25))
        if data_options['show_easy'] == True:
            window.blit(total_fireballs_dodged_easy_text, (50, 550))
            window.blit(total_birds_dodged_easy_text, (50, 580))
            window.blit(highest_meter_easy_text, (50, 610))
            window.blit(full_meter_easy_text, (50, 640))
        if data_options['show_normal'] == True:
            window.blit(total_fireballs_dodged_normal_text, (450, 550))
            window.blit(total_birds_dodged_normal_text, (450, 580))
            window.blit(highest_meter_normal_text, (450, 610))
            window.blit(full_meter_normal_text, (450, 640))
        if data_options['show_hard'] == True:
            window.blit(total_fireballs_dodged_hard_text, (850, 550))
            window.blit(total_birds_dodged_hard_text, (850, 580))
            window.blit(highest_meter_hard_text, (850, 610))
            window.blit(full_meter_hard_text, (850, 640))
        window.blit(Easy.image, (Easy.x, Easy.y))
        window.blit(Normal.image, (Normal.x, Normal.y))
        window.blit(Hard.image, (Hard.x, Hard.y))
        window.blit(Easy_Stats.image, (Easy_Stats.x, Easy_Stats.y))
        window.blit(Normal_Stats.image, (Normal_Stats.x, Normal_Stats.y))
        window.blit(Hard_Stats.image, (Hard_Stats.x, Hard_Stats.y))
        window.blit(Easy_Hide_Stats.image, (Easy_Hide_Stats.x, Easy_Hide_Stats.y))
        window.blit(Normal_Hide_Stats.image, (Normal_Hide_Stats.x, Normal_Hide_Stats.y))
        window.blit(Hard_Hide_Stats.image, (Hard_Hide_Stats.x, Hard_Hide_Stats.y))
        window.blit(Back.image, (Back.x, Back.y))
        window.blit(title_text, (150, 90))
        window.blit(version_text, (0, 0))
        window.blit(money_text, ((screen_width - money_text.get_width() - 225), 0))
        window.blit(Money.image, (Money.x, Money.y))
        display.update()
def mainspot():
    global data_shop
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
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                if io == 1 and diff == 1: #right
                    firstvideo_easy()
                elif io == 1 and diff == 2: #right
                    firstvideo_normal()
                elif io == 1 and diff == 3: #right
                    firstvideo_hard()
        begin_text = medium_font.render("Press D or Right key to Climb", 1, (0, 0, 255))
        keys = key.get_pressed()
        if keys[K_d] and diff == 1 or keys[K_RIGHT] and diff == 1:
            firstvideo_easy()
        elif keys[K_d] and diff == 2 or keys[K_RIGHT] and diff == 2:
            firstvideo_normal()
        elif keys[K_d] and diff == 3 or keys[K_RIGHT] and diff == 3:
            firstvideo_hard()
        window.fill((204, 102, 0))
        window.blit(bottom_cactus, (640, -500))
        window.blit(bg, (0, 0))
        window.blit(begin_player, (150, 400))
        window.blit(begin_text, (360, 600))
        if data_shop['cowboy_hat_equipped'] == True:
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        display.update()
def endvideo():
    run = True
    clockyy = time.Clock()
    endvid = VideoFileClip("Videos/end.mp4")
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
        endvid.preview()
        display.update()
        time.wait(5000)
        endvid.close()
        mainmenu()
def firstvideo_easy():
    run = True
    clockyy = time.Clock()
    beginvid = VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
        beginvid.preview()
        display.update()
        beginvid.close()
        main_easy()
def firstvideo_normal():
    run = True
    clockyy = time.Clock()
    beginvid = VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
        beginvid.preview()
        display.update()
        beginvid.close()
        main_normal()
def firstvideo_hard():
    run = True
    clockyy = time.Clock()
    beginvid = VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
        beginvid.preview()
        display.update()
        beginvid.close()
        main_hard()
def fireballdeathvid():
    run = True
    clockyy = time.Clock()
    fireballdeath = VideoFileClip("Videos/fireballdeath.mp4")
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
        fireballdeath.preview()
        display.update()
        time.wait(4000)
        fireballdeath.close()
        mainmenu()
def birddeathvid():
    run = True
    clockyy = time.Clock()
    birddeath = VideoFileClip("Videos/birddeath.mp4")
    while run:  
        clockyy.tick(60)
        for e in event.get():
            if e.type == QUIT:
                save_data()
                quit()
                run = False
        birddeath.preview()
        display.update()
        time.wait(4000)
        birddeath.close()
        mainmenu()
def main_easy():
    global data_easy, data_options, data_shop, data_achievements
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
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                if io == 1: #right 
                    if flap2 == True:
                        data_shop['money'] += 1
                        data_easy['meters_up'] += 1
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
                        data_easy['meters_up'] += 1
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
        top_cactus_rect = Rect(640, cactusy - 2800, 100, 800)
        if player_rect.colliderect(fireball_rect):
            if data_achievements['catch_on_fire'] == False:
                data_achievements['catch_on_fire'] = True
            with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
                dump(data_easy, save_data_easy)
            with open(join('data','save_data_easy.json')) as save_data_easy:
                data_easy = load(save_data_easy)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            fireballdeathvid()
        elif player_rect.colliderect(bird_rect):
            if data_achievements['get_hit'] == False:
                data_achievements['get_hit'] = True
            with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
                dump(data_easy, save_data_easy)
            with open(join('data','save_data_easy.json')) as save_data_easy:
                data_easy = load(save_data_easy)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            birddeathvid()
        keys = key.get_pressed()
        if keys[K_a] and keys[K_d]:
            maintheme.stop()
            mainmenu()
        elif keys[K_LEFT] and keys[K_RIGHT]:
            maintheme.stop()
            mainmenu()
        elif keys[K_a] and keys[K_RIGHT]:
            maintheme.stop()
            mainmenu()
        elif keys[K_LEFT] and keys[K_d]:
            maintheme.stop()
            mainmenu()
        if keys[K_a] or keys[K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                data_easy['meters_up'] += 1
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
                data_easy['meters_up'] += 1
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
        fireball1.y += 10
        if fireball1.y >= screen_height:
            fireball1.y = -1000
            fireball1.x = choice([585, 760])
            data_easy['fireballs_dodged'] += 1
            with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
                dump(data_easy, save_data_easy)
            fireballs_dodged += 1
        bird1.x += 10
        if bird1.x >= screen_width:
            bird1.x = -1000
            data_easy['birds_dodged'] += 1
            with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
                dump(data_easy, save_data_easy)
            birds_dodged += 1
        elif bird1.y >= screen_height:
            bird1.x = -1000
            bird1.y = randint(300, 800)
            data_easy['birds_dodged'] += 1
            with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
                dump(data_easy, save_data_easy)
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
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
        elif fireball1.y >= 0 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
        if bird_rect.colliderect(bird_rac_rect):   
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
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
            with open(join('data', 'save_data_easy.json'),'w') as save_data_easy:
                dump(data_easy, save_data_easy)
            with open(join('data','save_data_easy.json')) as save_data_easy:
                data_easy = load(save_data_easy)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            data_shop['money'] += 50
            with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                dump(data_shop, save_data_shop)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            win()
        high_score_text = medium_font.render("High Scores", 1, (255, 255, 255))
        total_fireballs_dodged_text = medium_font.render(f"Total Fireballs Dodged: {data_easy['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_text = medium_font.render(f"Total Meters Climbed: {data_easy['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_text = medium_font.render(f"Total Birds Dodged: {data_easy['birds_dodged']}", 1, (255, 255, 255))
        score_text = medium_font.render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = medium_font.render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = medium_font.render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = medium_font.render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        window.fill((204, 102, 0))
        window.blit(top_cactus, (640, cactusy - 2000))
        window.blit(mid_cactus, (640, cactusy - 1000))
        window.blit(bottom_cactus, (640, cactusy))
        window.blit(bg, (0, bgy))
        window.blit(score_text, (1100, 0))
        window.blit(fireballs_dodged_text, (screen_width - fireballs_dodged_text.get_width() - 10, 200))
        window.blit(birds_dodged_text, (screen_width - birds_dodged_text.get_width() - 10, 150))
        window.blit(meters_text, (screen_width - meters_text.get_width() - 10, 100))
        window.blit(high_score_text, (50, 0))
        window.blit(total_fireballs_dodged_text, (0, 200))
        window.blit(total_birds_dodged_text, (0, 150))
        window.blit(highest_meter_text, (0, 100))
        window.blit(money_text, ((screen_width - money_text.get_width() - 225), 600))
        window.blit(player1.img, (player1.x, player1.y))
        if data_shop['cowboy_hat_equipped'] == True:
            if player1.x == 740:
                Cowboy_Hat.x = 755
            elif player1.x == 590:
                Cowboy_Hat.x = 585
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            elif player1.x == 590:
                Thinking_Hat.x = 585
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            elif player1.x == 590:
                Top_Hat.x = 585
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            elif player1.x == 590:
                Red_Cap.image = transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            elif player1.x == 590:
                Party_Hat.x = 585
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            elif player1.x == 590:
                Witch_Hat.x = 585
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            elif player1.x == 590:
                Mexican_Hat.x = 585
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            elif player1.x == 590:
                King_Hat.x = 585
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(bird1.image, (bird1.x, bird1.y))
        window.blit(fireball1.image, (fireball1.x, fireball1.y))
        window.blit(Money.image, (Money.x, Money.y))
        display.update()
def main_normal():
    global data_normal, data_options, data_shop, data_achievements
    if data_options['play_music'] == True:
        maintheme.play(-1)
    fireballs_dodged = 0
    meters_up = 0
    birds_dodged = 0
    flap = False
    flap2 = True
    player1 = player(590, 300, 50, 100)
    bird1 = button(0, 600, 100, 100, bird_image)
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
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                if io == 1: #right 
                    if flap2 == True:
                        if data_achievements['first_steps'] == False:
                            data_achievements['first_steps'] = True
                        data_shop['money'] += 1
                        data_normal['meters_up'] += 1
                        meters_up += 1
                        player1.img = image.load(join('Images', 'player', 'player.png')).convert_alpha()
                        player1.img = transform.scale(player1.img, (player1.width, player1.height))
                        player1.x += 150
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
                        data_normal['meters_up'] += 1
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
        top_cactus_rect = Rect(640, cactusy - 5800, 100, 800)
        if player_rect.colliderect(fireball_rect):
            if data_achievements['catch_on_fire'] == False:
                data_achievements['catch_on_fire'] = True
            with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    dump(data_normal, save_data_normal)
            with open(join('data','save_data_normal.json')) as save_data_normal:
                    data_normal = load(save_data_normal)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                    dump(data_achievements, save_data_achievements)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    pass
            fireballdeathvid()
        elif player_rect.colliderect(bird_rect):
            if data_achievements['get_hit'] == False:
                data_achievements['get_hit'] = True
            with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    dump(data_normal, save_data_normal)
            with open(join('data','save_data_normal.json')) as save_data_normal:
                    data_normal = load(save_data_normal)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                    dump(data_achievements, save_data_achievements)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    pass
            birddeathvid()
        keys = key.get_pressed()
        if keys[K_a] and keys[K_d]:
            maintheme.stop()
            mainmenu()
        elif keys[K_LEFT] and keys[K_RIGHT]:
            maintheme.stop()
            mainmenu()
        elif keys[K_a] and keys[K_RIGHT]:
            maintheme.stop()
            mainmenu()
        elif keys[K_LEFT] and keys[K_d]:
            maintheme.stop()
            mainmenu()
        if keys[K_a] or keys[K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                data_normal['meters_up'] += 1
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
                data_normal['meters_up'] += 1
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
        fireball1.y += 10
        if fireball1.y >= screen_height:
            fireball1.y = 0
            fireball1.x = choice([585, 760])
            data_normal['fireballs_dodged'] += 1
            with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
                dump(data_normal, save_data_normal)
            fireballs_dodged += 1
        bird1.x += 10
        if bird1.x >= screen_width:
            bird1.x = -1000
            data_normal['birds_dodged'] += 1
            with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
                dump(data_normal, save_data_normal)
            birds_dodged += 1
        elif bird1.y >= screen_height:
            bird1.x = -1000
            bird1.y = randint(300, 800)
            data_normal['birds_dodged'] += 1
            with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
                dump(data_normal, save_data_normal)
            birds_dodged += 1
        dodge_text_red = small_font.render("dodge!", 1, (255, 0, 0))
        dodge_text = small_font.render("dodge!", 1, (255, 255, 255))
        if fireball1.y >= 0 and fireball1.x == 585 and player1.x == 590 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
        elif fireball1.y >= 0 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
        if bird_rect.colliderect(bird_rac_rect):
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
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
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            with open(join('data', 'save_data_normal.json'),'w') as save_data_normal:
                dump(data_normal, save_data_normal)
            with open(join('data','save_data_normal.json')) as save_data_normal:
                data_normal = load(save_data_normal)
            data_shop['money'] += 100
            with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                dump(data_shop, save_data_shop)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            win()
        high_score_text = medium_font.render("High Scores", 1, (255, 255, 255))
        total_fireballs_dodged_text = medium_font.render(f"Total Fireballs Dodged: {data_normal['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_text = medium_font.render(f"Total Meters Climbed: {data_normal['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_text = medium_font.render(f"Total Birds Dodged: {data_normal['birds_dodged']}", 1, (255, 255, 255))
        score_text = medium_font.render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = medium_font.render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = medium_font.render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = medium_font.render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        window.fill((204, 102, 0))
        window.blit(top_cactus, (640, cactusy - 5000))
        window.blit(mid_cactus, (640, cactusy - 4000))
        window.blit(mid_cactus, (640, cactusy - 3000))
        window.blit(mid_cactus, (640, cactusy - 2000))
        window.blit(mid_cactus, (640, cactusy - 1000))
        window.blit(bottom_cactus, (640, cactusy))
        window.blit(bg, (0, bgy))
        window.blit(score_text, (1100, 0))
        window.blit(fireballs_dodged_text, (screen_width - fireballs_dodged_text.get_width() - 10, 200))
        window.blit(birds_dodged_text, (screen_width - birds_dodged_text.get_width() - 10, 150))
        window.blit(meters_text, (screen_width - meters_text.get_width() - 10, 100))
        window.blit(high_score_text, (50, 0))
        window.blit(total_fireballs_dodged_text, (0, 200))
        window.blit(total_birds_dodged_text, (0, 150))
        window.blit(highest_meter_text, (0, 100))
        window.blit(money_text, ((screen_width - money_text.get_width() - 225), 600))
        window.blit(player1.img, (player1.x, player1.y))
        if data_shop['cowboy_hat_equipped'] == True:
            if player1.x == 740:
                Cowboy_Hat.x = 755
            elif player1.x == 590:
                Cowboy_Hat.x = 585
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            elif player1.x == 590:
                Thinking_Hat.x = 585
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            elif player1.x == 590:
                Top_Hat.x = 585
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            elif player1.x == 590:
                Red_Cap.image = transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            elif player1.x == 590:
                Party_Hat.x = 585
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            elif player1.x == 590:
                Witch_Hat.x = 585
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            elif player1.x == 590:
                Mexican_Hat.x = 585
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            elif player1.x == 590:
                King_Hat.x = 585
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(bird1.image, (bird1.x, bird1.y))
        window.blit(fireball1.image, (fireball1.x, fireball1.y))
        window.blit(Money.image, (Money.x, Money.y))
        display.update()
def main_hard():
    global data_hard, data_options, data_shop, data_achievements
    if data_options['play_music'] == True:
        maintheme.play(-1)
    fireballs_dodged = 0
    meters_up = 0
    birds_dodged = 0
    flap = False
    flap2 = True
    player1 = player(590, 300, 50, 100)
    bird1 = button(0, 600, 100, 100, bird_image)
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
            elif e.type == JOYAXISMOTION:
                io = round(joystick.Joystick(0).get_axis(0))
                if io == 1: #right 
                    if flap2 == True:
                        data_shop['money'] += 1
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
                        bird1.y += 50
                        fireball1.y += 50
                        flap2 = False
                        flap = True
                elif io == -1: #left
                    if flap == True:
                        data_shop['money'] += 1
                        data_hard['meters_up'] += 1
                        meters_up += 1
                        player1.img = image.load(join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                        player1.img = transform.scale(player1.img, (player1.width, player1.height))
                        player1.x -= 150
                        save_data()
                        cactusy += 50
                        bgy += 50
                        bird1.y += 50
                        fireball1.y += 50
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
        top_cactus_rect = Rect(640, cactusy - 10800, 100, 800)
        if player_rect.colliderect(fireball_rect):
            if data_achievements['catch_on_fire'] == False:
                data_achievements['catch_on_fire'] = True
            with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
                dump(data_hard, save_data_hard)
            with open(join('data','save_data_hard.json')) as save_data_hard:
                data_hard = load(save_data_hard)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            fireballdeathvid()
        elif player_rect.colliderect(bird_rect):
            if data_achievements['get_hit'] == False:
                data_achievements['get_hit'] = True
            with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
                dump(data_hard, save_data_hard)
            with open(join('data','save_data_hard.json')) as save_data_hard:
                data_hard = load(save_data_hard)
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            birddeathvid()
        keys = key.get_pressed()
        if keys[K_a] and keys[K_d]:
            maintheme.stop()
            mainmenu()
        elif keys[K_LEFT] and keys[K_RIGHT]:
            maintheme.stop()
            mainmenu()
        elif keys[K_a] and keys[K_RIGHT]:
            maintheme.stop()
            mainmenu()
        elif keys[K_LEFT] and keys[K_d]:
            maintheme.stop()
            mainmenu()
        if keys[K_a] or keys[K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                data_hard['meters_up'] += 1
                meters_up += 1
                player1.img = image.load(join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                player1.img = transform.scale(player1.img, (player1.width, player1.height))
                player1.x -= 150
                save_data()
                cactusy += 50
                bgy += 50
                bird1.y += 50
                fireball1.y += 50
                flap = False
                flap2 = True
        elif keys[K_d] or keys[K_RIGHT]:
            if flap2 == True:
                data_shop['money'] += 1
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
                bird1.y += 50
                fireball1.y += 50
                flap2 = False
                flap = True
        fireball1.y += 25
        if fireball1.y >= screen_height:
            fireball1.y = 0
            fireball1.x = choice([585, 760])
            data_hard['fireballs_dodged'] += 1
            with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
                dump(data_hard, save_data_hard)
            fireballs_dodged += 1
        bird1.x += 25
        if bird1.x >= screen_width:
            bird1.x = -100
            data_hard['birds_dodged'] += 1
            with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
                dump(data_hard, save_data_hard)
            birds_dodged += 1
        elif bird1.y >= screen_height:
            bird1.x = -100
            bird1.y = randint(300, 800)
            data_hard['birds_dodged'] += 1
            with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
                dump(data_hard, save_data_hard)
            birds_dodged += 1
        dodge_text_red = small_font.render("dodge!", 1, (255, 0, 0))
        dodge_text = small_font.render("dodge!", 1, (255, 255, 255))
        if fireball1.y >= 20 and fireball1.x == 585 and player1.x == 590 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            display.update()
        elif fireball1.y >= 20 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            display.update()
        if bird_rect.colliderect(bird_rac_rect):
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            display.update()
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
            if data_achievements['expert'] == False:
                data_achievements['expert'] = True
            with open(join('data', 'save_data_achievements.json'),'w') as save_data_achievements:
                dump(data_achievements, save_data_achievements)
            with open(join('data', 'save_data_hard.json'),'w') as save_data_hard:
                dump(data_hard, save_data_hard)
            with open(join('data','save_data_hard.json')) as save_data_hard:
                data_hard = load(save_data_hard)
            data_shop['money'] += 200
            with open(join('data', 'save_data_shop.json'),'w') as save_data_shop:
                dump(data_shop, save_data_shop)
            if data_options['controller_vibration'] == True:
                try:
                    joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            win()
        high_score_text = medium_font.render("High Scores", 1, (255, 255, 255))
        total_fireballs_dodged_text = medium_font.render(f"Total Fireballs Dodged: {data_hard['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_text = medium_font.render(f"Total Meters Climbed: {data_hard['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_text = medium_font.render(f"Total Birds Dodged: {data_hard['birds_dodged']}", 1, (255, 255, 255))
        score_text = medium_font.render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = medium_font.render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = medium_font.render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = medium_font.render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))
        money_text = large_font.render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        window.fill((204, 102, 0))
        window.blit(top_cactus, (640, cactusy - 10000))
        window.blit(mid_cactus, (640, cactusy - 9000))
        window.blit(mid_cactus, (640, cactusy - 8000))
        window.blit(mid_cactus, (640, cactusy - 7000))
        window.blit(mid_cactus, (640, cactusy - 6000))
        window.blit(mid_cactus, (640, cactusy - 5000))
        window.blit(mid_cactus, (640, cactusy - 4000))
        window.blit(mid_cactus, (640, cactusy - 3000))
        window.blit(mid_cactus, (640, cactusy - 2000))
        window.blit(mid_cactus, (640, cactusy - 1000))
        window.blit(bottom_cactus, (640, cactusy))
        window.blit(bg, (0, bgy))
        window.blit(score_text, (1100, 0))
        window.blit(fireballs_dodged_text, (screen_width - fireballs_dodged_text.get_width() - 10, 200))
        window.blit(birds_dodged_text, (screen_width - birds_dodged_text.get_width() - 10, 150))
        window.blit(meters_text, (screen_width - meters_text.get_width() - 10, 100))
        window.blit(high_score_text, (50, 0))
        window.blit(total_fireballs_dodged_text, (0, 200))
        window.blit(total_birds_dodged_text, (0, 150))
        window.blit(highest_meter_text, (0, 100))
        window.blit(money_text, ((screen_width - money_text.get_width() - 225), 600))
        window.blit(player1.img, (player1.x, player1.y))
        if data_shop['cowboy_hat_equipped'] == True:
            if player1.x == 740:
                Cowboy_Hat.x = 755
            elif player1.x == 590:
                Cowboy_Hat.x = 585
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            elif player1.x == 590:
                Thinking_Hat.x = 585
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            elif player1.x == 590:
                Top_Hat.x = 585
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            elif player1.x == 590:
                Red_Cap.image = transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            elif player1.x == 590:
                Party_Hat.x = 585
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            elif player1.x == 590:
                Witch_Hat.x = 585
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            elif player1.x == 590:
                Mexican_Hat.x = 585
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            elif player1.x == 590:
                King_Hat.x = 585
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(bird1.image, (bird1.x, bird1.y))
        window.blit(fireball1.image, (fireball1.x, fireball1.y))
        window.blit(Money.image, (Money.x, Money.y))
        display.update()
if __name__ == "__main__":
    start()