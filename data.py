from json import load, dump
from os.path import join
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