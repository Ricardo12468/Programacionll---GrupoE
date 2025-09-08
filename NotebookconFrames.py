# importación de librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("750x600")
edadVar=tk.StringVar()
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
    
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_nacimiento=datetime.now()
        fecha_actual=datetime.now()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edadentry=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edadentry)
    else:
        edadVar.set("")
        return True

#Llamando a la funcion de enmascarar fecha
def guardar_en_archivo():
    with open("pacientes.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']} | {paciente['Fecha de Nacimiento']} | {paciente['Edad']} | "
                          f"{paciente['Genero']} | {paciente['Grupo Sanguineo']} | {paciente['Tipo de Seguro']} | "
                          f"{paciente['Centro Medico']}\n")
def cargar_desde_archivo_paciente():
    try:
        with open("pacientes.txt","r",encoding="utf-8")as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                    "Nombre":datos[0],
                    "Fecha de Nacimiento":datos[1],
                    "Edad":datos[2],
                    "Genero":datos[3],
                    "Grupo Sanguineo":datos[4],
                    "Tipo de Seguro":datos[5],
                    "Centro Medico":datos[6]
                    }
                paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacientes.txt","w",encoding="utf-8").close()
pestañas=ttk.Notebook(ventana_principal)
#Crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
# Agregar pestañas al Notebook
pestañas.add(frame_pacientes, text="Pacientes")
# Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
# Crear frame de doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
pestañas.pack(expand=True, fill="both")
# NOmbre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5,pady=5)
#Fecha de Nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelFechaN.grid(row=2,column=0,sticky="w",padx=5,pady=5)
#EDad
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=3, column=0, sticky="w", pady=5, padx=5)
edadentry=tk.Entry(frame_pacientes,textvariable=edadVar, state="readonly")
edadentry.grid(row=3, column=1, sticky="w", pady=5, padx=5)
#genero
labelGenero=tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=4, column=0, sticky="w", pady=5, padx=5)
generoP=tk.StringVar()
generoP.set("Masculino")
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=generoP, value="Masculino")
radioMasculino.grid(row=4, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=generoP, value="Femenino")
radioFemenino.grid(row=5, column=1, sticky="w", padx=5)
# Grupo sanguineo
labelgruposanguineo=tk.Label(frame_pacientes, text="Grupo sanguineo")
labelgruposanguineo.grid(row=6, column=0, sticky="w", pady=5, padx=5)
entrygruposanguineo=tk.Entry(frame_pacientes)
entrygruposanguineo.grid(row=6, column=1, sticky="w", pady=5, padx=5)
#Tipo sanguineo
labeltiposanguineo=tk.Label(frame_pacientes, text="Tipo de Seguro")
labeltiposanguineo.grid(row=7,column=0,sticky="w",pady=5,padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")  #valer por defecto
combotseguro=ttk.Combobox(frame_pacientes,values=("Publico","Privado","Ninguno"),textvariable=tipo_seguro)
combotseguro.grid(row=7,column=1,sticky="w",pady=5,padx=5)
#dfgdf
labelcentromedico=tk.Label(frame_pacientes, text="Centro de Salud")
labelcentromedico.grid(row=8,column=0,sticky="w",pady=5,padx=5)
centromedico=tk.StringVar()
centromedico.set("Hospital Central")  
combotcentromedico=ttk.Combobox(frame_pacientes,values=("Hospital Central","Clinica Norte","Centro Sur"),textvariable=centromedico)
combotcentromedico.grid(row=8,column=1,sticky="w",pady=5,padx=5)
#frame oara los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=9,column=0,columnspan=2,sticky="w",pady=5)
#boton registrar

#boton eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=9,column=1,padx=5)
#crear 
treeview=ttk.Treeview(frame_pacientes, columns=("Nombre","Fecha","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")
#dgdfgfg
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=2, column=1, sticky="w", pady=5, padx=5)

paciente_data=[]                                                          
def registrarPaciente():
#Crear un diccionario con los datos ingresados
    paciente={
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":generoP.get(),
        "Grupo Sanguineo": entrygruposanguineo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Medico":centromedico.get()    
    }
    #Agregar paciente a la lista                                                         
    paciente_data.append(paciente)
    #Cargar el treeview
    cargar_treeview()
def cargar_treeview():
    #Limpiar el Treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i, item in enumerate (paciente_data):
        treeview.insert(
            "","end",iid=str(i),
        values=(
            item["Nombre"],
            item["Fecha de Nacimiento"],
            item["Edad"],
            item["Genero"],
            item["Grupo Sanguineo"],
            item["Tipo de Seguro"],
            item["Centro Medico"]
            )
        )
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=9,column=0,padx=5)
#definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("Fecha", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
#defnir Anchos de columna
treeview.column("Nombre",width=120)
treeview.column("Fecha",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=60,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)
#ubicar el TreeView en la cuadricula
treeview.grid(row=10,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=10,column=2,sticky="ns")


ventana_principal.mainloop()