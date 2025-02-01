
import math

# pedir user um nº inteiro e devolver raíz quadrada

num = int(input("introduzir um número inteiro: "))

quadrado = num**2

#agora com biblioteca

raizquad = math.sqrt(num)

#print("o seu numero ao quadrado é: ", quadrado)

print("a raiz quadrada do numero dado é: ", raizquad, "arredondado a", round(raizquad, 2))

print(f"a raiz quadrada do numero dado é: {raizquad} arredondado a {round(raizquad, 2)}")

