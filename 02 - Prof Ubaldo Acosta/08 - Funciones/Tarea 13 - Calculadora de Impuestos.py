# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# La función se llama calcular_total()
# La función recibe dos parámetros:
# 1. pago_sin_impuesto
# 2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)
# La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.
# Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0
# Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.
# pago_sin_impuesto = float(input('Introduce el valor de tu pedido: '))

# pago_sin_impuesto = float(input('Introduce el valor de tu pedido: '))

# def calcular_total(pago_sin_impuesto, impuesto):
#     print(f'''          Precio del articulo: {pago_sin_impuesto}
#           Impuestos a aplicar: {impuesto}%
#           Total a pagar : {total}          ''')
# impuesto = 10
# calculo = impuesto/100
# total = pago_sin_impuesto * calculo + pago_sin_impuesto

# calcular_total(pago_sin_impuesto, impuesto)


def calcular_total(pago_sin_impuesto, impuesto):
    return  pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)

pago_sin_impuesto = float(input('Introduce el valor de tu pedido: '))
impuesto = float(input('Introduce el monto del impuesto: '))
pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)

print(f'''          
          Precio del articulo: {pago_sin_impuesto}
          Impuestos a aplicar: {impuesto}%
          Total a pagar : {pago_con_impuesto}''')