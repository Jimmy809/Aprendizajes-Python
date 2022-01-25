# proporciona tu edad:
# 0-10: La infancia es increible...
# 10-20: Muchos cambios y mucho estudios...
# 20-30: Amor y comienza el trabaajo...
# Cualquier otro valor: Etapa de vida no reconocida
print('***Etapas de la Vida!!***')

etapas = int(input('Proporciona tu edad: '))

if etapas == 0 or etapas < 10:
    print('La infancia es increible...')
elif etapas == 10 or etapas < 20:
    print('Muchos cambios y mucho estudios...')
elif etapas == 20 or etapas < 30:
    print('Amor y comienza el trabaajo...')
else:
    print('Etapa de vida no reconocida')