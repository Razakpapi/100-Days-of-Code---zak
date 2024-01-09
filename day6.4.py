# Final Reeborg Exercise
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def walk():
    turn_right()
    move()
while right_is_clear():
    turn_right()
    move()

while wall_on_right():
    move()
if wall_in_front():
    turn_left()
else:
    turn_right()
while front_is_clear():
    move()

while not at_goal():
    walk()
    