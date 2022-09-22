from pico2d import*

open_canvas()

character = load_image('td.png')

t = 0
frame=0


for t in range(0,35,1):
    clear_canvas()
    character.clip_draw(frame*41+1,517,42,42,200,400)
    update_canvas()
    frame = (frame + 1)%7
    delay(0.05)
    get_events()

for t in range(0,125,1):
    clear_canvas()
    character.clip_draw(frame*43+1,438,44,75,3*t+200,1/2*(-t*3)+400+14)
    update_canvas()
    frame = (frame + 1)%25
    delay(0.05)
    get_events()


for t in range(0,4, 1):
    
    for t in range(0,16,1):
        clear_canvas()
        character.clip_draw(frame*73+147,245,74,58,600-25,200+20)
        update_canvas()
        frame = (frame + 1)%16
        delay(0.05)
        get_events()
        
    for t in range(0,10,1):
        clear_canvas()
        character.clip_draw(frame*73+74,181,74,58,600-25,200+20)
        update_canvas()
        frame = (frame + 1)%10
        delay(0.05)
        get_events()
    
#clip_draw(left,bottom,width,height,x,y)

close_canvas()
