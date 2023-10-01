from pico2d import *
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def moving_character(character_x, character_y, cursor_x, cursor_y, t):
    move_speed = 5
    character_x = lerp(character_x, cursor_x, t)
    character_y = lerp(character_y, cursor_y, t)
    return character_x, character_y, cursor_x, cursor_y

def lerp(start, end, t):
    return start + (end - start) * t

def random_xy():
    return random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
cursor_x, cursor_y = random_xy()
character_direction = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    t=0.1
    cursor.draw(cursor_x, cursor_y)
    character_x, character_y, dir_x, dir_y = moving_character(character_x, character_y, cursor_x, cursor_y,t)
    if character_x < cursor_x:
        character_direction = 1
    else:
        character_direction = 0
    sprite_row = 100 * character_direction
    character.clip_draw(frame * 100, sprite_row, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8
    distance_to_target = math.sqrt((character_x - cursor_x) ** 2 + (character_y - cursor_y) ** 2)
    if distance_to_target < 5:
        cursor_x, cursor_y = random_xy()
    delay(0.03)

close_canvas()
