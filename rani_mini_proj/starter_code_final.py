# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""

SQUARE_SIZE = 20
color_list = []
# Multi colored trash:
from PIL import Image #imports folder
im = Image.open('papernobg.png') #gets the image
pix = im.load() #load returns a pixel access object that can be used to read and modify pixels
print(im.size) #prints the image size in pixels [x,y]
print(pix[30,15]) #prints the RGB value of a chosen pixel [x,y]

# White
new_width  = SQUARE_SIZE
new_height = SQUARE_SIZE
WHITE = 'white_paper.gif'
imW = im.resize((new_width, new_height), Image.ANTIALIAS)
imW.save(WHITE)
color_list.append(WHITE) 

# Blue
width, height = im.size # assigns the 
for x in range(width): 
    for y in range(height):
        #print(pix[x,y])
        r,g,b = pix[x,y][:3]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r//2,g//2,b) #Why did I do //? Try it with normal division.
BLUE = 'blue_paper.gif'
imB = im.resize((new_width, new_height), Image.ANTIALIAS)
imB.save(BLUE)
color_list.append(BLUE)


# Red
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y][:3]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r*2,g,b//2) #Why did I do //? Try it with normal division.
RED = 'red_paper.gif'
imR = im.resize((new_width,new_height), Image.ANTIALIAS)
imR.save(RED)
color_list.append(RED)

# Green
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y][:3]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r//2,g*2,b) #Why did I do //? Try it with normal division.
GREEN = 'green_paper.gif'
imG = im.resize((new_width,new_height), Image.ANTIALIAS)
imG.save(GREEN)
color_list.append(GREEN)

# Yellow
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y][:3]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r*2,g,b//4) #Why did I do //? Try it with normal division.
YELLOW = 'yellow_paper.gif'
imY = im.resize((new_width,new_height), Image.ANTIALIAS)
imY.save(YELLOW)
color_list.append(YELLOW)



snake_color = input("Choose a color for your snake: ").lower()


import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly


SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
screen = turtle.Screen()                             #size. 

#imS = Image.open('bg.gif')
#pix = imS.load()
#imSR = imS.resize((SIZE_X, SIZE_Y), Image.ANTIALIAS)
#screen.bgpic(imSR)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")
snake.color(snake_color)
screen.bgcolor('black')


#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    Stamp = snake.stamp()
    stamp_list.append(Stamp)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")


#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
def down():
    global direction
    direction = DOWN
    print("You pressed the down key!")

def left():
    global direction
    direction = LEFT
    print("You pressed the left key!")

def right():
    global direction
    direction = RIGHT
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

for color in color_list:
    print(color)
    turtle.register_shape(color)

food = turtle.clone()
rand_color = random.randint(0,len(color_list)-1)
rand_Shape = color_list[rand_color]
food.shape(rand_Shape)

food_pos = [(100,100), (-100,100), (-100, -100), (100,-100)]
food_stamps = []

for pos in food_pos:
    food.goto(pos)
    st = food.stamp()
    food_stamps.append(st)

food.ht()
    


def make_food():
    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    rand_color = random.randint(0,len(color_list)-1)
    rand_Shape = color_list[rand_color]
    food.shape(rand_Shape)
    food.goto(food_x,food_y)

    st = food.stamp()
    rand_food_pos = (food_x,food_y)
    food_pos.append(rand_food_pos)
    food_stamps.append(st)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    #grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:  #check if you hit a wall
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    global food_stamps, food_pos
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    if snake.pos() not in food_pos:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    else:
        print("You just got longer!")
    
    
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind]) # remove stamp in index
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
    
    if len(food_stamps) <= 5:
        make_food()

    if snake.pos() in (pos_list[:len(pos_list)-1]):
        print("You ate yourself! Game over!")
        quit()

    turtle.ontimer(move_snake, TIME_STEP)

move_snake()



