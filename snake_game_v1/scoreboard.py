from turtle import Turtle

STARTING_SCORE = 0
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = STARTING_SCORE
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def addPoint(self):
        self.score += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)