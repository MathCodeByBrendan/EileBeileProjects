import turtle as t
import numpy as np
import math
import random

t1 = t.Turtle()
ct = t.Turtle()

#Helper functions
def is_string_fraction(n):
    if '/' in n:
        return True
    else:
        return False

def repeat() -> bool:
    while True:
        repeat = input("Play again? Y for yes, N for no: ").lower().strip()
        if repeat != 'y' and repeat !='n':
            print("Answer must be N or Y.")
            continue
        break
    if repeat == 'y':
        return True
    else:
        return False
    
def test_user(identity, val):
        while True:
            while True:
                try:
                    ans_to_simplify = input(f"Enter {identity}(θ) as a fraction (a/b) or a number (0.2342) with 4 decimal places: ")
                    #if function() -> bool: automatically checks for is True, if false, does not run
                    if is_string_fraction(ans_to_simplify):
                        a_to_simplify, b_to_simplify = ans_to_simplify.split('/')
                        a, b = float(a_to_simplify), float(b_to_simplify)
                        ans = a / b
                    else:
                        ans = float(ans_to_simplify)
                except ValueError:
                    print("Answer must be a number or fraction. Please try again.")
                    continue
                break

                #Within 0.1 percent
            if math.isclose(ans, val, rel_tol=1e-3):
                print('Awesome answer! CORRECT!!!')
                break
            else:
                print("So close!!!")
                if repeat():
                    continue
                else:
                    break

def test_user_g2(θ_radians, θ_degrees):
        while True:
                try:
                    ans_to_simplify = input(f"Enter θ in degrees (1 decimal place or radians (3 decimal places): ")
                    ans = float(ans_to_simplify)
                except ValueError:
                    print("Answer must be a number or fraction. Please try again.")
                    continue
    

                #Within 0.1 percent
                if math.isclose(ans, θ_radians, rel_tol=1e-3) or math.isclose(ans, θ_degrees, rel_tol=1e-1):
                    print('Awesome answer! CORRECT!!!')
                    break
                else:
                    print("So close!!!")
                    if repeat():
                        continue
                    else:
                        break

#Visualize Adjacent length
def visualize_adjacent():
        t1.penup()
        t1.setposition(green/2 -20, -30)
        t1.pencolor('green')
        t1.write(f'{green} units', font = Font_Main)

#Visualize Opposite length
def visualize_opposite():
        t1.penup()
        t1.setposition(green + 20, blue/2)
        t1.pencolor('blue')
        t1.write(f'{blue} units', font = Font_Main)

#Visualize Hypotenuse length
def visualize_hypotenuse():
        t1.penup()
        t1.setposition(green/2 - 110, blue/2)
        t1.pencolor('white')
        t1.write(f'~ {white:.2f} units', font = Font_Main)

def clear_triangle_and_markup():
    t1.clear()
    t1.setposition(0, 0)
    t1.setheading(0)
    ct.clear()
    ct.setposition(0, 0)
    ct.setheading(0)


#Set Background Color
t.bgcolor('black')
t.pensize(3)

#Let green be adjacent, blue be opposite, white be hypotenuse, define them using abstract number 0, and redefine later
green = 0
blue = 0
white = 0

#Main Turtle
t.Turtle()

#Fonts
Font_Main = ('Monospace', 12, 'bold')
Font_20 = ('Monospace', 20, 'bold')
Font_25 = ('Monospace', 25, 'bold')

#Create Title
t.color('yellow')
t.penup()
t.setposition(-300, 200)
t.pendown()
t.write('Trig Games', font = Font_25)
t.penup()
t.setposition(0, 0)

# Create Game Options User Interface
t.color("red")
for i in range(1, 4):
    t.penup()
    delta_y = 100 * (i - 1)
    y_pos = 100 - delta_y
    t.setposition(-300, y_pos)
    t.pendown()
    t.write(f'To play game {i} enter {i}', font = Font_Main)

def create_triangle()-> list:
    min_length = 50
    max_length = 250
    
    # Generate lengths (green, blue, white)
    green, blue = [np.random.randint(min_length, max_length) for _ in range(2)]
    white = np.hypot(green, blue)

    #Create Triangle
    ct.pendown()
    ct.pencolor('green')
    ct.forward(green)
    ct.pencolor('blue')
    ct.penup()
    ct.backward(30)
    ct.pendown()
    ct.left(90)
    ct.forward(30)
    ct.right(90)
    ct.forward(30)
    ct.left(90)
    ct.penup()
    ct.backward(30)
    ct.pendown()
    ct.pencolor('blue')
    ct.forward(blue)
    ct.color('white')
    ct.left(180-np.degrees(np.atan((green/blue))))
    ct.forward(white)

    # (P_1)!!!     #Create theta symbol
    x_position = 100 * ((max_length + 150) - (blue)) / (max_length + blue) - green/25
    ct.penup()
    ct.setposition(x_position, 0)
    ct.pendown()
    ct.color('light blue')
    ct.write('θ', font = Font_20)
    
    return green, blue, white

def game_1():
    while True:
        #Create subTurtle for game_1(), create triangle and define adjacent(green), opposite(blue) and hypot(white)
        global green, blue, white
        green, blue, white = create_triangle()
        #Visualize Adjacent length
        visualize_adjacent()
        #Visualize Opposite length
        visualize_opposite()
        #Visualize Hypotenuse length
        visualize_hypotenuse()
        #calculate sin(θ), cos(θ), and tan(θ)
        sin_val = blue/white
        cos_val = green/white
        tan_val = blue/green
        
        #Use sin/cos/tan verifying helper function

        tests = [
            ('sin', sin_val),
            ('cos', cos_val),
            ('tan', tan_val)
        ]

        random.shuffle(tests)

        for identity, val in tests:
            test_user(identity, val)

        clear_triangle_and_markup()
        if repeat():
            continue
        break
    #let user play new game
    select_game()

def play_game_2(side1, side2):
    global green, blue, white
    green, blue, white = create_triangle()
    θ_radians = np.atan(blue/green)
    θ_degrees = np.degrees(θ_radians)


    if side1 == 'opposite':
        visualize_opposite()
    elif side1 == 'adjacent':
        visualize_adjacent()
    else:
        print("Side one must be 'opposite' or 'adjacent'")
    

    if side2 == 'adjacent':
        visualize_adjacent()
    elif side2 == 'hypotenuse':
        visualize_hypotenuse()
    else:
        print("Side two must be 'adjacent' or 'hypotenuse'")

    print(f"Part 1: calculate θ based on {side1} and {side2} lengths:")

    test_user_g2(θ_radians, θ_degrees)

    clear_triangle_and_markup()

    

 
def game_2():
    while True:
        games = [
            ('opposite', 'hypotenuse'),
            ('adjacent', 'hypotenuse'),
            ('opposite', 'adjacent')
        ]

        random.shuffle(games)

        for side1, side2 in games:
            play_game_2(side1, side2)

        if repeat():
            clear_triangle_and_markup()
            continue
        else:
            break  
    #Let user select new game
    select_game()
        

def select_game():
    while True:
        selection = input("Enter 1 to play the easiest level, 2 for moderate. Upcoming levels are in the making. Expected completion: 07/27/2025: ")
        if selection == '1':
            game_1()
            break
        elif selection =='2':
            game_2()
            break
        else:
            print("Please enter 1 or 2")
            continue

select_game()

t.done()
