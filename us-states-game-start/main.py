import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")

all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's a state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        user_state = states_data[states_data.state == answer_state]
        state_location = (int(user_state["x"]), int(user_state["y"]))

        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(state_location)
        text.write(answer_state, align="center")
