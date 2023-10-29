from turtle import Turtle
ALIGHTMENT = "center"
FONT = ("Arial", 24 ,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.hideturtle()

        self.score = 1

    def write_score(self):
        self.clear()
        self.write(f'Score : {self.score}', False, align=ALIGHTMENT,font=FONT)
        self.score += 1
        #
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align = "center", font = FONT)