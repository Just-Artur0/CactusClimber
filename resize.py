from pygame import display, FULLSCREEN, NOFRAME, RESIZABLE, Surface, transform
BASE_WIDTH = 1280
BASE_HEIGHT = 720
current_width = BASE_WIDTH
current_height = BASE_HEIGHT
scale_x = 1.0
scale_y = 1.0
is_fullscreen = False
window = display.set_mode((BASE_WIDTH, BASE_HEIGHT), RESIZABLE)
game_surface = Surface((BASE_WIDTH, BASE_HEIGHT))
def handle_resize(new_width, new_height):
    global window, current_width, current_height, scale_x, scale_y
    current_width = new_width
    current_height = new_height
    scale_x = new_width / BASE_WIDTH
    scale_y = new_height / BASE_HEIGHT
def scale_mouse_pos(mouse_x, mouse_y):
    """Convert mouse coordinates back to game coordinates"""
    return int(mouse_x / scale_x), int(mouse_y / scale_y)
def toggle_fullscreen():
    global window, is_fullscreen, current_width, current_height
    if is_fullscreen:
        # Switch to windowed
        window = display.set_mode((BASE_WIDTH, BASE_HEIGHT), RESIZABLE)
        is_fullscreen = False
        handle_resize(BASE_WIDTH, BASE_HEIGHT)
    else:
        # Switch to fullscreen
        display_info = display.Info()
        window = display.set_mode(
            (display_info.current_w, display_info.current_h),
            NOFRAME | FULLSCREEN
        )
        is_fullscreen = True
        handle_resize(display_info.current_w, display_info.current_h)
def render_to_screen():
    if current_width != BASE_WIDTH or current_height != BASE_HEIGHT:
        scaled_surface = transform.scale(game_surface, (current_width, current_height))
        window.blit(scaled_surface, (0, 0))
    else:
        window.blit(game_surface, (0, 0))
    display.flip()