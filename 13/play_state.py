from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy
from bird import Bird


boy = None
grass = None
bird1 = None
bird2 = None
bird3 = None
bird4 = None
bird5 = None
bird6 = None
bird7 = None
bird8 = None
bird9 = None
bird10 = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass , bird1, bird2, bird3, bird4, bird5, bird6, bird7, bird8, bird9, bird10
    boy = Boy()
    grass = Grass()
    bird1 = Bird()
    bird2 = Bird()
    bird3 = Bird()
    bird4 = Bird()
    bird5 = Bird()
    bird6 = Bird()
    bird7 = Bird()
    bird8 = Bird()
    bird9 = Bird()
    bird10 = Bird()

    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(bird1,1)
    game_world.add_object(bird2, 1)
    game_world.add_object(bird3, 1)
    game_world.add_object(bird4, 1)
    game_world.add_object(bird5, 1)
    game_world.add_object(bird6, 1)
    game_world.add_object(bird7, 1)
    game_world.add_object(bird8, 1)
    game_world.add_object(bird9, 1)
    game_world.add_object(bird10, 1)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    #강제 성능 저하
    #delay(0.01)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
