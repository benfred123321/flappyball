import pgzrun
import random

HEIGHT = 800
WIDTH = 800
TITLE = "Flappy ball"
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
randcolor=(r,g,b)
gravity=2000 #pixles per second

class Ball:
    #creating construtor funtion 
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.velocity_x = 200
        self.velocity_y = 0
        self.radius = 40

    def draw(self):
        position = (self.x,self.y)
        screen.draw.filled_circle(position,self.radius,randcolor)

#creating ball object
ball1 = Ball(100,100)

def draw():
    screen.clear()
    ball1.draw()


def update(count):
    #appling constant acceleration formila
    vel_y = ball1.velocity_y
    ball1.velocity_y += gravity * count
    ball1.y += (vel_y + ball1.velocity_y) * count * 0.5

    #detect and handle bounce
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.velocity_y = -ball1.velocity_y *0.9
    ball1.x += ball1.velocity_x * count
    if ball1.x < ball1.radius or ball1.x > WIDTH - ball1.radius:
        ball1.velocity_x = -ball1.velocity_x
pgzrun.go()