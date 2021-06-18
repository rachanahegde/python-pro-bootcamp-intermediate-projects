from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-280, 260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", font=FONT)