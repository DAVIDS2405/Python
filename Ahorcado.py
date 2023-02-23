from tkinter import * 
from tkinter.messagebox import*
import pygame
import sys
from random import randint
from PIL import Image

#Archivo con las palabras a ocupar
#Funciones


Vidas = 7
letrasAcertadas=0

def colocarletras():
    x=50
    y=150
    contador= 0
    Label(canvas, text="Letras sin usar",font=("Verndana", 20)).place(x=50, y=100)
    for i in range(26):
        contador+=1
        letrasLabel[i].place(x=x,y=y)
        x+=30
        if contador==5:
            y+=35
            contador=0
            x=50
LetrasUsada= []
def probarletraFuncion():
    global Vidas
    global letrasAcertadas
    LetrasUsada.append(LetraObtenida.get())
    print (LetrasUsada)
    letrasLabel[ord(LetraObtenida.get())-97].config(text="")

    if LetraObtenida.get() in palabra:

        if palabra.count(LetraObtenida.get())>1:
            letrasAcertadas += palabra.count(LetraObtenida.get())
            for i in range(len(palabra)):
                if palabra[i]==LetraObtenida.get():
                    guiones[i].config(text=""+LetraObtenida.get())
        else:
            letrasAcertadas += 1
            guiones[palabra.index(LetraObtenida.get())].config(text=""+LetraObtenida.get()) 

        if letrasAcertadas == len(palabra):
            showwarning(title="Victoria",message="Acabas de ganar")
    else:
        Vidas-=1
        canvas.itemconfig(imagen_id,image=imagenes[Vidas]) 
        if Vidas==0:
            showwarning(title="Game over",message="Sin vidas")





#Inicio
raiz = Tk()
#Abrir el archivo para lectura de las palabras y que el jugador la busque en pantalla
archivo = open("Palabras.txt","r")
conjuntopalabras =list(archivo.read().split("\n"))
palabra=conjuntopalabras[randint(0,len(conjuntopalabras)-1)].lower()
LetraObtenida = StringVar()

#Ventana
raiz.config (width=1200,height=550)
raiz.title ("Ahorcado")
raiz.geometry ("1200x550")




#Inicializar del juego quien tendra todas las caracteristas del ahorcado

#Musica

pygame.mixer.init()
pygame.mixer.music.load('Sonido/megaman1.wav')
pygame.mixer.music.play(loops=-1)



#imagenes muneco 
canvas = Canvas(raiz,width=1300,height=650)
canvas.pack(expand=True,fill="both")
imagenes =[
    PhotoImage(file="images/a-8.png"),
    PhotoImage(file="images/a-7.png"),
    PhotoImage(file="images/a-6.png"),
    PhotoImage(file="images/a-5.png"),
    PhotoImage(file="images/a-4.png"),
    PhotoImage(file="images/a-3.png"),
    PhotoImage(file="images/a-2.png"),
    PhotoImage(file="images/a-1.png"),
    PhotoImage(file="images/bg-1.png")
]
#fondo juego
canvas.create_image(650,325, image=imagenes[8])
imagen_id = canvas.create_image(950, 300, image=imagenes[7])










#TEXTO PARA PERDIR AL USUARIO LA LETRAS A PONER 
Label(canvas, text="Introduce una letra", font=("Verndana", 20)
      ).grid(row=0, column=0, padx=10, pady=9)
letra = Entry(canvas, width=1, font=("Verdana", 24), textvariable=LetraObtenida
              ).grid(row=0, column=1, padx=10, pady=10)

probarletra = Button(canvas, text="Pulsar", bg="red", command=probarletraFuncion
              ).grid(row=2,column=0,pady=0)

letrasLabel=[Label(canvas,text=chr(j+97),font=("Verdana", 20))for j in range(26)]
colocarletras()
guiones = [Label(canvas, text="_", font=("Verdana", 30))for _ in palabra]
incialX=200
for i in range(len(palabra)):
    guiones[i].place(x=incialX,y=400)
    incialX+=50



raiz.mainloop ()           


