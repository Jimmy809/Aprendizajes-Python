# https://ellibrodepython.com/operadores-asignacion
# Operador	                 Ejemplo	            Equivalente
# =	                          x=7	                  x=7                   igual
# +=	                      x+=2	                  x=x+2 = 9             reasignacion suma
# -=	                      x-=2	                  x=x-2 = 5             reasignacion resta
# *=	                      x*=2                    x=x*2 = 14            reasignacion de multiplicacion
# /=	                      x/=2	                  x=x/2 = 3.5           reasiganacion de division
# %=	                      x%=2	                  x=x%2 = 1             reasiganacion de modulo
# //=	                      x//=2	                  x=x//2 = 3            reasiganacion de cociente
# **=	                      x**=2	                  x=x**2 = 49           reasiganacion de exponente
# &=	                      x&=2	                  x=x&2 = 2             El operador &= realiza la comparación & bit a bit entre dos variables y almacena su resultado en la primera. El equivalente de x&=1 sería x=x&1
# |=	                      x|=2	                  x=x|2 = 7             El operador |= realiza el operador | elemento a elemento entre dos variables y almacena su resultado en la primera. El equivalente de x|=2 sería x=x|2
# ^=	                      x^=2	                  x=x^2 = 5             El operador ^= realiza el operador ^ elemento a elemento entre dos variables y almacena su resultado en la primera. El equivalente de x^=2 sería x=x^2
# >>=	                      x>>=2	                  x=x>>2 = 1            El operador >>= es similar al operador >> pero permite almacenar el resultado en la primera variable. Por lo tanto x>>=3 sería equivalente a x=x>>3
                                                                            #Muy similar al anterior, <<= aplica el operador << y almacena su contenido en la primera variable. El equivalente de x<<=1 sería x=x<<1


a=7; b=2
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5
x=a; x%=b;  print("x%=", x)  # 1
x=a; x//=b; print("x//=", x) # 3
x=a; x**=b; print("x**=", x) # 49
x=a; x&=b;  print("x&=", x)  # 2
x=a; x|=b;  print("x|=", x)  # 7
x=a; x^=b; print("x^=", x)   # 5
x=a; x>>=b; print("x>>=", x) # 1    
x=a; x<<=b; print("x<<=", x) # 28                   