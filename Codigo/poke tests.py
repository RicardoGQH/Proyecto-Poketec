#Proyecto de introducción a la programación de Ricardo Gómez Quesada 2026009771
#Establesimiento de la ventana del proyecto
from tkinter import *
ventana=Tk()
ventana.title("Proyecto Ricardo")
ventana.minsize(700 , 500)

#insercion de imagenes
from tkinter import PhotoImage
from os import path
from PIL import *

def cargar_imagen(nombre):
    ruta = r"C:\Users\Ricar\Documents\proyecto\001.png"
    img = PhotoImage(file=ruta)
    return img

from tkinter import *
label=Label(ventana,text="hola mundo")
label.pack()

main_canva= Canvas(ventana, height=215, width=215, bg="white")
main_canva.place(x=552,y=525)

from cProfile import label
main_canva.fondo = cargar_imagen('fondo.png')
Fondo1 = main_canva.create_image(0,0,anchor=NW, image=main_canva.fondo)
ventana.mainloop()