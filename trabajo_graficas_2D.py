from tkinter import *

#-------------------------
# variables globales
#-------------------------
BASE = 654
ALTURA = 450

#-------------------------
# ventana principal
#-------------------------
ventana_principal = Tk()
ventana_principal.title("Graficas  2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("700x500")
ventana_principal.config(bg="white")

#-------------------------
# frame de graficacion 
#-------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="blue", width=678, height=470)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

# dibujar una linea recta
#linea_1 = c.create_line(BASE/2, ALTURA/2, BASE,0, fill="red", width=2)
#linea_2 = c.create_line(BASE, ALTURA, BASE/2, ALTURA/2, fill="yellow", width=2)
#linea_3 = c.create_line(0,ALTURA,BASE/2,ALTURA/2, fill="blue", width=2)
#linea_4 = c.create_line(0,0,BASE/2,ALTURA/2, fill="green", width=2)


# dibujar rectangulo
circ_4 = c.create_oval(BASE/2-240,ALTURA/2-50,BASE/2-160,ALTURA/2+50, fill="red")
rect_1 = c.create_rectangle(BASE/2-155,ALTURA/2-75,BASE/2+155,ALTURA/2+75,fill="maroon4",outline="blue")
rect_2 = c.create_rectangle(BASE/2-170,ALTURA/2-60,BASE/2-155,ALTURA/2+60,fill="maroon4", outline="blue")
rect_3 = c.create_rectangle(BASE/2-200,ALTURA/2-75,BASE/2-170,ALTURA/2+75,fill="maroon4", outline="blue")

# dibujar un circulo
circ_1 = c.create_oval(BASE/2-130,ALTURA/2+110,BASE/2-60,ALTURA/2+30, fill="red")
circ_2 = c.create_oval(BASE/2-30,ALTURA/2+110,BASE/2+40,ALTURA/2+30, fill="red")
circ_3 = c.create_oval(BASE/2+70,ALTURA/2+110,BASE/2+140,ALTURA/2+30, fill="red")


# desplegar ventana
ventana_principal.mainloop()

