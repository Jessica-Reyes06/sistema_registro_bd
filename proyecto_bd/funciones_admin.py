from customtkinter import *
from PIL import Image
from tkinter import filedialog, messagebox
from config_principal import calendario, limpiar_frame, crear_tarjeta
from formularios_bd import *

pendientes_admin = []

def mostrar_dashboard(frame):
    limpiar_frame(frame)

    header = CTkFrame(frame, height=60, fg_color="#154b74")
    header.pack(fill="x", pady=(0,20))

    titulo = CTkLabel(header,text="Panel de Administración",text_color="white",font=("Arial",28,"bold"))
    titulo.pack(pady=15)

    contenedor = CTkFrame(frame)
    contenedor.pack(fill="both", expand=True, padx=20, pady=(10, 0))

    for c in range(5):
        contenedor.grid_columnconfigure(c, weight=1)

    for r in range(3):
        contenedor.grid_rowconfigure(r, weight=1)

    icono_alumnos = CTkImage(light_image=Image.open("carpeta_iconos/iconos_admin/alumnos.png"),size=(64,64))
    icono_maestros = CTkImage(light_image=Image.open("carpeta_iconos/iconos_admin/maestros.png"),size=(64,64))
    icono_materias = CTkImage(light_image=Image.open("carpeta_iconos/iconos_admin/materias.png"),size=(64,64))
    icono_grupos = CTkImage(light_image=Image.open("carpeta_iconos/iconos_admin/grupos.png"),size=(64,64))
    icono_inscripciones = CTkImage(light_image=Image.open("carpeta_iconos/iconos_admin/inscripciones.png"),size=(64,64))

    crear_tarjeta(contenedor,"Alumnos",lambda: mostrar_alumnos(frame),"#510054",icono_alumnos).grid(row=0,column=0,padx=10,pady=10)
    crear_tarjeta(contenedor,"Maestros",lambda: mostrar_maestros(frame),"#004235",icono_maestros).grid(row=0,column=1,padx=10,pady=10)
    crear_tarjeta(contenedor,"Materias",lambda: mostrar_materias(frame),"#761127",icono_materias).grid(row=0,column=2,padx=10,pady=10)
    crear_tarjeta(contenedor,"Grupos",lambda: mostrar_grupos(frame),"#1f6aa5",icono_grupos).grid(row=0,column=3,padx=10,pady=10)
    crear_tarjeta(contenedor,"Inscripciones",lambda: mostrar_inscripciones(frame),"#7A3500",icono_inscripciones).grid(row=0,column=4,padx=10,pady=10)

    zona_inferior = CTkFrame(frame, height=120)
    zona_inferior.pack(side="bottom", fill="x", padx=20, pady=(0,15))
    zona_inferior.pack_propagate(False)

    frame_calendario = CTkFrame(zona_inferior, fg_color="#ffffff")
    frame_calendario.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

    calendario(frame_calendario)

    frame_texto = CTkFrame(zona_inferior, fg_color="#cfe5f3")
    frame_texto.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")

    frame_texto.grid_columnconfigure(0, weight=1)
    frame_texto.grid_columnconfigure(1, weight=1)

    CTkLabel(frame_texto,text="Enero - Junio 2026",justify="left",font=("Arial",16,"bold"),text_color="#000000").grid(row=0,column=0,columnspan=2,padx=15,pady=(10,5),sticky="w")

    eventos = [
        "7 al 16 de enero: Actividades intersemestrales",
        "12 al 16 de enero: Curso de inducción de nuevo ingreso",
        "19 y 20 de enero: Inscripciones",
        "21 al 23 de enero: Reinscripciones",
        "26 de enero: Inicio de clases",
        "30 de marzo al 10 de abril: Periodo vacacional",
        "29 de mayo: Fin de clases",
        "1 al 3 de junio: Evaluación sumativa de complementación",
        "4 y 5 de junio: Entrega de calificaciones a servicios escolares",
        "8 de julio al 3 de agosto: Actividades intersemestrales",
        "6 al 31 de julio: Periodo vacacional",
    ]

    mitad = (len(eventos)+1)//2

    for i in range(len(eventos)):
        if i < mitad:
            columna = 0
            fila = i+1
        else:
            columna = 1
            fila = (i-mitad)+1

        CTkLabel(frame_texto,text=eventos[i],justify="left",anchor="w",font=("Arial",14),text_color="#000000").grid(row=fila,column=columna,padx=(15,15),pady=2,sticky="w")

def mostrar_calendario_imagen(frame):
    limpiar_frame(frame)

    header = CTkFrame(frame,height=60,fg_color="#154b74")
    header.pack(fill="x",pady=10)

    CTkLabel(header,text="Calendario",text_color="white",font=("Arial",26,"bold")).pack(pady=15)

    cuerpo = CTkFrame(frame,fg_color="#ffffff")
    cuerpo.pack(fill="both",expand=True,padx=20,pady=10)

    imagen_cal = CTkImage(light_image=Image.open("carpeta_iconos/iconos_admin/calendario.png"),size=(600,800))

    CTkLabel(cuerpo,text="",image=imagen_cal).pack(expand=True)

def mostrar_pendientes(frame):
    limpiar_frame(frame)

    header = CTkFrame(frame,height=60,fg_color="#154b74")
    header.pack(fill="x",pady=10)

    CTkLabel(header,text="Pendientes",text_color="white",font=("Arial",26,"bold")).pack(pady=15)

    cuerpo = CTkFrame(frame,fg_color="#ffffff")
    cuerpo.pack(fill="both",expand=True,padx=20,pady=10)

    lista = CTkScrollableFrame(cuerpo,fg_color="#ffffff")
    lista.pack(fill="both",expand=True,padx=10,pady=10)

    if not pendientes_admin:
        CTkLabel(lista,text="No hay pendientes registrados",font=("Arial",16,"bold")).pack(pady=10)
    else:
        for i,texto in enumerate(pendientes_admin,start=1):
            CTkLabel(lista,text=f"{i}. {texto}",anchor="w",justify="left",font=("Arial",14)).pack(fill="x",padx=5,pady=4)

def mostrar_notificaciones(frame):
    limpiar_frame(frame)

    header = CTkFrame(frame,height=60,fg_color="#154b74")
    header.pack(fill="x",pady=10)

    CTkLabel(header,text="Notificaciones",text_color="white",font=("Arial",26,"bold")).pack(pady=15)

    cuerpo = CTkFrame(frame,fg_color="#ffffff")
    cuerpo.pack(fill="both",expand=True,padx=20,pady=10)

    CTkLabel(cuerpo,text="No hay notificaciones",font=("Arial",18,"bold")).pack(pady=20)

def mostrar_seccion_gestion(frame,titulo,color_header,color_menu,color_tabla,botones,headers,tabla_sql=None):
    limpiar_frame(frame)

    CTkButton(frame,text="←",width=80,command=lambda: mostrar_dashboard(frame)).pack(anchor="w",padx=20,pady=10)

    header = CTkFrame(frame,height=60,fg_color=color_header)
    header.pack(fill="x")

    CTkLabel(header,text=titulo,text_color="white",font=("Arial",26,"bold")).pack(pady=15)

    menu = CTkFrame(frame,fg_color=color_menu)
    menu.pack(fill="x",padx=20,pady=10)

    for i in range(len(botones)):
        menu.grid_columnconfigure(i,weight=1)

    area_contenido = CTkFrame(frame)
    area_contenido.pack(fill="both",expand=True,padx=20,pady=10)

    def mostrar_tabla_base():
        limpiar_frame(area_contenido)

        tabla = CTkFrame(area_contenido)
        tabla.pack(fill="both",expand=True)

        encabezado = CTkFrame(tabla,fg_color=color_tabla)
        encabezado.pack(fill="x")

        for i,h in enumerate(headers):
            encabezado.grid_columnconfigure(i,weight=1)
            CTkLabel(encabezado,text=h,text_color="white",font=("Arial",14,"bold")).grid(row=0,column=i,padx=10,pady=10,sticky="ew")

        # Cuerpo de la tabla con los registros de la base de datos
        cuerpo = CTkScrollableFrame(tabla, fg_color="#ffffff")
        cuerpo.pack(fill="both", expand=True)

        if tabla_sql:
            try:
                registros = ejecutar_select(f"SELECT * FROM {tabla_sql}")

                if not registros:
                    CTkLabel(cuerpo, text="No hay registros", font=("Arial", 14)).pack(pady=10)
                else:
                    for fila_idx, fila in enumerate(registros):
                        limite_columnas = min(len(headers), len(fila))
                        for col_idx in range(limite_columnas):
                            valor = fila[col_idx]
                            cuerpo.grid_columnconfigure(col_idx, weight=1)
                            CTkLabel(
                                cuerpo,
                                text=str(valor),
                                font=("Arial", 13),
                                anchor="w",
                                text_color="#000000"
                            ).grid(row=fila_idx, column=col_idx, padx=10, pady=4, sticky="ew")
            except Exception as e:
                CTkLabel(cuerpo, text=f"Error al cargar datos: {e}", text_color="red").pack(pady=10)

    mostrar_tabla_base()

    for i,btn in enumerate(botones):
        comando_base = btn.get("comando")
        cmd = (lambda cb=comando_base: cb(area_contenido,mostrar_tabla_base)) if comando_base else mostrar_tabla_base
        CTkButton(menu,text=btn["texto"],fg_color=btn["color"],command=cmd).grid(row=0,column=i,padx=10,pady=10)

def seleccionar_csv():
    return filedialog.askopenfilename(title="Selecciona CSV",filetypes=[("CSV","*.csv")])

def guardar_csv(nombre):
    return filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV","*.csv")],initialfile=nombre)

def ejecutar_importacion(tabla,volver):
    ruta = seleccionar_csv()
    if not ruta:
        return
    try:
        importar_csv(tabla,ruta)
        messagebox.showinfo("Importar CSV","Datos importados correctamente.")
        if volver:
            volver()
    except Exception as e:
        messagebox.showerror("Error",str(e))

def ejecutar_exportacion(tabla,nombre):
    ruta = guardar_csv(nombre)
    if not ruta:
        return
    try:
        exportar_csv(tabla,ruta)
        messagebox.showinfo("Exportar CSV","Datos exportados correctamente.")
    except Exception as e:
        messagebox.showerror("Error",str(e))

def mostrar_alumnos(frame):

    def registrar(area,volver):
        mostrar_form_registro_alumno(area,volver)

    def importar(area,volver):
        ejecutar_importacion("alumnos",volver)

    def exportar(area,volver):
        ejecutar_exportacion("alumnos","alumnos.csv")

    botones = [
        {"texto":"Registrar alumno","color":"#552157","comando":registrar},
        {"texto":"Importar CSV","color":"#552157","comando":importar},
        {"texto":"Exportar CSV","color":"#552157","comando":exportar},
    ]

    headers = ["No.Control","Nombre","A. Paterno","A. Materno","Correo","Carrera","Semestre","Estado"]

    mostrar_seccion_gestion(frame,"Gestión de Alumnos","#510054","#fafafa","#9880a0",botones,headers,"alumnos")

def mostrar_maestros(frame):

    def registrar(area,volver):
        mostrar_form_registro_maestro(area,volver)

    def importar(area,volver):
        ejecutar_importacion("maestros",volver)

    def exportar(area,volver):
        ejecutar_exportacion("maestros","maestros.csv")

    botones = [
        {"texto":"Registrar maestro","color":"#022A22","comando":registrar},
        {"texto":"Importar CSV","color":"#022A22","comando":importar},
        {"texto":"Exportar CSV","color":"#022A22","comando":exportar},
    ]

    headers = ["Matricula","Nombre","A. Paterno","A. Materno","Correo","Estatus","Estudios","Perfil","Carga Académica","Contrato","Cédula"]

    mostrar_seccion_gestion(frame,"Gestión de Maestros","#004235","#ffffff","#6F8A90",botones,headers,"maestros")

def mostrar_materias(frame):

    def registrar(area,volver):
        mostrar_form_registro_materia(area,volver)

    def importar(area,volver):
        ejecutar_importacion("materias",volver)

    def exportar(area,volver):
        ejecutar_exportacion("materias","materias.csv")

    botones = [
        {"texto":"Registrar materia","color":"#510113","comando":registrar},
        {"texto":"Importar CSV","color":"#510113","comando":importar},
        {"texto":"Exportar CSV","color":"#510113","comando":exportar},
    ]

    headers = ["Clave","Materia","Horas","Créditos","Tipo"]

    mostrar_seccion_gestion(frame,"Gestión de Materias","#761127","#ffffff","#9A0000",botones,headers,"materias")

def mostrar_grupos(frame):

    def registrar(area,volver):
        mostrar_form_registro_grupo(area,volver)

    def importar(area,volver):
        ejecutar_importacion("grupos",volver)

    def exportar(area,volver):
        ejecutar_exportacion("grupos","grupos.csv")

    botones = [
        {"texto":"Crear grupo","color":"#184c73","comando":registrar},
        {"texto":"Importar CSV","color":"#184c73","comando":importar},
        {"texto":"Exportar CSV","color":"#184c73","comando":exportar},
    ]

    headers = ["ID Grupo","Maestro","Materia","Horario","Cupo"]

    mostrar_seccion_gestion(frame,"Gestión de Grupos","#1f6aa5","#ffffff","#8fb1cb",botones,headers,"grupos")

def mostrar_inscripciones(frame):

    def registrar(area,volver):
        mostrar_form_registro_inscripcion(area,volver)

    def importar(area,volver):
        ejecutar_importacion("registros",volver)

    def exportar(area,volver):
        ejecutar_exportacion("registros","inscripciones.csv")

    botones = [
        {"texto":"Inscribir alumno","color":"#A64500","comando":registrar},
        {"texto":"Importar CSV","color":"#A64500","comando":importar},
        {"texto":"Exportar CSV","color":"#A64500","comando":exportar},
    ]

    headers = ["ID","No.Control","ID Grupo","Fecha","Estatus","Tipo"]

    mostrar_seccion_gestion(frame,"Inscripciones","#7A3500","#ffffff","#C75C00",botones,headers,"registros")