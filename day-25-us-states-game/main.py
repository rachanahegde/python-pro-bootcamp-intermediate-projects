import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_for_studying = []
        for state in states_list:
            if state not in correct_guesses:
                states_for_studying.append(state)
        states_to_learn = pandas.DataFrame(states_for_studying)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        correct_guesses.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        location = data[data.state == answer_state]
        x_coordinate = int(location.x)
        y_coordinate = int(location.y)
        timmy.setpos(x_coordinate, y_coordinate)
        timmy.write(answer_state)

# Convert guess to title case
# Check if guess is among 50 states
# Write correct guess onto map - find the location (x,y coordinates) for that state
# Use a loop to allow the user to keep guessing
# Record correct guesses in a list
# Track the score.
# Save the missing states to a .csv
