import turtle

def crearMastriz(screen: turtle.Screen, t:turtle.Turtle):
    t.pendown()
    t.hideturtle()
    t.speed(0)
    t.pencolor('blue')
    for x in range(-10, 40):
        t.penup()
        t.goto(x*10, -100)
        t.pendown()
        t.goto(x*10, 100)

    for y in range(-10, 40):
        t.penup()
        t.goto(-100, y*10)
        t.pendown()
        t.goto(400, y * 10)

    t.pencolor('black')
    for x in range(-10,40):
        t.penup()
        t.goto(x*10,0)
        t.pendown()
        t.write(x*10, align="center", font=("Arial", 10, "normal"))
        
        t.penup()
        t.goto(0,x*10)
        t.pendown()
        t.write(x*10, align="center", font=("Arial", 10, "normal"))
    t.penup()
def FxCuadratica(a:int,b:int,c:int,x):
    return (a * (x)**2 + (b * x) + c)

screen = turtle.Screen()
screen.setup(width=600, height=600)  # Tamaño de la ventana
screen.setworldcoordinates(-100, -100, 200, 100)  # Coordenadas del mundo
t = turtle.Turtle()

crearMastriz(screen,t)
    
###dibujar funcion 
tabx1 = -100
tabx2 = 200
for x in range(tabx1,tabx2):
    if x == tabx1:
        t.penup()
    y = FxCuadratica(-1,10,1,x/10)
    
    t.goto(x,y)
    
    if x == tabx1:
        t.pendown()
        t.begin_fill()
        

t.fillcolor("red")
t.end_fill()    

crearMastriz(screen,t)

screen.exitonclick()