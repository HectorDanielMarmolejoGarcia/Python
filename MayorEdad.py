#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
########################################
#Fecha:19-10-2021                      #
#Author: Hector Daniel Marmolejo Garcia#
########################################
f_Nac = int(input("Inserta tu año de nacimiento: "))
dif = (2021 - f_Nac)

if dif >= 18:
    print ("El usuario tienen ", dif, "años y es mayor de edad")
else:
    print ("El usuario tiene ", dif, "años y es menor de edad")



