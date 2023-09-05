import math as Math
# Resultado esperado: 2, 77, 52, 27, 2
# def relacion(xo, a, c, m):
#    xn = xo
#    while True:
#       xn = (a * xn + c) % m
#       u = xn / m
#       if xn == xo:
#          break
#       print(u)
#    return xn
        
# print(relacion(27,17,43,100))


# def realacion_r(xo, a, c, m):
#    xn = xo
#    dato = []
#    valor_inicial = xn = ( a * xn ) % m;
#    while True:
#       xn = ( a * xn ) % m
#       dato.append(xn)
#       if (valor_inicial == dato[-1]):
#          break
      
#    return dato

# dato = realacion_r(5, 12, 5, 21);
# for i in dato:
#     print(i)


import math

def relacion_factorizada(xo, a, m):
    q = math.floor(m / a)
    r = (m % a)
    xn_1 = xo
    m = a * q + r
    print("r: "+str(r), "q: "+str(q), "m: "+str(m))
    modulo = (a * xn_1) % m
    while True:
        if (a*(xn_1 % q)-r*math.floor(xn_1/q) >= 0):
            modulo = a *  (xn_1 % q)-r*math.floor(xn_1/q)
        else:
            modulo = a * (xn_1 % q)-r*math.floor(xn_1/q) + m
        
        xn_1 = modulo
    
    print(xn_1)
    

relacion_factorizada(5, 12, 21)


# def relacion_factorizada(xo, a, m):
#     q = math.floor(m / a)
#     r = (m % a)
#     xn_1 = xo
#     dato = []
#     m = a * q + r
#     while True:
#         if (a * (xn_1 % q) - r * math.floor(xn_1 / q)) >= 0:
#             modulo = a * (xn_1 % q) - r * math.floor(xn_1 / q)
#         else:
#             modulo = a * (xn_1 % q) - r * math.floor(xn_1 / q) + m
#         xn_1 = modulo
        
#         if xn_1 in dato:
#             break
#         else:
#             dato.append(xn_1)

    
#     print("r:", r, "q:", q, "m:", m, "xn_1:", xn_1)
#     return dato

# datos = relacion_factorizada(10, 12, 21)

# for i in datos:
#     print(i)


