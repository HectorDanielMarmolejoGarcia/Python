# -*- coding: utf-8 -*-
import os, sys
########################################
#Fecha:19-10-2021                      #
#Author: Hector Daniel Marmolejo Garcia#
########################################
f_Nac = int(input("Inserta tu fecha de nacimiento: "))
dif = int(2021 - f_Nac)

if dif >= 18:
    print ("El usuario tienen ", dif, "por lo tanto es mayor de edad")
else:
    print ("El usuario tiene ", dif, "por lo tanto es menor de edad")



