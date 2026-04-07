from customtkinter import *
from PIL import Image
from tkcalendar import Calendar
import datetime
import Grupos_Alumno as grupos_alumno

ventana = None
frame_contenido = None

#------------------FUNCIONES----------------
def mostrar_maximizada():
    ventana.state("zoomed")
    ventana.deiconify()

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def crear_icono_clases(frame_clases, columna, fila, nombre_grupo, maestro, materia, frame_contenido):
    frame_grupo_ind=CTkFrame(frame_clases,
                            fg_color="white")
    frame_grupo_ind.grid(row=fila, column=columna, padx=5, pady=5)     
    img_grupo = CTkImage(
        light_image=Image.open("carpeta_iconos/iconos_alumnos/archivo-de-carpetas.png"),
        size=(90, 90)
    )
    CTkButton(frame_grupo_ind,
                text=nombre_grupo,
                width=160,
                height=150,
                fg_color="#715a72",
                hover_color="#5e485f",
                text_color="white",
                image=img_grupo,
                compound="bottom",
                font=("Arial Rounded MT Bold", 18),
                command=lambda: grupos_alumno.Info_Grupo(frame_contenido)
                ).grid(row=0, column=0, padx=10, pady=5)
    CTkLabel(frame_grupo_ind,
                text=f"{materia}\n{maestro}",
                text_color="black",
                justify="left",
                font=("Arial Rounded MT Bold", 20)
                ).grid(row=1, column=0, padx=10, pady=(0,5), sticky="w")
    	
def menu_opcioneas(frame_menu):
    CTkLabel(frame_menu, 
        text="Nombre del Sistema", 
        text_color="black",
        font=("Arial Rounded MT Bold", 15)
        ).pack(pady=10, padx=20)

    frame_usuario=CTkFrame(frame_menu,
                        width=250,
                        fg_color="#cabece")
    frame_usuario.pack(pady=(5,10), padx=20)

    img_usuario=CTkImage(
        light_image=Image.open("carpeta_iconos/iconos_alumnos/avatar.png"),
        size=(100, 100)
    )
    CTkLabel(frame_usuario,
            text="",
            text_color="black",
            image=img_usuario,
            font=("Arial Rounded MT Bold", 15)
            ).pack(pady=10, padx=10, anchor="center")
    CTkLabel(frame_usuario,
            text="Nombre del usuario",
            text_color="black",
            compound="left",
            font=("Arial Rounded MT Bold", 22)
            ).pack(pady=10, padx=10)
    CTkLabel(frame_usuario,
            text="Numero de control",
            text_color="black",
            compound="left",
            font=("Arial Rounded MT Bold", 20)
            ).pack(pady=(0,10), padx=10)

    frame_opciones=CTkFrame(frame_menu,
                        width=250,
                        height=400,
                        fg_color="#cabece")
    frame_opciones.pack(pady=10, padx=20)

    crear_opciones_menu(frame_opciones,"      Inicio",img_hogar,5,lambda: Mis_Clases(frame_contenido))
    crear_opciones_menu(frame_opciones,"      Calendario",img_calendario,5,lambda: calendario(frame_contenido))
    crear_opciones_menu(frame_opciones,"      Tareas Pendientes",img_pendiente,5,lambda: tareas_pendientes(frame_contenido))
    crear_opciones_menu(frame_opciones,"      Notificaciones",img_notificaciones,5,lambda: notificaciones(frame_contenido))
    crear_opciones_menu(frame_opciones,"      Cerrar Sesión",img_cerrar_sesion,260,lambda: ventana.destroy())
    
def crear_opciones_menu(frame,texto,imagen,y,funcion=None):
    boton = CTkButton(frame,
                        text=texto,
                        width=300,
                        fg_color="#715a72",
                        hover_color="#5e485f",
                        #selected_color="#715a72",
                        text_color="white",
                        image=imagen,
                        anchor="w",
                        font=("Arial Rounded MT Bold", 15),
                        command=funcion
                        )
    boton.pack(pady=(y, 10), padx=10)

def crear_icono(ruta):
    imagen = CTkImage(
        light_image=Image.open(ruta),
        size=(20, 20)
    )
    return imagen

def Mis_Clases(frame_contenido):
    limpiar_frame(frame_contenido)

    CTkLabel(
        frame_contenido, 
		text="Mis Clases", 
		text_color="black",
		anchor="w",
		font=("Arial Rounded MT Bold", 30)
    ).pack(fill="x", anchor="w", pady=10, padx=10)

    frame_clases = CTkScrollableFrame(
                            frame_contenido,
                            fg_color="white", 
                            width=1200, 
                            height=700,
                            scrollbar_fg_color="white",
                            scrollbar_button_color="white",
                            scrollbar_button_hover_color="white"
                            )
    frame_clases.pack(pady=(5,10), padx=10, anchor="w")
    frame_clases.pack_propagate(False)
    if hasattr(frame_clases, "_scrollbar"):
        frame_clases._scrollbar.configure(width=0)

    crear_icono_clases(frame_clases, 0, 0, "Grupo A", "Maestro 1", "Matemáticas", frame_contenido)
    #Solo se podran poner un maximo de 6 clases por fila

def calendario(frame):
    limpiar_frame(frame)

    CTkLabel(
        frame, 
		text="Calendario", 
		text_color="black",
		anchor="w",
		font=("Arial Rounded MT Bold", 30)
    ).pack(fill="x", anchor="w", pady=10, padx=10)

    frame_calendario = CTkFrame(frame, fg_color="white", width=1200, height=700)
    frame_calendario.pack(pady=20, padx=20)
    frame_calendario.pack_propagate(False)

    hoy = datetime.date.today()

    cal = Calendar(
        frame_calendario,
        selectmode="day",
        year=hoy.year,
        month=hoy.month,
        day=hoy.day,
        font=("Arial Rounded MT Bold", 14),
        background="#715a72",
        foreground="white",
        headersbackground="#5e485f",
        headersforeground="white",
        normalbackground="#cabece",
        normalforeground="black",
        weekendbackground="#cabece",
        weekendforeground="black",
        selectbackground="#5e485f",
        selectforeground="white",
        bordercolor="#715a72"
    )
    cal.pack(fill="both", expand=True, padx=10, pady=10)
    
    return cal

def tareas_pendientes(frame):
    limpiar_frame(frame)

    CTkLabel(
        frame, 
		text="Tareas Pendientes", 
		text_color="black",
		anchor="w",
		font=("Arial Rounded MT Bold", 30)
    ).pack(fill="x", anchor="w", pady=10, padx=10)

def notificaciones(frame):
    limpiar_frame(frame)

    CTkLabel(
        frame, 
        text="Notificaciones", 
        text_color="black",
        anchor="w",
        font=("Arial Rounded MT Bold", 30)
    ).pack(fill="x", anchor="w", pady=10, padx=10)  





def iniciar_alumno():
    global ventana, frame_contenido, img_hogar, img_calendario, img_notificaciones, img_pendiente, img_cerrar_sesion, img_usuario

    ventana = CTk(fg_color="white")
    ventana.title("Inicio Alumnos")
    ventana.withdraw()
    ventana.after(0, mostrar_maximizada)

    img_hogar = crear_icono("carpeta_iconos/iconos_alumnos/hogar.png")
    img_calendario = crear_icono("carpeta_iconos/iconos_alumnos/calendario.png")
    img_notificaciones = crear_icono("carpeta_iconos/iconos_alumnos/reloj.png")
    img_pendiente = crear_icono("carpeta_iconos/iconos_alumnos/lista.png")
    img_cerrar_sesion = crear_icono("carpeta_iconos/iconos_alumnos/salida.png")
    img_usuario = crear_icono("carpeta_iconos/iconos_alumnos/avatar.png")

    frame_menu= CTkFrame(ventana, 
                        width=300,
                        corner_radius=0, 
                        fg_color="#cabece")
    frame_menu.pack(side="left", fill="y")
    frame_menu.pack_propagate(False)

    frame_contenido=CTkFrame(ventana,
                        fg_color="white")
    frame_contenido.pack(side="left", pady=10, padx=20, fill="both", expand=True)

    menu_opcioneas(frame_menu)
    Mis_Clases(frame_contenido)

    ventana.mainloop()


if __name__ == "__main__":
    iniciar_alumno()
