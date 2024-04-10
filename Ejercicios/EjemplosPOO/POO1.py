class Estudiante():
    def __init__(self, nombre, apellidos, grupo, edad, nia):
        self.nombre = nombre
        self.apellidos = apellidos
        self.grupo = grupo
        self.edad = edad
        self.nia = nia

    def mostrar(self):
        print()
        print(f'Nombre: {self.nombre}')
        print(f'Apellidos: {self.apellidos}')
        print(f'Grupo: {self.grupo}')
        print(f'Edad: {self.edad}')
        print(f'NIA: {self.nia}')    

    def esMayorDeEdad(self):
        if self.edad >= 18:
            print()
            print(True)
        else:
            print()
            print(False)


alumno1 = Estudiante("Antonio", "Gómez García", "4º ESO A", 16, 12345678)
alumno2 = Estudiante("María", "Jiménez Estellés", "2º BAC C", 18, 18765432)

alumno1.esMayorDeEdad()
alumno1.mostrar()

alumno2.esMayorDeEdad()
alumno2.mostrar()
