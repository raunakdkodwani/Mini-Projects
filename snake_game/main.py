'''Steps in which I will make this game:

1. Create a snake body
2. Move the snake
3. Create snake food
4. Detect collision with food 
5. Create a scoreboard
6. Detect collision with wall 
7. Detect collision with tail

'''



from turtle import  Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height = 600)
screen.bgcolor("pink")
screen.title("My Snake Game")
screen.tracer()

snake=Snake()
food =Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on =True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food 
    if snake.head.distance(food) < 15:
        scoreboard.increase_score(food.points)
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_is_on = False

        





screen.exitonclick()