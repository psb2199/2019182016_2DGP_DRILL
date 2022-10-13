from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1080, 720

open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
back_x, back_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = back_x, back_y
arrow_x, arrow_y = x, y
frame = 0
direction = 0
t = 0
hide_cursor()


def handle_events():
    global running, direction
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global arrow_x, arrow_y
    global back_x, back_y
    global t
    
    arrow_x,arrow_y = random.randint(0,TUK_WIDTH), random.randint(0,TUK_HEIGHT)
    back_x, back_y = x, y
    t = 0
    
    pass

def update_world():

    global x,y
    global t

    t += 0.01

    x = (1 - t) * back_x + t * arrow_x
    y = (1 - t) * back_y + t * arrow_y

    if t >= 1.0:
        reset_world()
    pass


reset_world()

while running:
    update_world()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(arrow_x, arrow_y)

    if (arrow_x<x):
        direction = 0
    elif (arrow_x>x):
        direction = 1

    character.clip_draw(frame * 100 , 100 * direction, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
