import pandas
import turtle

screen = turtle.Screen()
screen.title("States_Game")
pic = r"025 - StatesGame\blank_states_img.gif"
screen.addshape(pic)
turtle.shape(pic)

# def get_mouse_click_coor(x,y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv(r"025 - StatesGame\50_states.csv")
state_list = data["state"].to_list()
guessed = []

while len(guessed) < len(state_list):
    player_answer = turtle.textinput(
        title=f"{len(guessed)}/{len(state_list)} states guessed",
        prompt="Write a state's name",
    ).title()
    
    if player_answer == 'Exit':
        break

    if player_answer in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_row = data[data["state"] == player_answer]
        t.goto(int(answer_row["x"]), int(answer_row["y"]))
        t.write(answer_row["state"].item())
        guessed.append(player_answer)

for state in state_list:
    if state in guessed:
        state_list.remove(state)

states_dict = {
    'States_to_learn': state_list
}

states_data_file = pandas.DataFrame(states_dict)
states_data_file.to_csv(r'025 - StatesGame\StatesToLearn.csv')

