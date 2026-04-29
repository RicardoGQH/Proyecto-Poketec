#Proyecto introducción a la programación
#Ricardo Gómez Quesada carnet:2026009771

#Establecimiento de la ventana
from tkinter import *
import random
import tkinter as tk
main_window=Tk()
main_window.title("Pokemon stadium Tec edition")
main_window.state("zoomed") 

#establecimiento de los diccionarios de pokemons, usuario, oponente y apariencias
Pokemons={"pikachu":{"cualidades":{"vida":900,"defensa":70,"ataque":270},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\Pikachu frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\Pikachu atras.png")}},
          "charmander":{"cualidades":{"vida":1000, "defensa":80, "ataque":290},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\Charmander frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\charmnde espalda.png")}},
          "onix":{"cualidades":{"vida":1500,"defensa":20,"ataque":250},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\onix frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\onix espalda.png")}},
          "bulbasur":{"cualidades":{"vida":1100,"defensa":70,"ataque":280},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\bulbasaur frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\bulbasaur espalda.png")}},
          "ivy":{"cualidades":{"vida":1350,"defensa":40,"ataque":20},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\eevee frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\eevee espalda.png")}},
          "gyarados":{"cualidades":{"vida":850,"defensa":60,"ataque":380},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\gyarados frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\gyarados espalda.png")}},
          "squirtle":{"cualidades":{"vida":900,"defensa":10,"ataque":250},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\squirtle frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\squirtle espalda.png")}},
          "dragonite":{"cualidades":{"vida":1050,"defensa":80,"ataque":290},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\dragonite frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\dragonite espalda.png")}},
          "mewto":{"cualidades":{"vida":3500,"defensa":20,"ataque":135},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\mewtwo frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\mewtwo atras.png")}},
          "jiglypuff":{"cualidades":{"vida":800,"defensa":25,"ataque":220},"imagenes":{"frente":PhotoImage(file=r"..\imagenes\Pokemons\jigglypuff frente.png"),"espalda":PhotoImage(file=r"..\imagenes\Pokemons\jigglypuff espalda.png")}},}

apariencias={"avatar1":PhotoImage(file=r"..\imagenes\Apariencias\Avatar 1.png"),
             "avatar2":PhotoImage(file=r"..\imagenes\Apariencias\Avatar 2.png"),
             "avatar3":PhotoImage(file=r"..\imagenes\Apariencias\Avatar 3.png"),
             "avatar4":PhotoImage(file=r"..\imagenes\Apariencias\Avatar 4.png"),
             "avatar5":PhotoImage(file=r"..\imagenes\Apariencias\Avatar 5.png")}
 
Jugador={"nombre":{},
         "apariencia":{},
         "pokemones":{},
         "pokemon combatiente":{}}

oponente={"pokemons":{},
          "apariencia":{},
          "pokemon combatiente":{}}

#inserción de la imagen de pantalla de inicio y canvas
from PIL import Image, ImageTk
def cargar_imagen1(nombre):
    #esta funcion permite cargar la imagen que corresponte a la imagen de inicio
    pantalla_inicio= Image.open(r"..\imagenes\Pantalla inicio.png")
    pantalla_inicio= pantalla_inicio.resize((1580,850))
    return ImageTk.PhotoImage(pantalla_inicio)
img = cargar_imagen1("pantalla inicio")

main_canvas = Canvas(main_window, width=1800, height=1920, bg="pink")
main_canvas.pack(fill="both", expand=True)
primera=main_canvas.create_image(0, 0, anchor="nw", image=img)

#creación de botton start
def cargar_imagen2(nombre):
    #esta funcion sirve para usar la imagen de la seleccion de personaje
     pantalla_personaje=Image.open(r"..\imagenes\Diseño sin título (2).png")
     pantalla_personaje=pantalla_personaje.resize((1538,788))
     return ImageTk.PhotoImage(pantalla_personaje)
  
def iniciar():
    #esta funcion se encarga de canviar de cambiar del esenario 1 al escenario 2 y muestra otos botones
    #elimina la primera imagen y pone la nueva
    main_canvas.delete(primera)
    img2= cargar_imagen2('pantalla_personaje')
    segunda = main_canvas.create_image(0,0,anchor="nw",image=img2)
    
    #le da provicionalmente todos los pokemones al oponente como copia
    oponente["pokemons"]=Pokemons.copy()
    
    #muestra la caja de texto y los botones
    caja_nombre.place(x=700,y=685, width=750,height=70)
    boton_seleccionar1.place(x=120,y=600)
    boton_seleccionar2.place(x=420,y=600)
    boton_seleccionar3.place(x=720,y=600)
    boton_seleccionar4.place(x=1010,y=600)
    boton_seleccionar5.place(x=1300,y=600)
    boton_siguiente.place(x=1350,y=10)
    
    #se desaparece a si mismo
    boton_star.place_forget()

imagen_star=PhotoImage(file=r"..\imagenes\boton start.png")#imagen que usa el boton start
boton_star = tk.Button(main_window, text="START",command=iniciar, image=imagen_star)
boton_star.pack(fill="both",expand=True)
boton_star.place(x=700,y=500)
  
#creacion caja de texto
caja_nombre=Entry(main_window, width=5, font=("Pokemon pixel font",30))

def poner_nombre(palabre):
    #esta es una funcion simple la cual se encarga de cambiar el nombre de jugador a el escrito por el jugador
    Jugador["nombre"]=caja_nombre.get()
    
caja_nombre.bind("<Return>",poner_nombre)#esto sirve para que al presionar enter el nombre cambie

#creacion botones de seleccion del avatar
#mensaje de restriccion de avatares
restriccion_avatares= Label(main_window, text="SOLO PUEDES TENER UN ENTRENADOR, SI QUIERES CAMBIAR DESELECCIONA EL QUE NO QUIERES", font=("pokemon pixel font",30))

#imagenes para los botones seleccionadores y deseleccionadores
imagen_seleccionar=PhotoImage(file=r"..\imagenes\boton de seleccionar.png")
imagen_deseleccionadores=PhotoImage(file=r"..\imagenes\boton deseleccionar.png")

#Botones para seleccionar y deseleccionar avatar 1
def seleccionar_avatar1():
    #esta funcion se aplica al presionar el boton seleccionar, su funciones darle al jugador el avatar seleccionado y al oponente otro avatar
    #esta es una condicional que ayuda a que solo se pueda escoger una apariencia de entrenador
    restriccion_avatares.place_forget()
    if Jugador["apariencia"]:
        restriccion_avatares.place(x=300, y=60)
    else:
        Jugador["apariencia"]=apariencias["avatar1"]
        oponente["apariencia"]=apariencias["avatar5"]
        boton_seleccionar1.place_forget()
        boton_deseleccionar1.place(x=120,y=600)
    
def deseleccionar_avatar1():
    #su funcion es quitar el avatar que selecciono el jugador y al mismo tiempo el del oponente
    del Jugador["apariencia"]
    Jugador["apariencia"]={}#sirve para crear de nuevo la subseccion apariencia
    del oponente["apariencia"]
    boton_deseleccionar1.place_forget()
    boton_seleccionar1.place(x=120,y=600)

boton_seleccionar1= tk.Button(main_window,image=imagen_seleccionar, command=seleccionar_avatar1)
boton_seleccionar1.pack(fill=BOTH, expand=True)
boton_deseleccionar1=tk.Button(main_window,image=imagen_deseleccionadores, command=deseleccionar_avatar1)
boton_deseleccionar1.pack(fill=BOTH, expand=True)

#botones seleccionar y deseleccionar avatar 2
def seleccionar_avatar2():
    #esta funcion se aplica al presionar el boton seleccionar, su funciones darle al jugador el avatar seleccionado y al oponente otro avatar
    #esta es una condicional que ayuda a que solo se pueda escoger una apariencia de entrenador
    restriccion_avatares.place_forget()
    if Jugador["apariencia"]:
        restriccion_avatares.place(x=300,y=60)
    else:
        Jugador["apariencia"]=apariencias["avatar2"]
        oponente["apariencia"]=apariencias["avatar5"]
        boton_seleccionar2.place_forget()
        boton_deseleccionar2.place(x=420,y=600)
    
def deseleccionar_avatar2():
     #su funcion es quitar el avatar que selecciono el jugador y al mismo tiempo el del oponente
    del Jugador["apariencia"]
    Jugador["apariencia"]={}#sirve para crear de nuevo la subseccion apariencia
    del oponente["apariencia"]
    boton_deseleccionar2.place_forget()
    boton_seleccionar2.place(x=420,y=600)

boton_seleccionar2= tk.Button(main_window,image=imagen_seleccionar, command=seleccionar_avatar2)
boton_seleccionar2.pack(fill=BOTH, expand=True)
boton_deseleccionar2=tk.Button(main_window,image=imagen_deseleccionadores, command=deseleccionar_avatar2)
boton_deseleccionar2.pack(fill=BOTH, expand=True)

#seleccionador y deseleccionador avatar 3
def seleccionar_avatar3():
    #esta funcion se aplica al presionar el boton seleccionar, su funciones darle al jugador el avatar seleccionado y al oponente otro avatar
    #esta es una condicional que ayuda a que solo se pueda escoger una apariencia de entrenador
    restriccion_avatares.place_forget()
    if Jugador["apariencia"]:
        restriccion_avatares.place(x=300,y=60)
    else:
        Jugador["apariencia"]=apariencias["avatar3"]
        oponente["apariencia"]=apariencias["avatar5"]
        boton_seleccionar3.place_forget()
        boton_deseleccionar3.place(x=720,y=600)
    
def deseleccionar_avatar3():
     #su funcion es quitar el avatar que selecciono el jugador y al mismo tiempo el del oponente
    del Jugador["apariencia"]
    Jugador["apariencia"]={}#sirve para crear de nuevo la subseccion apariencia
    del oponente["apariencia"]
    boton_deseleccionar3.place_forget()
    boton_seleccionar3.place(x=720,y=600)
    
boton_seleccionar3= tk.Button(main_window,image=imagen_seleccionar, command=seleccionar_avatar3)
boton_seleccionar3.pack(fill=BOTH, expand=True)
boton_deseleccionar3=tk.Button(main_window,image=imagen_deseleccionadores, command=deseleccionar_avatar3)
boton_deseleccionar3.pack(fill=BOTH, expand=True)

#seleccionador y deseleccionador avatar 4
def seleccionar_avatar4():
    #esta funcion se aplica al presionar el boton seleccionar, su funciones darle al jugador el avatar seleccionado y al oponente otro avatar
    #esta es una condicional que ayuda a que solo se pueda escoger una apariencia de entrenador
    restriccion_avatares.place_forget()
    if Jugador["apariencia"]:
        restriccion_avatares.place(x=300,y=60)
    else:
        Jugador["apariencia"]=apariencias["avatar4"]
        oponente["apariencia"]=apariencias["avatar5"]
        boton_seleccionar4.place_forget()
        boton_deseleccionar4.place(x=1010,y=600)
    
def deseleccionar_avatar4():
     #su funcion es quitar el avatar que selecciono el jugador y al mismo tiempo el del oponente
    del Jugador["apariencia"]
    Jugador["apariencia"]={}#sirve para crear de nuevo la subseccion apariencia
    del oponente["apariencia"]
    boton_deseleccionar4.place_forget()
    boton_seleccionar4.place(x=1010,y=600)
    
boton_seleccionar4= tk.Button(main_window,image=imagen_seleccionar, command=seleccionar_avatar4)
boton_seleccionar4.pack(fill=BOTH, expand=True)
boton_deseleccionar4=tk.Button(main_window,image=imagen_deseleccionadores, command=deseleccionar_avatar4)
boton_deseleccionar4.pack(fill=BOTH, expand=True)

#seleccionador y deseleccionador avatar 5
def seleccionar_avatar5():
    #esta funcion se aplica al presionar el boton seleccionar, su funciones darle al jugador el avatar seleccionado y al oponente otro avatar
    #esta es una condicional que ayuda a que solo se pueda escoger una apariencia de entrenador
    restriccion_avatares.place_forget()
    if Jugador["apariencia"]:
        restriccion_avatares.place(x=300,y=60)
    else:
        Jugador["apariencia"]=apariencias["avatar5"]
        oponente["apariencia"]=apariencias["avatar1"]
        boton_seleccionar5.place_forget()
        boton_deseleccionar5.place(x=1300,y=600)
    
def deseleccionar_avatar5():
     #su funcion es quitar el avatar que selecciono el jugador y al mismo tiempo el del oponente
    del Jugador["apariencia"]
    Jugador["apariencia"]={}#sirve para crear de nuevo la subseccion apariencia
    del oponente["apariencia"]
    boton_deseleccionar5.place_forget()
    boton_seleccionar5.place(x=1300,y=600)
    
boton_seleccionar5= tk.Button(main_window,image=imagen_seleccionar, command=seleccionar_avatar5)
boton_seleccionar5.pack(fill=BOTH, expand=True)
boton_deseleccionar5=tk.Button(main_window,image=imagen_deseleccionadores, command=deseleccionar_avatar5)
boton_deseleccionar5.pack(fill=BOTH, expand=True)

#creacion label de falta de requisitos
mensaje_falta_requisitos= Label(main_window, text="SOLO PUEDES SELECCIONAR A UN ENTRENADOR, Y DEBES DE ESCRIBIR UN NOMBRE", font=("pokemon pixel font",30))

#establecimiento boton siguiente
def cargar_imagen3():
   pantalla_pokemons= Image.open(r"..\imagenes\seleccionador pokemons.png")
   pantalla_pokemons=pantalla_pokemons.resize((1532,787))
   return ImageTk.PhotoImage(pantalla_pokemons)

def seguir_pokemons():
    #se asegura de que si ya hubo un mensaje de error no se quede en la pantalla
    mensaje_falta_requisitos.place_forget()
    #es una condicional que se asegura de que el jugador haya escogido un avatar y escrito su nombre
    if Jugador["nombre"] and Jugador["apariencia"]:
        #elimina la imagen anterior
        img2= cargar_imagen2('pantalla_personaje')
        segunda = main_canvas.create_image(0,0,anchor="nw",image=img2)
        main_canvas.delete(segunda)
        
        #borra los botones anteriores
        boton_siguiente.place_forget()
        boton_seleccionar1.place_forget()
        boton_seleccionar2.place_forget()
        boton_seleccionar3.place_forget()
        boton_seleccionar4.place_forget()
        boton_seleccionar5.place_forget()
        boton_deseleccionar1.place_forget()
        boton_deseleccionar2.place_forget()
        boton_deseleccionar3.place_forget()
        boton_deseleccionar4.place_forget()
        boton_deseleccionar5.place_forget()
        caja_nombre.place_forget()
        #cargar imagen de seleccion de pokemons
        prie=cargar_imagen3()
        main_canvas.create_image(0,0,anchor="nw",image=prie)
        
        #posicionar botones de seleccion de pokemons y voton !VAMOS¡
        boton_pikachu.place(x=68,y=255)
        boton_charmander.place(x=355,y=255)
        boton_onix.place(x=655,y=255)
        boton_bulbasur.place(x=948,y=255)
        boton_ivy.place(x=1240,y=255)
        boton_gyarados.place(x=68,y=530)
        boton_squirtle.place(x=355,y=530)
        boton_dragonite.place(x=655,y=530)
        boton_mewto.place(x=948,y=530)
        boton_jiglypuff.place(x=1240,y=530)
        boton_vamos.place(x=1300,y=680)
    else:
        mensaje_falta_requisitos.place(x=300,y=60)
    
    
imagen_siguiente=PhotoImage(file=r"..\imagenes\boto seleccionar.png") 
boton_siguiente=tk.Button(main_window,text="Siguiente",command=seguir_pokemons, image=imagen_siguiente)
boton_siguiente.pack(fill=BOTH,expand=True)

#establecimiento de las funciones de los botones para seleccionar pokemons
#imagenes para los botones
imagen_seleccionadores=PhotoImage(file=r"..\imagenes\boton elegir pruebz.png")
imagen_eliminaciones=PhotoImage(file=r"..\imagenes\boton eliminar prueba.png")

#seleccionador y eliminador de pikachu
def elegir_pikachu():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["pikachu"]=Pokemons["pikachu"].copy()
    del oponente["pokemons"]["pikachu"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_pikachu.place_forget()
    boton_nopikachu.place(x=68,y=255)   
    
def no_pikachu():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["pikachu"]
    oponente["pokemons"]["pikachu"]=Pokemons["pikachu"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nopikachu.place_forget()
    boton_pikachu.place(x=68,y=255)

boton_pikachu =tk.Button(main_window, text="pikachu", command=elegir_pikachu,image=imagen_seleccionadores)
boton_pikachu.pack(fill=BOTH, expand=True)
boton_nopikachu=tk.Button(main_window, text="no pikachu",image=imagen_eliminaciones, command=no_pikachu)
boton_nopikachu.pack(fill=BOTH, expand=True)

#seleccionador y eliminador charmander
def elegir_charmander():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["charmander"]=Pokemons["charmander"].copy()
    del oponente["pokemons"]["charmander"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_charmander.place_forget()
    boton_nocharmander.place(x=360,y=255)   
    
def no_charmander():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["charmander"]
    oponente["pokemons"]["charmander"]=Pokemons["charmander"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nocharmander.place_forget()
    boton_charmander.place(x=360,y=255)

boton_charmander =tk.Button(main_window, command=elegir_charmander,image=imagen_seleccionadores)
boton_charmander.pack(fill=BOTH, expand=True)
boton_nocharmander=tk.Button(main_window,image=imagen_eliminaciones, command=no_charmander)
boton_nocharmander.pack(fill=BOTH, expand=True)
#seleccionador y eliminador onix
def elegir_onix():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["onix"]=Pokemons["onix"].copy()
    del oponente["pokemons"]["onix"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_onix.place_forget()
    boton_noonix.place(x=655,y=255)   
    
def no_onix():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["onix"]
    oponente["pokemons"]["onix"]=Pokemons["onix"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_noonix.place_forget()
    boton_onix.place(x=655,y=255)

boton_onix =tk.Button(main_window, command=elegir_onix,image=imagen_seleccionadores)
boton_onix.pack(fill=BOTH, expand=True)
boton_noonix=tk.Button(main_window,image=imagen_eliminaciones, command=no_onix)
boton_noonix.pack(fill=BOTH, expand=True)

#seleccionador y eliminador bulbasur
def elegir_bulbasur():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["bulbasur"]=Pokemons["bulbasur"].copy()
    del oponente["pokemons"]["bulbasur"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_bulbasur.place_forget()
    boton_nobulbasur.place(x=948,y=255)   
    
def no_bulbasur():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["bulbasur"]
    oponente["pokemons"]["bulbasur"]=Pokemons["bulbasur"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nobulbasur.place_forget()
    boton_bulbasur.place(x=948,y=255)

boton_bulbasur =tk.Button(main_window, command=elegir_bulbasur,image=imagen_seleccionadores)
boton_bulbasur.pack(fill=BOTH, expand=True)
boton_nobulbasur=tk.Button(main_window,image=imagen_eliminaciones, command=no_bulbasur)
boton_nobulbasur.pack(fill=BOTH, expand=True)

#seleccionador y eliminador ivy
def elegir_ivy():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["ivy"]=Pokemons["ivy"].copy()
    del oponente["pokemons"]["ivy"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_ivy.place_forget()
    boton_noivy.place(x=1240,y=255)   
    
def no_ivy():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["ivy"]
    oponente["pokemons"]["ivy"]=Pokemons["ivy"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_noivy.place_forget()
    boton_ivy.place(x=1240,y=255)

boton_ivy =tk.Button(main_window, command=elegir_ivy,image=imagen_seleccionadores)
boton_ivy.pack(fill=BOTH, expand=True)
boton_noivy=tk.Button(main_window,image=imagen_eliminaciones, command=no_ivy)
boton_noivy.pack(fill=BOTH, expand=True)

#seleccionador y eliminador gyarados
def elegir_gyarados():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["gyarados"]=Pokemons["gyarados"].copy()
    del oponente["pokemons"]["gyarados"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_gyarados.place_forget()
    boton_nogyarados.place(x=68,y=530)   
    
def no_gyarados():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["gyarados"]
    oponente["pokemons"]["gyarados"]=Pokemons["gyarados"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nogyarados.place_forget()
    boton_gyarados.place(x=68,y=530)

boton_gyarados =tk.Button(main_window, command=elegir_gyarados,image=imagen_seleccionadores)
boton_gyarados.pack(fill=BOTH, expand=True)
boton_nogyarados=tk.Button(main_window,image=imagen_eliminaciones, command=no_gyarados)
boton_nogyarados.pack(fill=BOTH, expand=True)

#seleccionador y eliminador squirtle
def elegir_squirtle():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["squirtle"]=Pokemons["squirtle"].copy()
    del oponente["pokemons"]["squirtle"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_squirtle.place_forget()
    boton_nosquirtle.place(x=355,y=530)   
    
def no_squirtle():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["squirtle"]
    oponente["pokemons"]["squirtle"]=Pokemons["squirtle"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nosquirtle.place_forget()
    boton_squirtle.place(x=355,y=530)

boton_squirtle =tk.Button(main_window, command=elegir_squirtle,image=imagen_seleccionadores)
boton_squirtle.pack(fill=BOTH, expand=True)
boton_nosquirtle=tk.Button(main_window,image=imagen_eliminaciones, command=no_squirtle)
boton_nosquirtle.pack(fill=BOTH, expand=True)

#seleccionador y eliminador dragonite
def elegir_dragonite():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["dragonite"]=Pokemons["dragonite"].copy()
    del oponente["pokemons"]["dragonite"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_dragonite.place_forget()
    boton_nodragonite.place(x=655,y=530)   
    
def no_dragonite():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["dragonite"]
    oponente["pokemons"]["dragonite"]=Pokemons["dragonite"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nodragonite.place_forget()
    boton_dragonite.place(x=655,y=530)

boton_dragonite =tk.Button(main_window, command=elegir_dragonite,image=imagen_seleccionadores)
boton_dragonite.pack(fill=BOTH, expand=True)
boton_nodragonite=tk.Button(main_window,image=imagen_eliminaciones, command=no_dragonite)
boton_nodragonite.pack(fill=BOTH, expand=True)

#seleccionador y eleminador mewto
def elegir_mewto():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["mewto"]=Pokemons["mewto"].copy()
    del oponente["pokemons"]["mewto"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_mewto.place_forget()
    boton_nomewto.place(x=948,y=530)   
    
def no_mewto():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["mewto"]
    oponente["pokemons"]["mewto"]=Pokemons["mewto"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nomewto.place_forget()
    boton_mewto.place(x=948,y=530)

boton_mewto =tk.Button(main_window, command=elegir_mewto,image=imagen_seleccionadores)
boton_mewto.pack(fill=BOTH, expand=True)
boton_nomewto=tk.Button(main_window,image=imagen_eliminaciones, command=no_mewto)
boton_nomewto.pack(fill=BOTH, expand=True)

#seleccionador y eliminador jiglypuff
def elegir_jiglypuff():
    #esta funcion permite agregar el pokemon al diccionario, se hace a manera de copia para siempre tener un valor orginal controlado y se borra del diccionario del oponente
    Jugador["pokemones"]["jiglypuff"]=Pokemons["jiglypuff"].copy()
    del oponente["pokemons"]["jiglypuff"]
    #pone en el mismo luga donde estaba un boton para eliminarlo del equipo pokemon si se desea
    boton_jiglypuff.place_forget()
    boton_nojiglypuff.place(x=1240,y=530)   
    
def no_jiglypuff():
    #esto revierte el boton de seleccionar a pikachu al quitar a pikachu del inventario de jugador y darselo al oponente quien ya no lo teniar
    del Jugador["pokemones"]["jiglypuff"]
    oponente["pokemons"]["jiglypuff"]=Pokemons["jiglypuff"].copy()
    #pone el boton elegir donde estaba el boton elegir
    boton_nojiglypuff.place_forget()
    boton_jiglypuff.place(x=1240,y=530)

boton_jiglypuff =tk.Button(main_window, command=elegir_jiglypuff,image=imagen_seleccionadores)
boton_jiglypuff.pack(fill=BOTH, expand=True)
boton_nojiglypuff=tk.Button(main_window,image=imagen_eliminaciones, command=no_jiglypuff)
boton_nojiglypuff.pack(fill=BOTH, expand=True)



#creacion del boton !VAMO! para inciar las batallas
def cargar_imagen4():
    pantalla_combate=Image.open(r"..\imagenes\imagen prebatalla.png")
    pantalla_combate=pantalla_combate.resize((1555,790))
    return ImageTk.PhotoImage(pantalla_combate)

def boton_vamos():
    #esta funcion crea una condional con la cual se asegura que el jugador solo pueda seleccionar los tres pokemones requeridos
    Label_falta_requisitos.place_forget()
    if len(Jugador["pokemones"])==3:
        #si la condicion se cumple primero va a eliminar la imagen anterior
        img4=cargar_imagen3()
        cuarta=main_canvas.create_image(0,0,anchor="nw",image=img4)
        main_canvas.delete(cuarta)
        
        #luego se pone la nueva imagen del fondo
        nueva_imagen=cargar_imagen4()
        main_canvas.create_image(0,0,anchor="nw",image=nueva_imagen)
        
        
        #se borran los botones de la seleccion de pokemones y a el mismo
        boton_pikachu.place_forget()
        boton_nopikachu.place_forget()
        boton_charmander.place_forget()
        boton_nocharmander.place_forget()
        boton_bulbasur.place_forget()
        boton_nobulbasur.place_forget()
        boton_dragonite.place_forget()
        boton_nodragonite.place_forget()
        boton_gyarados.place_forget()
        boton_nogyarados.place_forget()
        boton_ivy.place_forget()
        boton_noivy.place_forget()
        boton_jiglypuff.place_forget()
        boton_nojiglypuff.place_forget()
        boton_mewto.place_forget()
        boton_nomewto.place_forget()
        boton_squirtle.place_forget()
        boton_nosquirtle.place_forget()
        boton_onix.place_forget()
        boton_noonix.place_forget()
        boton_vamos.place_forget()
        
        #pone el avatar seleccionado y el avatar del rival en la pantalla de prebatalla
        imagen_avatar= Jugador["apariencia"]
        global label_avatar
        label_avatar=Label(main_window,image=imagen_avatar)
        label_avatar.place(x=128,y=175)
        global label_oponente
        imagen_oponente=oponente["apariencia"]
        label_oponente=Label(main_window, image=imagen_oponente)
        label_oponente.place(x=1150, y=175) 
        
        
        #seleccionador de pokemon para la batalla
        global menu_pokemons_disponibles
        global pokemon_peleador
        pokemon_peleador=StringVar()#esto ayuda a que se actualice constantemente
        pokemon_peleador.set("elige un pokemon para pelear")
        if len(Jugador["pokemones"])>0:
            menu_pokemons_disponibles= OptionMenu(main_window, pokemon_peleador, *Jugador["pokemones"].keys())
            menu_pokemons_disponibles.config(font=("Pokemon pixel font",30),width=30,bd=3,relief="solid")
            menu_pokemons_disponibles["menu"].config(font=("Pokemon pixel font",30),bd=3,relief="solid")
            
            menu_pokemons_disponibles.place(x=550,y=580)
        
        #coloca el boton para pelear
        boton_combate.place(x=620,y=300)
    else:
        Label_falta_requisitos.place(x=100,y=700)


imagen_vamos=PhotoImage(file=r"..\imagenes\Boton vamos (1).png")    
Label_falta_requisitos=Label(main_window, text="SOLAMENTE PUEDES AVANZAR SI TIENES 3 POKEMONES SELECCIONADOS", font=("pokemon pixel font",30))  
boton_vamos=tk.Button(main_window, command=boton_vamos, image=imagen_vamos)

#boton para combate
label_pokemon_necesario=Label(main_window,text="tienes que seleccionar un pokemon para pelear", font=("pokemon pixel font",30))

def cargar_imagen5():
    pantalla_batalla= Image.open(r"..\imagenes\campo batalla.png")
    pantalla_batalla=pantalla_batalla.resize((1555,790))
    return ImageTk.PhotoImage(pantalla_batalla)
def combatir():
    pokemon_seleccionado = pokemon_peleador.get()
    #condicional hecha para asegurarse de que el jugador seleccione un pokemon
    if pokemon_seleccionado in Jugador["pokemones"]:
        #mete a el pokemon seleccionado en la categoria de pokemon peleador
        Jugador["pokemon combatiente"] = {pokemon_seleccionado: Jugador["pokemones"][pokemon_seleccionado].copy()}
        
        #hace que el oponente seleccione un pokemon random
        pokemon_oponente= random.choice(list(oponente["pokemons"].keys()))
        oponente["pokemon combatiente"]={pokemon_oponente:oponente["pokemons"][pokemon_oponente].copy()}
        
        #elimina el label de error y los botones ademas del fondo
        img4=cargar_imagen4()
        quinta=main_canvas.create_image(0,0,anchor="nw", image=img4)
        del quinta
        label_pokemon_necesario.place_forget()
        label_avatar.place_forget()
        label_oponente.place_forget()
        boton_combate.place_forget()
        menu_pokemons_disponibles.place_forget()

        #pone el fondo de el escenario de batalla
        img5=cargar_imagen5()
        main_canvas.create_image(0,0,anchor="nw",image=img5)
        
        #poner las imagenes de los pokemones que combaten
        imagenen_pokemon_jugador= Jugador["pokemon combatiente"][pokemon_seleccionado]["imagenes"]["espalda"]
        main_canvas.create_image(300,395,image=imagenen_pokemon_jugador)
        
        imagen_pokemon_oponente=oponente["pokemon combatiente"][pokemon_oponente]["imagenes"]["frente"]
        main_canvas.create_image(1200,250,image=imagen_pokemon_oponente)
        
        #posisionamiento de las barras de vida
        vida_jugador()
        label_vida_jugador.place(x=950,y=395)
        vida_oponente()
        label_vida_oponente.place(x=500, y=60)
        
        #posisionamiento boton ataque
        boton_ataque.place(x=100,y=600)

    else:
        label_pokemon_necesario.place(x=0, y=0)
    
imagen_botonCombate=PhotoImage(file=r"..\imagenes\Boton batalla.png")
boton_combate= tk.Button(main_window, image=imagen_botonCombate, command=combatir)

#barras de vida
vida_pokemon_jugador=StringVar()
label_vida_jugador= Label(main_window, textvariable=vida_pokemon_jugador, font=("pokemon pixel font",50), bg="white", bd=3, relief="solid")

def vida_jugador():
    pokemon=list(Jugador["pokemon combatiente"].keys())[0]
    cualidades= Jugador["pokemon combatiente"][pokemon]
    vida_pokemon_jugador.set(f"{pokemon}          VIDA:{cualidades['cualidades']['vida']}" )


viida_pokemon_oponente=StringVar()
label_vida_oponente=Label(main_window, textvariable=viida_pokemon_oponente, font=("pokemon pixel font",50), bg="white",bd=3, relief="solid")

def vida_oponente():
    pokemon=list(oponente["pokemon combatiente"].keys())[0]
    cualidades=oponente["pokemon combatiente"][pokemon]
    viida_pokemon_oponente.set(f"{pokemon}          VIDA:{cualidades['cualidades']['vida']}")
    
    
#boton ataque
def atacar():
    # nombre y datos de los pokemons
    nombre_pokemon = list(Jugador["pokemon combatiente"].keys())[0]
    datos_pokemon = Jugador["pokemon combatiente"][nombre_pokemon]

    nombre_pokemon_oponente = list(oponente["pokemon combatiente"].keys())[0]
    datos_pokemon_oponete = oponente["pokemon combatiente"][nombre_pokemon_oponente]

    ataque_jugador = datos_pokemon["cualidades"]["ataque"]
    ataque_oponente = datos_pokemon_oponete["cualidades"]["ataque"]

    defensa_jugador = datos_pokemon["cualidades"]["defensa"]
    defensa_oponente = datos_pokemon_oponete["cualidades"]["defensa"]

    daño_jugador = ataque_jugador - defensa_oponente
    
    #es un restricción para asegurarse de que no hayan un "daño negativo"
    if daño_jugador < 1:
        daño_jugador = 1

    datos_pokemon_oponete["cualidades"]["vida"] -= daño_jugador
    
    #es una restriccion para que la vida pare en 0
    if datos_pokemon_oponete["cualidades"]["vida"] < 0:
        datos_pokemon_oponete["cualidades"]["vida"] = 0

    vida_oponente()

    #condicional por si el jugador gana
    if datos_pokemon_oponete["cualidades"]["vida"] <= 0:
        pokemon_ganado = datos_pokemon_oponete.copy()
        pokemon_ganado["cualidades"]["vida"] = Pokemons[nombre_pokemon_oponente]["cualidades"]["vida"]

        Jugador["pokemones"][nombre_pokemon_oponente] = pokemon_ganado
        del oponente["pokemons"][nombre_pokemon_oponente]

        Jugador["pokemon combatiente"] = {}
        oponente["pokemon combatiente"] = {}

        label_ganaste.place(x=600,y=400)
        boton_ataque.place_forget()
        boton_continuar.place(x=100,y=600)
        return

    daño_oponente = ataque_oponente - defensa_jugador

    if daño_oponente < 1:
        daño_oponente = 1

    datos_pokemon["cualidades"]["vida"] -= daño_oponente

    if datos_pokemon["cualidades"]["vida"] < 0:
        datos_pokemon["cualidades"]["vida"] = 0

    vida_jugador()
    
    #condicional por si el oponente gana
    if datos_pokemon["cualidades"]["vida"] <= 0:
        pokemon_perdido = datos_pokemon.copy()
        pokemon_perdido["cualidades"]["vida"] = Pokemons[nombre_pokemon]["cualidades"]["vida"]

        oponente["pokemons"][nombre_pokemon] = pokemon_perdido
        del Jugador["pokemones"][nombre_pokemon]

        Jugador["pokemon combatiente"] = {}
        oponente["pokemon combatiente"] = {}

        label_perdiste.place(x=600,y=400)
        boton_ataque.place_forget()
        boton_continuar.place(x=100,y=600)
    
        return
    
imagen_boton_ataque= PhotoImage(file=r"..\imagenes\Boton ataque.png")
boton_ataque= tk.Button(main_window, image=imagen_boton_ataque, command= atacar )   

label_ganaste= Label(main_window, text="GANASTE", font=("Pokemon pixel font",50))
label_perdiste= Label(main_window, text="PERDISTE", font=("Pokemon pixel font",50))

#establecimiento boton continuar
#luego se pone la nueva imagen del fondo
def continuar():
    global label_oponente
    global label_avatar
    global menu_pokemons_disponibles
    global pokemon_peleador
    img5= cargar_imagen5()
    quinta=main_canvas.create_image(0,0, anchor="nw", image=img5)
    main_canvas.delete(quinta)
    
    nueva_imagen=cargar_imagen4()
    main_canvas.create_image(0,0,anchor="nw",image=nueva_imagen)
    
    boton_continuar.place_forget()
    label_perdiste.place_forget()
    label_ganaste.place_forget()
    label_vida_jugador.place_forget()
    label_oponente.place_forget()
    label_vida_oponente.place_forget()
    
    #pone el avatar seleccionado y el avatar del rival en la pantalla de prebatalla
    imagen_avatar= Jugador["apariencia"]
   
    label_avatar=Label(main_window,image=imagen_avatar)
    label_avatar.place(x=128,y=175)
   
    imagen_oponente=oponente["apariencia"]
    label_oponente=Label(main_window, image=imagen_oponente)
    label_oponente.place(x=1150, y=175) 
        
        
    #seleccionador de pokemon para la batalla
   
    pokemon_peleador=StringVar()#esto ayuda a que se actualice constantemente
    pokemon_peleador.set("elige un pokemon para pelear")
    if len(Jugador["pokemones"])>0:
         menu_pokemons_disponibles= OptionMenu(main_window, pokemon_peleador, *Jugador["pokemones"].keys())
         menu_pokemons_disponibles.config(font=("Pokemon pixel font",30),width=30,bd=3,relief="solid")
         menu_pokemons_disponibles["menu"].config(font=("Pokemon pixel font",30),bd=3,relief="solid")
            
         menu_pokemons_disponibles.place(x=550,y=580)
        
    #coloca el boton para pelear
    boton_combate.place(x=620,y=300)
    
    
    
boton_continuar= tk.Button(main_window, image=imagen_siguiente,command=continuar)
        

    
main_window.mainloop()