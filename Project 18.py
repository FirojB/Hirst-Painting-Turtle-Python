import turtle as t # Turtle Library
import colorgram # Library for extracting the color from a jpeg image
import random # Library to generate random number

screen = t.Screen() # Object Creation for Output Screen

my_turtle = t.Turtle() # Object Creation for Turtle Module

my_turtle.hideturtle() # Hiding the Turtle from Screen
my_turtle.penup()

my_turtle.goto(-200, -200) # Setting turtle initial position
my_turtle.width(20) # setting the turtle size

t.colormode(255) # Turtle color mode for RGB

screen.title("Welcome to the Hirst painting!") # Turtle Screen Title

rgb_colors = [] # Empty list for RGB color
colors = colorgram.extract('image.jpg', 30) # importing the number of color(30) from the images

for color in colors: # To store the RGB values from the images
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


y = 25
for i in range(1, 10):  # Loop for coloumns
    for _ in range(1, 10): # Loop for Rows
        my_turtle.color(random.choice(rgb_colors))
        my_turtle.down()
        my_turtle.forward(0)
        my_turtle.up()
        my_turtle.forward(30)
    my_turtle.goto(-200, -200+ y) # Setting the Turtle position on the output screen.
    y += 25
screen.exitonclick() # Hold the output screen till the click