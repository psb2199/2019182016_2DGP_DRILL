import turtle

x=0
y=0

turtle. left(90)
while(x <= 5):
    turtle. pendown()
    turtle. forward(500)
    turtle. penup()
    turtle. goto(100 + 100*x,0)
    x = x+1

turtle. right(90)
turtle. goto(0,0)

while(y <= 5):
    turtle. pendown()
    turtle. forward(500)
    turtle. penup()
    turtle. goto(0,100 + 100*y)
    y = y+1

turtle. exiton.click()

