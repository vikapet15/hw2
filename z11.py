from turtle import*
from math import*
tracer(0)
xc,yc,r = map(int,input().split())
up()
# goto(xc, yc)
# dot (5)
goto(xc, yc - r)
down()
circle(r)
up()
x,y = map(int,input().split())
goto(x,y)
dot (5)
rs = sqrt((xc - x)**2 + (yc - y)**2)
if rs <= r:
    print('Точка внутри окружности')
else:
    print('Точка вне окружности')

update()
done()
