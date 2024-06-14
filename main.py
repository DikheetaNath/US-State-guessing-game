import turtle
import pandas as pd

# Screen settings
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# CSV
df = pd.read_csv("50_states.csv")
states = df.state.to_list()
df.x.astype(int)
df.y.astype(int)

# Dialog box
states_answered = []
no_of_right_states = 0


while no_of_right_states != 50:
    answer_input = screen.textinput(title=f"Score: {no_of_right_states}/50", prompt="Guess a state name")
    states_answered.append(answer_input.title())
    if answer_input.title() == "Exit":
        break
    if answer_input.title() in states:
        tim = turtle.Turtle()
        tim.pencolor('black')
        tim.hideturtle()
        tim.penup()
        state_coor = df[df.state == answer_input.title()]
        tim.goto(int(state_coor.x), int(state_coor.y))
        tim.write(answer_input)
        no_of_right_states += 1

with open("./states_to_learn.csv", 'w') as states_to_learn:

    for i in states:
        if i not in states_answered:
            states_to_learn.write(f"{i}\n")
