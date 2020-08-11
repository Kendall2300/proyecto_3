from reportlab.pdfgen import canvas
import PyPDF2
c = canvas.Canvas('sample.pdf')
c.save()
pdf_file = open('sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

import os
import time
import sys
from decimal import Decimal
import datetime
import warnings



URL_WSAA = "login url"
URL_WSFEv1 = "service screen url"
CUIT = 20267565393
CERT = "../reingart.crt"
PRIVATEKEY = "../reingart.key"
CACHE = "../cache"
CONF_PDF = dict(
    LOGO="../screen/logo.png",
    EMPRESA="Ejemplo de empresa",
    MEMBRETE1="Ejemplo de direccion",
    MEMBRETE2="Capital Federal",
    CUIT="CUIT 30-00000000-0",
    IIBB="exento",
    IVA="IVA Responsable Inscripto",
    INICIO="Inicio de Actividad: fecha",
    )


def facturar(registros):

    # inicialización AFIP:
    wsaa = WSAA()
    wsfev1 = WSFEv1()
    # login
    ta = wsaa.Autenticar("wsfe", CERT, PRIVATEKEY,
                         wsdl=URL_WSAA, cache=CACHE, debug=True)
    wsfev1.Cuit = CUIT
    wsfev1.SetTicketAcceso(ta)
    wsfev1.Conectar(CACHE, URL_WSFEv1)

    "build bill"
    fepdf = FEPDF()
    fepdf.CargarFormato("sample.pdf")
    fepdf.FmtCantidad = "0.2"
    fepdf.FmtPrecio = "0.2"
    fepdf.CUIT = CUIT
    for k, v in CONF_PDF.items():
        fepdf.AgregarDato(k, v)

    

    "registri data for bill + pdf generation"
    for reg in registros:
        hoy = datetime.date.today().strftime("%Y%m%d")
        cbte = Comprobante(tipo_cbte=6, punto_vta=4000, fecha_cbte=hoy,
                           cbte_nro=reg.get("nro"),
                           tipo_doc=96, nro_doc=reg["dni"],
                           nombre_cliente=reg["nombre"],      
                           domicilio_cliente=reg["domicilio"],  
                           fecha_serv_desde=reg.get("periodo_desde"),
                           fecha_serv_hasta=reg.get("periodo_hasta"),
                           fecha_venc_pago=reg.get("venc_pago", hoy),
                          )
        cbte.agregar_item(ds=reg["descripcion"],
                          qty=reg.get("cantidad", 1),
                          precio=reg.get("precio", 0),
                          tasa_iva=reg.get("tasa_iva", 21.),
                         )
        
        print("Factura autorizada", nro, cbte.encabezado["cae"])
        
        ok = cbte.generar_pdf(fepdf, "samplefinish.pdf".format(nro))
        print("PDF generado", ok)


"print pdf"
read_pdf = PyPDF2.PdfFileReader("samplefinish.pdf")
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content)