import statistics

semana1 = int(input("Introduce la semana inicial: "))
semana2 = int(input("Introduce la semana final: "))
temperatura = []

with open('yearTemperatures.csv','r') as semanas:
    for semana in semanas.readlines():
            semana = semana[0:-1]
            temp1 = semana.split(",")
            if temp1[0] == semana1 or semana2:
                temp2 = temp1[1:]
                for i in range(len(temp2)):
                    temp3 = []
                    temp3.append(float(temp2[i]))
                temp4 = statistics.mean(temp3)
