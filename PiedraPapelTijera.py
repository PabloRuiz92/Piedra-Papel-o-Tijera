from tkinter import *
import random

root=Tk()
root.title("Piedra, papel o tijeras")
root.geometry("300x250")
root.resizable(0,0)
root.iconbitmap("Fortune_Telling_Machine.ico")
#Creacion del canvas--------------------------------
background = PhotoImage(file="Stage_Basement_room.png")
canvas1 = Canvas(root, width=300, height=250)
canvas1.create_image( 0, 0, image = background, anchor = "nw")
canvas1.pack(fill = "both", expand = True)

#Randomizacion
def eleccion_random():
    piedraPapelTijera = ["Piedra", "Papel"]
    eleccion = random.choice(piedraPapelTijera)
    if eleccion == "Piedra":
        labelOponente.config(image=imagenPiedra)
        labelOponente.image = imagenPiedra
    elif eleccion == "Papel":
        labelOponente.config(image=imagenPapel)
        labelOponente.image = imagenPapel
    else:
        labelOponente.config(image=imagenTijera)
        labelOponente.image = imagenTijera

#Funciones de los botones---------------------------
def boton_piedra():
    eleccion_random()
    if labelOponente.image == imagenPiedra:
        canvas1.itemconfig(canvas_label_resultado, text="Empate")
    elif labelOponente.image == imagenPapel:
        canvas1.itemconfig(canvas_label_resultado, text="Perdiste")
    else:
        canvas1.itemconfig(canvas_label_resultado, text="Ganaste!")

def boton_papel():
    eleccion_random()
    if labelOponente.image == imagenPiedra:
        canvas1.itemconfig(canvas_label_resultado, text="Ganaste!")
    elif labelOponente.image == imagenPapel:
        canvas1.itemconfig(canvas_label_resultado, text="Empate")
    else:
        canvas1.itemconfig(canvas_label_resultado, text="Perdiste")

def boton_tijera():
    eleccion_random()
    if labelOponente.image == imagenPiedra:
        canvas1.itemconfig(canvas_label_resultado, text="Perdiste")
    elif labelOponente.image == imagenPapel:
        canvas1.itemconfig(canvas_label_resultado, text="Ganaste!")
    else:
        canvas1.itemconfig(canvas_label_resultado, text="Empate")


#Creacion y colocacion de botons/labels-------------
imagenPiedra = PhotoImage(file="Piedra.png")
botonPiedra = Button(root, image=imagenPiedra, bd=0, command=boton_piedra)

imagenPapel = PhotoImage(file="Papel.png")
botonPapel = Button(root, image=imagenPapel, bd=0, command=boton_papel)

imagenTijera = PhotoImage(file="Tijera.png")
botonTijera = Button(root, image=imagenTijera, bd=0, command=boton_tijera)

imagenInicial = PhotoImage(file="Isaac.png")
labelOponente = Label(root, textvariable="inicial" ,image=imagenInicial)

canvas_label_titulo = canvas1.create_text(150, 51, anchor=CENTER, text="Piedra, Papel o Tijera!")
canvas_label_oponente = canvas1.create_window(150, 81, anchor=CENTER,window=labelOponente)
canvas_boton_piedra = canvas1.create_window(118, 113, anchor=CENTER,window=botonPiedra)
canvas_boton_papel = canvas1.create_window(150, 113, anchor=CENTER,window=botonPapel)
canvas_boton_tijera = canvas1.create_window(182, 113, anchor=CENTER,window=botonTijera)
canvas_label_resultado = canvas1.create_text(150, 145, anchor=CENTER,text="")

root.mainloop()