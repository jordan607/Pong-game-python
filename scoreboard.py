from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.goto(-100,200)
        self.write(self.l_score,"center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, "center", font=("Courier", 80, "normal"))

    def score(self,p):
        if p == "l":
            self.l_score+=1
            self.clear()
            self.update_score()
        else:
            self.r_score+=1
            self.clear()
            self.update_score()