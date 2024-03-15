direcciones = {
    "juan": "C/ Moncófar, 5",
    "antonio": "C/ Enmedio, 15",
    "jose": "C/ Mayor, 30",
}

# print(direcciones.get("juanito"))

for nombre, direccion in direcciones.items():
    print(f"{nombre}: {direccion}")