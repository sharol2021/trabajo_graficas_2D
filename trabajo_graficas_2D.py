from tkinter import *

#-------------------------
# variables globales
#-------------------------
BASE = 460
ALTURA = 450

#-------------------------
# ventana principal
#-------------------------
ventana_principal = Tk()
ventana_principal.title("Graficas  2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#-------------------------
# frame de graficacion 
#-------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="blue", width=480, height=470)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

# dibujar rectangulo
rect_1 = c.create_rectangle(BASE/2-155,ALTURA/2-75,BASE/2+155,ALTURA/2+75,fill="gray",outline="blue")
rect_2 = c.create_rectangle(BASE/2-155,ALTURA/2-75,BASE/2+155,ALTURA/2-25,fill="gray",outline="blue")

# dibujar un circulo
circ_1 = c.create_oval(BASE/2-130,ALTURA/2+110,BASE/2-60,ALTURA/2+30, fill="blue")
circ_2 = c.create_oval(BASE/2-30,ALTURA/2+110,BASE/2+40,ALTURA/2+30, fill="blue")
circ_3 = c.create_oval(BASE/2+70,ALTURA/2+110,BASE/2+140,ALTURA/2+30, fill="blue")

# desplegar ventana
ventana_principal.mainloop()

