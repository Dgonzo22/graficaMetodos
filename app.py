from tkinter import Tk,LabelFrame, Entry, Button,Label, IntVar,END,INSERT,Text
from grafica import Grafica,FxCuadratica

class app(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=10)
        self.rowconfigure(0,weight=1)
        
        self.menu = LabelFrame(self)
        self.menu.columnconfigure(0,weight=1)
        self.menu.columnconfigure(1,weight=5)
        self.menu.grid(column=0,row=0,sticky="SNEW")
        self.initElemenMenu()
        self.insertValores()
        
        self.grafica = Grafica(self)
        self.grafica.grid(column=1,row=0,sticky="SNEW") 
        self.grafica.config(cursor="wait")
        self.grafica.crearMastriz()
        self.grafica.config(cursor="arrow")
        self.mainloop()
    def initElemenMenu(self):
        Label(self.menu,text="Numero Puntos").grid(column=0,row=0)
                
        self.entradaNpuntos = Entry(self.menu)
        self.entradaNpuntos.grid(column=1,row=0,sticky="SNEW")

        
        Label(self.menu,text="a").grid(column=0,row=1)
                
        self.entradaA = Entry(self.menu)
        self.entradaA.grid(column=1,row=1,sticky="SNEW")

        Label(self.menu,text="b").grid(column=0,row=2)
                
        self.entradaB = Entry(self.menu)
        self.entradaB.grid(column=1,row=2,sticky="SNEW")
        
        self.panelFx =  LabelFrame(self.menu,text="Funcion Cuadratica")
        self.panelFx.grid(column=0,row=3,columnspan=2,sticky="SNEW")
        
        self.funcionA = Entry(self.panelFx)
        self.funcionA.grid(column=0,row=0)
        Label(self.panelFx,text="X² +").grid(column=1,row=0,sticky="SNEW")
        
        self.funcionB = Entry(self.panelFx)
        self.funcionB.grid(column=2,row=0)
        Label(self.panelFx,text="X  +").grid(column=3,row=0,sticky="SNEW")
        
        self.funcionC = Entry(self.panelFx)
        self.funcionC.grid(column=4,row=0)
        
        self.btnCuadratica = Button(self.menu,text="Mostrar",command=lambda: self.mostrarGraficaCuadratica())
        self.btnCuadratica.grid(column=0,row=4,sticky="SNEW")
        
        self.btnCuadraticaMetodoTrapezoide = Button(self.menu,text="Metodo Trapezoide",command=lambda: self.calular_trapezoide())
        self.btnCuadraticaMetodoTrapezoide.grid(column=1,row=4,sticky="SNEW")
        
        self.btnMatriz = Button(self.menu,text="Matriz",command=lambda: self.grafica.crearMastriz())
        self.btnMatriz.grid(column=0,row=5,sticky="SNEW")
        
        self.cajaTexto = Text(self.menu)
        self.cajaTexto.grid(column=0,row=6,sticky="SNEW",columnspan=2)
    def insertValores(self):
        self.entradaNpuntos.insert(END,6)
        self.entradaA.insert(END,-100)
        self.entradaB.insert(END,200)
        
        self.funcionA.insert(END,-0.5)
        self.funcionB.insert(END,20)
        self.funcionC.insert(END,10)
    def mostrarGraficaCuadratica(self):
        self.grafica.config(cursor="wait")
        a = self.funcionA.get()
        b = self.funcionB.get()
        c = self.funcionC.get()        
        a = float(a)
        b = float(b)
        c = float(c)
        self.grafica.dibujarFuncionCudartica(a,b,c)
        self.grafica.config(cursor="arrow")
    def calular_trapezoide(self):
        nPuntos = self.entradaNpuntos.get()
        A = self.entradaA.get()
        B = self.entradaB.get()
        
        nPuntos = int(nPuntos)
        A = int(A)
        B = int(B)
        
        h = (B - A) / nPuntos
        op1 = f"h =  ({B} - ({A})) / {nPuntos}  = {h} \n"
        self.mostrarProcedimiento(op1)
        self.mostrarProcedimiento('|-----------------Calcular el punto de corte-----------------| \n')
        listaPuntos = []
        for i in range(0,nPuntos +1):
            listaPuntos.append(A + (i * h))
            self.mostrarProcedimiento('|------------------------------------------------------------|')
            self.mostrarProcedimiento(f"|     x{i}     |     {A} + ({i} x {h})|      {A + (i * h)}")
        self.mostrarProcedimiento('|------------------------------------------------------------| \n')
        self.mostrarProcedimiento('|-----------------Calcular por cada intervalo----------------| \n')
        listaFx = []
        for i in range(0,nPuntos+1):
            x1 = listaPuntos[i]
            if i < nPuntos:
                x2 = listaPuntos[i + 1]            
            a = float(self.funcionA.get())
            b = float(self.funcionB.get())
            c = float(self.funcionC.get())       
            
            
            y1 = FxCuadratica(a,b,c,x1)
            
            if i < nPuntos:
                self.grafica.dibujarTrapecio(px1=x1, py1=0,
                                             px2=x2, py2=0,
                                             px3=x2, py3=FxCuadratica(a,b,c,x2/10),
                                             px4=x1, py4=FxCuadratica(a,b,c,x1/10))
            self.mostrarProcedimiento(f"|  x = {x1} |Fx(x)|  = ({a})x² + ({b})x + ({c}) = {y1}")
            listaFx.append(y1)
        
        opDeArea = ""
        valorFinal = 0
        for i,fx in enumerate(listaFx):
            if i == 0 or i == len(listaFx)- 1:
                valorFinal = valorFinal + fx
                opDeArea += f'{fx}'
            else:
                valorFinal = valorFinal + (2 * fx)
                opDeArea += f' + 2({fx}) '
                
        valorFinal = valorFinal * (h / 2)
        opDeArea += f" ({h} / 2) = {str(valorFinal)}"
        self.mostrarProcedimiento(opDeArea)
    def mostrarProcedimiento(self,text:str):
        self.cajaTexto.insert(INSERT, text+ '\n')
app()        