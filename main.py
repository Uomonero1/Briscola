import random
from functions import mainloop, inizio_gioco

vittoria_gioc1 = 0
pareggi = 0
vittoria_gioc2 = 0

for i in range(1):
    print("--------------------------------------------------------------------")
    print(f"Giro {i+1}")
    briscola, mazzo, carte_gioc1, carte_gioc2, numero_carte = inizio_gioco()
    vittoria1, vittoria2, pareggio = mainloop(briscola, mazzo, carte_gioc1, carte_gioc2, numero_carte)
    if vittoria1 == 1:
        vittoria_gioc1 += 1
    elif vittoria2 == 1:
        vittoria_gioc2 += 1
    else:
        pareggi += 1

print("STATISTICHE FINALI")    
print(vittoria_gioc1, pareggi, vittoria_gioc2)