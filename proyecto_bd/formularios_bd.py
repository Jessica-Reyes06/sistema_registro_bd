import os, random, datetime, csv, customtkinter
from config_principal import limpiar_frame
from db_conexion import ejecutar_insert, ejecutar_select, conexion

# -------------------------------

CARRERAS_ITVER = [
    "Ingeniería en Sistemas Computacionales",
    "Ingeniería Industrial",
    "Ingeniería Electromecánica",
    "Ingeniería Eléctrica",
    "Ingeniería Electrónica",
    "Ingeniería Civil",
    "Ingeniería Química",
    "Ingeniería Bioquímica",
    "Ingeniería en Gestión Empresarial",
    "Licenciatura en Administración",
]

SEMESTRES_ITVER = [str(i) for i in range(1,13)]
ESTADOS_ALUMNO = ["Activo","Baja","Egresado"]


def generar_numero_control_unico():
    year = datetime.date.today().year % 100
    prefijo = f"A{year:02d}"

    while True:
        sufijo = "".join(str(random.randint(0,9)) for _ in range(5))
        numero = prefijo + sufijo

        existe = ejecutar_select(
            "SELECT numero_control FROM alumnos WHERE numero_control=%s",
            (numero,)
        )

        if not existe:
            return numero

# CONSTRUCTOR DE CAMPOS

def crear_campo(frame,fila,texto):
    label = customtkinter.CTkLabel(frame,text=texto,font=("Arial",14))
    label.grid(row=fila,column=0,padx=10,pady=5,sticky="w")

    entry = customtkinter.CTkEntry(frame,width=260)
    entry.grid(row=fila,column=1,padx=10,pady=5,sticky="w")

    return entry


def crear_combo(frame,fila,texto,opciones):

    label = customtkinter.CTkLabel(frame,text=texto,font=("Arial",14))
    label.grid(row=fila,column=0,padx=10,pady=5,sticky="w")

    combo = customtkinter.CTkComboBox(
        frame,
        values=opciones,
        width=260,
        state="readonly"
    )

    combo.set(opciones[0])
    combo.grid(row=fila,column=1,padx=10,pady=5,sticky="w")

    return combo

# FORMULARIO GENERICO

def crear_formulario_generico(frame_contenido,titulo,campos,sql_insert,volver_a_lista=None):

    limpiar_frame(frame_contenido)

    titulo_label = customtkinter.CTkLabel(
        frame_contenido,
        text=titulo,
        font=("Arial",22,"bold")
    )
    titulo_label.pack(pady=(10,20))

    cuerpo = customtkinter.CTkFrame(frame_contenido)
    cuerpo.pack(padx=20,pady=10,fill="x")

    entradas = {}

    for i,campo in enumerate(campos):
        entradas[campo] = crear_campo(cuerpo,i,campo)

    estado_label = customtkinter.CTkLabel(frame_contenido,text="")
    estado_label.pack()

    def guardar():

        valores = [entradas[c].get() for c in campos]

        if "" in valores:
            estado_label.configure(text="Todos los campos deben llenarse",text_color="red")
            return

        try:
            ejecutar_insert(sql_insert,tuple(valores))
            estado_label.configure(text="Registro guardado correctamente",text_color="green")

            if volver_a_lista:
                volver_a_lista()

        except Exception as e:
            estado_label.configure(text=str(e),text_color="red")

    botones = customtkinter.CTkFrame(frame_contenido,fg_color="transparent")
    botones.pack(pady=20)

    customtkinter.CTkButton(
        botones,
        text="Guardar",
        command=guardar
    ).grid(row=0,column=0,padx=10)

    customtkinter.CTkButton(
        botones,
        text="Cancelar",
        command=lambda: volver_a_lista() if volver_a_lista else None
    ).grid(row=0,column=1,padx=10)

# FORMULARIO ALUMNOS

def mostrar_form_registro_alumno(frame_contenido,volver_a_lista=None):

    limpiar_frame(frame_contenido)

    titulo = customtkinter.CTkLabel(frame_contenido,text="Registrar alumno",font=("Arial",22,"bold"))
    titulo.pack(pady=(10,20))

    cuerpo = customtkinter.CTkFrame(frame_contenido)
    cuerpo.pack(padx=20,pady=10,fill="x")

    entradas = {}

    entradas["Nombre"] = crear_campo(cuerpo,0,"Nombre")
    entradas["ApellidoPaterno"] = crear_campo(cuerpo,1,"Apellido paterno")
    entradas["ApellidoMaterno"] = crear_campo(cuerpo,2,"Apellido materno")

    entradas["Carrera"] = crear_combo(cuerpo,3,"Carrera",CARRERAS_ITVER)
    entradas["Semestre"] = crear_combo(cuerpo,4,"Semestre",SEMESTRES_ITVER)
    entradas["Estado"] = crear_combo(cuerpo,5,"Estado",ESTADOS_ALUMNO)

    estado_label = customtkinter.CTkLabel(frame_contenido,text="")
    estado_label.pack()

    valores_generados = {"numero":"","correo":""}

    def generar():

        numero = generar_numero_control_unico()
        correo = f"{numero}@tecnm.mx"

        valores_generados["numero"]=numero
        valores_generados["correo"]=correo

        estado_label.configure(text=f"Número generado: {numero}",text_color="green")

    def guardar():

        if valores_generados["numero"]=="":
            estado_label.configure(text="Primero genera número de control",text_color="red")
            return

        datos = (
            valores_generados["numero"],
            entradas["Nombre"].get(),
            entradas["ApellidoPaterno"].get(),
            entradas["ApellidoMaterno"].get(),
            valores_generados["correo"],
            entradas["Carrera"].get(),
            entradas["Semestre"].get(),
            entradas["Estado"].get()
        )

        sql = """
        INSERT INTO alumnos
        (numero_control,nombre_alumno,apellido_paterno,apellido_materno,
        correo_alumno,carrera,semestre,estatus_alumno)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        ejecutar_insert(sql,datos)

        estado_label.configure(text="Alumno guardado",text_color="green")

    botones = customtkinter.CTkFrame(frame_contenido,fg_color="transparent")
    botones.pack(pady=20)

    customtkinter.CTkButton(botones,text="Generar número",command=generar).grid(row=0,column=0,padx=10)
    customtkinter.CTkButton(botones,text="Guardar",command=guardar).grid(row=0,column=1,padx=10)
    customtkinter.CTkButton(botones,text="Cancelar",command=lambda: volver_a_lista() if volver_a_lista else None).grid(row=0,column=2,padx=10)

# MAESTROS

def mostrar_form_registro_maestro(frame_contenido,volver_a_lista=None):

    campos = [
        "matricula",
        "nombre",
        "apellido_paterno",
        "apellido_materno",
        "correo",
        "estatus",
        "estudios",
        "perfil",
        "carga_academica",
        "contrato",
        "cedula"
    ]

    sql = """
    INSERT INTO maestros
    (matricula,nombre,apellido_paterno,apellido_materno,
    correo,estatus,estudios,perfil,carga_academica,contrato,cedula)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    crear_formulario_generico(frame_contenido,"Registrar maestro",campos,sql,volver_a_lista)

# MATERIAS

def mostrar_form_registro_materia(frame_contenido,volver_a_lista=None):

    campos = ["clave","nombre_materia","horas","creditos","tipo"]

    sql = """
    INSERT INTO materias
    (clave,nombre_materia,horas,creditos,tipo)
    VALUES (%s,%s,%s,%s,%s)
    """

    crear_formulario_generico(frame_contenido,"Registrar materia",campos,sql,volver_a_lista)

# GRUPOS

def mostrar_form_registro_grupo(frame_contenido,volver_a_lista=None):

    campos = ["matricula_maestro","clave_materia","horario","cupo"]

    sql = """
    INSERT INTO grupos
    (matricula_maestro,clave_materia,horario,cupo)
    VALUES (%s,%s,%s,%s)
    """

    crear_formulario_generico(frame_contenido,"Crear grupo",campos,sql,volver_a_lista)

# INSCRIPCIONES

def mostrar_form_registro_inscripcion(frame_contenido,volver_a_lista=None):

    campos = ["numero_control","id_grupo","fecha","estatus","tipo"]

    sql = """
    INSERT INTO inscripciones
    (numero_control,id_grupo,fecha,estatus,tipo)
    VALUES (%s,%s,%s,%s,%s)
    """

    crear_formulario_generico(frame_contenido,"Inscribir alumno",campos,sql,volver_a_lista)
def importar_csv(tabla, ruta_csv):

        with open(ruta_csv, newline="", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)
            encabezados = next(lector)

            placeholders = ",".join(["%s"] * len(encabezados))
            columnas = ",".join(encabezados)

            sql = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"

            cursor = conexion.cursor()

            for fila in lector:
                cursor.execute(sql, fila)

            conexion.commit()
            cursor.close()
    
def exportar_csv(tabla, ruta_destino):

    cursor = conexion.cursor()

    cursor.execute(f"SELECT * FROM {tabla}")

    filas = cursor.fetchall()
    columnas = [col[0] for col in cursor.description]

    with open(ruta_destino, "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow(columnas)

        for fila in filas:
            escritor.writerow(fila)

    cursor.close()