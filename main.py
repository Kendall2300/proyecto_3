from tkinter import ttk
from tkinter import *
import sqlite3
import tkinter as tk

class MainStream(tk.Tk):

    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (second_menu, productos,recibos):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(second_menu)

    def show_frame(self,cont):

        frame=self.frames[cont]
        frame.tkraise()


class second_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #label=tk.Label(self, text="Start Page")
        #label.pack(pady=10,padx=10)


        button_menu_services=tk.Button(self,text=
        	"Contratar servicios",command=lambda:controller.show_frame(productos))

        button_menu_services.pack(pady=10,padx=10)

        button_menu_recibos=tk.Button(self,text="Facturas Generadas",command=lambda:controller.show_frame(recibos))

        button_menu_recibos.pack(pady=10,padx=10)

#Definiendo y creando la clase de productos/servicios a ofrecer
class productos(tk.Frame):
	db_name = "database.db"
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		#label = tk.Label(self, text="Start Page")
		#label.pack(pady=10,padx=10)
		button_second_menu = tk.Button(self, text="Volver a la pagina principal", command=lambda: controller.show_frame(second_menu))
		button_second_menu.pack(pady=10,padx=10)

		#Creando un los contendeores
		big_box=LabelFrame(self)
		big_box.pack(pady=15,padx=15)
		lef_box=LabelFrame(self,big_box,text="Inserte el nombre de los servicios\nque desea añadir",labelanchor=N)
		lef_box.pack(side=LEFT,pady=15,padx=15)
		right_box=LabelFrame(self,big_box,text="Estos son los servicios que\nha añadido a su orden",labelanchor=N)
		right_box.pack(side=RIGHT,pady=15,padx=15)

		#Introduccion de las id de los servicios
		Label(lef_box,text="Servicio:").grid(row=1,column=0)
		self.service_entry=Entry(lef_box)
		self.service_entry.grid(row=1,column=1)
		self.service_entry.focus()

		#Introduccion del precio por servicio
		Label(lef_box,text="Precio:").grid(row=2,column=0)
		self.price_entry=Entry(lef_box)
		self.price_entry.grid(row=2,column=1)

		#Botones de añadir servicios a la lista de compra
		self.button_add_services=ttk.Button(lef_box,text="Añadir servicio",command=self.insertar_dato)
		self.button_add_services.grid(row=3,columnspan=4,sticky=W+E,pady=10,padx=10)

		#Boton eliminar servicios?

		#Creando la tabla de servicios con su respectivo id
		self.services_tree=ttk.Treeview(lef_box,height=10,columns=2)
		self.services_tree.grid(row=4,column=0,columnspan=3,pady=20,padx=20)
		self.services_tree.heading("#0",text="Nombre",anchor=CENTER)
		self.services_tree.heading("#1",text="Precio en $", anchor=CENTER)

		#LABEL DE LADO DERECHO
		Label(right_box)
		self.print_button=ttk.Button(right_box,text="Imprimir")
		self.print_button.grid(row=1,columnspan=3,sticky=W+E)

		#Tabla de servicios contratados
		self.contratados_tree=ttk.Treeview(right_box,heigh=10,columns=2)
		self.contratados_tree.grid(row=2,column=0,columnspan=3,pady=20,padx=20)
		self.contratados_tree.heading("#0",text="Nombre",anchor=CENTER)
		self.contratados_tree.heading("#1",text="Precio en $",anchor=CENTER)

		#Colocando los productos en la tabla de servicios
		self.get_products()
	#Llamando a la base de datos
	def run_query(self,query,parameters=()):
		with sqlite3.connect(self.db_name)as conn:
			cursor=conn.cursor()
			result=cursor.execute(query,parameters)
			conn.commit()
		return result

	#Obteniendo los productos de la base de datos
	def get_products(self):
		#Limpiando la base de datos
		records=self.services_tree.get_children()
		for elements in records:
			self.services_tree.delete(elements)
		query="SELECT * FROM Product ORDER BY nombre DESC"
		db_rows=self.run_query(query)
		#Recorriendo la lista de productos para insertarlos en la tablla
		for row in db_rows:
			self.services_tree.insert("",0,text=row[1],values=row[2])

	#Insertando los datos en la tabla de servicios contratados
	def insertar_dato(self):
		texto=[self.service_entry.get()]
		costo=[self.price_entry.get()]
		self.contratados_tree.insert("",0,text=texto[0],values=costo[0])

class recibos(tk.Frame):
	db_name = "database.db"
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		button_second_menu=tk.Button(self,text="Menu principal",command=lambda:controller.show_frame(second_menu))
		button_second_menu.pack(pady=10,padx=10)

		#Creando el contenedor de la lista de pdf generados
		main_box=LabelFrame(self,text="Estas son todas las facturas generadas",labelanchor=N)
		main_box.pack(pady=15,padx=15)

		#Creando la tabla de facturas generadas
		self.facturas_tree=ttk.Treeview(main_box,height=10,columns=2)
		self.facturas_tree.grid(row=0,column=0,pady=20,padx=20)
		self.facturas_tree.heading("#0",text="Id de la factura",anchor=CENTER)
		self.facturas_tree.heading("#1",text="Nombre de la factura",anchor=CENTER)

		#Colocando las facturas en la tabla de servicios
		self.get_recives()

	#Llamando a la base de datos
	def run_query_recives(self,query,parameters=()):
		with sqlite3.connect(self.db_name) as conn:
			cursor=conn.cursor()
			result=cursor.execute(query,parameters)
			conn.commit()
		return result

	#Obteniendo las facturas de la base de datos
	def get_recives(self):
		#Limpiando la base de datos
		records=self.facturas_tree.get_children()
		for elements in records:
			self.facturas_tree.delete(elements)
		query="SELECT * FROM Facturas ORDER BY nombre DESC"
		db_rows=self.run_query_recives(query)
		#Recorriendo la lista de productos para insertarlos en la tabla
		for row in db_rows:
			self.facturas_tree.insert("",0,values=row[1],text=row[0])


#Iniciando la aplicación
app= MainStream()
app.mainloop()
