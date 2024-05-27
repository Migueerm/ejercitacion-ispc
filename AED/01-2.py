#Cuadrado de un binomio
#Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que:
#Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del
#primero por el segundo más el cuadrado del segundo.

a = int(input("Ingrese el primer Valor: "))
b = int(input("Ingrese el segundo Valor: "))

binomio = (a**2) + (2*a*b) + (b**2)

print("El binomio al cuadrado es: ", binomio)
