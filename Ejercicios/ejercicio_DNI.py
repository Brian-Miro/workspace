letra_dni = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")

dni = int(input("Dime los números de tu DNI y yo calcularé la letra: "))
print(f'La letra para tu DNI {dni} es: {letra_dni[dni%23]}')
