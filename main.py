print("The Game is launching.", end="\n")
#importing the modules
import moviepy.editor
import pygame
import random
import moviepy
import json
import os
#initializing
pygame.font.init()
pygame.mixer.init()
pygame.joystick.init()

#screen
screen_width = 1280
screen_height = 720
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cactus Climber")

#Joystick
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

#loading images
bottom_cactus = pygame.image.load(os.path.join('Images', 'cactus', 'bottom_cactus.png')).convert()
bottom_cactus = pygame.transform.scale(bottom_cactus, (100, 1000))

mid_cactus = pygame.image.load(os.path.join('Images', 'cactus', 'mid_cactus.png')).convert()
mid_cactus = pygame.transform.scale(mid_cactus, (100, 1000))

top_cactus = pygame.image.load(os.path.join('Images', 'cactus', 'top_cactus.png')).convert()
top_cactus = pygame.transform.scale(top_cactus, (100, 1000))
#setting the icon to an image
pygame.display.set_icon(mid_cactus)

#loading images
bg = pygame.image.load(os.path.join('Images', 'bg.png')).convert_alpha()

#variables + booleans
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

#loading images
easy_image = pygame.image.load(os.path.join('Images', 'difficulty', 'easy.png')).convert()
normal_image = pygame.image.load(os.path.join('Images', 'difficulty', 'normal.png')).convert()
hard_image = pygame.image.load(os.path.join('Images', 'difficulty', 'hard.png')).convert()
show_stats_image = pygame.image.load(os.path.join('Images', 'difficulty', 'show_stats.png')).convert()
hide_stats_image = pygame.image.load(os.path.join('Images', 'difficulty', 'hide_stats.png')).convert()

begin_player = pygame.image.load(os.path.join('Images', 'player', 'begin_player.png')).convert_alpha()
begin_player = pygame.transform.scale(begin_player, (100, 200))

back_image = pygame.image.load(os.path.join('Images', 'ui', 'back.png')).convert()
checked_off_image = pygame.image.load(os.path.join('Images', 'ui', 'checked_off.png')).convert()
checked_image = pygame.image.load(os.path.join('Images', 'ui', 'checked.png')).convert()
credits_image = pygame.image.load(os.path.join('Images', 'ui', 'credits.png')).convert()
music_image = pygame.image.load(os.path.join('Images', 'ui', 'music.png')).convert()
options_image = pygame.image.load(os.path.join('Images', 'ui', 'options.png')).convert()
play_image = pygame.image.load(os.path.join('Images', 'ui', 'play.png')).convert()
quit_image = pygame.image.load(os.path.join('Images', 'ui', 'quit.png')).convert()
sfx_image = pygame.image.load(os.path.join('Images', 'ui', 'sfx.png')).convert()
shop_image = pygame.image.load(os.path.join('Images', 'ui', 'shop.png')).convert()
reset_image = pygame.image.load(os.path.join('Images', 'ui', 'reset.png')).convert()

select_box_image = pygame.image.load(os.path.join('Images', 'ui', 'select_box.png')).convert_alpha()

textbox_image = pygame.image.load(os.path.join('Images', 'ui', 'TextBox.png')).convert()
yes_image = pygame.image.load(os.path.join('Images', 'ui', 'yes.png')).convert()
no_image = pygame.image.load(os.path.join('Images', 'ui', 'no.png')).convert()

red_cap_image = pygame.image.load(os.path.join('Images', 'shop', 'red_cap.png')).convert_alpha()
thinking_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'thinking_hat.png')).convert_alpha()
top_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'top_hat.png')).convert_alpha()
cowboy_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'cowboy_hat.png')).convert_alpha()
king_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'king_hat.png')).convert_alpha()
mexican_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'mexican_hat.png')).convert_alpha()
witch_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'witch_hat.png')).convert_alpha()
party_hat_image = pygame.image.load(os.path.join('Images', 'shop', 'party_hat.png')).convert_alpha()

money_image = pygame.image.load(os.path.join('Images', 'shop', 'money.png')).convert()
equip_image = pygame.image.load(os.path.join('Images', 'shop', 'equip.png')).convert()
unequip_image = pygame.image.load(os.path.join('Images', 'shop', 'unequip.png')).convert()
buy_image = pygame.image.load(os.path.join('Images', 'shop', 'buy.png')).convert()

credits_bg_image = pygame.image.load(os.path.join('Images', 'credits', 'credits_bg.png')).convert()

#loading sounds and music
maintheme = pygame.mixer.Sound(os.path.join('Music', 'maintheme.mp3'))
dodgemusic = pygame.mixer.Sound(os.path.join('Music', 'dodge!.mp3'))
firesound = pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'fire.mp3'))
birdsound = pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'bird.mp3'))

#data
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
    'show_easy': False,
    'show_normal': False,
    'show_hard': False
}
#loading data
try:
    with open(os.path.join('data','save_data_easy.json')) as save_data_easy:
        data_easy = json.load(save_data_easy)
    with open(os.path.join('data','save_data_normal.json')) as save_data_normal:
        data_normal = json.load(save_data_normal)
    with open(os.path.join('data','save_data_hard.json')) as save_data_hard:
        data_hard = json.load(save_data_hard)
    with open(os.path.join('data','save_data_shop.json')) as save_data_shop:
        data_shop = json.load(save_data_shop)
    with open(os.path.join('data','save_data_options.json')) as save_data_options:
        data_options = json.load(save_data_options)
except:
    print("")

#classes
class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
        self.img = pygame.transform.flip(self.img, 90, 0)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

class bird:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(os.path.join('Images', 'obstacles', 'bird.png')).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

class fireball:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(os.path.join('Images', 'obstacles', 'fireball.png')).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

class bird_rac:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(bottom_cactus, (self.width, self.height))

class difficulty_button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

class ui_button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

def win():
    Money = ui_button(1030, 600, 250, 100, money_image)
    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                pygame.quit()
                run = False
            
            if event.type == pygame.JOYAXISMOTION:
                io = round(pygame.joystick.Joystick(0).get_axis(0))
                if io == -1: #left
                    endvideo()
                 
        #text
        money_text = pygame.font.SysFont('comicsans', 80).render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        main_text = pygame.font.SysFont('comicsans', 40).render("Press A or Left key to Go Back Down", 1, (0, 0, 255))
        win_text = pygame.font.SysFont('comicsans', 40).render("You Reached the Top!", 1, (0, 0, 255))
        win1_text = pygame.font.SysFont('comicsans', 40).render("but at what Cost?", 1, (255, 0, 0))
        window.blit(win_text, (500, 0))
        window.blit(win1_text, (550, 50))
        window.blit(main_text, (360, 600))

        #keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            pygame.display.update()
            pygame.time.wait(3000)
            endvideo()
        
        #displaying on screen
        window.blit(money_text, ((screen_width - money_text.get_width() - 225), 600))

        window.blit(Money.image, (Money.x, Money.y))

        pygame.display.update()
def credits():
    global data_options
    Back = ui_button(1030, 600, 250, 100, back_image)
    Credits = ui_button(0, 0, screen_width, screen_height, credits_bg_image)
    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(1):
                        start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                back_rect = pygame.Rect(Back.x, Back.y, Back.width, Back.height)
                if back_rect.collidepoint(mousex, mousey):
                    start()
        window.blit(Credits.image, (Credits.x, Credits.y))
        window.blit(Back.image, (Back.x, Back.y))
        pygame.display.update()
def shop():
    global show_select_box, data_shop, data_options, play_denied, play_denied2, play_denied3, play_denied4, play_denied5, play_denied6, play_denied7, play_denied8

    move_delay = 150  # milliseconds
    last_move_time = pygame.time.get_ticks()

    Back = ui_button(0, 600, 250, 100, back_image)
    Select_Box = ui_button(50, 200, 100, 50, select_box_image)
    Cowboy_Hat = ui_button(50, 150, 100, 50, cowboy_hat_image)
    Thinking_Hat = ui_button(350, 150, 100, 50, thinking_hat_image)
    Top_Hat = ui_button(650, 150, 100, 50, top_hat_image)
    Red_Cap = ui_button(950, 150, 100, 50, red_cap_image)
    Party_Hat = ui_button(50, 300, 100, 50, party_hat_image)
    Witch_Hat = ui_button(350, 300, 100, 50, witch_hat_image)
    Mexican_Hat = ui_button(650, 300, 100, 50, mexican_hat_image)
    King_Hat = ui_button(950, 300, 100, 50, king_hat_image)
    Money = ui_button(0, 0, 250, 100, money_image)
    Equip = ui_button(10000, 200, 100, 50, equip_image)
    Equip2 = ui_button(10000, 200, 100, 50, equip_image)
    Equip3 = ui_button(10000, 200, 100, 50, equip_image)
    Equip4 = ui_button(10000, 200, 100, 50, equip_image)
    Equip5 = ui_button(10000, 350, 100, 50, equip_image)
    Equip6 = ui_button(10000, 350, 100, 50, equip_image)
    Equip7 = ui_button(10000, 350, 100, 50, equip_image)
    Equip8 = ui_button(10000, 350, 100, 50, equip_image)
    Unequip = ui_button(10000, 200, 100, 50, unequip_image)
    Unequip2 = ui_button(10000, 200, 100, 50, unequip_image)
    Unequip3 = ui_button(10000, 200, 100, 50, unequip_image)
    Unequip4 = ui_button(10000, 200, 100, 50, unequip_image)
    Unequip5 = ui_button(10000, 350, 100, 50, unequip_image)
    Unequip6 = ui_button(10000, 350, 100, 50, unequip_image)
    Unequip7 = ui_button(10000, 350, 100, 50, unequip_image)
    Unequip8 = ui_button(10000, 350, 100, 50, unequip_image)
    Buy = ui_button(50, 200, 100, 50, buy_image)
    Buy2 = ui_button(350, 200, 100, 50, buy_image)
    Buy3 = ui_button(650, 200, 100, 50, buy_image)
    Buy4 = ui_button(950, 200, 100, 50, buy_image)
    Buy5 = ui_button(50, 350, 100, 50, buy_image)
    Buy6 = ui_button(350, 350, 100, 50, buy_image)
    Buy7 = ui_button(650, 350, 100, 50, buy_image)
    Buy8 = ui_button(950, 350, 100, 50, buy_image)
    if data_shop['cowboy_hat_unlocked'] == True:
        Buy.image = pygame.transform.scale(buy_image, (0, 0))
        Buy.x = 10000
        Equip.image = pygame.transform.scale(equip_image, (100, 50))
        Equip.x = 50
    if data_shop['thinking_hat_unlocked'] == True:
        Buy2.image = pygame.transform.scale(buy_image, (0, 0))
        Buy2.x = 10000
        Equip2.image = pygame.transform.scale(equip_image, (100, 50))
        Equip2.x = 350
    if data_shop['top_hat_unlocked'] == True:
        Buy3.image = pygame.transform.scale(buy_image, (0, 0))
        Buy3.x = 10000
        Equip3.image = pygame.transform.scale(equip_image, (100, 50))
        Equip3.x = 650
    if data_shop['red_cap_unlocked'] == True:
        Buy4.image = pygame.transform.scale(buy_image, (0, 0))
        Buy4.x = 10000
        Equip4.image = pygame.transform.scale(equip_image, (100, 50))
        Equip4.x = 950
    if data_shop['party_hat_unlocked'] == True:
        Buy5.image = pygame.transform.scale(buy_image, (0, 0))
        Buy5.x = 10000
        Equip5.image = pygame.transform.scale(equip_image, (100, 50))
        Equip5.x = 50
    if data_shop['witch_hat_unlocked'] == True:
        Buy6.image = pygame.transform.scale(buy_image, (0, 0))
        Buy6.x = 10000
        Equip6.image = pygame.transform.scale(equip_image, (100, 50))
        Equip6.x = 350
    if data_shop['mexican_hat_unlocked'] == True:
        Buy7.image = pygame.transform.scale(buy_image, (0, 0))
        Buy7.x = 10000
        Equip7.image = pygame.transform.scale(equip_image, (100, 50))
        Equip7.x = 650
    if data_shop['king_hat_unlocked'] == True:
        Buy8.image = pygame.transform.scale(buy_image, (0, 0))
        Buy8.x = 10000
        Equip8.image = pygame.transform.scale(equip_image, (100, 50))
        Equip8.x = 950

    if data_shop['cowboy_hat_equipped'] == True:
        Equip.image = pygame.transform.scale(equip_image, (0, 0))
        Equip.x = 10000
        Unequip.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip.x = 50
    if data_shop['thinking_hat_equipped'] == True:
        Equip2.image = pygame.transform.scale(equip_image, (0, 0))
        Equip2.x = 10000
        Unequip2.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip2.x = 350
    if data_shop['top_hat_equipped'] == True:
        Equip3.image = pygame.transform.scale(equip_image, (0, 0))
        Equip3.x = 10000
        Unequip3.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip3.x = 650
    if data_shop['red_cap_equipped'] == True:
        Equip4.image = pygame.transform.scale(equip_image, (0, 0))
        Equip4.x = 10000
        Unequip4.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip4.x = 950
    if data_shop['party_hat_equipped'] == True:
        Equip5.image = pygame.transform.scale(equip_image, (0, 0))
        Equip5.x = 10000
        Unequip5.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip5.x = 50
    if data_shop['witch_hat_equipped'] == True:
        Equip6.image = pygame.transform.scale(equip_image, (0, 0))
        Equip6.x = 10000
        Unequip6.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip6.x = 350
    if data_shop['mexican_hat_equipped'] == True:
        Equip7.image = pygame.transform.scale(equip_image, (0, 0))
        Equip7.x = 10000
        Unequip7.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip7.x = 650
    if data_shop['king_hat_equipped'] == True:
        Equip8.image = pygame.transform.scale(equip_image, (0, 0))
        Equip8.x = 10000
        Unequip8.image = pygame.transform.scale(unequip_image, (100, 50))
        Unequip8.x = 950

    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
            current_time = pygame.time.get_ticks()
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(1):
                        start()
                #press triangle to show select box
                if pygame.joystick.Joystick(0).get_button(3):
                        show_select_box = True
                if pygame.joystick.Joystick(0).get_button(0):
                        if Select_Box.x == Buy.x and Select_Box.y == Buy.y and data_shop['money'] >= 100 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 100
                            data_shop['show_cost'] = False
                            data_shop['cowboy_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy.x = 10000
                            Equip.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip.x = 50
                            play_denied = False
                            last_move_time = current_time
                        if Select_Box.x == Buy2.x and Select_Box.y == Buy2.y and data_shop['money'] >= 250 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 250
                            data_shop['show_cost2'] = False
                            data_shop['thinking_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy2.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy2.x = 10000
                            Equip2.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip2.x = 350
                            play_denied2 = False
                            last_move_time = current_time
                        if Select_Box.x == Buy3.x and Select_Box.y == Buy3.y and data_shop['money'] >= 500 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 500
                            data_shop['show_cost3'] = False
                            data_shop['top_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy3.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy3.x = 10000
                            Equip3.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip3.x = 650
                            play_denied3 = False
                            last_move_time = current_time
                        if Select_Box.x == Buy4.x and Select_Box.y == Buy4.y and data_shop['money'] >= 1000 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 1000
                            data_shop['show_cost4'] = False
                            data_shop['red_cap_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy4.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy4.x = 10000
                            Equip4.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip4.x = 950
                            play_denied4 = False
                            last_move_time = current_time                        
                        if Select_Box.x == Buy5.x and Select_Box.y == Buy5.y and data_shop['money'] >= 100 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 100
                            data_shop['show_cost5'] = False
                            data_shop['party_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy5.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy5.x = 10000
                            Equip5.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip5.x = 50
                            play_denied5 = False
                            last_move_time = current_time
                        if Select_Box.x == Buy6.x and Select_Box.y == Buy6.y and data_shop['money'] >= 500 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 500
                            data_shop['show_cost7'] = False
                            data_shop['witch_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy6.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy6.x = 10000
                            Equip6.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip6.x = 350
                            play_denied6 = False
                            last_move_time = current_time
                        if Select_Box.x == Buy7.x and Select_Box.y == Buy7.y and data_shop['money'] >= 250 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 250
                            data_shop['show_cost6'] = False
                            data_shop['mexican_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy7.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy7.x = 10000
                            Equip7.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip7.x = 650
                            play_denied7 = False
                            last_move_time = current_time
                        if Select_Box.x == Buy8.x and Select_Box.y == Buy8.y and data_shop['money'] >= 2000 and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                            data_shop['money'] -= 2000
                            data_shop['show_cost8'] = False
                            data_shop['king_hat_unlocked'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Buy8.image = pygame.transform.scale(buy_image, (0, 0))
                            Buy8.x = 10000
                            Equip8.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip8.x = 950
                            play_denied8 = False
                            last_move_time = current_time
                        if Select_Box.x == Equip.x and Select_Box.y == Equip.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['cowboy_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip.x = 10000
                            Unequip.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip.x = 50
                            last_move_time = current_time
                        if Select_Box.x == Equip2.x and Select_Box.y == Equip2.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['thinking_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip2.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip2.x = 10000
                            Unequip2.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip2.x = 350
                            last_move_time = current_time
                        if Select_Box.x == Equip3.x and Select_Box.y == Equip3.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['top_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip3.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip3.x = 10000
                            Unequip3.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip3.x = 650
                            last_move_time = current_time
                        if Select_Box.x == Equip4.x and Select_Box.y == Equip4.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['red_cap_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip4.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip4.x = 10000
                            Unequip4.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip4.x = 950
                            last_move_time = current_time
                        if Select_Box.x == Equip5.x and Select_Box.y == Equip5.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['party_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip5.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip5.x = 10000
                            Unequip5.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip5.x = 50 
                            last_move_time = current_time
                        if Select_Box.x == Equip6.x and Select_Box.y == Equip6.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['witch_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip6.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip6.x = 10000
                            Unequip6.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip6.x = 350
                            last_move_time = current_time
                        if Select_Box.x == Equip7.x and Select_Box.y == Equip7.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['mexican_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip7.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip7.x = 10000
                            Unequip7.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip7.x = 650
                            last_move_time = current_time
                        if Select_Box.x == Equip8.x and Select_Box.y == Equip8.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_shop['king_hat_equipped'] = True
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip8.image = pygame.transform.scale(equip_image, (0, 0))
                            Equip8.x = 10000
                            Unequip8.image = pygame.transform.scale(unequip_image, (100, 50))
                            Unequip8.x = 950
                            last_move_time = current_time
                        if Select_Box.x == Unequip.x and Select_Box.y == Unequip.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['cowboy_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip.x = 50
                            Unequip.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip2.x and Select_Box.y == Unequip2.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['thinking_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip2.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip2.x = 350
                            Unequip2.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip2.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip3.x and Select_Box.y == Unequip3.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['top_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip3.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip3.x = 650
                            Unequip3.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip3.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip4.x and Select_Box.y == Unequip4.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['red_cap_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip4.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip4.x = 950
                            Unequip4.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip4.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip5.x and Select_Box.y == Unequip5.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['party_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip5.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip5.x = 50
                            Unequip5.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip5.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip6.x and Select_Box.y == Unequip6.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['witch_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip6.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip6.x = 350
                            Unequip6.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip6.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip7.x and Select_Box.y == Unequip7.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['mexican_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip7.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip7.x = 650
                            Unequip7.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip7.x = 10000
                            last_move_time = current_time
                        if Select_Box.x == Unequip8.x and Select_Box.y == Unequip8.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_shop['king_hat_equipped'] = False
                            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                                json.dump(data_shop, save_data_shop)
                            Equip8.image = pygame.transform.scale(equip_image, (100, 50))
                            Equip8.x = 950
                            Unequip8.image = pygame.transform.scale(unequip_image, (0, 0))
                            Unequip8.x = 10000
                            last_move_time = current_time
            #moving the select box
            if event.type == pygame.JOYAXISMOTION:
                io = round(pygame.joystick.Joystick(0).get_axis(0))
                io2 = round(pygame.joystick.Joystick(0).get_axis(1))
                if io == 1 and Select_Box.x < 900 and current_time - last_move_time > move_delay: #right
                    Select_Box.x += 300
                    last_move_time = current_time
                if io == -1 and Select_Box.x > 50 and current_time - last_move_time > move_delay: #left
                    Select_Box.x -= 300
                    last_move_time = current_time
                if io2 == -1 and Select_Box.y >= 350 and current_time - last_move_time > move_delay: #up
                    Select_Box.y -= 150
                    last_move_time = current_time
                if io2 == 1 and Select_Box.y < 350 and current_time - last_move_time > move_delay: #down
                    Select_Box.y += 150
                    last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                back_rect = pygame.Rect(Back.x, Back.y, Back.width, Back.height)
                equip_rect = pygame.Rect(Equip.x, Equip.y, Equip.width, Equip.height)
                unequip_rect = pygame.Rect(Unequip.x, Unequip.y, Unequip.width, Unequip.height)
                equip2_rect = pygame.Rect(Equip2.x, Equip2.y, Equip2.width, Equip2.height)
                unequip2_rect = pygame.Rect(Unequip2.x, Unequip2.y, Unequip2.width, Unequip2.height)
                equip3_rect = pygame.Rect(Equip3.x, Equip3.y, Equip3.width, Equip3.height)
                unequip3_rect = pygame.Rect(Unequip3.x, Unequip3.y, Unequip3.width, Unequip3.height)
                equip4_rect = pygame.Rect(Equip4.x, Equip4.y, Equip4.width, Equip4.height)
                unequip4_rect = pygame.Rect(Unequip4.x, Unequip4.y, Unequip4.width, Unequip4.height)
                equip5_rect = pygame.Rect(Equip5.x, Equip5.y, Equip5.width, Equip5.height)
                unequip5_rect = pygame.Rect(Unequip5.x, Unequip5.y, Unequip5.width, Unequip5.height)
                equip6_rect = pygame.Rect(Equip6.x, Equip6.y, Equip6.width, Equip6.height)
                unequip6_rect = pygame.Rect(Unequip6.x, Unequip6.y, Unequip6.width, Unequip6.height)
                equip7_rect = pygame.Rect(Equip7.x, Equip7.y, Equip7.width, Equip7.height)
                unequip7_rect = pygame.Rect(Unequip7.x, Unequip7.y, Unequip7.width, Unequip7.height)
                equip8_rect = pygame.Rect(Equip8.x, Equip8.y, Equip8.width, Equip8.height)
                unequip8_rect = pygame.Rect(Unequip8.x, Unequip8.y, Unequip8.width, Unequip8.height)
                buy_rect = pygame.Rect(Buy.x, Buy.y, Buy.width, Buy.height)
                buy2_rect = pygame.Rect(Buy2.x, Buy2.y, Buy2.width, Buy2.height)
                buy3_rect = pygame.Rect(Buy3.x, Buy3.y, Buy3.width, Buy3.height)
                buy4_rect = pygame.Rect(Buy4.x, Buy4.y, Buy4.width, Buy4.height)
                buy5_rect = pygame.Rect(Buy5.x, Buy5.y, Buy5.width, Buy5.height)
                buy6_rect = pygame.Rect(Buy6.x, Buy6.y, Buy6.width, Buy6.height)
                buy7_rect = pygame.Rect(Buy7.x, Buy7.y, Buy7.width, Buy7.height)
                buy8_rect = pygame.Rect(Buy8.x, Buy8.y, Buy8.width, Buy8.height)
                if back_rect.collidepoint(mousex, mousey):
                    start()

                if buy_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 100:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 100
                    data_shop['show_cost'] = False
                    data_shop['cowboy_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy.x = 10000
                    Equip.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip.x = 50
                    play_denied = False

                if buy_rect.collidepoint(mousex, mousey) and data_shop['money'] < 100 and play_denied == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if buy2_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 250:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 250
                    data_shop['show_cost2'] = False
                    data_shop['thinking_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy2.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy2.x = 10000
                    Equip2.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip2.x = 350
                    play_denied2 = False

                if buy2_rect.collidepoint(mousex, mousey) and data_shop['money'] < 250 and play_denied2 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if buy3_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 500:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 500
                    data_shop['show_cost3'] = False
                    data_shop['top_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy3.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy3.x = 10000
                    Equip3.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip3.x = 650
                    play_denied3 = False

                if buy3_rect.collidepoint(mousex, mousey) and data_shop['money'] < 500 and play_denied3 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if buy4_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 1000:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 1000
                    data_shop['show_cost4'] = False
                    data_shop['red_cap_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy4.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy4.x = 10000
                    Equip4.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip4.x = 950
                    play_denied4 = False

                if buy4_rect.collidepoint(mousex, mousey) and data_shop['money'] < 1000 and play_denied4 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if equip_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['cowboy_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip.x = 10000
                    Unequip.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip.x = 50 

                if unequip_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['cowboy_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip.x = 50
                    Unequip.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip.x = 10000

                if equip2_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['thinking_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip2.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip2.x = 10000
                    Unequip2.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip2.x = 350

                if unequip2_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['thinking_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip2.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip2.x = 350
                    Unequip2.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip2.x = 10000
                
                if equip3_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['top_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip3.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip3.x = 10000
                    Unequip3.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip3.x = 650
                
                if unequip3_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['top_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip3.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip3.x = 650
                    Unequip3.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip3.x = 10000
                
                if equip4_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['red_cap_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip4.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip4.x = 10000
                    Unequip4.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip4.x = 950

                if unequip4_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['red_cap_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip4.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip4.x = 950
                    Unequip4.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip4.x = 10000

                if buy5_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 100:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 100
                    data_shop['show_cost5'] = False
                    data_shop['party_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy5.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy5.x = 10000
                    Equip5.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip5.x = 50
                    play_denied5 = False

                if buy5_rect.collidepoint(mousex, mousey) and data_shop['money'] < 100 and play_denied5 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if buy6_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 500:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 500
                    data_shop['show_cost7'] = False
                    data_shop['witch_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy6.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy6.x = 10000
                    Equip6.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip6.x = 350
                    play_denied6 = False

                if buy6_rect.collidepoint(mousex, mousey) and data_shop['money'] < 500 and play_denied6 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if buy7_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 250:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 250
                    data_shop['show_cost6'] = False
                    data_shop['mexican_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy7.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy7.x = 10000
                    Equip7.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip7.x = 650
                    play_denied7 = False

                if buy7_rect.collidepoint(mousex, mousey) and data_shop['money'] < 250 and play_denied7 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if buy8_rect.collidepoint(mousex, mousey) and data_shop['money'] >= 2000:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'buy.mp3')).play()
                    data_shop['money'] -= 2000
                    data_shop['show_cost8'] = False
                    data_shop['king_hat_unlocked'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Buy8.image = pygame.transform.scale(buy_image, (0, 0))
                    Buy8.x = 10000
                    Equip8.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip8.x = 950
                    play_denied8 = False

                if buy8_rect.collidepoint(mousex, mousey) and data_shop['money'] < 2000 and play_denied8 == True:
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()

                if equip5_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['party_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip5.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip5.x = 10000
                    Unequip5.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip5.x = 50 

                if unequip5_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['party_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip5.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip5.x = 50
                    Unequip5.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip5.x = 10000

                if equip6_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['witch_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip6.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip6.x = 10000
                    Unequip6.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip6.x = 350

                if unequip6_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['witch_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip6.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip6.x = 350
                    Unequip6.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip6.x = 10000
                
                if equip7_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['mexican_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip7.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip7.x = 10000
                    Unequip7.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip7.x = 650
                
                if unequip7_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['mexican_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip7.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip7.x = 650
                    Unequip7.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip7.x = 10000
                
                if equip8_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_shop['king_hat_equipped'] = True
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip8.image = pygame.transform.scale(equip_image, (0, 0))
                    Equip8.x = 10000
                    Unequip8.image = pygame.transform.scale(unequip_image, (100, 50))
                    Unequip8.x = 950

                if unequip8_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_shop['king_hat_equipped'] = False
                    with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                        json.dump(data_shop, save_data_shop)
                    Equip8.image = pygame.transform.scale(equip_image, (100, 50))
                    Equip8.x = 950
                    Unequip8.image = pygame.transform.scale(unequip_image, (0, 0))
                    Unequip8.x = 10000

        cost_text = pygame.font.SysFont('comicsans', 40).render("100", 1, (64, 255, 25))
        cost2_text = pygame.font.SysFont('comicsans', 40).render("250", 1, (64, 255, 25))
        cost3_text = pygame.font.SysFont('comicsans', 40).render("500", 1, (64, 255, 25))
        cost4_text = pygame.font.SysFont('comicsans', 40).render("1000", 1, (64, 255, 25))
        cost5_text = pygame.font.SysFont('comicsans', 40).render("100", 1, (64, 255, 25))
        cost6_text = pygame.font.SysFont('comicsans', 40).render("250", 1, (64, 255, 25))
        cost7_text = pygame.font.SysFont('comicsans', 40).render("500", 1, (64, 255, 25))
        cost8_text = pygame.font.SysFont('comicsans', 40).render("2000", 1, (64, 255, 25))
        money_text = pygame.font.SysFont('comicsans', 80).render(f": {data_shop['money']}", 1, (64, 255, 25))
        
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
        pygame.display.update()
                
def options():
    global data_options, show_select_box

    move_delay = 150  # milliseconds
    last_move_time = pygame.time.get_ticks()

    Select_Box = ui_button(760, 400, 250, 100, select_box_image)
    Back = ui_button(0, 600, 250, 100, back_image)
    Checked_off = ui_button(10000, 400, 250, 100, checked_off_image)
    Checked_off2 = ui_button(10000, 300, 250, 100, checked_off_image)
    Checked = ui_button(760, 400, 250, 100, checked_image)
    Checked2 = ui_button(760, 300, 250, 100, checked_image)
    Music = ui_button(500, 400, 250, 100, music_image)
    SFX = ui_button(500, 300, 250, 100, sfx_image)

    
    if data_options['play_music'] == False: 
        Checked.image = pygame.transform.scale(checked_image, (0, 0))
        Checked.x = 10000
        Checked_off.image = pygame.transform.scale(checked_off_image, (250, 100))
        Checked_off.x = 760
    if data_options['play_music'] == True:
        Checked.image = pygame.transform.scale(checked_image, (250, 100))
        Checked.x = 760
        Checked_off.image = pygame.transform.scale(checked_off_image, (0, 0))
        Checked_off.x = 10000
    if data_options['play_sfx'] == False:
        Checked2.image = pygame.transform.scale(checked_image, (0, 0))
        Checked2.x = 10000
        Checked_off2.image = pygame.transform.scale(checked_off_image, (250, 100))
        Checked_off2.x = 760
    if data_options['play_sfx'] == True:
        Checked2.image = pygame.transform.scale(checked_image, (250, 100))
        Checked2.x = 760
        Checked_off2.image = pygame.transform.scale(checked_off_image, (0, 0))
        Checked_off2.x = 10000

    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
            current_time = pygame.time.get_ticks()
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(1):
                        start()
                if pygame.joystick.Joystick(0).get_button(3):
                        show_select_box = True
                if pygame.joystick.Joystick(0).get_button(0):
                        if Select_Box.y == Checked.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_options['play_music'] = False
                            with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                                json.dump(data_options, save_data_options)
                            Checked.image = pygame.transform.scale(checked_image, (0, 0))
                            Checked.x = 10000
                            Checked_off.image = pygame.transform.scale(checked_off_image, (250, 100))
                            Checked_off.x = 760
                            last_move_time = current_time
                        if Select_Box.y == Checked_off.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            data_options['play_music'] = True
                            with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                                json.dump(data_options, save_data_options)
                            Checked.image = pygame.transform.scale(checked_image, (250, 100))
                            Checked.x = 760
                            Checked_off.image = pygame.transform.scale(checked_off_image, (0, 0))
                            Checked_off.x = 10000
                            last_move_time = current_time
                        if Select_Box.y == Checked2.y and current_time - last_move_time > move_delay:
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                            data_options['play_sfx'] = False
                            with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                                json.dump(data_options, save_data_options)
                            Checked2.image = pygame.transform.scale(checked_image, (0, 0))
                            Checked2.x = 10000
                            Checked_off2.image = pygame.transform.scale(checked_off_image, (250, 100))
                            Checked_off2.x = 760
                            last_move_time = current_time
                        if Select_Box.y == Checked_off2.y and current_time - last_move_time > move_delay:
                            data_options['play_sfx'] = True
                            if data_options['play_sfx'] == True:
                                pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                            with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                                json.dump(data_options, save_data_options)
                            Checked2.image = pygame.transform.scale(checked_image, (250, 100))
                            Checked2.x = 760
                            Checked_off2.image = pygame.transform.scale(checked_off_image, (0, 0))
                            Checked_off2.x = 10000
                            last_move_time = current_time

            if event.type == pygame.JOYAXISMOTION:
                io2 = round(pygame.joystick.Joystick(0).get_axis(1))
                if io2 == -1 and Select_Box.y >= 400: #up
                    Select_Box.y -= 100
                    
                if io2 == 1 and Select_Box.y < 400: #down
                    Select_Box.y += 100
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                back_rect = pygame.Rect(Back.x, Back.y, Back.width, Back.height)
                checked_off_rect = pygame.Rect(Checked_off.x, Checked_off.y, Checked_off.width, Checked_off.height)
                checked_rect = pygame.Rect(Checked.x, Checked.y, Checked.width, Checked.height)
                checked_off2_rect = pygame.Rect(Checked_off2.x, Checked_off2.y, Checked_off2.width, Checked_off2.height)
                checked2_rect = pygame.Rect(Checked2.x, Checked2.y, Checked2.width, Checked2.height)

                if back_rect.collidepoint(mousex, mousey):
                    start()
                if checked_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_options['play_music'] = False
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Checked.image = pygame.transform.scale(checked_image, (0, 0))
                    Checked.x = 10000
                    Checked_off.image = pygame.transform.scale(checked_off_image, (250, 100))
                    Checked_off.x = 760
                if checked_off_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    data_options['play_music'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Checked.image = pygame.transform.scale(checked_image, (250, 100))
                    Checked.x = 760
                    Checked_off.image = pygame.transform.scale(checked_off_image, (0, 0))
                    Checked_off.x = 10000
                if checked2_rect.collidepoint(mousex, mousey):
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                    data_options['play_sfx'] = False
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Checked2.image = pygame.transform.scale(checked_image, (0, 0))
                    Checked2.x = 10000
                    Checked_off2.image = pygame.transform.scale(checked_off_image, (250, 100))
                    Checked_off2.x = 760
                if checked_off2_rect.collidepoint(mousex, mousey):
                    data_options['play_sfx'] = True
                    if data_options['play_sfx'] == True:
                        pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Checked2.image = pygame.transform.scale(checked_image, (250, 100))
                    Checked2.x = 760
                    Checked_off2.image = pygame.transform.scale(checked_off_image, (0, 0))
                    Checked_off2.x = 10000
        window.fill((204, 102, 25))
        window.blit(Back.image, (Back.x, Back.y))
        window.blit(Music.image, (Music.x, Music.y))
        window.blit(SFX.image, (SFX.x, SFX.y))
        window.blit(Checked.image, (Checked.x, Checked.y))
        window.blit(Checked_off.image, (Checked_off.x, Checked_off.y))
        window.blit(Checked2.image, (Checked2.x, Checked2.y))
        window.blit(Checked_off2.image, (Checked_off2.x, Checked_off2.y))
        if show_select_box == True:
            window.blit(Select_Box.image, (Select_Box.x, Select_Box.y))
        pygame.display.update()
def start():
    global show_textbox, show_start, data_easy, data_normal, data_hard, data_options, data_shop
    Play = ui_button(500, 150, 250, 100, play_image)
    Options = ui_button(500, 260, 250, 100, options_image)
    Shop = ui_button(500, 370, 250, 100, shop_image)
    Credits = ui_button(500, 480, 250, 100, credits_image)
    Quit = ui_button(500, 600, 250, 100, quit_image)
    Reset = ui_button(1030, 0, 250, 100, reset_image)
    Yes = ui_button(450, 500, 150, 100, yes_image)
    No = ui_button(700, 500, 150, 100, no_image)
    TextBox = ui_button(450, 200, 400, 400, textbox_image)
    show_textbox = False
    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
            if event.type == pygame.JOYBUTTONDOWN:
                if show_textbox == True:
                    if pygame.joystick.Joystick(0).get_button(1):
                        if data_options['play_sfx'] == True:
                            pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                        show_textbox = False
                        show_start = True
                        start()
                    if pygame.joystick.Joystick(0).get_button(0):
                        if data_options['play_sfx'] == True:
                            pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
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
                        with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                            json.dump(data_easy, save_data_easy)
                        with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                            json.dump(data_normal, save_data_normal)
                        with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                            json.dump(data_hard, save_data_hard)
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                            json.dump(data_options, save_data_options)
                        show_start = True
                        start()
                if show_start == True:
                    if pygame.joystick.Joystick(0).get_button(0):
                        mainmenu()
                    if pygame.joystick.Joystick(0).get_button(2):
                        shop()
                    if pygame.joystick.Joystick(0).get_button(3):
                        credits()
                    if pygame.joystick.Joystick(0).get_button(4):
                        run = False
                        pygame.quit()
                    if pygame.joystick.Joystick(0).get_button(5):
                        show_textbox = True
                        show_start = False
                    if pygame.joystick.Joystick(0).get_button(7):
                        options()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()

                play_rect = pygame.Rect(Play.x, Play.y, Play.width, Play.height)
                options_rect = pygame.Rect(Options.x, Options.y, Options.width, Options.height)
                shop_rect = pygame.Rect(Shop.x, Shop.y, Shop.width, Shop.height)
                credits_rect = pygame.Rect(Credits.x, Credits.y, Credits.width, Credits.height)
                quit_rect = pygame.Rect(Quit.x, Quit.y, Quit.width, Quit.height)
                reset_rect = pygame.Rect(Reset.x, Reset.y, Reset.width, Reset.height)
                yes_rect = pygame.Rect(Yes.x, Yes.y, Yes.width, Yes.height)
                no_rect = pygame.Rect(No.x, No.y, No.width, No.height)
                if show_start == True:
                    if play_rect.collidepoint(mousex, mousey):
                        mainmenu()
                    if quit_rect.collidepoint(mousex, mousey):
                        run = False
                        pygame.quit()
                    if options_rect.collidepoint(mousex, mousey):
                        options()
                    if shop_rect.collidepoint(mousex, mousey):
                        shop()
                    if credits_rect.collidepoint(mousex, mousey):
                        credits()
                if show_textbox == True:
                    if no_rect.collidepoint(mousex, mousey):
                        if data_options['play_sfx'] == True:
                            pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'denied.mp3')).play()
                        show_textbox = False
                        show_start = True
                        start()
                    if yes_rect.collidepoint(mousex, mousey):
                        if data_options['play_sfx'] == True:
                            pygame.mixer.Sound(os.path.join('Music', 'Sounds', 'equipped.mp3')).play()
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
                        with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                            json.dump(data_easy, save_data_easy)
                        with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                            json.dump(data_normal, save_data_normal)
                        with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                            json.dump(data_hard, save_data_hard)
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                            json.dump(data_options, save_data_options)
                        show_start = True
                        start()
                if reset_rect.collidepoint(mousex, mousey):
                    show_textbox = True
                    show_start = False
        #text5
        title_text = pygame.font.SysFont('comicsans', 90).render("Cactus Climber", 1, (64, 255, 25)) 
        version_text = pygame.font.SysFont('comicsans', 40).render("v1.2.6", 1, (64, 255, 25))
        window.fill((204, 102, 25))
        window.blit(Play.image, (Play.x, Play.y))
        window.blit(Options.image, (Options.x, Options.y))
        window.blit(Shop.image, (Shop.x, Shop.y))
        window.blit(Credits.image, (Credits.x, Credits.y))
        window.blit(Quit.image, (Quit.x, Quit.y))
        window.blit(Reset.image, (Reset.x, Reset.y))
        window.blit(title_text, (350, 0))
        window.blit(version_text, (0, 0))
        if show_textbox == True:
            window.blit(TextBox.image, (TextBox.x, TextBox.y))
            window.blit(No.image, (No.x, No.y))
            window.blit(Yes.image, (Yes.x, Yes.y))
        pygame.display.update()

def mainmenu():
    global diff, data_options
    Money = ui_button(1030, 0, 250, 100, money_image)
    Back = ui_button(0, 670, 100, 50, back_image)
    Easy = difficulty_button(50, 300, 350, 200, easy_image)
    Normal = difficulty_button(450, 300, 350, 200, normal_image)
    Hard = difficulty_button(850, 300, 350, 200, hard_image)
    Easy_Stats = difficulty_button(50, 500, 250, 50, show_stats_image)
    Normal_Stats = difficulty_button(450, 500, 250, 50, show_stats_image)
    Hard_Stats = difficulty_button(850, 500, 250, 50, show_stats_image)
    Easy_Hide_Stats = difficulty_button(10050, 500, 250, 50, hide_stats_image)
    Normal_Hide_Stats = difficulty_button(1450, 500, 250, 50, hide_stats_image)
    Hard_Hide_Stats = difficulty_button(1850, 500, 250, 50, hide_stats_image)
    if data_options['show_easy'] == True:
            Easy_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
            Easy_Stats.x = 10000
            Easy_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
            Easy_Hide_Stats.x = 50
    if data_options['show_normal'] == True:
            Normal_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
            Normal_Stats.x = 10000
            Normal_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
            Normal_Hide_Stats.x = 450
    if data_options['show_hard'] == True:
            Hard_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
            Hard_Stats.x = 10000
            Hard_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
            Hard_Hide_Stats.x = 850
    maintheme.stop()
    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                pygame.quit()
                run = False
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(3):
                    diff = 1
                    mainspot()
                if pygame.joystick.Joystick(0).get_button(2):
                    diff = 2
                    mainspot()
                if pygame.joystick.Joystick(0).get_button(0):
                    diff = 3
                    mainspot()
                if pygame.joystick.Joystick(0).get_button(1):
                    start()
                if pygame.joystick.Joystick(0).get_button(4):
                    data_options['show_easy'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Easy_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Easy_Stats.x = 10000
                    Easy_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
                    Easy_Hide_Stats.x = 50
                if pygame.joystick.Joystick(0).get_button(5):
                    data_options['show_normal'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Normal_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Normal_Stats.x = 10000
                    Normal_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
                    Normal_Hide_Stats.x = 450
                if pygame.joystick.Joystick(0).get_button(7):
                    data_options['show_hard'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Hard_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Hard_Stats.x = 10000
                    Hard_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
                    Hard_Hide_Stats.x = 850
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()

                easy_rect = pygame.Rect(Easy.x, Easy.y, Easy.width, Easy.height)
                normal_rect = pygame.Rect(Normal.x, Normal.y, Normal.width, Normal.height)
                hard_rect = pygame.Rect(Hard.x, Hard.y, Hard.width, Hard.height)
                easy_stats_rect = pygame.Rect(Easy_Stats.x, Easy_Stats.y, Easy_Stats.width, Easy_Stats.height)
                normal_stats_rect = pygame.Rect(Normal_Stats.x, Normal_Stats.y, Normal_Stats.width, Normal_Stats.height)
                hard_stats_rect = pygame.Rect(Hard_Stats.x, Hard_Stats.y, Hard_Stats.width, Hard_Stats.height)
                easy_hide_stats_rect = pygame.Rect(Easy_Hide_Stats.x, Easy_Hide_Stats.y, Easy_Hide_Stats.width, Easy_Hide_Stats.height)
                normal_hide_stats_rect = pygame.Rect(Normal_Hide_Stats.x, Normal_Hide_Stats.y, Normal_Hide_Stats.width, Normal_Hide_Stats.height)
                hard_hide_stats_rect = pygame.Rect(Hard_Hide_Stats.x, Hard_Hide_Stats.y, Hard_Hide_Stats.width, Hard_Hide_Stats.height)
                back_rect = pygame.Rect(Back.x, Back.y, Back.width, Back.height)
                
                if easy_rect.collidepoint(mousex, mousey):
                    diff = 1
                    mainspot()
                if normal_rect.collidepoint(mousex, mousey):
                    diff = 2
                    mainspot()
                if hard_rect.collidepoint(mousex, mousey):
                    diff = 3
                    mainspot()

                if easy_stats_rect.collidepoint(mousex, mousey):   
                    data_options['show_easy'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Easy_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Easy_Stats.x = 10000
                    Easy_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
                    Easy_Hide_Stats.x = 50
                
                if easy_hide_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_easy'] = False
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Easy_Stats.image = pygame.transform.scale(show_stats_image, (250, 50))
                    Easy_Stats.x = 50
                    Easy_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Easy_Hide_Stats.x = 10000

                if normal_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_normal'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Normal_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Normal_Stats.x = 10000
                    Normal_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
                    Normal_Hide_Stats.x = 450
                
                if normal_hide_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_normal'] = False
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Normal_Stats.image = pygame.transform.scale(show_stats_image, (250, 50))
                    Normal_Stats.x = 450
                    Normal_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Normal_Hide_Stats.x = 10000

                if hard_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_hard'] = True
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Hard_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Hard_Stats.x = 10000
                    Hard_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (250, 50))
                    Hard_Hide_Stats.x = 850

                if hard_hide_stats_rect.collidepoint(mousex, mousey):
                    data_options['show_hard'] = False
                    with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                        json.dump(data_options, save_data_options)
                    Hard_Stats.image = pygame.transform.scale(show_stats_image, (250, 50))
                    Hard_Stats.x = 850
                    Hard_Hide_Stats.image = pygame.transform.scale(hide_stats_image, (0, 0))
                    Hard_Hide_Stats.x = 1850
                
                if back_rect.collidepoint(mousex, mousey):
                    start()

        #text
        full_meter_normal_text = pygame.font.SysFont('comicsans', 20).render("(cactus is 117m)", 1, (255, 255, 255))
        total_fireballs_dodged_normal_text = pygame.font.SysFont('comicsans', 20).render(f"Total Fireballs Dodged: {data_normal['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_normal_text = pygame.font.SysFont('comicsans', 20).render(f"Total Meters Climbed: {data_normal['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_normal_text = pygame.font.SysFont('comicsans', 20).render(f"Total Birds Dodged: {data_normal['birds_dodged']}", 1, (255, 255, 255))

        full_meter_hard_text = pygame.font.SysFont('comicsans', 20).render("(cactus is 217m)", 1, (255, 255, 255))
        total_fireballs_dodged_hard_text = pygame.font.SysFont('comicsans', 20).render(f"Total Fireballs Dodged: {data_hard['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_hard_text = pygame.font.SysFont('comicsans', 20).render(f"Total Meters Climbed: {data_hard['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_hard_text = pygame.font.SysFont('comicsans', 20).render(f"Total Birds Dodged: {data_hard['birds_dodged']}", 1, (255, 255, 255))
        
        full_meter_easy_text = pygame.font.SysFont('comicsans', 20).render("(cactus is 57m)", 1, (255, 255, 255))
        total_fireballs_dodged_easy_text = pygame.font.SysFont('comicsans', 20).render(f"Total Fireballs Dodged: {data_easy['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_easy_text = pygame.font.SysFont('comicsans', 20).render(f"Total Meters Climbed: {data_easy['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_easy_text = pygame.font.SysFont('comicsans', 20).render(f"Total Birds Dodged: {data_easy['birds_dodged']}", 1, (255, 255, 255))

        title_text = pygame.font.SysFont('comicsans', 140).render("Cactus Climber", 1, (64, 255, 25)) 
        version_text = pygame.font.SysFont('comicsans', 40).render("v1.2.6", 1, (64, 255, 25))
        money_text = pygame.font.SysFont('comicsans', 80).render(f"{data_shop['money']} : ", 1, (64, 255, 25))

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
        pygame.display.update()

def mainspot():
    global data_shop
    Cowboy_Hat = ui_button(175, 380, 40, 30, cowboy_hat_image)
    Thinking_Hat = ui_button(175, 380, 40, 30, thinking_hat_image)
    Top_Hat = ui_button(175, 375, 40, 30, top_hat_image)
    Red_Cap = ui_button(180, 380, 40, 30, red_cap_image)
    Red_Cap.image = pygame.transform.flip(Red_Cap.image, 90, 0)
    Party_Hat = ui_button(175, 380, 40, 30, party_hat_image)
    Witch_Hat = ui_button(175, 375, 40, 30, witch_hat_image)
    Mexican_Hat = ui_button(175, 380, 40, 30, mexican_hat_image)
    King_Hat = ui_button(175, 380, 40, 30, king_hat_image)
    maintheme.stop()
    run = True
    clockyy = pygame.time.Clock()
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
            if event.type == pygame.JOYAXISMOTION:
                io = round(pygame.joystick.Joystick(0).get_axis(0))
                if io == 1 and diff == 1: #right
                    firstvideo_easy()
                if io == 1 and diff == 2: #right
                    firstvideo_normal()
                if io == 1 and diff == 3: #right
                    firstvideo_hard()

        begin_text = pygame.font.SysFont('comicsans', 40).render("Press D or Right key to Climb", 1, (0, 0, 255))
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and diff == 1 or keys[pygame.K_RIGHT] and diff == 1:
            firstvideo_easy()

        if keys[pygame.K_d] and diff == 2 or keys[pygame.K_RIGHT] and diff == 2:
            firstvideo_normal()

        if keys[pygame.K_d] and diff == 3 or keys[pygame.K_RIGHT] and diff == 3:
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
        pygame.display.update()

def endvideo():
    run = True
    clockyy = pygame.time.Clock()
    endvid = moviepy.editor.VideoFileClip("Videos/end.mp4")
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
                
        endvid.preview()
        pygame.display.update()
        pygame.time.wait(5000)

        endvid.close()
        mainmenu()

def firstvideo_easy():
    run = True
    clockyy = pygame.time.Clock()
    beginvid = moviepy.editor.VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
                
        beginvid.preview()
        pygame.display.update()

        beginvid.close()
        main_easy()

def firstvideo_normal():
    run = True
    clockyy = pygame.time.Clock()
    beginvid = moviepy.editor.VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
                
        beginvid.preview()
        pygame.display.update()

        beginvid.close()
        main_normal()

def firstvideo_hard():
    run = True
    clockyy = pygame.time.Clock()
    beginvid = moviepy.editor.VideoFileClip("Videos/begin.mp4")
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
                
        beginvid.preview()
        pygame.display.update()

        beginvid.close()
        main_hard()

def fireballdeathvid():
    run = True
    clockyy = pygame.time.Clock()
    fireballdeath = moviepy.editor.VideoFileClip("Videos/fireballdeath.mp4")
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
                
        fireballdeath.preview()
        pygame.display.update()

        pygame.time.wait(4000)
        fireballdeath.close()
        mainmenu()

def birddeathvid():
    run = True
    clockyy = pygame.time.Clock()
    birddeath = moviepy.editor.VideoFileClip("Videos/birddeath.mp4")
    while run:  
        clockyy.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                pygame.quit()
                run = False
                
        birddeath.preview()
        pygame.display.update()

        pygame.time.wait(4000)
        birddeath.close()
        mainmenu()

def main_easy():
    global data_easy, data_options, data_shop
    if data_options['play_music'] == True:
        maintheme.play(-1)
    fireballs_dodged = 0
    meters_up = 0
    birds_dodged = 0
    flap = False
    flap2 = True
    player1 = player(590, 300, 50, 100)
    bird1 = bird(0, 720, 100, 100)
    fireball1 = fireball(760, player1.y - 1000, 25, 25)
    bird_rac1 = bird_rac(0, 300, 740, 100)
    Money = ui_button(1030, 600, 250, 100, money_image)
    
    run = True
    bgy = 0
    cactusy = -500
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                run = False
                pygame.quit()
            if event.type == pygame.JOYAXISMOTION:
                io = round(pygame.joystick.Joystick(0).get_axis(0))
                if io == 1: #right 
                    if flap2 == True:
                        data_shop['money'] += 1
                        data_easy['meters_up'] += 1
                        meters_up += 1
                        player1.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
                        player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                        player1.x += 150
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                            json.dump(data_easy, save_data_easy)
                        cactusy += 50
                        bgy += 50
                        bird1.y += 150
                        fireball1.y += 150
                        flap2 = False
                        flap = True
                if io == -1: #left
                    if flap == True:
                        data_shop['money'] += 1
                        data_easy['meters_up'] += 1
                        meters_up += 1
                        player1.img = pygame.image.load(os.path.join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                        player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                        player1.x -= 150
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                            json.dump(data_easy, save_data_easy)
                        cactusy += 50
                        bgy += 50
                        bird1.y += 150
                        fireball1.y += 150
                        flap = False
                        flap2 = True
        Cowboy_Hat = ui_button(player1.x, player1.y - 20, 40, 30, cowboy_hat_image)
        Thinking_Hat = ui_button(player1.x, player1.y - 20, 40, 30, thinking_hat_image)
        Top_Hat = ui_button(player1.x, player1.y - 20, 40, 30, top_hat_image)
        Red_Cap = ui_button(player1.x, player1.y - 20, 40, 30, red_cap_image)
        Party_Hat = ui_button(player1.x, player1.y - 20, 40, 30, party_hat_image)
        Witch_Hat = ui_button(player1.x, player1.y - 20, 40, 30, witch_hat_image)
        Mexican_Hat = ui_button(player1.x, player1.y - 20, 40, 30, mexican_hat_image)
        King_Hat = ui_button(player1.x, player1.y - 20, 40, 30, king_hat_image)
        fireball_rect = pygame.Rect(fireball1.x, fireball1.y, fireball1.width, fireball1.height)
        bird_rect = pygame.Rect(bird1.x, bird1.y, bird1.width, bird1.height)
        bird_rac_rect = pygame.Rect(bird_rac1.x, bird_rac1.y, bird_rac1.width, bird_rac1.height)
        player_rect = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
        top_cactus_rect = pygame.Rect(640, cactusy - 2800, 100, 800)

        if player_rect.colliderect(fireball_rect):
            with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
            with open(os.path.join('data','save_data_easy.json')) as save_data_easy:
                    data_easy = json.load(save_data_easy)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            fireballdeathvid()
        if player_rect.colliderect(bird_rect):
            with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
            with open(os.path.join('data','save_data_easy.json')) as save_data_easy:
                    data_easy = json.load(save_data_easy)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            birddeathvid()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                data_easy['meters_up'] += 1
                meters_up += 1
                player1.img = pygame.image.load(os.path.join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                player1.x -= 150
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                cactusy += 50
                bgy += 50
                bird1.y += 150
                fireball1.y += 150
                flap = False
                flap2 = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if flap2 == True:
                data_shop['money'] += 1
                data_easy['meters_up'] += 1
                meters_up += 1
                player1.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
                player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                player1.x += 150
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
                cactusy += 50
                bgy += 50
                bird1.y += 150
                fireball1.y += 150
                flap2 = False
                flap = True
        
        fireball1.y += 10
        if fireball1.y >= screen_height:
            fireball1.y = -1000
            fireball1.x = random.choice([585, 760])
            data_easy['fireballs_dodged'] += 1
            with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
            fireballs_dodged += 1
    
        bird1.x += 10
        if bird1.x >= screen_width:
            bird1.x = -1000
            data_easy['birds_dodged'] += 1
            with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
            birds_dodged += 1
        if bird1.y >= screen_height:
            bird1.x = -1000
            bird1.y = random.randint(300, 800)
            data_easy['birds_dodged'] += 1
            with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
            birds_dodged += 1

        dodge_text_red = pygame.font.SysFont('comicsans', 20).render("dodge!", 1, (255, 0, 0))
        dodge_text = pygame.font.SysFont('comicsans', 20).render("dodge!", 1, (255, 255, 255))
    
        #show dogde text when fireball above player
        if fireball1.y >= 0 and fireball1.x == 585 and player1.x == 590 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()

        if fireball1.y >= 0 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            
        if bird_rect.colliderect(bird_rac_rect):   
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
        
        if bird_rac_rect.colliderect(top_cactus_rect):
            with open(os.path.join('data', 'save_data_easy.json'),'w') as save_data_easy:
                    json.dump(data_easy, save_data_easy)
            with open(os.path.join('data','save_data_easy.json')) as save_data_easy:
                    data_easy = json.load(save_data_easy)
            data_shop['money'] += 100
            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
            if data_options['play_sfx'] == True:
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            win()

        high_score_text = pygame.font.SysFont('comicsans', 40).render("High Scores", 1, (255, 255, 255))
        total_fireballs_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Total Fireballs Dodged: {data_easy['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_text = pygame.font.SysFont('comicsans', 40).render(f"Total Meters Climbed: {data_easy['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Total Birds Dodged: {data_easy['birds_dodged']}", 1, (255, 255, 255))

        score_text = pygame.font.SysFont('comicsans', 40).render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = pygame.font.SysFont('comicsans', 40).render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))

        money_text = pygame.font.SysFont('comicsans', 80).render(f"{data_shop['money']} : ", 1, (64, 255, 25))
        
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
            if player1.x == 590:
                Cowboy_Hat.x = 585
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            if player1.x == 590:
                Thinking_Hat.x = 585
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            if player1.x == 590:
                Top_Hat.x = 585
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            if player1.x == 590:
                Red_Cap.image = pygame.transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            if player1.x == 590:
                Party_Hat.x = 585
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            if player1.x == 590:
                Witch_Hat.x = 585
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            if player1.x == 590:
                Mexican_Hat.x = 585
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            if player1.x == 590:
                King_Hat.x = 585
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(bird1.img, (bird1.x, bird1.y))
        window.blit(fireball1.img, (fireball1.x, fireball1.y))

        window.blit(Money.image, (Money.x, Money.y))
        
        pygame.display.update()

def main_normal():
    global data_normal, data_options, data_shop
    if data_options['play_music'] == True:
        maintheme.play(-1)
    fireballs_dodged = 0
    meters_up = 0
    birds_dodged = 0
    flap = False
    flap2 = True
    player1 = player(590, 300, 50, 100)
    bird1 = bird(0, 600, 100, 100)
    fireball1 = fireball(760, player1.y - 1000, 25, 25)
    bird_rac1 = bird_rac(0, 300, 740, 100)
    Money = ui_button(1030, 600, 250, 100, money_image)
    run = True
    bgy = 0
    cactusy = -500
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                run = False
                pygame.quit()
            if event.type == pygame.JOYAXISMOTION:
                io = round(pygame.joystick.Joystick(0).get_axis(0))
                if io == 1: #right 
                    if flap2 == True:
                        data_shop['money'] += 1
                        data_normal['meters_up'] += 1
                        meters_up += 1
                        player1.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
                        player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                        player1.x += 150
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                            json.dump(data_normal, save_data_normal)
                        cactusy += 50
                        bgy += 50
                        bird1.y += 150
                        fireball1.y += 150
                        flap2 = False
                        flap = True
                if io == -1: #left
                    if flap == True:
                        data_shop['money'] += 1
                        data_normal['meters_up'] += 1
                        meters_up += 1
                        player1.img = pygame.image.load(os.path.join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                        player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                        player1.x -= 150
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                            json.dump(data_normal, save_data_normal)
                        cactusy += 50
                        bgy += 50
                        bird1.y += 150
                        fireball1.y += 150
                        flap = False
                        flap2 = True
        Cowboy_Hat = ui_button(player1.x, player1.y - 20, 40, 30, cowboy_hat_image)
        Thinking_Hat = ui_button(player1.x, player1.y - 20, 40, 30, thinking_hat_image)
        Top_Hat = ui_button(player1.x, player1.y - 20, 40, 30, top_hat_image)
        Red_Cap = ui_button(player1.x, player1.y - 20, 40, 30, red_cap_image)
        Party_Hat = ui_button(player1.x, player1.y - 20, 40, 30, party_hat_image)
        Witch_Hat = ui_button(player1.x, player1.y - 20, 40, 30, witch_hat_image)
        Mexican_Hat = ui_button(player1.x, player1.y - 20, 40, 30, mexican_hat_image)
        King_Hat = ui_button(player1.x, player1.y - 20, 40, 30, king_hat_image)
        fireball_rect = pygame.Rect(fireball1.x, fireball1.y, fireball1.width, fireball1.height)
        bird_rect = pygame.Rect(bird1.x, bird1.y, bird1.width, bird1.height)
        bird_rac_rect = pygame.Rect(bird_rac1.x, bird_rac1.y, bird_rac1.width, bird_rac1.height)
        player_rect = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
        top_cactus_rect = pygame.Rect(640, cactusy - 5800, 100, 800)

        if player_rect.colliderect(fireball_rect):
            with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
            with open(os.path.join('data','save_data_normal.json')) as save_data_normal:
                    data_normal = json.load(save_data_normal)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            fireballdeathvid()
        if player_rect.colliderect(bird_rect):
            with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
            with open(os.path.join('data','save_data_normal.json')) as save_data_normal:
                    data_normal = json.load(save_data_normal)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            birddeathvid()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                data_normal['meters_up'] += 1
                meters_up += 1
                player1.img = pygame.image.load(os.path.join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                player1.x -= 150
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                cactusy += 50
                bgy += 50
                bird1.y += 150
                fireball1.y += 150
                flap = False
                flap2 = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if flap2 == True:
                data_shop['money'] += 1
                data_normal['meters_up'] += 1
                meters_up += 1
                player1.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
                player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                player1.x += 150
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
                cactusy += 50
                bgy += 50
                bird1.y += 150
                fireball1.y += 150
                flap2 = False
                flap = True
        
        fireball1.y += 10
        if fireball1.y >= screen_height:
            fireball1.y = 0
            fireball1.x = random.choice([585, 760])
            data_normal['fireballs_dodged'] += 1
            with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
            fireballs_dodged += 1
    
        bird1.x += 10
        if bird1.x >= screen_width:
            bird1.x = -1000
            data_normal['birds_dodged'] += 1
            with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
            birds_dodged += 1
        if bird1.y >= screen_height:
            bird1.x = -1000
            bird1.y = random.randint(300, 800)
            data_normal['birds_dodged'] += 1
            with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
            birds_dodged += 1

        dodge_text_red = pygame.font.SysFont('comicsans', 20).render("dodge!", 1, (255, 0, 0))
        dodge_text = pygame.font.SysFont('comicsans', 20).render("dodge!", 1, (255, 255, 255))
    
        if fireball1.y >= 0 and fireball1.x == 585 and player1.x == 590 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()

        if fireball1.y >= 0 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            
        if bird_rect.colliderect(bird_rac_rect):
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
        
        if bird_rac_rect.colliderect(top_cactus_rect):
            with open(os.path.join('data', 'save_data_normal.json'),'w') as save_data_normal:
                    json.dump(data_normal, save_data_normal)
            with open(os.path.join('data','save_data_normal.json')) as save_data_normal:
                    data_normal = json.load(save_data_normal)
            data_shop['money'] += 100
            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
            if data_options['play_sfx'] == True:
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            win()

        high_score_text = pygame.font.SysFont('comicsans', 40).render("High Scores", 1, (255, 255, 255))
        total_fireballs_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Total Fireballs Dodged: {data_normal['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_text = pygame.font.SysFont('comicsans', 40).render(f"Total Meters Climbed: {data_normal['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Total Birds Dodged: {data_normal['birds_dodged']}", 1, (255, 255, 255))

        score_text = pygame.font.SysFont('comicsans', 40).render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = pygame.font.SysFont('comicsans', 40).render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))

        money_text = pygame.font.SysFont('comicsans', 80).render(f"{data_shop['money']} : ", 1, (64, 255, 25))

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
            if player1.x == 590:
                Cowboy_Hat.x = 585
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            if player1.x == 590:
                Thinking_Hat.x = 585
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            if player1.x == 590:
                Top_Hat.x = 585
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            if player1.x == 590:
                Red_Cap.image = pygame.transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            if player1.x == 590:
                Party_Hat.x = 585
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            if player1.x == 590:
                Witch_Hat.x = 585
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            if player1.x == 590:
                Mexican_Hat.x = 585
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            if player1.x == 590:
                King_Hat.x = 585
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(bird1.img, (bird1.x, bird1.y))
        window.blit(fireball1.img, (fireball1.x, fireball1.y))

        window.blit(Money.image, (Money.x, Money.y))
        
        pygame.display.update()

def main_hard():
    global data_hard, data_options, data_shop
    if data_options['play_music'] == True:
        maintheme.play(-1)
    fireballs_dodged = 0
    meters_up = 0
    birds_dodged = 0
    flap = False
    flap2 = True
    player1 = player(590, 300, 50, 100)
    bird1 = bird(0, 600, 100, 100)
    fireball1 = fireball(760, player1.y - 1000, 25, 25)
    bird_rac1 = bird_rac(0, 300, 740, 100)
    Money = ui_button(1030, 600, 250, 100, money_image)
    run = True
    bgy = 0
    cactusy = -500
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_options.json'),'w') as save_data_options:
                    json.dump(data_options, save_data_options)
                run = False
                pygame.quit()
            if event.type == pygame.JOYAXISMOTION:
                io = round(pygame.joystick.Joystick(0).get_axis(0))
                if io == 1: #right 
                    if flap2 == True:
                        data_shop['money'] += 1
                        data_hard['meters_up'] += 1
                        meters_up += 1
                        player1.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
                        player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                        player1.x += 150
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                            json.dump(data_hard, save_data_hard)
                        cactusy += 50
                        bgy += 50
                        bird1.y += 50
                        fireball1.y += 50
                        flap2 = False
                        flap = True
                if io == -1: #left
                    if flap == True:
                        data_shop['money'] += 1
                        data_hard['meters_up'] += 1
                        meters_up += 1
                        player1.img = pygame.image.load(os.path.join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                        player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                        player1.x -= 150
                        with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                            json.dump(data_shop, save_data_shop)
                        with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                            json.dump(data_hard, save_data_hard)
                        cactusy += 50
                        bgy += 50
                        bird1.y += 50
                        fireball1.y += 50
                        flap = False
                        flap2 = True
        Cowboy_Hat = ui_button(player1.x, player1.y - 20, 40, 30, cowboy_hat_image)
        Thinking_Hat = ui_button(player1.x, player1.y - 20, 40, 30, thinking_hat_image)
        Top_Hat = ui_button(player1.x, player1.y - 20, 40, 30, top_hat_image)
        Red_Cap = ui_button(player1.x, player1.y - 20, 40, 30, red_cap_image)
        Party_Hat = ui_button(player1.x, player1.y - 20, 40, 30, party_hat_image)
        Witch_Hat = ui_button(player1.x, player1.y - 20, 40, 30, witch_hat_image)
        Mexican_Hat = ui_button(player1.x, player1.y - 20, 40, 30, mexican_hat_image)
        King_Hat = ui_button(player1.x, player1.y - 20, 40, 30, king_hat_image)
        fireball_rect = pygame.Rect(fireball1.x, fireball1.y, fireball1.width, fireball1.height)
        bird_rect = pygame.Rect(bird1.x, bird1.y, bird1.width, bird1.height)
        bird_rac_rect = pygame.Rect(bird_rac1.x, bird_rac1.y, bird_rac1.width, bird_rac1.height)
        player_rect = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
        top_cactus_rect = pygame.Rect(640, cactusy - 10800, 100, 800)

        if player_rect.colliderect(fireball_rect):
            with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
            with open(os.path.join('data','save_data_hard.json')) as save_data_hard:
                    data_hard = json.load(save_data_hard)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                firesound.play()
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            fireballdeathvid()
        if player_rect.colliderect(bird_rect):
            with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
            with open(os.path.join('data','save_data_hard.json')) as save_data_hard:
                    data_hard = json.load(save_data_hard)
            maintheme.stop()
            if data_options['play_sfx'] == True:
                birdsound.play()
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            birddeathvid()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if flap == True:
                data_shop['money'] += 1
                data_hard['meters_up'] += 1
                meters_up += 1
                player1.img = pygame.image.load(os.path.join('Images', 'player', 'flippedplayer.png')).convert_alpha()
                player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                player1.x -= 150
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                cactusy += 50
                bgy += 50
                bird1.y += 50
                fireball1.y += 50
                flap = False
                flap2 = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if flap2 == True:
                data_shop['money'] += 1
                data_hard['meters_up'] += 1
                meters_up += 1
                player1.img = pygame.image.load(os.path.join('Images', 'player', 'player.png')).convert_alpha()
                player1.img = pygame.transform.scale(player1.img, (player1.width, player1.height))
                player1.x += 150
                with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
                with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
                cactusy += 50
                bgy += 50
                bird1.y += 50
                fireball1.y += 50
                flap2 = False
                flap = True
        
        fireball1.y += 25
        if fireball1.y >= screen_height:
            fireball1.y = 0
            fireball1.x = random.choice([585, 760])
            data_hard['fireballs_dodged'] += 1
            with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
            fireballs_dodged += 1
    
        bird1.x += 25
        if bird1.x >= screen_width:
            bird1.x = -100
            data_hard['birds_dodged'] += 1
            with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
            birds_dodged += 1
        if bird1.y >= screen_height:
            bird1.x = -100
            bird1.y = random.randint(300, 800)
            data_hard['birds_dodged'] += 1
            with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
            birds_dodged += 1

        dodge_text_red = pygame.font.SysFont('comicsans', 20).render("dodge!", 1, (255, 0, 0))
        dodge_text = pygame.font.SysFont('comicsans', 20).render("dodge!", 1, (255, 255, 255))
    
        if fireball1.y >= 20 and fireball1.x == 585 and player1.x == 590 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x - 10, player1.y - 30))
            pygame.display.update()

        if fireball1.y >= 20 and fireball1.x == 760 and player1.x == 740 and player1.y >= fireball1.y:
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text_red, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            
        if bird_rect.colliderect(bird_rac_rect):
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            window.blit(dodge_text, (player1.x + 10, player1.y - 30))
            pygame.display.update()
            if data_options['play_sfx'] == True:
                dodgemusic.play()
                dodgemusic.set_volume(0.1)
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
        
        if bird_rac_rect.colliderect(top_cactus_rect):
            with open(os.path.join('data', 'save_data_hard.json'),'w') as save_data_hard:
                    json.dump(data_hard, save_data_hard)
            with open(os.path.join('data','save_data_hard.json')) as save_data_hard:
                    data_hard = json.load(save_data_hard)
            data_shop['money'] += 100
            with open(os.path.join('data', 'save_data_shop.json'),'w') as save_data_shop:
                    json.dump(data_shop, save_data_shop)
            if data_options['play_sfx'] == True:
                try:
                    pygame.joystick.Joystick(0).rumble(5.0, 10.0, 30)
                except:
                    print("")
            win()

        high_score_text = pygame.font.SysFont('comicsans', 40).render("High Scores", 1, (255, 255, 255))
        total_fireballs_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Total Fireballs Dodged: {data_hard['fireballs_dodged']}", 1, (255, 255, 255))
        highest_meter_text = pygame.font.SysFont('comicsans', 40).render(f"Total Meters Climbed: {data_hard['meters_up']}", 1, (255, 255, 255))
        total_birds_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Total Birds Dodged: {data_hard['birds_dodged']}", 1, (255, 255, 255))

        score_text = pygame.font.SysFont('comicsans', 40).render("Scores", 1, (255, 255, 255))
        fireballs_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Fireballs Dodged: {fireballs_dodged}", 1, (255, 255, 255))
        meters_text = pygame.font.SysFont('comicsans', 40).render(f"Meters Up: {meters_up}", 1, (255, 255, 255))
        birds_dodged_text = pygame.font.SysFont('comicsans', 40).render(f"Birds Dodged: {birds_dodged}", 1, (255, 255, 255))

        money_text = pygame.font.SysFont('comicsans', 80).render(f"{data_shop['money']} : ", 1, (64, 255, 25))

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
            if player1.x == 590:
                Cowboy_Hat.x = 585
            window.blit(Cowboy_Hat.image, (Cowboy_Hat.x, Cowboy_Hat.y))
        if data_shop['thinking_hat_equipped'] == True:
            if player1.x == 740:
                Thinking_Hat.x = 755
            if player1.x == 590:
                Thinking_Hat.x = 585
            window.blit(Thinking_Hat.image, (Thinking_Hat.x, Thinking_Hat.y))
        if data_shop['top_hat_equipped'] == True:
            if player1.x == 740:
                Top_Hat.x = 755
            if player1.x == 590:
                Top_Hat.x = 585
            window.blit(Top_Hat.image, (Top_Hat.x, Top_Hat.y))
        if data_shop['red_cap_equipped'] == True:
            if player1.x == 740:
                Red_Cap.x = 750
            if player1.x == 590:
                Red_Cap.image = pygame.transform.flip(Red_Cap.image, 90, 0)
                Red_Cap.x = 590
            window.blit(Red_Cap.image, (Red_Cap.x, Red_Cap.y))
        if data_shop['party_hat_equipped'] == True:
            if player1.x == 740:
                Party_Hat.x = 755
            if player1.x == 590:
                Party_Hat.x = 585
            window.blit(Party_Hat.image, (Party_Hat.x, Party_Hat.y))
        if data_shop['witch_hat_equipped'] == True:
            if player1.x == 740:
                Witch_Hat.x = 755
            if player1.x == 590:
                Witch_Hat.x = 585
            window.blit(Witch_Hat.image, (Witch_Hat.x, Witch_Hat.y))
        if data_shop['mexican_hat_equipped'] == True:
            if player1.x == 740:
                Mexican_Hat.x = 755
            if player1.x == 590:
                Mexican_Hat.x = 585
            window.blit(Mexican_Hat.image, (Mexican_Hat.x, Mexican_Hat.y))
        if data_shop['king_hat_equipped'] == True:
            if player1.x == 740:
                King_Hat.x = 755
            if player1.x == 590:
                King_Hat.x = 585
            window.blit(King_Hat.image, (King_Hat.x, King_Hat.y))
        window.blit(bird1.img, (bird1.x, bird1.y))
        window.blit(fireball1.img, (fireball1.x, fireball1.y))

        window.blit(Money.image, (Money.x, Money.y))
        
        pygame.display.update()
if __name__ == "__main__":
    start()