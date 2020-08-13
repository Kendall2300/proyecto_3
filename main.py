from tkinter import ttk
import os
import cv2
from tkinter import *
import face_recognition
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

        for F in (second_menu, productos,recibos,añadir_productos,starting_screen,loggin):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(starting_screen)

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

        button_menu_productos=tk.Button(self,text="Anadir Productos",command=lambda:controller.show_frame(añadir_productos))
        button_menu_productos.pack(pady=10,padx=10)


#Definiendo y creando la clase de productos/servicios a ofrecer
class productos(tk.Frame):
	db_name = "database.db"
	right_box = None
	def __init__(self, parent, controller):
		global right_box

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
		self.contratados_tree=ttk.Treeview(right_box,heigh=10,columns=("#1"))
		self.contratados_tree.grid(row=2,column=0,columnspan=3,pady=20,padx=20)
		self.contratados_tree.heading("#0",text="Nombre",anchor=CENTER)
		self.contratados_tree.heading("#1",text="Precio en $",anchor=CENTER)

		Label(right_box,text="Subtotal:  " + "0 $").grid(row=3,column=1)
		Label(right_box,text="Descuento: ").grid(row=4,column=1)
		Label(right_box,text="Tax: %").grid(row=5,column=1)
		Label(right_box,text="Total: 0 $").grid(row=6,column=1)
		
		#Colocando los productos en la tabla de servicios
		self.get_products()

	#------------
	def subtotal(self):
		subtotal=self.price_entry.get()
		return subtotal
		print(subtotal)

	#Print
	def print(self):
		URL_WSAA = "login url"
		URL_WSFEv1 = "service screen url"
		CUIT = 20267565393
		CERT = "../reingart.crt"
		PRIVATEKEY = "../reingart.key"
		CACHE = "../cache"
		CONF_PDF = dict(LOGO="../screen/logo.png",EMPRESA="Ejemplo de empresa",MEMBRETE1="Ejemplo de direccion",MEMBRETE2="Capital Federal",CUIT="CUIT 30-00000000-0",IIBB="exento",IVA="IVA Responsable Inscripto",INICIO="Inicio de Actividad: fecha")


		def facturar(registros):
			#login

			if face_login ==(false):
				"return to login"
			else:
				"build bill"
				fepdf = FEPDF()
				fepdf.CargarFormato("sample.pdf")
				fepdf.FmtCantidad = "0.2"
				fepdf.FmtPrecio = "0.2"
				fepdf.CUIT = CUIT
				for k, v in CONF_PDF.items():
					fepdf.AgregarDato(k, v)
			"registri data for bill + pdf generation"
			for reg in 'registros':
				hoy = datetime.date.today().strftime("%Y%m%d")
				cbte = Comprobante(tipo_cbte=6, punto_vta=4000, fecha_cbte=hoy,cbte_nro=reg.get("nro"),tipo_doc=96, nro_doc=reg["dni"],nombre_cliente=reg["nombre"],domicilio_cliente=reg["domicilio"],fecha_serv_desde=reg.get("periodo_desde"),fecha_serv_hasta=reg.get("periodo_hasta"),fecha_venc_pago=reg.get("venc_pago", hoy))
				cbte.agregar_item(ds=reg["descripcion"],qty=reg.get("cantidad", 1),precio=reg.get("precio", 0),tasa_iva=reg.get("tasa_iva", 21.))
				print("Factura autorizada")
				ok = cbte.generar_pdf(fepdf, "samplefinish.pdf".format(nro))
				print("PDF generado", ok)


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

		subtotal = self.subtotal()
		print("SUBTOTAL ", subtotal)

		Label(right_box,text="Subtotal:  " + str(subtotal) + "$").grid(row=3,column=1)

class recibos(tk.Frame):
	db_name = "database.db"
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		button_second_menu=tk.Button(self,text="Menu principal",command=lambda:controller.show_frame(second_menu))
		button_second_menu.pack(pady=10,padx=10)

		#Creando el contenedor de la lista de pdf generados
		main_box=LabelFrame(self,text="Estas son todas las facturas generadas",labelanchor=N)
		main_box.pack(pady=15,padx=15)

		#Creando en boton delete
		ttk.Button(main_box,text = 'DELETE', command = self.delete_product).grid(row = 0, column = 0, sticky = W + E)


		#Creando la tabla de facturas generadas
		self.facturas_tree=ttk.Treeview(main_box,height=18,columns=("#1","#2","#3","#4"))
		self.facturas_tree.grid(row=1,column=0,pady=20,padx=20)
		self.facturas_tree.heading("#0",text="Nombre del Cliente",anchor=CENTER)
		self.facturas_tree.heading("#1",text="Id de la factura",anchor=CENTER)
		self.facturas_tree.heading("#2",text="Fecha de la factura",anchor=CENTER)
		self.facturas_tree.heading("#3",text="Monto",anchor=CENTER)
		self.facturas_tree.heading("#4",text="Fecha de Vencimiento",anchor=CENTER)

		#Messages outpus
		self.message = Label(main_box,text = '', fg = 'red')
		self.message.grid(row = 10, column = 0, columnspan = 2, sticky = W + E)

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
		query="SELECT * FROM Facturas ORDER BY id DESC"
		db_rows=self.run_query_recives(query)
		#Recorriendo la lista de productos para insertarlos en la tabla
		for row in db_rows:
			self.facturas_tree.insert("", "end", text=row[1], values=(row[0], row[2], row[3], row[4]))


	def delete_product(self):
		self.message['text'] = ''
		try:
			self.facturas_tree.item(self.facturas_tree.selection())['text'][0]
		except IndexError as e:
			self.message['text'] = 'Please select a Record'
			return
		self.message['text'] = ''
		name = self.facturas_tree.item(self.facturas_tree.selection())['text']
		query = 'DELETE FROM Facturas WHERE Nombre = ?'
		self.run_query_recives(query,(name,))
		self.message['text']='Record {} deleted successfylly'.format(name)
		self.get_recives()

class añadir_productos(tk.Frame):
	db_name = "database.db"
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		button_menu_services=tk.Button(self,text="Menu principal",command=lambda:controller.show_frame(second_menu))
		button_menu_services.pack(pady=10,padx=10)

		#Box
		box=LabelFrame(self)
		box.pack(pady=10,padx=10)

		#Label
		Label(box,text="Nombre del servicio:").grid(row=0,column=0)
		self.service_entry=Entry(box)
		self.service_entry.grid(row=0,column=1)
		self.service_entry.focus()

		#Boton servicios
		ttk.Button(box,text="Save Product",command=self.add_services).grid(row=2,columnspan=2,sticky=W+E)

		#Label2
		Label(box,text="Precio del servicio:").grid(row=1,column=0)
		self.price_entry=Entry(box)
		self.price_entry.grid(row=1,column=1)

		#Creando la tabla de servicios con su respectivo id
		self.services_tree=ttk.Treeview(box,height=10,columns=2)
		self.services_tree.grid(row=5,column=0,columnspan=3,pady=20,padx=20)
		self.services_tree.heading("#0",text="Nombre del servicio",anchor=CENTER)
		self.services_tree.heading("#1",text="Precio en $", anchor=CENTER)
		self.get_servicios()

		#Messages
		self.message=Label(text="",fg="red")
		self.message.pack()

		#Button delete and edit
		ttk.Button(box,text='DELETE',command=self.delete_product).grid(row=3,columnspan=2,sticky=W+E)
		ttk.Button(box,text='EDIT',command=self.edit_product).grid(row=4,columnspan=2,sticky=W+E)

	#Call database
	def run_query(self,query,parameters=()):
		with sqlite3.connect(self.db_name) as conn:
			cursor=conn.cursor()
			result=cursor.execute(query,parameters)
			conn.commit()
		return result

	#Get Products from database
	def get_servicios(self):
		#Limpiando la base de datos
		records=self.services_tree.get_children()
		for elements in records:
			self.services_tree.delete(elements)
		query="SELECT * FROM Product ORDER BY nombre DESC"
		db_rows=self.run_query(query)
		#Recorriendo la lista de productos para insertarlos en la tablla
		for row in db_rows:
			self.services_tree.insert("",0,text=row[1],values=row[2])

	def validation(self):
		return len(self.service_entry.get())!=0 and len(self.price_entry.get())!=0

	def add_services(self):
		if self.validation():
			query="INSERT INTO Product VALUES(NULL,?,?)"
			parameters=(self.service_entry.get(),self.price_entry.get())
			self.run_query(query,parameters)
			self.message["text"]='Product {} added Succesfully'.format(self.service_entry.get())
			self.service_entry.delete(0,END)
			self.price_entry.delete(0,END)
		else:
			self.message['text']='Name and Price is requiered'
		self.get_servicios()

	def delete_product(self):
		self.message['text']=''
		try:
			self.services_tree.item(self.services_tree.selection())['text'][0]
		except IndexError as e:
			self.message['text']='Please select a Record'
			return
		self.message['text']=''
		name=self.services_tree.item(self.services_tree.selection())['text']
		query='DELETE FROM Product WHERE Nombre=?'
		self.run_query(query,(name,))
		self.message['text']='Record {} deleted Succesfully'.format(name)
		self.get_servicios()

	def edit_product(self):
		self.message["text"]=""
		try:
			self.services_tree.item(self.services_tree.selection())['values'][0]
		except IndexError as e:
			self.message['text']='Please,select Record'
			return
		name=self.services_tree.item(self.services_tree.selection())['text']
		old_price=self.services_tree.item(self.services_tree.selection())['values'][0]
		self.edit_wind=Toplevel()
		self.edit_wind.title='Edit Product'
		#Old Name
		Label(self.edit_wind,text='Old Name:').grid(row=0,column=1)
		Entry(self.edit_wind,textvariable=StringVar(self.edit_wind,value=name),state='readonly').grid(row=0,column=2)
		#New Name
		Label(self.edit_wind,text='New Name:').grid(row=1,column=1)
		new_name=Entry(self.edit_wind)
		new_name.grid(row=1,column=2)

		#Old Price
		Label(self.edit_wind, text = 'Old Price:').grid(row = 2, column = 1)
		Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
		#New Price
		Label(self.edit_wind, text = 'New Price:').grid(row = 3, column = 1)
		new_price= Entry(self.edit_wind)
		new_price.grid(row = 3, column = 2)

		Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
		self.edit_wind.mainloop()

	def edit_records(self, new_name, name, new_price, old_price):
		query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
		parameters = (new_name, new_price,name, old_price)
		self.run_query(query, parameters)
		self.edit_wind.destroy()
		self.message['text'] = 'Record {} updated successfylly'.format(name)
		self.get_products()

class loggin(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		KNOWN_FACES_DIR = "./known_faces"
		TOLERANCE = 0.6
		FRAME_THIKNESS = 3
		FONT_THIKNESS = 2
		MODEL = "cnn"
		video = cv2.VideoCapture(0)
		print("loading known faces")
		known_faces = []
		known_names = []

		for name in os.listdir(KNOWN_FACES_DIR):
			for filename in os.listdir(KNOWN_FACES_DIR):
				image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{filename}")
				encoding = face_recognition.face_encodings(image)[0]
				known_faces.append(encoding)
				known_names.append(name)

		print("procesing unknown faces")
		while True:
			ret, image = video.read()
			rgb_image = image[:, :, ::-1]
			locations = face_recognition.face_locations(rgb_image)
			encodings = face_recognition.face_encodings(rgb_image, locations)
			for face_encoding, face_location in zip(encodings, locations):
				results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
				match = None
				if True in results:
					match = known_names[results.index(True)]
					print(f"match found: {match}")
					top_left = (face_location[3], face_location[0])
					bottom_right = (face_location[1], face_location[2])
					color = [0, 255, 0]
					cv2.rectangle(image, top_left, bottom_right, color, FRAME_THIKNESS)
					top_left = (face_location[3], face_location[2])
					bottom_right = (face_location[1], face_location[2] + 22)
					cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
					cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 0), FONT_THIKNESS)
					return tk.Button(self,text="Continuar", command =lambda:controller.show_frame(second_menu)).pack()

			cv2.imshow('filename', image)
			if cv2.waitKey(1) & 0xFF == ord("q"):
				break

class starting_screen(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		tk.Button(text="Login", command =lambda:controller.show_frame(loggin)).pack()





#Iniciando la aplicación
app = MainStream()
app.mainloop()
