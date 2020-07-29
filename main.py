from tkinter import ttk
from tkinter import *
#import sqlite3


#Definiendo y creando la clase de productos/servicios a ofrecer
class productos:
	#Programando el inicio y display de la aplicación
	def __init__(self,window):
		self.wind=window
		self.wind.title('3C Service Browser')

		#Creando un contenedor
		frame=LabelFrame(self.wind,text='Inserte el nombre del producto que desea añadir')
		frame.grid(row=0,column=0,columnspan=3,pady=20)

		#Creo que de momento no se va a utilizar esto
		# Label(frame,text='Nombre del producto').grid(row=1,column=0)
		# self.name=Entry(frame)
		# self.name.grid(row=1,column=1)
		# self.name.focus()

		#Introducción de las id de los servicios
		Label(frame,text="Id: ").grid(row=1,column=0)
		self.price=Entry(frame)
		self.price.grid(row=1,column=1)

		#Boton de añadir servicio
		ttk.Button(frame,text='Anadir producto').grid(row=2,columnspan=2,sticky= W + E)

		#Creando la tabla de servicios con su respectivo id
		self.tree=ttk.Treeview(height=10,column=2)
		self.tree.grid(row=4,column=0,columnspan=2)

#Iniciando la aplicación
if __name__=='__main__':
	window= Tk()
	application=productos(window)
	window.mainloop()