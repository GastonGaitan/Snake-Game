from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("White")
        self.goto(0, 330)
        self.hideturtle()
        self.update_scoreboard()
        #Below code stands for the line that limits the score from the game.
        self.score_underline = Turtle()
        self.score_underline.hideturtle()
        self.score_underline.goto(-350, 330)
        self.score_underline.pencolor("white")
        self.score_underline.forward(700)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} | High score {self.high_score}", align="center", font=("Arial", 10, "normal"))
    


        