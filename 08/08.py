from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global dir_x
    global dir_y
    global right, left, up, down

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:

            if event.key == SDLK_RIGHT:
                dir_x += 1
                right = True

            elif event.key == SDLK_LEFT:
                dir_x -= 1
                left = True

            elif event.key == SDLK_UP:
                dir_y += 1
                up = True
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                down = True
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:

            if event.key == SDLK_RIGHT:
                dir_x -= 1
                right = False
            elif event.key == SDLK_LEFT:
                dir_x += 1
                left = False
            elif event.key == SDLK_UP:
                dir_y -= 1
                up= False
            elif event.key == SDLK_DOWN:
                dir_y += 1
                down = False
    pass


open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
dir_x = 0
dir_y = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

right = True
left = True
up = True
down = True


# x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
# frame = 0
# hide_cursor()



while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH//2, TUK_HEIGHT // 2)


    if right == True or up == True or down == True:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
    elif left == True or up == True or down == True:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        update_canvas()

    if x > TUK_WIDTH:
        x = TUK_WIDTH
    elif x < 0:
        x = 0
    elif y > TUK_HEIGHT - 150:
        y = TUK_HEIGHT - 150
    elif y < 200:
        y = 200

    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 10
    y += dir_y * 10
    delay(0.01)




    # clear_canvas()
    # TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    # character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    # update_canvas()
    # frame = (frame + 1) % 8
    #
    # handle_events()

close_canvas()




