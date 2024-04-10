class Cuenta():
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print()
        print(f'Titular: {self.titular}')
        print(f'Cantidad: {self.cantidad}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if self.cantidad > 0:
            self.cantidad -= cantidad

cuenta1 = Cuenta("Pedro", 2500)
cuenta2 = Cuenta("Juana", -500)

cuenta1.mostrar()
cuenta1.retirar(2000)
cuenta1.mostrar()
cuenta1.ingresar(1250)
cuenta1.mostrar()
cuenta1.retirar(3000)
cuenta1.mostrar()

cuenta2.mostrar()
cuenta2.retirar(500)
cuenta2.mostrar()
cuenta2.ingresar(100)
cuenta2.mostrar()
cuenta2.ingresar(450.50)
cuenta2.mostrar()

