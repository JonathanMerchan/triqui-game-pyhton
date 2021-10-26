def renderizar_tablero(juego) -> str:
 
  cells_tmpl = '| {} | {} | {} |'  #formato de cada fila del tablero
  bar = '-------------' # línea divisoria
  tablero="\n" # inicializa el tablero en fin de linea (return)
  tablero= tablero.join([bar,cells_tmpl.format(*juego[:3]),bar, # Preguntale a tu formador el porque del *
                        cells_tmpl.format(*juego[3:6]),bar,
                        cells_tmpl.format(*juego[6:]),bar])
 
  #La funcion join concatena todos los elementos de la lista y los separa con el caracter \n 
  return tablero

def actualizar_movimiento(juego,jugada,jugador) -> str:
 
  # Validación del tipo y el rango de la jugada 
  if not (jugada.isdigit() and int(jugada) in range(1, 10)): # Condiciones que debe cumplir
    print(f'Jugada no válida "{jugada}", Solo ingrese valores entre  1-9')
    return juego # El juego no cambia
  
  # Validación de jugada permitida
  numero_jugada = int(jugada)
  if juego[numero_jugada - 1] in 'XO': # Esta ocupada con otra jugada
    print(f'La casilla "{jugada}" ya esta ocupada')
    return juego # El juego no cambia

  #actualiza el juego con la nueva jugada
  juego=juego[:numero_jugada-1]+jugador+juego[numero_jugada:]
  return juego 


def encontrar_ganador(juego) -> str:
 
  # Opciones de ganar el juego representadas con tuplas
  ganadores = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
               (2, 5, 8), (0, 4, 8), (2, 4, 6))
 
  for jugador in ('X', 'O'):# Verificar por cada jugador 
    for i, j, k in ganadores: # buscar por cada opción ganadora en la lista de ganadores
      linea = (juego[i], juego[j], juego[k]) #obtiene una tupla de los simbolos en las posiciones
      if linea == (jugador, jugador, jugador): #compara si la tupla tiene el simbolo del jugador 
        return jugador 
  return None #No hay ganador

def jugar_triqui()->None:
  
  juego="123456789" # Inicia el tablero sin jugadas
  jugador='X'  # Inicia el jugador X
  contador = 1  #Agragamos un contador de intentos
  t = True #genramos un bool para datener el ciclo
  while t: # Ciclo infinito
    print("Paso ",contador)
    if (contador <7): # se valida el numero de intentos
      print(renderizar_tablero(juego))  # Dibuja el tablero
      jugada = input(f'Jugador {jugador}, ¿Cual es la jugada? [q para terminar]: ')
      
      if jugada=='q': # Se retira
        print("Has perdido por W")
        break
      
      juego=actualizar_movimiento(juego,jugada,jugador) # actualiza el tablero
      ganador=encontrar_ganador(juego) # Busca al ganador
      
      if ganador!=None: # hay un ganador
        print(f"{ganador} has ganado!")
        break
    
      if jugador=='X':  # Cambia el símbolo del jugador para la próxima jugada
        jugador='O'
      else:
        jugador='X'
      contador+=1 #contamos el intento
    else:
      print("\nEl numero de intentos ha sido superado\n")
      t=False #cancelamos el ciclo y salimos del programa

#====================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# ===================================================================

jugar_triqui()
