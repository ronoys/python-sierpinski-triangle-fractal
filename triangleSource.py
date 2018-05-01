import turtle
import random
window = turtle.Screen()
q = turtle.Turtle()
size = int(input("Enter the size of the triangle in pixels "))
loop = int(input("Enter the number of levels of the fractal to be created "))


q.penup()
q.goto(0-(size/2),0-(size/2))
q.pendown()


def triangle(x,y):
 
    colors = ['red','orange','yellow','green', 'blue', 'purple', 'pink']
    q.fillcolor(random.choice(colors))
    q.begin_fill()
    
    if y != 0:
        triangle(x/2,y-1)
        q.forward(x/2)
        triangle(x/2,y-1)
        q.backward(x/2)
        q.left(60)
        q.forward(x/2)
        q.right(60)
        triangle(x/2,y-1)
        q.left(60)
        q.backward(x/2)
        q.right(60)
        
    else:
        
        for i in range(0,3):
            q.forward(x)
            q.left(120)
            
    q.end_fill()
            
triangle(size,loop)

