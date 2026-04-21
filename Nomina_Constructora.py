
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime
from abc import ABC, abstractmethod
# Severo codigo

class Usuario():
    def __init__(self, nombre, id, genero, salario_dia, cargo, dias, fecha):
        self.nombre = nombre
        self.identificacion = id
        self.genero = genero
        self.cargo = cargo
        self.salario_dia = salario_dia
        self.dias = dias
        self.fecha = fecha

    def calcular_total(self):
        valor_dia = empleos.get(self.cargo, 0)
        return valor_dia * self.dias

        
 #Diccionario de cargo / precio respectivo.  
empleos = {
    "Servicios Generales":40000,
    "Administrativo":50000,
    "Electricista":60000,
    "Mecanico":80000,
    "Soldador":90000
}
# def constantes ( autos/nombre ) 
autor_app ="Juan David Cruz"
nombre_app ="Gestion de Empleados"

#Verificar clave 
def verificar_inicio():
    clave= entrada_clave.get().strip()

    if clave == "4682":
        ventana_inicio.destroy()
        abrir_registro()
    else:
        messagebox.showerror("Error","Contraseña incorrecta.")
        entrada_clave.delete(0, tk.END)

def alternar_clave():
    if entrada_clave.cget("show") == "*":
        entrada_clave.config(show="") 
    else:
        entrada_clave.config(show="*")

 # Ventana de inicio 
ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio Sesion")
ventana_inicio.geometry("360x220")
ventana_inicio.resizable(False, False)

tk.Label(
    ventana_inicio,
    text=f"Aplicacion: {nombre_app}",
    font=("Arial",11,"bold")
).pack(pady=10)

tk.Label(
    ventana_inicio,
    text=f"Autor:{autor_app}",
    font=("Arial",11)
).pack()

tk.Label(
    ventana_inicio,
    text="Contraseña"
).pack(pady=10)

entrada_clave = tk.Entry(ventana_inicio, show="*", width=25)
entrada_clave.pack()

tk.Checkbutton(
    ventana_inicio,
    text="Mostrar Clave",
    command = alternar_clave
).pack(pady=5)

tk.Button(
    ventana_inicio,
    text="Ingresar",
    width=12,
    command=verificar_inicio
).pack(pady=10)



# Funciones de registro     

def actualizar_salario(seleccion):
     if seleccion in empleos:
        salariodia = empleos [seleccion]
        caja_salariodia.config(state="normal")
        caja_salariodia.delete(0, tk.END)
        caja_salariodia.insert(0, str(salariodia))
        caja_salariodia.config(state="readonly")

def guardar_registro():
    global empleado_guardado
 
    try:
        empleado = Usuario(
          id =caja_id.get().strip(),
          nombre=caja_nombre.get().strip(),
          genero = variable_genero.get(),
          cargo = variable_cargo.get(),
          dias=int(caja_dias.get().strip()),
          salario_dia=float(caja_salariodia.get().strip()),
          fecha=datetime.now().strftime("%d/%m/%Y")
         )

        empleado_guardado = empleado
        caja_fecha.config(state ="normal")
        caja_fecha.delete(0, tk.END)
        caja_fecha.insert(0, empleado.fecha)
        caja_fecha.config(state="readonly")
        
        messagebox.showinfo("Exito","Registro guardado correctamente")

    except ValueError as e:
        messagebox.showerror("Error",str(e))
     
def mostrar_reporte():
    global empleado_guardado
    
    if empleado_guardado is None:
        messagebox.showwarning("Atencion","Primero debe guardar el registro.")
        return
    
    total = empleado_guardado.calcular_total()

    ventana_reporte = tk.Toplevel()
    ventana_reporte.title("Reporte")
    ventana_reporte.geometry("420x360")
    ventana_reporte.resizable(False, False)

    texto_reporte = (
        f"Nombre: {empleado_guardado.nombre}\n"
        f"ID:{empleado_guardado.identificacion}\n"
        f"Género:{empleado_guardado.genero}\n"
        f"Días Laborados:{empleado_guardado.dias}\n"
        f"Fecha de Registro:{empleado_guardado.fecha}\n"
        f"Valor día trabajo: ${empleado_guardado.salario_dia:,.0f}\n"
        f"Total a Pagar: ${total:,.0f}\n"
    )

    tk.Label(
        ventana_reporte,    
        text="Reporte",
        font=("Arial",14, "bold"),
    ).pack(pady=10)

    tk.Label(
        ventana_reporte,
        text=texto_reporte,
        justify="left",
        font=("Arial",11),
    ).pack(padx=20, pady=10)

    tk.Button(
        ventana_reporte,
        text="Regresar",
        width=12,
        command=ventana_reporte.destroy
    ).pack(pady=15)

def salir_aplicacion():
    respuesta = messagebox.askyesno("Confirmar salida")
    if respuesta:
       ventana_registro.destroy()

def limpiar_campos():
    caja_id.delete(0, tk.END)
    caja_nombre.delete(0, tk.END)
    caja_dias.delete(0, tk.END)

    variable_cargo.set("Seleccione un cargo")

    caja_salariodia.config(state="normal")
    caja_salariodia.delete(0, tk.END)
    caja_salariodia.config(state="readonly")

    caja_fecha.config(state="normal")
    caja_fecha.delete(0,tk.END)
    caja_fecha.config(state="readonly")

def abrir_registro():
    global ventana_registro
    global caja_nombre, caja_id, caja_dias, caja_salariodia
    global variable_cargo , variable_genero , caja_fecha 

    ventana_registro = tk.Tk()
    ventana_registro.title("Registro de empleados")
    ventana_registro.geometry("420x420")
    ventana_registro.resizable(False, False)

    tk.Label (ventana_registro, text="Cedula").place(x=30, y=30)
    caja_id = tk.Entry(ventana_registro, width=28)
    caja_id.place (x=170, y=30)
    
    tk.Label (ventana_registro, text="Nombre completo").place(x=30, y=70)
    caja_nombre = tk.Entry(ventana_registro, width=28)
    caja_nombre.place(x=170, y=70)
    
    tk.Label(ventana_registro, text="Género").place(x=30, y=110)
    variable_genero = tk.StringVar()
    variable_genero.set("Masculino")  # valor por defecto
    tk.Radiobutton(ventana_registro, text="Masculino", variable=variable_genero, value="Masculino").place(x=170, y=110)
    tk.Radiobutton(ventana_registro, text="Femenino", variable=variable_genero, value="Femenino").place(x=270, y=110)

    tk.Label(ventana_registro, text="Cargo laboral").place(x=30, y=150)
    variable_cargo = tk.StringVar()
    variable_cargo.set("Seleccione un cargo")
    menu_cargo = tk.OptionMenu(ventana_registro, variable_cargo, *empleos.keys(),command=actualizar_salario)
    menu_cargo.config(width=20)
    menu_cargo.place(x=170, y=145)
 
    tk.Label(ventana_registro, text="Salario día").place(x=30, y=190)
    caja_salariodia = tk.Entry(ventana_registro, width=30, state="readonly")
    caja_salariodia.place(x=170, y=190)

    tk.Label(ventana_registro, text="Dias laborados").place(x=30, y=230)
    caja_dias = tk.Entry(ventana_registro, width=28)
    caja_dias.place(x=170, y=230)

    tk.Label (ventana_registro, text="Fecha de registro").place(x=30, y=250)
    caja_fecha = tk.Entry(ventana_registro,  width=30, state="readonly")
    caja_fecha.place(x=170, y=250)

    tk.Button(
       ventana_registro,
       text="Guardar Registro",
       width=16,
       command=guardar_registro
    ).place(x=30, y=320)
  
    tk.Button(
       ventana_registro,
       text = "Calcular Nomina/ Mostrar reporte",
       width=26,
       command=mostrar_reporte
    ).place(x=160, y=320)
    
    tk.Button(
       ventana_registro,
       text="Limpiar",
       width=10,
       command= limpiar_campos
    ).place(x=100, y=360)

    tk.Button(
       ventana_registro,
       text="Salir",
       width=10,
       command=salir_aplicacion
    ).place(x=220, y=360)

    ventana_registro.mainloop()
ventana_inicio.mainloop()
