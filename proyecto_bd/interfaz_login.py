from customtkinter import *
from funciones_login import mostrar_ocultar, generar_mensaje_login, cambiar_modo

set_appearance_mode("light")
set_default_color_theme("blue")

ventana_login = CTk()
ventana_login.title("Login")
ventana_login.geometry("300x380")

frame = CTkFrame(ventana_login)
frame.pack(fill="both", expand=True, padx=20, pady=20)

switch_var = StringVar(value="off")
switch = CTkSwitch(ventana_login,
                                            text="Modo oscuro",
                                            command=cambiar_modo,
                                            variable=switch_var,
                                            onvalue="on",
                                            offvalue="off")
switch.pack(pady=10)

label_usuario = CTkLabel(frame, text="Usuario:")
label_usuario.pack(anchor="w")

entry_usuario = CTkEntry(frame, width=220)
entry_usuario.pack(pady=(0, 10))

label_contra = CTkLabel(frame, text="Contraseña:")
label_contra.pack(anchor="w")

entry_contra = CTkEntry(frame, width=220, show="*")
entry_contra.pack(pady=(0, 10))

# Botón para mostrar/ocultar contraseña
boton_contra = CTkButton(frame, text="Mostrar")
boton_contra.pack(pady=(0, 5))

boton_contra.configure(command=lambda: mostrar_ocultar(entry_contra, boton_contra))

# Label para mensajes de validación (vacío al inicio)
label_mensaje = CTkLabel(frame, text="")
label_mensaje.pack(pady=(5, 0), fill="x")


def on_login():
    usuario = entry_usuario.get()
    contrasena = entry_contra.get()

    mensaje = generar_mensaje_login(usuario, contrasena)

    label_mensaje.configure(
        text=mensaje["texto"],
        fg_color=mensaje["fg_color"],
        text_color=mensaje["text_color"],
    )

    if mensaje["exitoso"] is True:
        # Cerrar ventana de login
        ventana_login.destroy()

        # Abrir la plataforma según el rol
        if mensaje["rol"] == "administrador":
            from main_administrador import iniciar_admin
            iniciar_admin()
        elif mensaje["rol"] == "alumno":
            from Inicio_Alumnos import iniciar_alumno
            iniciar_alumno()
    

boton_login = CTkButton(frame, text="Iniciar sesión", command=on_login)
boton_login.pack(pady=(5, 0))

ventana_login.mainloop()

