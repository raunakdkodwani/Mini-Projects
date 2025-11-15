from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        
        self.speed("fastest")
        self.refresh()

    
    def refresh(self):
        random_large_food_drop= random.randint(0,3)
        print(random_large_food_drop)
        if random_large_food_drop == 3:
            self.shapesize(stretch_len = 1.5, stretch_wid =1.5)
            self.color("red")
            self.points = 3
        else:
            self.shapesize(stretch_len = 0.5, stretch_wid =0.5)
            self.color("blue")
            self.points = 1 
        random_x= random.randint(-280,280)
        random_y= random.randint(-280,280)
        self.goto(random_x,random_y)
