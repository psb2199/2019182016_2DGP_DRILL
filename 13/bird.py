from pico2d import *
import random
import game_framework

class Bird:
    image = None


    def __init__(self, x = 25, y = 300, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.x = random.randint(40, 300)
        self.y = random.randint(300, 500)
        self.frame = 0


    def draw(self):
        global ioio
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.velocity == -1:
            self.image.clip_composite_draw(int(self.frame) * 180, 300 - ioio, 180, 200, 0, 'h', self.x, self.y, 100, 100)

        if self.velocity == 1:
            self.image.clip_composite_draw(int(self.frame) * 180, 300 - ioio, 180, 200, 0, '', self.x, self.y, 100, 100)

        ioio += 150
        if ioio == 300:
            ioio = 0


    def update(self):
        self.x += self.velocity

        if self.x > 1600:
            self.velocity = -1

        if self.x < 0:
            self.velocity = 1

ioio = 0

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8
