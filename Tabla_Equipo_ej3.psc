Algoritmo Tabla_Equipo_ej3
    // Definici�n de variables
    Definir partidosPerdidos, partidosGanados, partidosEmpatados Como Entero
    Definir puntosPorPartidoPerdido, puntosPorPartidoGanado, puntosPorPartidoEmpatado, puntajeTotal Como Real
    
    // Inicializaci�n de puntos por resultado de partido
    puntosPorPartidoEmpatado = 1
    puntosPorPartidoGanado = 3
    puntosPorPartidoPerdido = 0
    
    // Solicitar al usuario los resultados de los partidos
    Escribir "Ingrese los partidos jugados y su resultado para obtener el puntaje total del equipo."
    
    Escribir "Partidos Perdidos: "
    Leer partidosPerdidos
    
    Escribir "Partidos Ganados: "
    Leer partidosGanados
    
    Escribir "Partidos Empatados: "
    Leer partidosEmpatados
    
    // C�lculo del puntaje total
    puntajeTotal = (puntosPorPartidoEmpatado * partidosEmpatados) + (puntosPorPartidoGanado * partidosGanados) + (puntosPorPartidoPerdido * partidosPerdidos)
    
    // Mostrar el puntaje total
    Escribir "El puntaje final del torneo es: ", puntajeTotal
FinAlgoritmo
