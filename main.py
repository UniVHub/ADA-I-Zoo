# ---------------------------------------------------------------------------- #
#                                  SOLUCIÓN 1                                  #
# ---------------------------------------------------------------------------- #

# --------- INFORMACIÓN ACERCA DE LAS ESTRUCTURAS DE DATOS A UTILIZAR -------- #
# Para almacenar la información de los animales se utilizará un diccionario
# Para almacenar las escenas se utilizaran las listas. Cada escena será una lista de 3 elementos
# Para almacenar las partes se utilizaran las listas. Cada parte será una lista de escenas

# -------------- INFORMACIÓN ACERCA DE LOS ALGORITMOS A UTILIZAR ------------- #
# Para ordenar las escenas y las partes podemos utilizar el algoritmo de ordenamiento por mezcla (merge sort) con algunas modificaciones, las cuales no afectaran la complejidad del algoritmo


from Solucion_1.ConcertZoo import ConcertZoo

# ---------------------------- VARIABLES INICIALES --------------------------- #
n = 6
m = 3
k = 2

animals = {
  'Ci': 1,
  'Li': 2,
  'Ga': 3,
  'Pe': 4,
  'Ta': 5,
  'Nu': 6
}


aperture = [
  ['Pe', 'Nu', 'Ta'],
  ['Ta', 'Pe', 'Ga'],
  ['Ta', 'Ci', 'Ga'],
  ['Ga', 'Li', 'Ci'],
]

rest_of_show = [
  [['Ta', 'Ci', 'Ga'], ['Pe', 'Nu', 'Ta']],
  [ ['Ta', 'Pe', 'Ga'], ['Ci', 'Li', 'Ga']],
  ]


if __name__ == "__main__":
  concert = ConcertZoo(n, m, k)
  concert.add_animals(animals)
  concert.add_aperture(aperture)
  concert.add_rest_of_show(rest_of_show)

  concert.show()

  #  ordenamos la paertura y la mostrmaos
  # show.show_sorted_aperture()
  concert.show_sorted()