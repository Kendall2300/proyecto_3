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
		frame=LabelFrame(self.wind,text='Inserte el nombre del servicio\nque desea añadir')
		frame.grid(row=0,column=0,columnspan=3,pady=20)

		#Creo que de momento no se va a utilizar esto
		# Label(frame,text='Nombre del producto').grid(row=1,column=0)
		# self.name=Entry(frame)
		# self.name.grid(row=1,column=1)
		# self.name.focus()

		#Introducción de las id de los servicios
		Label(frame,text="Servicio: ").grid(row=1,column=0)
		self.service=Entry(frame)
		self.service.grid(row=1,column=1)
		self.service.focus()

		#Boton de añadir servicio
		self.bservicios = ttk.Button(frame,text='Anadir servicio')#,command=self.add_service)
		self.bservicios.grid(row=2,columnspan=3,sticky=W+E)

		#Creando la tabla de servicios con su respectivo id
		self.tree=ttk.Treeview(height=10,columns=2)
		self.tree.grid(row=1,column=0,columnspan=2,pady=5,padx=5)
		self.tree.heading("#0", text="Nombre", anchor=CENTER)
		self.tree.heading("#1", text="Precio", anchor=CENTER)

		#
		frame2=LabelFrame(self.wind,text="Estos son los servicios agregados\n a su pedido")
		frame2.grid(row=0,column=3,columnspan=3, pady=20)
		Label(frame2,text="").grid(row=1,column=3)

		#Creando la tabla de servicios contratados
		self.treec=ttk.Treeview(heigh=10,columns=2)
		self.treec.grid(row=1,column=3,columnspan=2,pady=5,padx=5)
		self.treec.heading("#0", text="Nombre", anchor=CENTER)
		self.treec.heading("#1", text="Precio", anchor=CENTER)


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
			self.tree.insert("", 0, text= row[1],values=row[2])

	# def validation(self):
	# 	if len(self.service.get())!=0:
	# 		return True
	# 	else:
	# 		return False

	# def add_service(self):
	# 	if self.validation()==True:
	# 		query = "INSERT INTO product VALUES(NULL,?)"
	# 		parameters=(self.service.get())
	# 	else:
	# 		print ("Ponga el nombre del servicio")
	# 	self.add_service()





#Iniciando la aplicación
if __name__=='__main__':
	window= Tk()
	application=productos(window)
	window.mainloop()
