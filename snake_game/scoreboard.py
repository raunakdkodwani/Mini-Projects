from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("purple")
        # self.write(f"Score: {self.score}", align ="center", font = ("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align ="center", font = ("Arial", 24, "normal"))
    
    def game_over(self):
        GOT
        self.write("Game Over",  align ="center", font = ("Arial", 24, "normal"))

    def increase_score(self, meal):
        if(meal==3):
            self.score+=3
        else:
            self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align ="center", font = ("Arial", 24, "normal"))
        