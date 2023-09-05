#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
#maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def arpakuutio(tahkot):
    noppa = 0
    while noppa!=tahkot:
        noppa = random.randint(1, tahkot)
        print(noppa)
    return noppa
maara = int(input('Syötä tahkojen määrä: '))
arpakuutio(maara)