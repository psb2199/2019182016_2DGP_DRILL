from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x= 0
y= 0

t = 0
xx= 0
yy = 0


while (x < 700):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x =x+5
    delay(0.01)


while(1):

    t = 0

    while (y < 500):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(699,y+90)
        y =y+5
        delay(0.01)

    while (x > 100):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,589)
        x =x-5
        delay(0.01)

    while (y > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(100,y+90)
        y =y-5
        delay(0.01)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x =x+5
        delay(0.01)






    while(t<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(xx+400,yy+300)
        t = t+5
        xx = math.sin(t / 360*2*math.pi)*200
        yy = math.cos(t/360*2*math.pi)*200*(-1)
        delay(0.01)


    

    while (x < 700):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x =x+5
        delay(0.01)



#=============

close_canvas()
