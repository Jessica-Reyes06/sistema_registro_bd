import customtkinter
from customtkinter import *


def return_to_switch(event: None) -> None:
    switch.focus_set()


def execute_switch(event: None) -> None:
    switch.toggle()  # QUE ES TOGGLE?


def go_to_user(event: None) -> None:
    user_entry.focus_set()


def go_to_password(event: None) -> None:
    password_entry.focus_set()


def return_to_user(event: None) -> None:
    user_entry.focus_set()


def return_to_password(event: None) -> None:
    password_entry.focus_set()


def go_to_button(event: None) -> None:
    login_button.focus_set()


def execute_login_button(event: None) -> None:
    login_button.invoke()  # QUE ES INVOKE?


def on_focus_in(event: None) -> None:
    login_button.configure(fg_color=("gray80", "gray25"),
                           border_width=2,
                           border_color="#ffffff")


def on_focus_out(event: None) -> None:
    login_button.configure(fg_color=("gray80", "gray25"),
                           border_width=0)


def validate_login() -> None:
    control_number = user_entry.get()
    password = password_entry.get()
    if control_number.strip() == "" or password.strip() == "":
        message.configure(text="Por favor, complete ambos campos.",
                          fg_color=("#FFF4CC", "#5A4B00"),
                          text_color=("#9A6B00", "#FFE8A3"))
    elif control_number == "123" and password == "asd":
        message.configure(text="¡Inicio de sesión exitoso!",
                          fg_color=("#DDF7E3", "#1F6F3C"),
                          text_color=("#1F6F3C", "#9EF0B0"))
    else:
        message.configure(text="Usuario o contraseña incorrectos.",
                          fg_color=("#FCE1E1", "#8A1F1F"),
                          text_color=("#B00020", "#FFB3B3"))


def switch_event():
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")


customtkinter.set_appearance_mode("Light")

app = CTk()

window_width = 420
window_height = 340

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

app.geometry(f"{window_width}x{window_height}+{x}+{y}")

app.title("Login")

switch_var = customtkinter.StringVar(value="off")
switch = customtkinter.CTkSwitch(app,
                                 text="Modo oscuro",
                                 command=switch_event,
                                 variable=switch_var,
                                 onvalue="on",
                                 offvalue="off")
switch.pack(pady=10)

user = CTkLabel(app,
                text="Numero de control",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                corner_radius=12,
                width=200)
user.pack(pady=10)

user_entry = CTkEntry(app,
                      placeholder_text="Ingrese su numero de control",
                      width=200)
user_entry.pack(pady=10)

password = CTkLabel(app,
                    text="Contraseña",
                    fg_color="transparent",
                    text_color=("gray10", "gray90"),
                    corner_radius=12,
                    width=200)
password.pack(pady=10)

password_entry = CTkEntry(app,
                          placeholder_text="Ingrese su contraseña",
                          show="*",
                          width=200)
password_entry.pack(pady=10)

login_button = CTkButton(app,
                         text="Iniciar sesión",
                         fg_color=("gray80", "gray25"),
                         hover_color=("gray70", "gray35"),
                         text_color=("gray10", "gray90"),
                         command=validate_login,
                         width=200)
login_button.pack(pady=20)

message = CTkLabel(app,
                   text="")
message.pack(pady=10)

# Bind

switch.bind("<Return>", execute_switch)
switch.bind("<Down>", go_to_user)
switch.bind("<KP_Enter>", execute_switch)

user_entry.bind("<Up>", return_to_switch)
user_entry.bind("<Return>", go_to_password)  # QUE ES .BIND?
user_entry.bind("<Down>", go_to_password)

password_entry.bind("<Up>", return_to_user)
password_entry.bind("<BackSpace>", return_to_user)

password_entry.bind("<Return>", go_to_button)
password_entry.bind("<Down>", go_to_button)

login_button.bind("<Up>", return_to_password)
login_button.bind("<BackSpace>", return_to_password)
login_button.bind("<KP_Enter>", execute_login_button)
login_button.bind("<Return>", execute_login_button)
login_button.bind("<FocusIn>", on_focus_in)
login_button.bind("<FocusOut>", on_focus_out)

# Foco inicial

app.after(100, user_entry.focus_set)  # QUE ES FOCUS_SET?

app.mainloop()