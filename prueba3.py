from os import replace
from tkinter import *
from math import *
from sympy import *

def btnClik(num):
    global x
    global operador
    operador=operador+str(num)
    input_text.set(operador)

def resultado():
    global operador
    global z
    global y
    try:    
        if "limit(" in operador:
            operador = operador.replace("limit(", "")
            operador = operador.split(")")
            z = operador.pop(0)
            operador = ''.join(operador)
            opera = (limit(operador,x,z))
            input_text.set(opera)
            
            plot(operador, xlim=[-10,10], ylim=[-30,30])

        elif "limitLAT(" in operador:
            operador = operador.replace("limitLAT(", "")
            operador = operador.split(")")
            z = operador.pop(0)
            y = operador.pop(1)
            operador = ''.join(operador)
            opera = (limit(operador,x,z, y))
            input_text.set(opera)
            
            plot(operador, xlim=[-10,10], ylim=[-30,30])

        else:

            opera=str(eval(operador))
            input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
def delete():
    Salida_state = Salida.get()
    if len(Salida_state):
        Salida_new_state= Salida_state[-1]
        clear()
        Salida.insert(0, Salida_new_state)
    else:
        clear()


def clear():
    global operador
    operador=("")
    input_text.set("0")

ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x660")
ventana.configure(background="SkyBlue4")
color_boton=("gray77")
z = 0
y = 0
ancho_boton=8
alto_boton=2
input_text=StringVar()
operador=""
x = Symbol('x')

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=10,y=60)

Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=240)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=197,y=300)
Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=300)
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt(")).place(x=17,y=420)
Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=480)
Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log(")).place(x=287,y=480)
Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)
Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=420)
Button(ventana,text="limit",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("limit(")).place(x=17,y=540)
Button(ventana,text="x",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("x")).place(x=107,y=540)
Button(ventana,text="oo",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("oo")).place(x=197,y=540)
Button(ventana,text="-oo",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-oo")).place(x=287,y=540)
Button(ventana,text="limitLAT",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("limitLAT(")).place(x=17,y=600)
Button(ventana,text="Del",bg=color_boton,width=6,height=1,command=lambda:delete()).place(x=287,y=150)

clear()

ventana.mainloop()  