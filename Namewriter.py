import turtle, random
import turtlealphabet

wn = turtle.Screen()
wn.bgcolor("black")                          # Created a window to draw and setted it's attiributes
wn.title("Python Turtle Name Writer")
wn.colormode(255)
name = wn.textinput("Name, Please.","Write your name")      # Getting his/her names from user


charsinname = []                 # Created an empty list to fill with necessary letters

charsinnamewithduplicates = list(name)         # Seperated name in to a list


for i in charsinnamewithduplicates:
    if i ==" ":                               # Removing duplicates and spaces
        i ==" "
    elif i not in charsinname:
        charsinname.append(i)


del charsinname[5:]              # Removed unnecessary letters(We only need first 5 index)




NameWriter = turtle.Turtle()     # Created a turtle to write letters
NameWriter.pensize(2)
NameWriter.color("blue")
NameWriter.penup()               # Configured its attiributes and set a starting position
NameWriter.goto(-300,0)    
NameWriter.pendown()


for i in charsinname:                                # Looping for every letter we will draw
    r =int((255*random.random()))
    g =int((255*random.random()))
    b =int((255*random.random()))
    NameWriter.color(r,g,b)
    turtlealphabet.trtshape(NameWriter,i)



wn.exitonclick()