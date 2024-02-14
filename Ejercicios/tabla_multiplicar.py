tabla_numerica = int(input("Dime el número para calcular la tabla de multiplicar: "))
for factor_de_multiplicacion in range (1,10):
    resultado = tabla_numerica * factor_de_multiplicacion
    print(f'{tabla_numerica} * {factor_de_multiplicacion} = {resultado}')