# -*-coding:Latin-1 -*

import math

#----------------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------------

#Creation de la fonction qui calcule le Delta V:

def delta_v (ispengine, masstot, massdry):

	mfraction = masstot / massdry
	ln = math.log(mfraction)
	DeltaV = ispengine * ln * 9.82
	return DeltaV
	

#----------------------------------------------------------------------------------
# Programme
# ---------------------------------------------------------------------------------

restart = True

while restart == True:
		
	isp = float(input("""
	Entrez l'isp : """))
	mtot = float(input("Entrez la masse totale : "))
	mfuel =	float(input("Entrez la masse du fuel : "))

	mdry = mtot - mfuel
		
	result = delta_v(isp, mtot, mdry)

	print ("Delta V = {} m/s".format(result))
	
	again = int(input("""
	Pour recommencer tapez 1 : """))
	
	if again == 1:
		restart = True
	
	else:
		restart = False

