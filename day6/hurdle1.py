

# This function is part of the website
def turn_left():
    print("Turn left")

# This function is part of the website
def move():
    print("One step forward")

def is_facing_north():
    print("Is faching north?")

def at_goal():
    print("At goal?")

def wall_on_right():
    print("Wall on right?")

def front_is_clear():
    print("Front is clear?")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def do_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for step in range(1,7):
#  move()
#  do_hurdle()

#hurd_number = 6
#while hurd_number > 0:
#    move()
#    do_hurdle()
#    hurd_number -= 1

#while not at_goal():
#    if front_is_clear():
#        move()
#    elif wall_in_front():
#        do_hurdle()
    
while not at_goal():
    if is_facing_north():
        if wall_on_right():
            move()
        else:
            turn_right()
            move()
            turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
    