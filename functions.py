import random

def vittoria_mano(seme1: str, seme2: str, seme_di_briscola: str, numero1: int, numero2: int, carte_vinte1: list, carte_vinte2: list, carichi: dict):
    """Popola le liste che contengono le carte vinte da ogni giocatore ad ogni mano

    Args:
        seme1 (str): seme della carta giocata dal giocatore1
        seme2 (str): seme della carta giocata dal giocatore2
        seme_di_briscola (str): seme della briscola
        numero1 (int): numero della carta giocata dal giocatore1
        numero2 (int): numero della carta giocata dal giocatore2
        carte_vinte1 (list): lista delle carte vinte dal giocatore1
        carte_vinte2 (list): lista delle carte vinte dal giocatore2
        carichi (dict): dizionario contenente coppie numero carta : valore della carta
    """
    if seme1 == seme2:
        if carichi[numero1] > carichi[numero2]:
            carte_vinte1.append(carichi[numero1])
            carte_vinte1.append(carichi[numero2])
        else:
            carte_vinte2.append(carichi[numero1])
            carte_vinte2.append(carichi[numero2])
    
    else:
        if seme1 == seme_di_briscola and seme2 != seme_di_briscola:
            carte_vinte1.append(carichi[numero1])
            carte_vinte1.append(carichi[numero2])
        else:
            carte_vinte2.append(carichi[numero1])
            carte_vinte2.append(carichi[numero2])


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
        print(f"Carte1: {carte_vinte1}")
        print(f"Carte2: {carte_vinte2}")
    elif punti1 < punti2:
        vittoria2 += 1
        print(f"Vince il giocatore 2. {punti1} - {punti2}")
        print(f"Carte1: {carte_vinte1}")
        print(f"Carte2: {carte_vinte2}")
    else:
        pareggio += 1
        print("Pareggio.")
        print(f"Carte1: {carte_vinte1}")
        print(f"Carte2: {carte_vinte2}")

    return(vittoria1, vittoria2, pareggio)


def giocata_carte(carte_giocatore: list):
    """Simula in modo randomico la giocata di una carta ad ogni turno da parte di un giocatore

    Args:
        carte_giocatore (list): lista delle carte attualmente in mano al giocatore

    Returns:
        numero (int): numero della carta giocata
        seme (str): seme della carta giocata
    """
    giocata = random.choice(carte_giocatore)
    numero, seme = giocata
    carte_giocatore.remove(giocata)
    return (numero, seme)


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






