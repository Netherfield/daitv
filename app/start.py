


import os
import sys

"""
E ○    il numero di film per ogni anno 
E ○   il numero di film per ogni genere

D ○    i film che hanno recensioni al di sotto di 3 per un numero 250 di persone in modo da eliminarli

F ○    la top 10 per ogni intervallo di età e sesso

J ○    rating film - i voti dal meno preferito al più preferito per fasce di età
creare una vista che raggruppa i film per fascia d'eta' in ordine di valutazione media

P ○    il numero degli iscritti alla piattaforma nelle varie province, voglio vedere le prime 20

E ○    il numero degli abbonati in base al lavoro
"""

this_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.insert(0, base_dir)

from app.queries import *

if __name__ == "__main__":
    # users()
    # ratings()

    os.system("pyclean .")

