import tkinter as tk
from tkinter import Label, PhotoImage, ttk

# Función de conversión para las unidades del SI
def convertir(combo_origen, combo_destino, entry_valor, label_resultado, conversiones):
    unidad_origen = combo_origen.get()
    unidad_destino = combo_destino.get()
    valor = float(entry_valor.get())
    
    try:
        resultado = valor * conversiones[unidad_origen][unidad_destino]
        label_resultado.config(text=f'{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}')
    except KeyError:
        label_resultado.config(text='Conversión no válida')

# Función para la conversión de prefijos
def convertir_prefijo():
    prefijo_origen = combo_prefijo_origen.get()
    prefijo_destino = combo_prefijo_destino.get()
    valor = float(entry_valor_prefijo.get())
    
    # Tabla de prefijos
    prefijos = {
        'T': 1e10, 'G': 1e9, 'M': 1e6, 'k': 1e3, 'h': 1e2, 'da': 10,
        '': 1, 'd': 1e-1, 'c': 1e-2, 'm': 1e-3, 'µ': 1e-6, 'n': 1e-9, 'p': 1e-10
    }
    
    try:
        resultado = valor * (prefijos[prefijo_origen] / prefijos[prefijo_destino])
        label_resultado_prefijo.config(text=f'{valor} {prefijo_origen} = {resultado:.4f} {prefijo_destino}')
    except KeyError:
        label_resultado_prefijo.config(text='Conversión no válida')

ventana = tk.Tk()
ventana.title('Calculadora de Conversión de Unidades')
ventana.config(bg="purple")
ventana.geometry("700x600")

# Estilo para aumentar el tamaño de las flechas del Combobox
style = ttk.Style()
style.configure('TCombobox', arrowsize=70)  # Aumenta el tamaño de las flechas


# Diccionarios de conversiones
conversiones_longitud = {
    'm': {'m': 1, 'cm': 100, 'ft': 3.28084, 'yard': 1.09361, 'km': 0.001, 'mile': 0.000621371},
    'cm': {'m': 0.01, 'cm': 1, 'ft': 0.0328084, 'yard': 0.0109361, 'km': 1e-5, 'mile': 6.2137e-6},
    'ft': {'m': 0.3048, 'cm': 30.48, 'ft': 1, 'yard': 0.333333, 'km': 0.0003048, 'mile': 0.000189394},
    'yard': {'m': 0.9144, 'cm': 91.44, 'ft': 3, 'yard': 1, 'km': 0.0009144, 'mile': 0.000568182},
    'km': {'m': 1000, 'cm': 100000, 'ft': 3280.84, 'yard': 1093.61, 'km': 1, 'mile': 0.621371},
    'mile': {'m': 1609.34, 'cm': 160934, 'ft': 5280, 'yard': 1760, 'km': 1.60934, 'mile': 1}
}

conversiones_peso = {
    'kg': {'kg': 1, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
    'g': {'kg': 0.001, 'g': 1, 'lb': 0.00220462, 'oz': 0.035274},
    'lb': {'kg': 0.453592, 'g': 453.592, 'lb': 1, 'oz': 16},
    'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625, 'oz': 1}
}

conversiones_volumen = {
    'L': {'L': 1, 'mL': 1000, 'gal': 0.264172, 'fl oz': 33.814, 'pulgada³': 61.0237, 'pie³': 0.0353147, 'm³': 0.001, 'cm³': 1000},
    'mL': {'L': 0.001, 'mL': 1, 'gal': 0.000264172, 'fl oz': 0.033814, 'cm³': 1, 'm³': 1e-6, 'pie³': 3.5310e-5, 'pulgada³': 0.0610237},
    'gal': {'L': 3.78541, 'mL': 3785.41, 'gal': 1, 'fl oz': 108, 'pulgada³': 231, 'pie³': 0.133681, 'm³': 0.00378541, 'cm³': 3785.41},
    'fl oz': {'L': 0.0295735, 'mL': 29.5735, 'gal': 0.0078105, 'fl oz': 1, 'cm³': 29.5735, 'm³': 2.9574e-5, 'pie³': 0.00104438, 'pulgada³': 1.80469},
    'm³ ': {'pie³': 35.3147, 'pulgada3': 61023.7, 'cm³': 1000000, 'gal': 264.172, 'fl oz': 33814, 'L': 1000, 'mL': 1e6, 'm³': 1},
    'cm³': {'m³': 1e-6, 'pie³': 3.5310e-5, 'pulgada': 0.0610237, 'gal': 0.000264172, 'fl oz': 0.033814, 'L': 0.001, 'mL': 1, 'cm³': 1},
    'pie³': {'cm³': 283016.8, 'm³': 0.0283168, 'pulgada3': 1728, 'gal': 7.48052, 'fl oz': 957.506, 'L': 28.3168, 'mL': 28316.8, 'pie³': 1},
    'pulgada³': {'pie³': 0.000578704, 'm³': 1.6387e-5, 'cm³': 16.3871, 'gal': 0.004329, 'fl oz': 0.554113, 'L': 0.0163871, 'mL': 16.3871, 'pulgada³': 1}
}

conversiones_energia = {
    'J': {'J': 1, 'cal': 0.239006, 'kWh': 2.77778e-7},
    'cal': {'J': 4.184, 'cal': 1, 'kWh': 1.16222e-6},
    'kWh': {'J': 3600000, 'cal': 860420, 'kWh': 1}
}

conversiones_fuerza = {
    'N': {'N': 1, 'kgf': 0.101972, 'lbf': 0.224809},
    'kgf': {'N': 9.80665, 'kgf': 1, 'lbf': 2.20462},
    'lbf': {'N': 4.44822, 'kgf': 0.453592, 'lbf': 1}
}

# Marco para la conversión de unidades del SI (Longitud)
Longitud = ttk.LabelFrame(ventana, text='Conversión de Unidades (Longitud)')
Longitud.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(Longitud, text='Valor:').grid(row=0, column=0)
entry_valorL = ttk.Entry(Longitud)
entry_valorL.grid(row=0, column=1)

ttk.Label(Longitud, text='De:').grid(row=1, column=0)
combo_origenL = ttk.Combobox(Longitud, values=['m', 'cm', 'ft', 'yard', 'km', 'mile'])
combo_origenL.grid(row=1, column=1)

ttk.Label(Longitud, text='A:').grid(row=2, column=0)
combo_destinoL = ttk.Combobox(Longitud, values=['m', 'cm', 'ft', 'yard', 'km', 'mile'])
combo_destinoL.grid(row=2, column=1)

boton_convertirL = ttk.Button(Longitud, text='Convertir', command=lambda: convertir(combo_origenL, combo_destinoL, entry_valorL, label_resultadoL, conversiones_longitud))
boton_convertirL.grid(row=3, column=0, columnspan=2)

label_resultadoL = ttk.Label(Longitud, text='')
label_resultadoL.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Peso)
Peso = ttk.LabelFrame(ventana, text='Conversión de Unidades (Peso)')
Peso.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(Peso, text='Valor:').grid(row=0, column=0)
entry_valorP = ttk.Entry(Peso)
entry_valorP.grid(row=0, column=1)

ttk.Label(Peso, text='De:').grid(row=1, column=0)
combo_origenP = ttk.Combobox(Peso, values=['kg', 'g', 'lb', 'oz'])
combo_origenP.grid(row=1, column=1)

ttk.Label(Peso, text='A:').grid(row=2, column=0)
combo_destinoP = ttk.Combobox(Peso, values=['kg', 'g', 'lb', 'oz'])
combo_destinoP.grid(row=2, column=1)

boton_convertirP = ttk.Button(Peso, text='Convertir', command=lambda: convertir(combo_origenP, combo_destinoP, entry_valorP, label_resultadoP, conversiones_peso))
boton_convertirP.grid(row=3, column=0, columnspan=2)

label_resultadoP = ttk.Label(Peso, text='')
label_resultadoP.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Volumen)
Volumen = ttk.LabelFrame(ventana, text='Conversión de Unidades (Volumen)')
Volumen.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(Volumen, text='Valor:').grid(row=0, column=0)
entry_valorV = ttk.Entry(Volumen)
entry_valorV.grid(row=0, column=1)

ttk.Label(Volumen, text='De:').grid(row=1, column=0)
combo_origenV = ttk.Combobox(Volumen, values=['L', 'mL', 'gal', 'fl oz', 'm³', 'cm³', 'pie³', 'pulgada³'])
combo_origenV.grid(row=1, column=1)

ttk.Label(Volumen, text='A:').grid(row=2, column=0)
combo_destinoV = ttk.Combobox(Volumen, values=['L', 'mL', 'gal', 'fl oz', 'm³', 'cm³', 'pie³', 'pulgada³'])
combo_destinoV.grid(row=2, column=1)

boton_convertirV = ttk.Button(Volumen, text='Convertir', command=lambda: convertir(combo_origenV, combo_destinoV, entry_valorV, label_resultadoV, conversiones_volumen))
boton_convertirV.grid(row=3, column=0, columnspan=2)

label_resultadoV = ttk.Label(Volumen, text='')
label_resultadoV.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Energía)
Energia = ttk.LabelFrame(ventana, text='Conversión de Unidades (Energía)')
Energia.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(Energia, text='Valor:').grid(row=0, column=0)
entry_valorE = ttk.Entry(Energia)
entry_valorE.grid(row=0, column=1)

ttk.Label(Energia, text='De:').grid(row=1, column=0)
combo_origenE = ttk.Combobox(Energia, values=['J', 'cal', 'kWh'])
combo_origenE.grid(row=1, column=1)

ttk.Label(Energia, text='A:').grid(row=2, column=0)
combo_destinoE = ttk.Combobox(Energia, values=['J', 'cal', 'kWh'])
combo_destinoE.grid(row=2, column=1)

boton_convertirE = ttk.Button(Energia, text='Convertir', command=lambda: convertir(combo_origenE, combo_destinoE, entry_valorE, label_resultadoE, conversiones_energia))
boton_convertirE.grid(row=3, column=0, columnspan=2)

label_resultadoE = ttk.Label(Energia, text='')
label_resultadoE.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Fuerza)
Fuerza = ttk.LabelFrame(ventana, text='Conversión de Unidades (Fuerza)')
Fuerza.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(Fuerza, text='Valor:').grid(row=0, column=0)
entry_valorF = ttk.Entry(Fuerza)
entry_valorF.grid(row=0, column=1)

ttk.Label(Fuerza, text='De:').grid(row=1, column=0)
combo_origenF = ttk.Combobox(Fuerza, values=['N', 'kgf', 'lbf'])
combo_origenF.grid(row=1, column=1)

ttk.Label(Fuerza, text='A:').grid(row=2, column=0)
combo_destinoF = ttk.Combobox(Fuerza, values=['N', 'kgf', 'lbf'])
combo_destinoF.grid(row=2, column=1)

boton_convertirF = ttk.Button(Fuerza, text='Convertir', command=lambda: convertir(combo_origenF, combo_destinoF, entry_valorF, label_resultadoF, conversiones_fuerza))
boton_convertirF.grid(row=3, column=0, columnspan=2)

label_resultadoF = ttk.Label(Fuerza, text='')
label_resultadoF.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de prefijos
Prefijos = ttk.LabelFrame(ventana, text='Conversión de Prefijos')
Prefijos.grid(row=1, column=2, padx=10, pady=10)

ttk.Label(Prefijos, text='Valor:').grid(row=0, column=0)
entry_valor_prefijo = ttk.Entry(Prefijos)
entry_valor_prefijo.grid(row=0, column=1)

ttk.Label(Prefijos, text='De:').grid(row=1, column=0)
combo_prefijo_origen = ttk.Combobox(Prefijos, values=['T', 'G', 'M', 'k', 'h', 'da',  'd', 'c', 'm', 'µ', 'n', 'p'])
combo_prefijo_origen.grid(row=1, column=1)

ttk.Label(Prefijos, text='A:').grid(row=2, column=0)
combo_prefijo_destino = ttk.Combobox(Prefijos, values=['T', 'G', 'M', 'k', 'h', 'da', 'd', 'c', 'm', 'µ', 'n', 'p'])
combo_prefijo_destino.grid(row=2, column=1)

boton_convertir_prefijo = ttk.Button(Prefijos, text='Convertir', command=convertir_prefijo)
boton_convertir_prefijo.grid(row=3, column=0, columnspan=2)

label_resultado_prefijo = ttk.Label(Prefijos, text='')
label_resultado_prefijo.grid(row=4, column=0, columnspan=2)
import tkinter as tk
from tkinter import Label, PhotoImage, ttk

# Función de conversión para las unidades del SI
def convertir(combo_origen, combo_destino, entry_valor, label_resultado, conversiones):
    unidad_origen = combo_origen.get()
    unidad_destino = combo_destino.get()
    valor = float(entry_valor.get())
    
    try:
        resultado = valor * conversiones[unidad_origen][unidad_destino]
        label_resultado.config(text=f'{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}')
    except KeyError:
        label_resultado.config(text='Conversión no válida')

# Función para la conversión de prefijos
def convertir_prefijo():
    prefijo_origen = combo_prefijo_origen.get()
    prefijo_destino = combo_prefijo_destino.get()
    valor = float(entry_valor_prefijo.get())
    
    # Tabla de prefijos
    prefijos = {
        'T': 1e10, 'G': 1e9, 'M': 1e6, 'k': 1e3, 'h': 1e2, 'da': 10,
        '': 1, 'd': 1e-1, 'c': 1e-2, 'm': 1e-3, 'µ': 1e-6, 'n': 1e-9, 'p': 1e-10
    }
    
    try:
        resultado = valor * (prefijos[prefijo_origen] / prefijos[prefijo_destino])
        label_resultado_prefijo.config(text=f'{valor} {prefijo_origen} = {resultado:.4f} {prefijo_destino}')
    except KeyError:
        label_resultado_prefijo.config(text='Conversión no válida')

ventana = tk.Tk()
ventana.title('Calculadora de Conversión de Unidades')
ventana.config(bg="purple")
ventana.geometry("700x600")

# Estilo para aumentar el tamaño de las flechas del Combobox
style = ttk.Style()
style.configure('TCombobox', arrowsize=70)  # Aumenta el tamaño de las flechas


# Diccionarios de conversiones
conversiones_longitud = {
    'm': {'m': 1, 'cm': 100, 'ft': 3.28084, 'yard': 1.09361, 'km': 0.001, 'mile': 0.000621371},
    'cm': {'m': 0.01, 'cm': 1, 'ft': 0.0328084, 'yard': 0.0109361, 'km': 1e-5, 'mile': 6.2137e-6},
    'ft': {'m': 0.3048, 'cm': 30.48, 'ft': 1, 'yard': 0.333333, 'km': 0.0003048, 'mile': 0.000189394},
    'yard': {'m': 0.9144, 'cm': 91.44, 'ft': 3, 'yard': 1, 'km': 0.0009144, 'mile': 0.000568182},
    'km': {'m': 1000, 'cm': 100000, 'ft': 3280.84, 'yard': 1093.61, 'km': 1, 'mile': 0.621371},
    'mile': {'m': 1609.34, 'cm': 160934, 'ft': 5280, 'yard': 1760, 'km': 1.60934, 'mile': 1}
}

conversiones_peso = {
    'kg': {'kg': 1, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
    'g': {'kg': 0.001, 'g': 1, 'lb': 0.00220462, 'oz': 0.035274},
    'lb': {'kg': 0.453592, 'g': 453.592, 'lb': 1, 'oz': 16},
    'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625, 'oz': 1}
}

conversiones_volumen = {
    'L': {'L': 1, 'mL': 1000, 'gal': 0.264172, 'fl oz': 33.814, 'pulgada³': 61.0237, 'pie³': 0.0353147, 'm³': 0.001, 'cm³': 1000},
    'mL': {'L': 0.001, 'mL': 1, 'gal': 0.000264172, 'fl oz': 0.033814, 'cm³': 1, 'm³': 1e-6, 'pie³': 3.5310e-5, 'pulgada³': 0.0610237},
    'gal': {'L': 3.78541, 'mL': 3785.41, 'gal': 1, 'fl oz': 108, 'pulgada³': 231, 'pie³': 0.133681, 'm³': 0.00378541, 'cm³': 3785.41},
    'fl oz': {'L': 0.0295735, 'mL': 29.5735, 'gal': 0.0078105, 'fl oz': 1, 'cm³': 29.5735, 'm³': 2.9574e-5, 'pie³': 0.00104438, 'pulgada³': 1.80469},
    'm³ ': {'pie³': 35.3147, 'pulgada3': 61023.7, 'cm³': 1000000, 'gal': 264.172, 'fl oz': 33814, 'L': 1000, 'mL': 1e6, 'm³': 1},
    'cm³': {'m³': 1e-6, 'pie³': 3.5310e-5, 'pulgada': 0.0610237, 'gal': 0.000264172, 'fl oz': 0.033814, 'L': 0.001, 'mL': 1, 'cm³': 1},
    'pie³': {'cm³': 283016.8, 'm³': 0.0283168, 'pulgada3': 1728, 'gal': 7.48052, 'fl oz': 957.506, 'L': 28.3168, 'mL': 28316.8, 'pie³': 1},
    'pulgada³': {'pie³': 0.000578704, 'm³': 1.6387e-5, 'cm³': 16.3871, 'gal': 0.004329, 'fl oz': 0.554113, 'L': 0.0163871, 'mL': 16.3871, 'pulgada³': 1}
}

conversiones_energia = {
    'J': {'J': 1, 'cal': 0.239006, 'kWh': 2.77778e-7},
    'cal': {'J': 4.184, 'cal': 1, 'kWh': 1.16222e-6},
    'kWh': {'J': 3600000, 'cal': 860420, 'kWh': 1}
}

conversiones_fuerza = {
    'N': {'N': 1, 'kgf': 0.101972, 'lbf': 0.224809},
    'kgf': {'N': 9.80665, 'kgf': 1, 'lbf': 2.20462},
    'lbf': {'N': 4.44822, 'kgf': 0.453592, 'lbf': 1}
}

# Marco para la conversión de unidades del SI (Longitud)
Longitud = ttk.LabelFrame(ventana, text='Conversión de Unidades (Longitud)')
Longitud.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(Longitud, text='Valor:').grid(row=0, column=0)
entry_valorL = ttk.Entry(Longitud)
entry_valorL.grid(row=0, column=1)

ttk.Label(Longitud, text='De:').grid(row=1, column=0)
combo_origenL = ttk.Combobox(Longitud, values=['m', 'cm', 'ft', 'yard', 'km', 'mile'])
combo_origenL.grid(row=1, column=1)

ttk.Label(Longitud, text='A:').grid(row=2, column=0)
combo_destinoL = ttk.Combobox(Longitud, values=['m', 'cm', 'ft', 'yard', 'km', 'mile'])
combo_destinoL.grid(row=2, column=1)

boton_convertirL = ttk.Button(Longitud, text='Convertir', command=lambda: convertir(combo_origenL, combo_destinoL, entry_valorL, label_resultadoL, conversiones_longitud))
boton_convertirL.grid(row=3, column=0, columnspan=2)

label_resultadoL = ttk.Label(Longitud, text='')
label_resultadoL.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Peso)
Peso = ttk.LabelFrame(ventana, text='Conversión de Unidades (Peso)')
Peso.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(Peso, text='Valor:').grid(row=0, column=0)
entry_valorP = ttk.Entry(Peso)
entry_valorP.grid(row=0, column=1)

ttk.Label(Peso, text='De:').grid(row=1, column=0)
combo_origenP = ttk.Combobox(Peso, values=['kg', 'g', 'lb', 'oz'])
combo_origenP.grid(row=1, column=1)

ttk.Label(Peso, text='A:').grid(row=2, column=0)
combo_destinoP = ttk.Combobox(Peso, values=['kg', 'g', 'lb', 'oz'])
combo_destinoP.grid(row=2, column=1)

boton_convertirP = ttk.Button(Peso, text='Convertir', command=lambda: convertir(combo_origenP, combo_destinoP, entry_valorP, label_resultadoP, conversiones_peso))
boton_convertirP.grid(row=3, column=0, columnspan=2)

label_resultadoP = ttk.Label(Peso, text='')
label_resultadoP.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Volumen)
Volumen = ttk.LabelFrame(ventana, text='Conversión de Unidades (Volumen)')
Volumen.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(Volumen, text='Valor:').grid(row=0, column=0)
entry_valorV = ttk.Entry(Volumen)
entry_valorV.grid(row=0, column=1)

ttk.Label(Volumen, text='De:').grid(row=1, column=0)
combo_origenV = ttk.Combobox(Volumen, values=['L', 'mL', 'gal', 'fl oz', 'm³', 'cm³', 'pie³', 'pulgada³'])
combo_origenV.grid(row=1, column=1)

ttk.Label(Volumen, text='A:').grid(row=2, column=0)
combo_destinoV = ttk.Combobox(Volumen, values=['L', 'mL', 'gal', 'fl oz', 'm³', 'cm³', 'pie³', 'pulgada³'])
combo_destinoV.grid(row=2, column=1)

boton_convertirV = ttk.Button(Volumen, text='Convertir', command=lambda: convertir(combo_origenV, combo_destinoV, entry_valorV, label_resultadoV, conversiones_volumen))
boton_convertirV.grid(row=3, column=0, columnspan=2)

label_resultadoV = ttk.Label(Volumen, text='')
label_resultadoV.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Energía)
Energia = ttk.LabelFrame(ventana, text='Conversión de Unidades (Energía)')
Energia.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(Energia, text='Valor:').grid(row=0, column=0)
entry_valorE = ttk.Entry(Energia)
entry_valorE.grid(row=0, column=1)

ttk.Label(Energia, text='De:').grid(row=1, column=0)
combo_origenE = ttk.Combobox(Energia, values=['J', 'cal', 'kWh'])
combo_origenE.grid(row=1, column=1)

ttk.Label(Energia, text='A:').grid(row=2, column=0)
combo_destinoE = ttk.Combobox(Energia, values=['J', 'cal', 'kWh'])
combo_destinoE.grid(row=2, column=1)

boton_convertirE = ttk.Button(Energia, text='Convertir', command=lambda: convertir(combo_origenE, combo_destinoE, entry_valorE, label_resultadoE, conversiones_energia))
boton_convertirE.grid(row=3, column=0, columnspan=2)

label_resultadoE = ttk.Label(Energia, text='')
label_resultadoE.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de unidades del SI (Fuerza)
Fuerza = ttk.LabelFrame(ventana, text='Conversión de Unidades (Fuerza)')
Fuerza.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(Fuerza, text='Valor:').grid(row=0, column=0)
entry_valorF = ttk.Entry(Fuerza)
entry_valorF.grid(row=0, column=1)

ttk.Label(Fuerza, text='De:').grid(row=1, column=0)
combo_origenF = ttk.Combobox(Fuerza, values=['N', 'kgf', 'lbf'])
combo_origenF.grid(row=1, column=1)

ttk.Label(Fuerza, text='A:').grid(row=2, column=0)
combo_destinoF = ttk.Combobox(Fuerza, values=['N', 'kgf', 'lbf'])
combo_destinoF.grid(row=2, column=1)

boton_convertirF = ttk.Button(Fuerza, text='Convertir', command=lambda: convertir(combo_origenF, combo_destinoF, entry_valorF, label_resultadoF, conversiones_fuerza))
boton_convertirF.grid(row=3, column=0, columnspan=2)

label_resultadoF = ttk.Label(Fuerza, text='')
label_resultadoF.grid(row=4, column=0, columnspan=2)

# Marco para la conversión de prefijos
Prefijos = ttk.LabelFrame(ventana, text='Conversión de Prefijos')
Prefijos.grid(row=1, column=2, padx=10, pady=10)

ttk.Label(Prefijos, text='Valor:').grid(row=0, column=0)
entry_valor_prefijo = ttk.Entry(Prefijos)
entry_valor_prefijo.grid(row=0, column=1)

ttk.Label(Prefijos, text='De:').grid(row=1, column=0)
combo_prefijo_origen = ttk.Combobox(Prefijos, values=['T', 'G', 'M', 'k', 'h', 'da',  'd', 'c', 'm', 'µ', 'n', 'p'])
combo_prefijo_origen.grid(row=1, column=1)

ttk.Label(Prefijos, text='A:').grid(row=2, column=0)
combo_prefijo_destino = ttk.Combobox(Prefijos, values=['T', 'G', 'M', 'k', 'h', 'da', 'd', 'c', 'm', 'µ', 'n', 'p'])
combo_prefijo_destino.grid(row=2, column=1)

boton_convertir_prefijo = ttk.Button(Prefijos, text='Convertir', command=convertir_prefijo)
boton_convertir_prefijo.grid(row=3, column=0, columnspan=2)

label_resultado_prefijo = ttk.Label(Prefijos, text='')
label_resultado_prefijo.grid(row=4, column=0, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
