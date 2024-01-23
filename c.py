import tkinter as tk
import tkinter.ttk as ttk
import random
#import matplotlib.pyplot as plt
#from matplotlib_venn import venn2
from matplotlib import pyplot as plt
from matplotlib_venn import venn2



class Subconjunto: #clase que crea objeto basado en los subconjuntos
    letra = str()
    def _init_(self, letra= str(), lista=None):
        if lista is None:
            lista = []
        self.conjunto = set(lista) #actualiza
        self.letra = letra
        
    @property
    def Letra(self):
        return self.letra

    @Letra.setter
    def Letra(self, letra):
        self.letra = letra

class ventana(ttk.Frame): #clase que contiene informacion de la ventana 
    def _init_(self, master):
        super()._init_(master)
        self.master =master
        self.pack()

#variables relacionadas a la clase subconjuntos
texto_operacion = str() #texto generado para actualizar la operacion
conjunto_list =[] 


def mostrar_enVentana(letra,le):
    global texto_operacion
    global conjunto_list
    
    objecto = Subconjunto(letra,le.split(","))
    conjunto_list.append(objecto)
    texto_operacion += letra + " "
    #ubica y actualiza el texto que genero canvas
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_operacion}")
    contenido = canvas.itemcget(texto_conjuntos, 'text') #BORRAR
    print(contenido)#BORRAR
    #print(letra, le) BORRAR



def mostrar_operaciones(letra): #muestra los iconos de las operaciones
    global texto_operacion
    
    texto_operacion += letra + " "
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_operacion}")

def quitar_elemento():
    global texto_operacion
    
    operadores = ["A","B","C","D","u","∩","'","-","(",")"]
    conjuntos = ["A","B","C","D"]
    
    for operador in reversed(texto_operacion):
        if operador in operadores:
            texto_operacion = texto_operacion.replace(operador, "", 1)
            try:
                texto_operacion = texto_operacion.replace(" ", "", 1)
            except:
                pass
            if operador in conjuntos:
                conjunto_list.pop
            break
    
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_operacion}")

def mostrar_resultados(texto, lista_conjuntos):
    #global nuevo_Subconjunto
    operadores = {"u", "∩", "'", "-"}

    conjunto_actual = set()
    operacion_actual = 'u'  # Operación predeterminada (unión)
    conjunto_temporal = []
    valor_bandera = True #BORRAR
    
    contador = 0
    
    print(len(lista_conjuntos))

    for char in texto:
        if char.isalpha() and char not in operadores:  # Si es una letra, la consideramos como un conjunto
            conjunto_temporal.append(lista_conjuntos[contador].conjunto)
            contador += 1
            print(contador)
        elif char in operadores:  # Si es un operador, cambiamos la operación actual
            operacion_actual = char
        elif char == '(':  # Si es un paréntesis de apertura, reiniciamos el conjunto temporal
            conjunto_temporal = []
        elif char == ')':  # Si es un paréntesis de cierre, realizamos la operación y actualizamos el conjunto actual
            conjunto_actual = realizar_operacion(conjunto_temporal, operacion_actual)
            conjunto_temporal.append(list(conjunto_actual))
            print("l")

    resultado_ordenado = sorted(conjunto_actual)
    canvas.itemconfig(tagOrId=texto_Respuesta, text=f"{resultado_ordenado}")
    
    print(f"Resultado final: {resultado_ordenado}") #BORRAR
    
    contador = 0
    
    
def realizar_operacion(lista_de_conjuntos, operacion_actual):
    global lista_universal 
    
    lista_universal = universal.get().split(",") #Accede y separa el conjunto universal
    conjunto_retornar = []
    
    if(operacion_actual == "u"): #union
        conjunto_retornar = set(lista_de_conjuntos[-1]) | set(list(lista_de_conjuntos[-2]))
        return conjunto_retornar
    
    elif(operacion_actual == "∩"):#interseccion
        conjunto_retornar = set(lista_de_conjuntos[-1]) & set(lista_de_conjuntos[-2])
        return conjunto_retornar
    
    elif(operacion_actual == "'"):#complemento
        conjunto_retornar = set(lista_universal) - set(lista_de_conjuntos[-1])
        return conjunto_retornar
    
    elif(operacion_actual == "-"): #difernecia
        conjunto_retornar = set(lista_de_conjuntos[-1]) - set(lista_de_conjuntos[-2])
        return conjunto_retornar

def limpiar(): #ACOMODAR
    canvas.itemconfig(tagOrId=texto_conjuntos, text="")
    canvas.itemconfig(tagOrId=texto_Respuesta,text="")


window = tk.Tk()
window.geometry("1200x645")
window.configure(bg = "white")    
window.resizable(False, False)
#f= tk.Frame(window,bg="gray").place(width=1000,height=605,x=100,y=20) #guia

canvas =tk.Canvas(window,background="#F4F3FF",
    width = 1000,height=605,
    bd = 0,
    highlightthickness = 0)
canvas.place(x=100,y=20) #revisar si existe un posible error
#texto e imagen de la operacin y respuesta
imgOperacion = tk.PhotoImage(
    file="operacion.png")
image_1 = canvas.create_image(
    450.0,
    291.5,
    image=imgOperacion
)
texto_conjuntos = canvas.create_text(
    260.0,284.0,
    anchor="nw",
    text="Inserte la operacion a realizar",
    fill="#413E64",
    font=("Arial", 10))


imgRespuesta = tk.PhotoImage(
    file="operacion.png")
image_2 = canvas.create_image(
    640.5,
    410,
    image=imgRespuesta
)
texto_Respuesta = canvas.create_text(
    450.0,401.5,
    anchor="nw",
    text="Conjunto Generado",
    fill="#413E64",
    font=("Arial", 10))
 #aqui va lo de los botones

#conjunto universal
ttk.Label(window,text="U=",background="#F4F3FF",foreground="#6557FF").place(x=380,y=65)
universal= tk.StringVar()
entry_universal = ttk.Entry(window,textvariable=universal).place(x=400,y=65,width=400)#y60
#subconjuntos Entry
ttk.Label(window,text="A=",background="#F4F3FF",foreground="#6557FF").place(x=250,y=115)
a1 = tk.StringVar()
a_entry = ttk.Entry(window,textvariable=a1,).place(x=270,y=115,width=200)
boton_a =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("A", a1.get())).place(x=475,y=115)

ttk.Label(window,text="B=",background="#F4F3FF",foreground="#6557FF").place(x=250,y=155)
b1 =tk.StringVar()
b_entry = ttk.Entry(window,textvariable=b1).place(x=270,y=155,width=200)
boton_b =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("B", b1.get())).place(x=475,y=155)

ttk.Label(window,text="C=",foreground="#6557FF",background="#F4F3FF").place(x=640,y=115)
c1 =tk.StringVar()
c_entry = ttk.Entry(window,textvariable=c1).place(x=660,y=115,width=200)
boton_c =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("C", c1.get())).place(x=865,y=115)

ttk.Label(window,text="D=",background="#F4F3FF",foreground="#6557FF",font=("Arial", 10)).place(x=640,y=155)
d1 =tk.StringVar()
d_entry = ttk.Entry(window,textvariable=d1).place(x=660,y=155,width=200)
boton_d =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("D", d1.get())).place(x=865,y=155)

#botones random y teclado
boton_aleatorio =  ttk.Button(window,text="Generar Datos Aleatorios").place(width=150,x=470,y=30)
boton_teclado =  ttk.Button(window,text="Ingresar Datos").place(width=90,x=620,y=30)
#botones de operaciones
boton_Interseccion= ttk.Button(window, text="Interseccion (n)",command=lambda: mostrar_operaciones("∩")
                               ).place(width=100,x=260,y=240)
boton_Union= ttk.Button(window, text="Union (u)",command=lambda: mostrar_operaciones("u")
                        ).place(width=70,x=405,y=240)
boton_Diferencia= ttk.Button(window, text="Diferencia (-)",command=lambda: mostrar_operaciones("-")
                             ).place(width=100,x=520,y=240)
boton_Complemento= ttk.Button(window, text="Complemento (')",command=lambda: mostrar_operaciones("'")
                              ).place(width=100,x=665,y=240)
boton_Todo= ttk.Button(window, text="Todas las Operaciones").place(width=130,x=810,y=240)

boton_1 =ttk.Button(window, text="(",command=lambda: mostrar_operaciones("(")
                   ).place(width=20,x=300,y=300)
boton_2 =ttk.Button(window, text=")",command=lambda: mostrar_operaciones(")")
                    ).place(width=20,x=325,y=300)
#botones que calculan o borran elmentos del subconjunto
boton_calcular =ttk.Button(window, text="Calclular",
                           command=lambda: mostrar_resultados(canvas.itemcget(texto_conjuntos, 'text'), conjunto_list)
                           ).place(width=65,x=830,y=300)
boton_borrar =ttk.Button(window, text="Borrar",command=lambda: quitar_elemento()
                           ).place(width=65,x=760,y=300)
#botones que limpiam operacion o guardan nuevo subconjunto
boton_nuevaOperacion = ttk.Button(window,text="Nueva Operacion",command=limpiar).place(width=115,x=826,y=450)
#boton_nuevoSubconjunto = ttk.Button(window,text="Guardar nuevo subconjunto", command=adjuntar).place(width=160,x=660,y=450)
#tk.Frame(window,background="white").place(width=230,height=230,x=270,y=380)

w =ventana(window)
w.mainloop()