import turtle
import sympy
import numpy as np
import math
#Helper functions
def is_string_fraction(n):
    if '/' in n:
        return True
    else:
        return False

#Set Background Color
turtle.bgcolor('black')
turtle.pensize(3)

#Create basic right triangle, define theta position
green, blue = [np.random.randint(100, 350) for _ in range(2)]
white = np.hypot(green, blue)

#Create Title
turtle.penup()
turtle.setposition(-150, 200)
turtle.pendown()

turtle.color("orange")
turtle.write('Trig Games', font = ('Monospace', 25, 'bold'))
turtle.penup()
turtle.setposition(0, 0)

#Create Triangle
turtle.pendown()
turtle.pencolor('green')
turtle.forward(green)
turtle.pencolor('blue')
turtle.penup()
turtle.backward(30)
turtle.pendown()
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.penup()
turtle.backward(30)
turtle.pendown()
turtle.pencolor('blue')
turtle.forward(blue)
angle2_position = turtle.position()
turtle.color('white')
turtle.left(180-np.degrees(np.atan((green/blue))))
turtle.forward(white)

#Create theta symbol
x_position = 0
if blue < 150:
    x_position = 50 + green/25
elif blue < 250:
    x_position = 35 + green/25
else:
    x_position = 25 + green/25
turtle.penup()
turtle.setposition(x_position, 0)
turtle.pendown()
turtle.color('light blue')
turtle.write('θ', font = ('Monospace', 20, 'bold'))

for i in range(1, 4):
    turtle.penup()
    delta_y = 100 * (i - 1)
    y_pos = 100 - delta_y
    turtle.setposition(-300, y_pos)
    turtle.pendown()
    turtle.write(f'To play game {i} enter {i}', font = ('Monospace', 12, 'bold'))

def game_1():
    #Creating a number turtle
    game1_turtle = turtle.Turtle()

    #Visualize Adjacent length
    game1_turtle.penup()
    game1_turtle.setposition(green/2 -20, -30)
    game1_turtle.pencolor('green')
    game1_turtle.write(f'{green} units', font = ('Monospace', 10, 'bold'))
    #Visualize Opposite length
    game1_turtle.penup()
    game1_turtle.setposition(green + 20, blue/2)
    game1_turtle.pencolor('blue')
    game1_turtle.write(f'{blue} units', font = ('Monospace', 10, 'bold'))
    #Visualize Opposite length
    game1_turtle.penup()
    game1_turtle.setposition(green/2 - 110, blue/2)
    game1_turtle.pencolor('white')
    game1_turtle.write(f'~ {white:.2f} units', font = ('Monospace', 10, 'bold'))

    sin_val = blue/white
    cos_val = green/white
    tan_val = blue/green
    
    #Define sin/cos/tan verifying helper function
    def test_user(identity, trig_val):
        while True:
            while True:
                try:
                    ans_to_simplify = input(f"Enter {identity}(θ) as a fraction (a/b) or a number (0.2342) with 4 decimal places: ")
                    if is_string_fraction(ans_to_simplify) is True:
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
            if math.isclose(ans, trig_val, rel_tol=1e-3):
                print('Awesome answer! CORRECT!!!')
                break
            else:
                repeat = input("False. Would you like to try again? Press N for no, Y for yes:").lower().strip()
                if repeat == 'n':
                    break
                elif repeat == 'y':
                    continue
                else:
                    print("Answer must be Y, or N.")
    while True:
        test_user('sin', sin_val)
        test_user('cos', cos_val)
        test_user('tan', tan_val)
        while True:
            repeat = input("Play again? Y for yes, N for no: ").lower().strip()
            if repeat != 'y' and repeat !='n':
                print("Answer must be N or Y.")
                continue
            break
        if repeat == 'y':
            continue
        break
    game1_turtle.clear()

def select_game():
    while True:
        selection = input("Enter 1 to play the easiest level. Upcoming levels are in the making. Expected completion: 07/27/2025: ")
        if selection == '1':
            game_1()
            break
        else:
            print("Please enter 1")
            continue

select_game()

turtle.done()