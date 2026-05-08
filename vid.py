from pygame import event, QUIT, VIDEORESIZE, KEYDOWN, K_F11, K_ESCAPE, time
from resize import handle_resize, toggle_fullscreen, is_fullscreen, window, render_to_screen, game_surface
from assets import begin_1_image, begin_2_image, begin_3_image, begin_4_image, begin_5_image, begin_6_image, begin_7_image, begin_8_image, begin_9_image, begin_10_image
from assets import end_1_image, end_2_image, end_3_image, end_4_image, end_5_image, end_6_image, end_7_image, end_8_image, end_9_image, end_10_image, end_11_image, end_12_image
from assets import end_13_image, end_14_image, end_15_image, end_16_image, end_17_image, end_18_image, end_19_image, birddeath_1_image, birddeath_2_image, birddeath_3_image
from assets import birddeath_4_image, birddeath_5_image, birddeath_6_image, birddeath_7_image, birddeath_8_image, birddeath_9_image, birddeath_10_image, birddeath_11_image
from assets import fireballdeath_1_image, fireballdeath_2_image, fireballdeath_3_image, fireballdeath_4_image, fireballdeath_5_image, fireballdeath_6_image, fireballdeath_7_image
from assets import fireballdeath_8_image, fireballdeath_9_image, fireballdeath_10_image, fireballdeath_11_image, fireballdeath_12_image
from data import save_data
from sys import exit
def vid_preview(video=0):
    global window, is_fullscreen
    run = True
    clock = time.Clock()
    if video == 0:
        clip = [(200, begin_1_image),
                (200, begin_2_image),
                (200, begin_3_image),
                (200, begin_4_image),
                (200, begin_5_image),
                (200, begin_6_image),
                (200, begin_7_image),
                (200, begin_8_image),
                (200, begin_9_image),
                (200, begin_10_image)]
    elif video == 1:
        clip = [(250, end_1_image),
                (250, end_2_image),
                (250, end_3_image),
                (250, end_4_image),
                (250, end_5_image),
                (250, end_6_image),
                (250, end_7_image),
                (250, end_8_image),
                (250, end_9_image),
                (250, end_10_image),
                (250, end_11_image),
                (250, end_12_image),
                (250, end_13_image),
                (250, end_14_image),
                (250, end_15_image),
                (250, end_16_image),
                (250, end_17_image),
                (250, end_18_image),
                (250, end_19_image)]
    elif video == 2:
        clip = [(330, birddeath_1_image),
                (330, birddeath_2_image),
                (330, birddeath_3_image),
                (330, birddeath_4_image),
                (330, birddeath_5_image),
                (330, birddeath_6_image),
                (330, birddeath_7_image),
                (330, birddeath_8_image),
                (330, birddeath_9_image),
                (330, birddeath_10_image),
                (330, birddeath_11_image)]
    elif video == 3:
        clip = [(250, fireballdeath_1_image),
                (250, fireballdeath_2_image),
                (250, fireballdeath_3_image),
                (250, fireballdeath_4_image),
                (250, fireballdeath_5_image),
                (250, fireballdeath_6_image),
                (250, fireballdeath_7_image),
                (250, fireballdeath_8_image),
                (250, fireballdeath_9_image),
                (250, fireballdeath_10_image),
                (250, fireballdeath_11_image),
                (250, fireballdeath_12_image)]
    elif video >= 4:
        clip = [(200, begin_1_image),
                (200, begin_2_image),
                (200, begin_3_image),
                (200, begin_4_image),
                (200, begin_5_image),
                (200, begin_6_image),
                (200, begin_7_image),
                (200, begin_8_image),
                (200, begin_9_image),
                (200, begin_10_image)]
    for duration, intro_background_image in clip:
        start_time = time.get_ticks()
        running = True
        while running:
            clock.tick(60)
            now = time.get_ticks()
            events = event.get()
            for e in events:
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
            game_surface.blit(intro_background_image, (0, 0))
            render_to_screen()
            # Wait for the specific duration
            if now - start_time >= duration:
                running = False