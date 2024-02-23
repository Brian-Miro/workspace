from tkinter import *

operador = ""
numero1 = 0

def operacion(op):
    global numero1
    global operador
    numero1 = float(textbox.get())
    operador = op
    textbox.delete(0, END)

def suma():
    operacion("+")

def resta():
    operacion("-")

def multiplicacion():
    operacion("*")

def division():
    operacion("/")

def borrar():
    textbox.delete(0, END)

def evaluar():
    numero2 = float(textbox.get())
    textbox.delete(0, END)
    if operador == "+":
        textbox.insert(END, numero1 + numero2)
    elif operador == "-":
        textbox.insert(END, numero1 - numero2)
    elif operador == "*":
        textbox.insert(END, numero1 * numero2)
    elif operador == "/":
        textbox.insert(END, numero1 / numero2)
    else:
        textbox.insert(END, "Error")

# Crea la ventana principal
ventana = Tk()
ventana.title('Calculadora')

textbox = Entry(ventana, width = 20)
textbox.grid(row = 0, column = 0, columnspan = 3)

boton_suma = Button(ventana, text = "+", width = 3, command = suma)
boton_suma.grid(row = 2, column = 0)
boton_resta = Button(ventana, text = "-", width = 3, command = resta)
boton_resta.grid(row = 2, column = 1)
boton_multiplicacion = Button(ventana, text = "*", width = 3, command = multiplicacion)
boton_multiplicacion.grid(row = 3, column = 0)
boton_division = Button(ventana, text = "/", width = 3, command = division)
boton_division.grid(row = 3, column = 1)
boton_igual = Button(ventana, text = "=", width = 6, command = evaluar)
boton_igual.grid(row = 4, column = 0, columnspan = 2)
boton_borrar = Button(ventana, text = "CLEAR", width = 6, command = borrar)
boton_borrar.grid(row = 4, column = 2, sticky = E)

# Bucle evento principal
ventana.mainloop()