def muestraDatos(datosEntrada):
    global media
    media = sum(datosEntrada)/len(datosEntrada)
    print(f'Puntuación media: {media}')
    print(f'Las puntuaciones van desde: ')
    print(f'{min(datosEntrada)} a {max(datosEntrada)}')

# Programa principal
media = 0
puntuaciones = [4,6,8,5,6,7,9,10,5,1,3,2]
muestraDatos(puntuaciones)
print()
print(f'Puntuación media: {media}')