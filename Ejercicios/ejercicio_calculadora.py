numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
operacion = input("Introduce la operación aritmética (+, -, * o /): ")

while operacion not in ("+", "-", "*", "/"):
    print("Esa no es una operación aritmética.")
    operacion = input("Introduce la operación aritmética (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
else:
    resultado = numero1 / numero2

print(f'El resultado de la operación aritmética de {numero1} {operacion} {numero2} es: {resultado}')