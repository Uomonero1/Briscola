import random
from functions import calcolo_punteggio, giocata_carte, pescata_carte, vittoria_mano

def inizio_gioco():
    """Inizializza il gioco: crea e mescola il mazzo, sceglie la briscola,
    la rimuove dal mazzo, distribuisce tre carte ai due giocatori

    Returns:
        briscola(tuple): numero e seme della briscola
        mazzo(list): lista delle carte rimaste nel mazzo
        carte_gioc1(list): lista delle carte nelle mani del giocatore1
        carte_gioc2(list): lista delle carte nelle mani del giocatore2
        carte_rimaste(int): numero di carte rimaste nel mazzo
    """
    SEMI = ["Bastoni", "Coppe", "Denari", "Spade"]
    NUMERI = [x for x in range(1,11)]
    mazzo = [(i,j) for i in NUMERI for j in SEMI]
    carte_rimaste = len(mazzo)
    carte_gioc_1 = []
    carte_gioc_2 = []

    # mescolamento mazzo
    random.shuffle(mazzo)

    # scelta briscola e rimozione dal mazzo
    briscola = random.choice(mazzo)
    mazzo.remove(briscola)
    carte_rimaste -= 1

    # distribuzione prime tre carte ai giocatori
    for _ in range(3):
        carta1 = mazzo[0]
        carte_gioc_1.append(carta1)
        mazzo.pop(0)
        carta2 = mazzo[0]
        carte_gioc_2.append(carta2)
        mazzo.pop(0)
        carte_rimaste -= 2

    return(briscola, mazzo, carte_gioc_1, carte_gioc_2, carte_rimaste)


def mainloop(briscola: tuple, mazzo: list, carte_gioc1: list, carte_gioc2: list, numero_carte: int):
    """Fa svolgere il gioco finchè ci sono carte nel mazzo.

    Args:
        briscola(tuple): numero e seme della briscola
        mazzo(list): lista delle carte rimaste nel mazzo
        carte_gioc1(list): lista delle carte nelle mani del giocatore1
        carte_gioc2(list): lista delle carte nelle mani del giocatore2
        numero_carte(int): numero di carte rimaste nel mazzo
    """
    carte_vinte1 = []
    carte_vinte2 = []
    seme_di_briscola = briscola[1]
    
    # LISTA "SCARTI" INUTILE
    carichi = {1: 11, 2: 0, 3: 10, 4: 0, 5: 0, 6: 0, 7: 0,
    8: 2, 9: 3, 10: 4}

    while numero_carte > 1:
        print("-----------------------------------------------------")
        print(f"Briscola: {briscola}")

        # giocata carte
        print(f"Le tue carte {carte_gioc1}")
        giocata1 = int(input("Quale carta vuoi giocare(1,2,3): "))-1
        numero1, seme1 = carte_gioc1[giocata1]
        carte_gioc1.pop(giocata1)
        print(f"Il giocatore 1 gioca la carta {numero1} di {seme1}.")
        numero2, seme2 = giocata_carte(carte_gioc2)
        print(f"Il giocatore 2 gioca la carta {numero2} di {seme2}.")

        vittoria_mano(seme1, seme2, seme_di_briscola, numero1, numero2, carte_vinte1, carte_vinte2, carichi)

        pescata_carte(mazzo, carte_gioc1)
        pescata_carte(mazzo, carte_gioc2)
        
        numero_carte -= 2
        print(f"Numero di carte nel mazzo {numero_carte}")
    
    print("-----------------------------------------------------")
    print(f"Briscola: {briscola}")

    # giocata carte
    print(f"Le tue carte {carte_gioc1}")
    giocata1 = int(input("Quale carta vuoi giocare(1,2,3): "))-1
    numero1, seme1 = carte_gioc1[giocata1]
    carte_gioc1.pop(giocata1)
    print(f"Il giocatore 1 gioca la carta {numero1} di {seme1}.")
    numero2, seme2 = giocata_carte(carte_gioc2)
    print(f"Il giocatore 2 gioca la carta {numero2} di {seme2}.")

    vittoria_mano(seme1, seme2, seme_di_briscola, numero1, numero2, carte_vinte1, carte_vinte1, carichi)
    
    # pescata carte
    carte_gioc1.append(mazzo[0])
    mazzo.pop(0)
    carte_gioc2.append(briscola)

    vittoria1, vittoria2, pareggio = calcolo_punteggio(carte_vinte1, carte_vinte2)
    return(vittoria1, vittoria2, pareggio)

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

print("STASTICHE FINALI")    
print(vittoria_gioc1, pareggi, vittoria_gioc2)