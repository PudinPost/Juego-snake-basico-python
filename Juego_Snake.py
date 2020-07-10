import turtle
import time
import random

posponer = 0.1
#Marcador
puntaje = 0
mejor_puntaje = 0
#Personalización
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("white")
wn.setup (width = 600, height = 600)
wn.tracer (0)


#Cabeza de la serpiente
cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction= "stop"

#Comida
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente
segmentos = []

#Indicar Puntaje
texto= turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntaje: 0     Mejor Puntaje: 0", align="center", font=("Calibri",24, "normal"))





#Movimientos
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
    
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    elif cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    elif cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    
    elif cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# TECLADO
wn.listen()
wn.onkey(arriba, "Up")
wn.onkey(abajo, "Down")
wn.onkey(izquierda, "Left")
wn.onkey(derecha, "Right")

while True:
    wn.update()


    if cabeza.distance(comida) < 20:
        y = random.randint(-280,280)
        x = random.randint(-280,280)
        comida.goto (x,y)

        nuevo_segmento= turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        #Hacer crecer el puntaje
        puntaje+=10

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje

            texto.clear()
        texto.write("Puntaje: {}     Mejor Puntaje: {}".format(puntaje, mejor_puntaje),
            align="center", font=("Calibri",24, "normal"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor ()
        y = cabeza.ycor ()
        segmentos[0].goto(x,y)


    mov()
    #Game over cuerpo de la serpiente
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"

            for segmento in segmentos:
                segmento.goto(5000,5000)
            
            segmentos.clear()

            #Resetear marcador
            puntaje = 0
            texto.clear()
            texto.write("Puntaje: {}        Mejor Puntaje: {}".format(puntaje, mejor_puntaje),
                 align="center", font=("Calibri", 24 , "normal"))

    time.sleep(posponer)

turtle.mainloop()