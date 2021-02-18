from turtle import Turtle


class Ball(Turtle):
    def __init__(self,x,y):
        super().__init__()

        self.pu()
        self.color("white")
        self.shape("circle")
        self.x_move=x
        self.y_move=y
        self.ball_speed=0.1

    def move(self):
        new_x = self.xcor() +self.x_move
        new_y =  self.ycor() +self.y_move
        self.goto(new_x,new_y)

    def bouncey(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1
        self.ball_speed*=0.9

    def resetme(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.bouncex()