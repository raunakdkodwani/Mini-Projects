from turtle import Turtle, Screen


screen= Screen()
screen.setup(500,400)

user_input = screen.textinput(title="Place your bet",prompt="which colour turtle u wanna choose")
colours = ["Red", "yellow", "green","pink","orange","black"]
y_axis = [-70,-40,-10,20,50,80]

for i in range (0,6):
    tim = Turtle(shape="Turtle")
    tim.penup()
    tim.color(colours[i])
    tim.goto(-230,y_axis[i])

if user_input:
    race= True


# screen.exitonclick()