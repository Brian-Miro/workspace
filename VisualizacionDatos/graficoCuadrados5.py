import matplotlib.pyplot as plt

valores = [n for n in range(1,5001)]
cubos = [n**3 for n in valores]
fig, ax = plt.subplots()
ax.plot(valores, cubos, linewidth = 3)

ax.set_title("Cubos de los números", fontsize=18)
ax.set_xlabel("Valor", fontsize=12)
ax.set_ylabel("Cubo del valor", fontsize=12)

ax.tick_params(axis='both', labelsize=12)

plt.show()

# fig.savefig('graficoCuadrados.png')