import random

def vittoria_mano(seme1: str, seme2: str, seme_di_briscola: str, numero1: int, numero2: int, carte_vinte1: list, carte_vinte2: list, valore: dict):
    """Popola le liste che contengono le carte vinte da ogni giocatore ad ogni mano

    Args:
        seme1 (str): seme della carta giocata dal giocatore1
        seme2 (str): seme della carta giocata dal giocatore2
        seme_di_briscola (str): seme della briscola
        numero1 (int): numero della carta giocata dal giocatore1
        numero2 (int): numero della carta giocata dal giocatore2
        carte_vinte1 (list): lista delle carte vinte dal giocatore1
        carte_vinte2 (list): lista delle carte vinte dal giocatore2
        valore (dict): dizionario contenente coppie numero carta : valore della carta
    """
    if seme1 == seme2:
        if valore[numero1] >= valore[numero2]:
            carte_vinte1.append(valore[numero1])
            carte_vinte1.append(valore[numero2])
            print("Vince il giocatore 1")
        else:
            carte_vinte2.append(valore[numero1])
            carte_vinte2.append(valore[numero2])
            print("Vince il giocatore 2")
    
    else:
        if seme1 == seme_di_briscola and seme2 != seme_di_briscola:
            carte_vinte1.append(valore[numero1])
            carte_vinte1.append(valore[numero2])
            print("Vince il giocatore 1")
        elif seme1 != seme_di_briscola and seme2 == seme_di_briscola:
            carte_vinte2.append(valore[numero1])
            carte_vinte2.append(valore[numero2])
            print("Vince il giocatore 2")
        else:
            carte_vinte1.append(valore[numero1])
            carte_vinte1.append(valore[numero2])
            print("Vince il giocatore 1")


def calcolo_punteggio(carte_vinte1: list, carte_vinte2: list):
    """Restituisce una tupla contenente un valore uguale a 1 in corrispondenza dell'esito della partita.
    (Vittoria del giocatore1, Vittoria del giocatore2, Pareggio)

    Args:
        carte_vinte1 (list): lista delle carte vinte dal giocatore1
        carte_vinte2 (list): lista delle carte vinte dal giocatore2

    Returns:
        vittoria1 (int): vero se uguale a 1
        vittoria2 (int): vero se uguale a 1
        pareggio (int): vero se uguale a 1
    """
    punti1 = 0
    punti2 = 0
    vittoria1 = 0
    vittoria2 = 0
    pareggio = 0

    for i in carte_vinte1:
        punti1 += i
    for j in carte_vinte2:
        punti2 += j

    if punti1 > punti2:
        vittoria1 += 1
        print(f"Vince il giocatore 1. {punti1} - {punti2}")
        print(f"Carte1: {[x for x in carte_vinte1 if x != 0]}")
        print(f"Carte2: {[x for x in carte_vinte2 if x != 0]}")
    elif punti1 < punti2:
        vittoria2 += 1
        print(f"Vince il giocatore 2. {punti1} - {punti2}")
        print(f"Carte1: {[x for x in carte_vinte1 if x != 0]}")
        print(f"Carte2: {[x for x in carte_vinte2 if x != 0]}")
    else:
        pareggio += 1
        print("Pareggio.")
        print(f"Carte1: {[x for x in carte_vinte1 if x != 0]}")
        print(f"Carte2: {[x for x in carte_vinte2 if x != 0]}")

    return(vittoria1, vittoria2, pareggio)

def pescata_carte(mazzo: list, carte_giocatore: list):
    """Simula la pescata della prima carta del mazzo, la inserisce
    nelle carte in mano al giocatore e la rimuove dal mazzo

    Args:
        mazzo (list): mazzo con le carte disponibili
        carte_giocatore (list): lista delle carte in mano al giocatore
    """
    carta = mazzo[0]
    carte_giocatore.append(carta)
    mazzo.pop(0)

def cpu(carte_giocatore: list, carta_avv: tuple, briscola: tuple, valori: dict):
    seme_di_briscola = briscola[1]
    numero1 = carta_avv[0]
    seme1 = carta_avv[1]

    for carta in carte_giocatore:
        numero2 = carta[0]
        seme2 = carta[1]
        # se l'avversario ha una briscola
        if seme1 == seme_di_briscola:
            if seme2 == seme_di_briscola and valori[numero2] > valori[numero1]:
                carte_giocatore.remove(carta)
                return(carta)
            else:
                carta = min(carte_giocatore, key=lambda x:x[1])
                carte_giocatore.remove(carta)
                return(carta)
        else:
            # stesso seme, nessuna è briscola
            if seme2 == seme1 and seme1 != seme_di_briscola and seme2 != seme_di_briscola:
                if valori[numero2] > valori[numero1]:
                    carte_giocatore.remove(carta)
                    return(carta)
                else:
                    carta = min(carte_giocatore, key=lambda x:x[1])
                    carte_giocatore.remove(carta)
                    return(carta)
            else: # seme diverso
                if seme2 == seme_di_briscola:
                    carte_giocatore.remove(carta)
                    return(carta)
                else:
                    carta = min(carte_giocatore, key=lambda x:x[1])
                    carte_giocatore.remove(carta)
                    return(carta)

def prima_carta_mazzo(mazzo: list, carte_giocatore: list):
    carta = mazzo[0]
    carte_giocatore.append(carta)
    mazzo.pop(0)
    return(mazzo, carte_giocatore)

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
        numero2, seme2 = cpu(carte_gioc2, (numero1, seme1), briscola, carichi)
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
    numero2, seme2 = cpu(carte_gioc2, (numero1, seme1), briscola, carichi)
    print(f"Il giocatore 2 gioca la carta {numero2} di {seme2}.")

    vittoria_mano(seme1, seme2, seme_di_briscola, numero1, numero2, carte_vinte1, carte_vinte1, carichi)
    
    # pescata carte
    carte_gioc1.append(mazzo[0])
    mazzo.pop(0)
    carte_gioc2.append(briscola)

    carte_rimaste_gioco = len(carte_gioc2)
    while carte_rimaste_gioco > 0:
        print("-----------------------------------------------------")
        print(f"Briscola: {briscola}")

        print(f"Le tue carte {carte_gioc1}")
        giocata1 = int(input("Quale carta vuoi giocare(1,2,3): "))-1
        numero1, seme1 = carte_gioc1[giocata1]
        carte_gioc1.pop(giocata1)
        print(f"Il giocatore 1 gioca la carta {numero1} di {seme1}.")
        numero2, seme2 = cpu(carte_gioc2, (numero1, seme1), briscola, carichi)
        print(f"Il giocatore 2 gioca la carta {numero2} di {seme2}.")
        carte_rimaste_gioco -= 1

        vittoria_mano(seme1, seme2, seme_di_briscola, numero1, numero2, carte_vinte1, carte_vinte1, carichi)
        
    vittoria1, vittoria2, pareggio = calcolo_punteggio(carte_vinte1, carte_vinte2)
    return(vittoria1, vittoria2, pareggio)

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
        prima_carta_mazzo(mazzo, carte_gioc_1)
        prima_carta_mazzo(mazzo, carte_gioc_2)
        carte_rimaste -= 2

    return(briscola, mazzo, carte_gioc_1, carte_gioc_2, carte_rimaste)

