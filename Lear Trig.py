import turtle as t
import numpy as np
import math

t1 = t.Turtle()

#Helper functions
def is_string_fraction(n):
    if '/' in n:
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
                while True:
                    repeat = input("False. Would you like to try again? Press N for no, Y for yes:").lower().strip()
                    if repeat != 'n' and repeat != 'y':
                        print("Answer must be Y, or N.")
                        continue
                    break
                if repeat == 'n':
                    break
                else:
                    continue

def test_user_g2(θ_radians, θ_degrees):
        while True:
            while True:
                try:
                    ans_to_simplify = input(f"Enter θ in degrees (1 decimal place or radians (3 decimal places): ")
                    ans = float(ans_to_simplify)
                except ValueError:
                    print("Answer must be a number or fraction. Please try again.")
                    continue
                break

                #Within 0.1 percent
            if math.isclose(ans, θ_radians, rel_tol=1e-3) or math.isclose(ans, θ_degrees, rel_tol=1e-1):
                print('Awesome answer! CORRECT!!!')
                break
            else:
                while True:
                    repeat = input("False. Would you like to try again? Press N for no, Y for yes:").lower().strip()
                    if repeat != 'n' and repeat != 'y':
                        print("Answer must be Y, or N.")
                        continue
                    break
                if repeat == 'n':
                    break
                else:
                    continue
#Set Background Color
t.bgcolor('black')
t.pensize(3)

#Let green be adjacent, blue be oppisite, white be hypotenuse, define them using abstract number 0, and redefine later
green = 0
blue = 0
white = 0

#Main Turtle
t.Turtle()
t.pencolor('orange')

#Fonts
Font_Main = ('Monospace', 12, 'bold')
Font_20 = ('Monospace', 20, 'bold')
Font_25 = ('Monospace', 25, 'bold')

# Create Game Options
for i in range(1, 4):
    t.penup()
    delta_y = 100 * (i - 1)
    y_pos = 100 - delta_y
    t.setposition(-300, y_pos)
    t.pendown()
    t.write(f'To play game {i} enter {i}', font = Font_Main)

#Create basic right triangle, define theta position

ct = t.Turtle()

def create_triangle()-> list:
    min_length = 100
    max_length = 350
    
    # Generate lengths (green, blue, white)
    green, blue = [np.random.randint(min_length, max_length) for _ in range(2)]
    white = np.hypot(green, blue)

    #Create Title
    ct.penup()
    ct.setposition(-150, 200)
    ct.pendown()
    ct.color("orange")
    ct.write('Trig Games', font = Font_25)
    ct.penup()
    ct.setposition(0, 0)

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
        #Create subTurtle for game_1(), create triangle and define adjacent(green), oppisite(blue) and hypot(white)
        green, blue, white = create_triangle()

        #Visualize Adjacent length
        t1.penup()
        t1.setposition(green/2 -20, -30)
        t1.pencolor('green')
        t1.write(f'{green} units', font = Font_Main)
        #Visualize Opposite length
        t1.penup()
        t1.setposition(green + 20, blue/2)
        t1.pencolor('blue')
        t1.write(f'{blue} units', font = Font_Main)
        #Visualize Hypotenuse length
        t1.penup()
        t1.setposition(green/2 - 110, blue/2)
        t1.pencolor('white')
        t1.write(f'~ {white:.2f} units', font = Font_Main)

        #calculate sin(θ), cos(θ), and tan(θ)
        sin_val = blue/white
        cos_val = green/white
        tan_val = blue/green
        
        #Use sin/cos/tan verifying helper function
        while True:
            test_user('sin', sin_val)
            test_user('cos', cos_val)
            test_user('tan', tan_val)
            repeat = input("Play again? Y for yes, N for no: ").lower().strip()
            if repeat != 'y' and repeat !='n':
                print("Answer must be N or Y.")
                continue
            break
            
        if repeat == 'y':
            t1.clear()
            t1.setposition(0, 0)
            t1.setheading(0)
            ct.clear()
            ct.setposition(0, 0)
            ct.setheading(0)
            continue
        else:
            break  
        
    t1.clear()
    t1.setposition(0, 0)
    t1.setheading(0)
    ct.clear()
    ct.setposition(0, 0)
    ct.setheading(0)


'''
Need to create functions to visualize each individual side length: oppisite, adjacent, hypotenuse. 
Then need to cycle through showing oppisite and hypot only, adjacent and hypot only, then oppisite and adjacent only. 
During each phase of the cycle need to visualize new triangle.
'''

def play_game_2(side1, side2):
    green, blue, white = create_triangle()
    θ_radians = np.atan(blue/green)
    θ_degrees = np.degrees(θ_radians)

    #Visualize Adjacent length
    def visualize_adjacent():
        t1.penup()
        t1.setposition(green/2 -20, -30)
        t1.pencolor('green')
        t1.write(f'{green} units', font = Font_Main)
    #Visualize Opposite length
    def visualize_oppisite():
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


    if side1 == 'opposite':
        visualize_oppisite()
        side1 = 'opposite'
    elif side1 == 'adjacent':
        visualize_adjacent()
        side1 = 'adjacent'
    else:
        print("Side one must be 'opposite' or 'adjacent'")
    

    if side2 == 'adjacent':
        visualize_adjacent()
        side2 = 'adjacent'
    elif side2 == 'hypotenuse':
        visualize_hypotenuse()
        side2 = 'hypotenuse'
    else:
        print("Side two must be 'adjacent' or 'hypotenuse'")

    print(f"Part 1: calculate θ based on {side1} and {side2} lengths:")

    test_user_g2(θ_radians, θ_degrees)

    t1.clear()
    t1.setposition(0, 0)
    t1.setheading(0)
    ct.clear()
    ct.setposition(0, 0)
    ct.setheading(0)


 
def game_2():
    while True:
        play_game_2('opposite', 'hypotenuse')
        play_game_2('adjacent', 'hypotenuse')
        play_game_2('opposite', 'adjacent')
        repeat = input("Play again? Y for yes, N for no: ").lower().strip()
        while True:
            if repeat != 'y' and repeat !='n':
                print("Answer must be N or Y.")
                continue
            break
            
        if repeat == 'y':
            t1.clear()
            t1.setposition(0, 0)
            t1.setheading(0)
            ct.clear()
            ct.setposition(0, 0)
            ct.setheading(0)
            continue
        else:
            break  
        

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
