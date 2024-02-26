import random

def cambiaTexto1(palabra):
    longitudPalabra = len(palabra)
    if longitudPalabra <=2:
        return palabra
    elif longitudPalabra>2 and longitudPalabra<=6:
        temp1 = palabra[0:2]
        temp2 = palabra[len(palabra)-2:]
        palabra = temp2 + palabra + temp1
        return palabra
    else:
        temp1 = palabra[0:3]
        temp2 = palabra[len(palabra)-3:]
        print(temp1,temp2)
        palabra = temp2 + temp1
        return palabra

def cambiaTexto2(palabra):
    if palabra.lower() == palabra:
        return palabra.upper()
    elif palabra.upper() == palabra:
        return palabra.lower()
    else:
        return "mezclado"

def cambiaTexto3(palabra):
    longitud = 5 * len(palabra)
    palabra = str(longitud-5) + palabra + str(longitud)
    return palabra

def cambiaTexto4(palabra):
    longitud_palabra = len(palabra)
    if longitud_palabra <= 5:
        temp1 = palabra[:3]
        temp2 = palabra[3:]
        palabra = temp1 + "_" + temp2
        return palabra
    else:
        temp1 = palabra[:(longitud_palabra//4)]
        temp2 = palabra[(longitud_palabra//4):(longitud_palabra*2//4)]
        temp3 = palabra[(longitud_palabra*2//4):(longitud_palabra*3//4)]
        temp4 = palabra[(longitud_palabra*3//4):]
        palabra = temp1 + "_" + temp2 + "_" + temp3 + "_" + temp4
        return palabra

texto = input("Por favor, introduce tu palabra: ")
numero = random.randint(1,3)
print(f'El número aleatorio es {numero}')

if numero == 1:
    texto = cambiaTexto4(cambiaTexto3(cambiaTexto2(cambiaTexto1(texto))))
elif numero == 2:
    texto = cambiaTexto3(cambiaTexto1(cambiaTexto4(cambiaTexto2(texto))))
else:
    texto = cambiaTexto4(cambiaTexto1(cambiaTexto2(cambiaTexto3(texto))))

if len(texto) > 10:
    texto = texto[:10]
elif len(texto) < 10:
    while len(texto) < 10:
        texto = texto + str(random.randint(0,9))
else:
    texto = texto

print(f'Tu contraseña es: {texto}')