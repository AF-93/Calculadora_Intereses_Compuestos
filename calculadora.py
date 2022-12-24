## Importamos lo que necesitaremos de la librería Tkiner.
import tkinter as tk
from tkinter import messagebox

## Armamos la ventana donde se ingresarán los datos.
ventana = tk.Tk()
ventana.geometry('640x360')
ventana.title('Calculadora de Intereses Compuestos')
ventana.configure(bg='steel blue')
tk.Label(text='Valor Inicial',bg='lightblue',font=('Arial Black',13)).pack(fill='both')

current = tk.Entry(justify='center',font=('Arial',13))
current.pack(pady=10)

tk.Label(text='Adicion Anual',bg='lightblue',font=('Arial Black',13)).pack(pady=5,fill='x')

anual_add = tk.Entry(justify='center',font=('Arial',13))
anual_add.pack(pady=10)

tk.Label(text='Plazo (en años)',bg='lightblue',font=('Arial Black',13)).pack(pady=5,fill='x')

years = tk.Entry(justify='center',font=('Arial',13))
years.pack(pady=10)

tk.Label(text='Intereses Anuales (en %)',bg='lightblue',font=('Arial Black',13)).pack(pady=5,fill='x')

interest_rate = tk.Entry(justify='center',font=('Arial',13))
interest_rate.pack(pady=10)

## Definimos la funcion que calculará los intereses compuestos.

def intereses_compuestos():

    ## Guardamos en variables los datos ingresador por el usuario.  
    
    c = int(current.get())
    a = int(anual_add.get())
    y = int(years.get())
    r = int(interest_rate.get())
    result=c
    
    ## Realizamos un ciclo 'for' que se repite la cantidad de veces equivalente a los años que se quieran calcular los intereses combinados.    
    
    for i in range(y):
        result=result+a
        result=result+(result*r/100)

    ## Ventana emergente con el resultado

    tk.messagebox.showinfo(message=f'Generarias ${round(result,2)}',title='Resultados')

## El botón abajo llama a la funcion antes definida.

calcular=tk.Button(text='Calcular Intereses' ,command= intereses_compuestos,font=('Arial Black',10)).pack(pady=5)

ventana.mainloop()