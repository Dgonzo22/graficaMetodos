from tkinter import LabelFrame
from turtle import *

def FxCuadratica(a:int,b:int,c:int,x):
    return (a * (x)**2 + (b * x) + c)

class Grafica(LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        canvas = ScrolledCanvas(self)
        canvas.grid(column=0,row=0,sticky="SNEW")
        screen = TurtleScreen(canvas)
        screen.bgcolor("white")
        screen.setworldcoordinates(-100, -100, 200, 100)
        self.t = RawTurtle(screen)
        self.t.speed(0)
    def crearMastriz(self):
        self.t.pendown()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.pencolor('blue')
        for x in range(-40, 40):
            self.t.penup()
            self.t.goto(x*10, -400)
            self.t.pendown()
            self.t.goto(x*10, 400)

        for y in range(-40, 40):
            self.t.penup()
            self.t.goto(-400,y*10)
            self.t.pendown()
            self.t.goto(400, y* 10)

        self.t.pencolor('black')
        for x in range(-40,40):
            self.t.penup()
            self.t.goto(x*10,0)
            self.t.pendown()
            self.t.write(x*10, align="center", font=("Arial", 10, "normal"))
            
            self.t.penup()
            self.t.goto(0,x*10)
            self.t.pendown()
            self.t.write(x*10, align="center", font=("Arial", 10, "normal"))
        self.t.penup()
    def dibujarFuncionCudartica(self,a:int,b:int,c:int):
        
        tabx1 = -400
        tabx2 = 400
        for x in range(tabx1,tabx2):
            if x == tabx1:
                self.t.penup()
            y = FxCuadratica(a,b,c,x/10)
            
            self.t.goto(x,y)
            
            if x == tabx1:
                self.t.pendown()
                self.t.begin_fill()
        
        self.t.fillcolor("green")
        self.t.end_fill()
        self.t.penup()
    def dibujarTrapecio(self,px1,py1,px2,py2,px3,py3,px4,py4):
        
        self.t.penup()
        
        self.t.goto(px1,py1)
        self.t.begin_fill()
        self.t.pendown()
        self.t.goto(px1,py1)
        self.t.goto(px2,py2)
        self.t.goto(px3,py3)
        self.t.goto(px4,py4)
        self.t.goto(px1,py1)
        self.t.fillcolor("blue")
        self.t.end_fill()
        self.t.penup()
        
        