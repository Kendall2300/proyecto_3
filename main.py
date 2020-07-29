from tkinter import ttk
from tkinter import *
import sqlite3


#Definiendo y creando la clase de productos/servicios a ofrecer
class productos:

	#Almacenando la base de datos dentro de la aplicación
	db_name = "database.db"

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
		self.tree.heading("#0", text="Nombre", anchor=CENTER)
		self.tree.heading("#1", text="Precio", anchor=CENTER)

		#Colocando los productos en la tabla de servicios
		self.get_product()

	#Llamando a la base de datos
	def run_query(self,query,parameters = ()):
		with sqlite3.connect(self.db_name) as conn:
			cursor = conn.cursor()
			result = cursor.execute(query, parameters)
			conn.commit()
		return result 
	#Obteniendo los productos de la base de datos
	def get_product(self):
		#Limpiando los datos que están en la tabla
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		query = "SELECT * FROM Product ORDER BY Nombre DESC"
		db_rows = self.run_query(query)
		#Recorriendo la lista de productos para insertarlos en la tabla
		for row in db_rows:
			self.tree.insert("", 0, text= row[1], values= row[2])





#Iniciando la aplicación
if __name__=='__main__':
	window= Tk()
	application=productos(window)
	window.mainloop()
