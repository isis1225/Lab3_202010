"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import map as map

from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 3")
    print("1- Cargar información")
    print("2- Buscar libro por titulo")
    print("3- Buscar información de autor por nombre ...")
    print("4- Requerimiento 3 ...")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de peliculas
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las peliculas en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print ('Mapa Libros cargados: ' + str(map.size(catalog['booksMap'])))
        print ('Lista Libros cargados: ' + str(lt.size(catalog['booksList'])))
        print ('Autores cargados: ' + str(map.size(catalog['authors'])))
        
    elif int(inputs[0])==2:
        bookTitle = input("Nombre del libro a buscar: ")
        book = controller.getBookInfo (catalog, bookTitle)
        if book:
            print("Libro encontrado:",book['title'],",Rating:",book['average_rating'])
        else:
            print("Libro No encontrado")    

    elif int(inputs[0])==3:
        authorName = input("Nombre del autor a buscar: ")
        author = controller.getAuthorInfo (catalog, authorName)
        if author:
            print("Libros del autor",authorName,":",lt.size(author['authorBooks']))
            print("Promedio  e Votación: ",authorName,(author['sum_average_rating']/lt.size(author['authorBooks'])))
        else:
            print("Autor No encontrado")    


    elif int(inputs[0])==4:
        label = input (" ")
        pass
    else:
        sys.exit(0)
sys.exit(0)