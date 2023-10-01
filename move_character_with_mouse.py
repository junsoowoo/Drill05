from pico2d import *
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def moving_character(character_x, character_y, cursor_x, cursor_y):
    dir_x = cursor_x - character_x
    dir_y = cursor_y - character_y
    move_speed = 5
    distance = math.sqrt(dir_x ** 2 + dir_y ** 2)
    if distance > move_speed:
        dir_x /= distance
        dir_y /= distance
        character_x += dir_x * move_speed
        character_y += dir_y * move_speed

    return character_x, character_y

def random_xy():
    return random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
cursor_x, cursor_y = random_xy()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    cursor.draw(cursor_x, cursor_y)
    character_x, character_y = moving_character(character_x, character_y, cursor_x, cursor_y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8
    distance_to_target = math.sqrt((character_x - cursor_x) ** 2 + (character_y - cursor_y) ** 2)
    if distance_to_target < 5:
        cursor_x, cursor_y = random_xy()
    delay(0.009)

close_canvas()
