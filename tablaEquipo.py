print ("Puntos Equipo Futbol")

#ingreso de datos

partidos_perdidos = int(input("ingrese los partidos perdidos: "))
partidos_ganados = int(input("ingrese los partidos ganados: ")) 
partidos_empatados = int(input("ingrese los partidos empatados: "))

#calculo de los puntos
puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados * 1
puntos_perdidos = partidos_perdidos * 0
puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos

#impresion de los puntos

print(f"los puntos ganados son: {puntos_ganados}")
print(f"los puntos empatados son: {puntos_empatados}")
print(f"los puntos perdidos son: {puntos_perdidos}")
print(f"los puntos totales son: {puntos_totales}")
