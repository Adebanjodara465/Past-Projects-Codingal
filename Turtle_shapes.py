import turtle
   #TO DO---DRAW A HEXAGON, EQUILATERAL TRIANGLE AND A RECTANGLE
pen = turtle.Turtle() 
paper = turtle.Screen()
paper.setup(700, 700)

bg = input("What colour of background do you want?")
paper.bgcolor(bg)

fc = input("What colour crayon do you want?")
pen.fillcolor(fc)

#code for the square 
pen.goto(0,0)
pen.begin_fill()
for x in range(4):
    pen.forward(100)
    pen.right(90) #the .left and .right are to turn the angle of the turtle pen
pen.end_fill()    

pen.penup()


cl = input("Choose another color: ")
pen.fillcolor(cl)

#equilateral triangle
pen.goto(120,0)
pen.pendown()

pen.begin_fill()
for t in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()
  
  
hc = input("The color for the hexagon?: ")    
pen.fillcolor(hc)

pen.penup()
pen.goto(-120,0)
pen.pendown()

#for the hexagon; 6 sides
pen.begin_fill()
for h in range(6):
    pen.forward(80)
    pen.left(60)
pen.end_fill()

pen.penup()  


rc = input("The last color?")
pen.fillcolor(rc)


pen.goto(0,200)
pen.begin_fill()
for x in range(2): #since a rec has TWO PAIR of sides; long and short
    pen.forward(150)
    pen.right(90) #the .left and .right are to turn the angle of the turtle pen
    pen.forward(50)
    pen.right(90)
pen.end_fill()    

pen.penup()
  
paper.mainloop()