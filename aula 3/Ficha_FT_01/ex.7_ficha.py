import math

dist = float(input("indique a distância em km: \n"))

quant = float(input("indique a quantidade de combustível consumida: \n"))

consumo = round(dist/quant, 2)

consumo_medio = round((quant/dist)*100, 2)

print("o consumo foi de: ", consumo, "km/l")

print("o Consumo médio por 100 km é: ", consumo_medio, "l/100km")

