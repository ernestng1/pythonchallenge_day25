import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen_turtle = Turtle()
screen_turtle.shape(image)

us_states_data = pandas.read_csv('50_states.csv')
state = us_states_data['state']
x_coord = us_states_data['x']
y_coord = us_states_data['y']
game_is_on = True
state_list = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
while game_is_on:
    if answer_state.title() == "Exit":
        missing_state = []
        for official_states in state.values:
            if official_states not in state_list:
                missing_state.append(official_states)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('State_to_learn.csv')
        print(new_data)
        break
    elif answer_state.title() in state.values:
        answer_state = answer_state.title()
        new_turtle = Turtle()
        new_turtle.teleport((us_states_data[us_states_data['state']==answer_state]['x']).values[0],(us_states_data[us_states_data['state']==answer_state]['y']).values[0])
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.write(f"{answer_state}", True)
        state_list.append(new_turtle)
        if len(state_list) == len(state):
            game_is_on = False
            answer_state = screen.textinput(title="You win!", prompt="Congrats")
        else:
            answer_state = screen.textinput(title=f"{len(state_list)}/{len(state)} correct", prompt="Try another state:")
    else:
        answer_state = screen.textinput(title=f"{len(state_list)}/{len(state)} correct", prompt="Try another state:")