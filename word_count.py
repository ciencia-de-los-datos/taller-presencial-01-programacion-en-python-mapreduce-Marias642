#
# Escriba la función load_input que recive como parámetro un folder y retorna
# una lista de tuplas donde el primer elemento de cada tupla es el nombre del
# archivo y el segundo es una línea del archivo. La función convierte a tuplas
# todas las lineas de cada uno de los archivos. La función es genérica y debe
# leer todos los archivos de folder entregado como parámetro.
#
# Por ejemplo:
#   [
#     ('text0'.txt', 'Analytics is the discovery, inter ...'),
#     ('text0'.txt', 'in data. Especially valuable in ar...').
#     ...
#     ('text2.txt'. 'hypotheses.')
#   ]
import glob   #permite leer el contenido los archivos
import fileinput    #permite iterar (ciclos) y operar en archivos

def load_input(input_directory):

    sequence =[] # crea una lista vacía
    filenames= glob.glob(input_directory + "/*") # regresa la ubicación del archivo
    with fileinput.input(files=filenames) as f: # crea una lista de los archivos
        for line in f: # línea por línea de los archivos contenidos en el objeto f
            sequence.append((fileinput.filename(), line)) # Adiciona a la lista el nombre del archivo y la línea 
    return sequence # da el resultado
    

filenames = load_input("input") 
# print(filenames[2]) # muestra el resultado, muestra el tercero


#
# Escriba una función llamada maper que recibe una lista de tuplas de la
# función anterior y retorna una lista de tuplas (clave, valor). En este caso,
# la clave es cada palabra y el valor es 1, puesto que se está realizando un
# conteo.
#
#   [
#     ('Analytics', 1),
#     ('is', 1),
#     ...
#   ]

def mapper(sequence):
    new_sequence =[] # crea una lista vacía
    for _, text in sequence: # recorre la lista de duplas
        words = text.split() # separa las palabras y las aloja en un alista denominada words
        for word in words: # recorre la lista words
            word = word.replace(",","")
            word = word.replace(".","")
            word = word.lower()
            new_sequence.append ((word,1)) # Agrega la dupla en la lista new_sequence 
    return new_sequence # retorna la lista
  
sequence = load_input("input")
sequence = mapper(sequence)
# print(sequence)


#
# Escriba la función shuffle_and_sort que recibe la lista de tuplas entregada
# por el mapper, y retorna una lista con el mismo contenido ordenado por la
# clave.
#
#   [
#     ('Analytics', 1),
#     ('Analytics', 1),
#     ...
#   ]

def shuffle_and_sort(sequence): 
    sorted_sequence = sorted(sequence, key=lambda x: x[0]) # ordena las duplas
    return sorted_sequence # retorna la lista de duplas ordenada

sequence = load_input("input")
sequence = mapper(sequence)
sequence = shuffle_and_sort(sequence)
# print(sequence)


#
# Escriba la función reducer, la cual recibe el resultado de shuffle_and_sort y
# reduce los valores asociados a cada clave sumandolos. Como resultado, por
# ejemplo, la reducción indica cuantas veces aparece la palabra analytics en el
# texto.
#
# def reducer(sequence):
    # pass


def reducer(sequence):

    diccionario = {}
    for key, value  in sequence:
        if key not in diccionario.keys():
            diccionario[key] = 0
        diccionario[key] += value

    new_sequence =[]
    for key, value in diccionario.items():
        tupla= (key,value)
        new_sequence.append(tupla)

    return new_sequence

sequence = load_input("input")
sequence = mapper(sequence)
sequence = shuffle_and_sort(sequence)
sequence = reducer(sequence)
#print(sequence)


#
# Escriba la función create_ouptput_directory que recibe un nombre de directorio
# y lo crea. Si el directorio existe, la función falla.
#

import os.path

def create_ouptput_directory(output_directory):
    
    if os.path.exists(output_directory):
        raise FileExistsError(f"The directory '{output_directory}' alredy exists.")
    os.makedirs(output_directory)


#
# Escriba la función save_output, la cual almacena en un archivo de texto llamado
# part-00000 el resultado del reducer. El archivo debe ser guardado en el
# directorio entregado como parámetro, y que se creo en el paso anterior.
# Adicionalmente, el archivo debe contener una tupla por línea, donde el primer
# elemento es la clave y el segundo el valor. Los elementos de la tupla están
# separados por un tabulador.
#

def save_output(output_directory, sequence):
    with open(output_directory + "/part-00000", "w") as file:
        for key, value in sequence:
            file.write(f"{key}\t{value}\n")
   


#
# La siguiente función crea un archivo llamado _SUCCESS en el directorio
# entregado como parámetro.
#
def create_marker(output_directory):
    with open(output_directory + "/_SUCCESS","w") as file:
        file.write("")
    

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def job(input_directory, output_directory):

    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_ouptput_directory(output_directory)
    save_output(output_directory, sequence)
    create_marker(output_directory)


if __name__ == "__main__":
    job(
        "input",
        "output",
    )
  