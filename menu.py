# -*- coding: utf8 -*-
#Nombre: Menu
#Funcion: Menu del estacionamiento ejercicio examen
#Autor: Josue Nolasco
#Fecha: 03/13/2020

import sys
import platform
import datetime
import random

class Menu:
    """ Muestra las opciones del Menu """

    def __init__(self):
        self.Vehiculo = list()

        self.opciones = {"1":self.Entrada,
                         "2":self.Carros,
                         "3":self.Salidas,
                         "4":self.Total,
                         "5":self.Salir

                        }

    def mostrar_menu(self):
        print("""
            Menu
            1:Entrada
            2:Salidas
            3:Total
            4:Salir
            """)

    def Entrada(self):
        self.numplaca = input("Ingrese el numero de placa: ")
        self.marca = input("Ingrese la marca : ")
        self.modelo = input("Ingrese el modelo: ")
        self.tipo = input("Ingrese el tipo: ")
        self.hora = input("Ingrese la hota de entrada: ")
        self.estado = True
        pass

    def Salidas(self):
         pass

    def Total(self):
         pass

    def Salir(self):
        print("Aplicacion Cerrada")
        sys.exit(0)

    def horas(self):
        horas_vehiculo = random(1,5)
        print(horas_vehiculo)