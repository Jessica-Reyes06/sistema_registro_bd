from customtkinter import *
from PIL import Image
from tkinter import filedialog
import os


#------------------FUNCIONES----------------
def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def componentes_anuncios(frame_tab):
    frame_anuncio=CTkFrame(frame_tab,
                            fg_color="#cabece")
    frame_anuncio.pack(pady=5, padx=5, fill="x")
    CTkLabel(frame_anuncio,
                text="Titulo del anuncio",
                text_color="black",
                justify="left",
                font=("Arial Rounded MT Bold", 20)
                ).pack(pady=5, padx=10, anchor="w")
    CTkLabel(frame_anuncio,
                text="Contenido del anuncio",
                text_color="black",
                justify="left",
                font=("Arial Rounded MT Bold", 14)
                ).pack(pady=5, padx=10, anchor="w")
    
def componentes_actividades(frame_tab, titulo):
    limpiar_frame(frame_tab)

#funcion para seleccionar archivo y mostrar su nombre en una etiqueta
    def seleccionar_archivo():
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Todos los archivos", "*.*"), ("PDF", "*.pdf"), ("Word", "*.docx")]
        )
        if ruta:
            label_archivo.configure(text=f"Archivo: {os.path.basename(ruta)}")

    frame_actividad = CTkFrame(frame_tab, fg_color="#cabece")
    frame_actividad.pack(pady=5, padx=5, fill="x")
    CTkLabel(
        frame_actividad,
        text=titulo,
        text_color="black",
        justify="left",
        font=("Arial Rounded MT Bold", 20)
    ).pack(pady=5, padx=10, anchor="w")
    CTkLabel(
        frame_actividad,
        text="Descripción de la actividad",
        text_color="black",
        justify="left",
        font=("Arial Rounded MT Bold", 14)
    ).pack(pady=5, padx=10, anchor="w")

    label_archivo = CTkLabel(
        frame_actividad,
        text="Archivo: ninguno",
        text_color="black",
        justify="left",
        font=("Arial Rounded MT Bold", 14)
    )
    label_archivo.pack(pady=(5, 8), padx=10, anchor="w")

    frame_botones = CTkFrame(frame_actividad, fg_color="#cabece")
    frame_botones.pack(fill="x", padx=10, pady=(0, 5))

    CTkButton(
        frame_botones,
        text="Seleccionar archivo",
        fg_color="#715a72",
        text_color="white",
        hover_color="#5e485f",
        font=("Arial Rounded MT Bold", 14),
        command=seleccionar_archivo
    ).pack(side="left")

    CTkButton(
        frame_botones,
        text="Enviar actividad",
        fg_color="#715a72",
        text_color="white",
        hover_color="#5e485f",  
        font=("Arial Rounded MT Bold", 14)
    ).pack(side="right")


def boton_unidad_grupo(frame_tab, frame_detalle, titulo_unidad, actividades):
    frame_grupo = CTkFrame(frame_tab, fg_color="white")
    frame_grupo.pack(pady=0, padx=5, fill="x")

    img_unidad = CTkImage(
        Image.open("carpeta_iconos/iconos_alumnos/resaltador.png"),
        size=(30, 30)
    )

    frame_opciones = CTkFrame(frame_grupo, fg_color="white")
    desplegado = {"activo": False}

    def toggle_menu():
        if desplegado["activo"]:
            frame_opciones.pack_forget()
            desplegado["activo"] = False
        else:
            frame_opciones.pack(fill="x", padx=0, pady=0, anchor="w")
            desplegado["activo"] = True

    boton_unidad = CTkButton(
        frame_grupo,
        text=f"     {titulo_unidad}",
        image=img_unidad,
        compound="left",
        anchor="w",
        width=1190,
        fg_color="#5e485f",
        hover_color="#4c304e",
        text_color="white",
        font=("Arial Rounded MT Bold", 25),
        command=toggle_menu
    )
    boton_unidad.pack(pady=0, padx=0, fill="x", anchor="w")

    for actividad in actividades:
        CTkButton(
            frame_opciones,
            text=f"{actividad}",
            anchor="w",
            width=1190,
            fg_color="#715a72",
            hover_color="#5e485f",
            text_color="white",
            corner_radius=0,
            font=("Arial Rounded MT Bold", 14),
            command=lambda titulo=actividad: componentes_actividades(frame_detalle, titulo)
        ).pack(fill="x", padx=0, pady=0)

def Anuncios(tab):
    limpiar_frame(tab)
    CTkLabel(
        tab, 
        text="Anuncios del grupo", 
        font=("Arial Rounded MT Bold", 20),
        text_color="black"
        ).pack(pady=10)
    
    componentes_anuncios(tab)
    
def Documentacion(tab):
    limpiar_frame(tab)
    CTkLabel(
            tab, 
            text="Documentos del grupo", 
            font=("Arial Rounded MT Bold", 20),
            text_color="black"
            ).pack(pady=10)

def Actividades(tab):
    limpiar_frame(tab)
    CTkLabel(
        tab,
        text="Actividades del grupo", 
        font=("Arial Rounded MT Bold", 20),
        text_color="black"
        ).pack(pady=10)
    
    frame_menu_unidades = CTkFrame(tab, fg_color="white")
    frame_menu_unidades.pack(fill="x", padx=5, pady=0)

    frame_detalle = CTkFrame(tab, fg_color="white")
    frame_detalle.pack(fill="x", padx=5, pady=(5, 0))

    boton_unidad_grupo(
        frame_menu_unidades,
        frame_detalle,
        "Unidad 1",
        ["Actividad 1", "Actividad 2", "Actividad 3"]
    )
    boton_unidad_grupo(
        frame_menu_unidades,
        frame_detalle,
        "Unidad 2",
        ["Actividad 4", "Actividad 5"]
    )

def componentes_calificaciones(frame_tab, titulo, calificacion):
    frame_item = CTkFrame(frame_tab, fg_color="#cabece")
    frame_item.pack(fill="x", padx=0, pady=0)

    CTkLabel(
        frame_item,
        text=titulo,
        anchor="w",
        justify="left",
        text_color="black",
        font=("Arial Rounded MT Bold", 14)
    ).pack(side="left", padx=10, pady=6)

    CTkLabel(
        frame_item,
        text=calificacion,
        anchor="e",
        justify="right",
        text_color="black",
        font=("Arial Rounded MT Bold", 14)
    ).pack(side="right", padx=10, pady=6)

def bloque_calificaciones_unidad(frame_tab, titulo_unidad, items):
    frame_bloque = CTkFrame(frame_tab, fg_color="white")
    frame_bloque.pack(fill="x", padx=5, pady=0)

    CTkLabel(
        frame_bloque,
        text=f"     {titulo_unidad}",
        anchor="w",
        justify="left",
        text_color="white",
        fg_color="#715a72",
        font=("Arial Rounded MT Bold", 25)
    ).pack(fill="x", padx=0, pady=0)

    frame_lista = CTkFrame(frame_bloque, fg_color="white")
    frame_lista.pack(fill="x", padx=0, pady=0)

    for titulo, calificacion in items:
        componentes_calificaciones(frame_lista, titulo, calificacion)

def Calificaciones(tab):
    limpiar_frame(tab)
    CTkLabel(
        tab,
        text="Calificaciones",
        font=("Arial Rounded MT Bold", 20),
        text_color="black"
    ).pack(pady=10)

    frame_calificaciones = CTkFrame(tab, fg_color="white")
    frame_calificaciones.pack(fill="x", padx=5, pady=0)

    bloque_calificaciones_unidad(
        frame_calificaciones,
        "Unidad 1",
        [
            ("Actividad 1", "90"),
            ("Actividad 2", "85"),
            ("Actividad 3", "95")
        ]
    )
    bloque_calificaciones_unidad(
        frame_calificaciones,
        "Unidad 2",
        [
            ("Actividad 4", "88"),
            ("Actividad 5", "92")
        ]
    )

def opciones_menu(tabview):
    opcion_activa = tabview.get()

    if opcion_activa == "Anuncios":
        Anuncios(tabview.tab("Anuncios"))
    elif opcion_activa == "Documentos":
        Documentacion(tabview.tab("Documentos"))
    elif opcion_activa == "Actividades":
        Actividades(tabview.tab("Actividades"))
    elif opcion_activa == "Calificaciones":
        Calificaciones(tabview.tab("Calificaciones"))


def Info_Grupo(frame_contenido, materia="Matematicas", profesor="Maestro 1", nombre_grupo="Grupo A"):
    limpiar_frame(frame_contenido)

    frame_info_general = CTkFrame(frame_contenido, fg_color="#cabece")
    frame_info_general.pack(fill="x", padx=5, pady=(5, 2))

    CTkLabel(
        frame_info_general,
        text=f"{materia}",
        text_color="black",
        anchor="w",
        justify="left",
        font=("Arial Rounded MT Bold", 30)
    ).pack(fill="x", anchor="w", pady=2, padx=10)
    CTkLabel(
        frame_info_general,
        text=f"{profesor}",
        text_color="black",
        anchor="w",
        justify="left",
        font=("Arial Rounded MT Bold", 20)
    ).pack(fill="x", anchor="w", pady=2, padx=10)
    CTkLabel(
        frame_info_general,
        text=f"{nombre_grupo}",
        text_color="black",
        anchor="w",
        justify="left",
        font=("Arial Rounded MT Bold", 20)
    ).pack(fill="x", anchor="w", pady=2, padx=10)

    opciones_grupo = CTkTabview(        
        frame_contenido,
        width=1200,
        height=700,
        fg_color="white",
        command=lambda: opciones_menu(opciones_grupo)
    )
    opciones_grupo.pack(pady=0, padx=0)
    opciones_grupo.add("Anuncios")
    opciones_grupo.add("Documentos")
    opciones_grupo.add("Actividades")
    opciones_grupo.add("Calificaciones")

    opciones_grupo._segmented_button.configure(
                                    width=150,
                                    font=("Arial Rounded MT Bold",16),
                                        fg_color="#715a72",
                                        selected_color="#5e485f",
                                        selected_hover_color="#5e485f",
                                    unselected_hover_color="#715a72",
                                    )
    opciones_menu(opciones_grupo)
