# Uso del if (Si)
# Un ejemplo sería si tenemos dos valores a y b que queremos dividir. 
# Antes de entrar en el bloque de código que divide a/b, sería importante verificar que b es distinto de cero, 
# ya que la división por cero no está definida. Es aquí donde entran los condicionales if.

condicion = True
# la condicion siempre sera positiva siempre y cuando la variable tenga argumentos, si esta vacia '' dara negativo o falso
if condicion == True:
    print('Condicion Verdadera')
    
# Uso de else y elif
# Es posible que no solo queramos hacer algo si una determinada condición se cumple, 
# sino que además queramos hacer algo de lo contrario. Es aquí donde entra la cláusula else. 
# La parte del if se comporta de la manera que ya hemos explicado, con la diferencia que si esa condición no se cumple, 
# se ejecutará el código presente dentro del else. Nótese que ambos bloque de código son excluyentes, 
# se entra o en uno o en otro, pero nunca se ejecutarán los dos.
elif condicion == False:  
    print('Condicion Falsa')
else:
    print('Condicion no reconocida')