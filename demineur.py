import random
 
mines = set()           #on crée un set car l'une de ses propriétés consiste à ne pas avoir deux fois la même coordonnée
mines2 = set()
 
def demo(n, k):
    """Cette fonction a pour but des grilles de taille n avec k bombes.
    Elle permet de placer les bombes et les numéros autour de celles ci 
    Args: n entier positif -> taille de la grille
          k entier positif -> nombre de bombes"""
    arr = [[0 for ligne in range(n)] for colonne in range(n)]  #arr est une matrice 
    while len(mines)< k:
        x_random = random.randint(0,n-1)
        y_random = random.randint(0,n-1)
        mines.add((x_random, y_random))  #rajoute les coordonées créées aléatoirement dans le set
 
    for mine in mines:  
        x, y =mine
        arr[y][x] = 'X' 
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):          
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # centre droit
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # centre gauche
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # haut gauche
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # haut droit
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # haut centre
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bas droite
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bas gauche
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bas milieu
    for ligne in arr:
        print("\t".join(str(cell) for cell in ligne)) # permet de faire des tabulaions sur une même ligne pour espacer les bombes et les bombes
        print("")           #permet de faire un espace entre chaque lignes
if __name__ == "__main__":  #Affiche les demos des 3 niveaux possibles
    print("=====DEBUTANT=====")
    demo(5, 3) #niveau debutant
    print("=======================")
 
    print("=====INTERMEDIAIRE=====")
    demo(6, 8) #niveau intermediaire
    print("================")
 
    print("=====EXPERT=====")
    demo(8, 20) #niveau expert
    print("================")
 
 
def Generateur_bombe_grille(n, k):
    """Cette fonction a pour but des grilles de taille n avec k bombes.
    Elle permet de placer les bombes et les numéros autour de celles ci 
    Args: n entier positif -> taille de la grille
          k entier positif -> nombre de bombes
    Returns: une grille de taille n*n avec k bombes"""
    arr = [[0 for ligne in range(n)] for colonne in range(n)]
    while len(mines2)< k:
        x_random = random.randint(0,n-1)
        y_random = random.randint(0,n-1)
        mines2.add((x_random, y_random))
 
    for mine in mines2:
        x, y =mine
        arr[y][x] = 'X'
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # centre droit
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # centre gauche
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # haut gauche
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # haut droite
 
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # haut centre
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bas droite
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bas gauche
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bas milieu
    return arr
def Generateur_grille_joueur(n):
    """Affiche des "-" partout pour cacher les bombes et les chiffres qui ne sont pas encore découverts
    Args: n entier positif -> taille de la grille
    Return: la grille "cachée" """
    arr = [['-' for ligne in range(n)] for colonne in range(n)]
    return arr
def Afficher_grille(grille):
    """Ajoute des epaces entre chaque lignes et chaque cellules 
    Args: grille liste"""
    for ligne in grille:
        print("\t".join(str(cell) for cell in ligne)) #.join permet d'ajouter des espaces entre chaque cellules 
        print(" ")
def Verifie_victoire(grille):
    """parcourt la grille et tant qu'il y a encore des "-", la partie n'est pas finie
    Args : grille liste 
    Return: booléen"""
    for ligne in grille:
        for cell in ligne:
            if cell == '-':
                return False
    return True
def Continue_partie(score):
    """A la fin d'une partie cette fonction affiche son score et permet de rejouer ou non
    Args score entier positif
    Return: booléen"""
    print("Ton score: ", score)
    On_continue = input("Veux tu rejouer? (oui/non) :")
    if On_continue == 'non':
        return False
    return True
def Game():
    """Permet à l'utilisateur de rentrer les coordonnées qu'il souhaite pour jouer"""
    Partie_en_cours = True
    while Partie_en_cours:
        difficulty = input("Selectionne ta difficulte (d, i, e):")  
        if difficulty.lower() == 'd':           #.lower() permet d'accepter les majuscules (D/I)
            n = 5
            k = 3
        elif difficulty.lower() == 'i':
            n = 6
            k = 8
        else:
            n = 8
            k = 20
 
        grille_demineur = Generateur_bombe_grille(n, k)
        grille_joueur = Generateur_grille_joueur(n)
        score = 0
        while True:
            if Verifie_victoire(grille_joueur) == False:  #tant qu'il reste des "-" sur la grille on propose d'ouvrir une cellule
                print("Entre la case que tu veux ouvrir :")
                print("X ( 1 a", n,")")
                print("Y ( 1 a", n,")")
                x = input("X= ")
                y = input("Y= ")
                x = int(x) - 1 # adaptation pour parcourir la liste en langage python (1 à 8 devient 0 à 7)
                y = int(y) - 1 
                if (grille_demineur[y][x] == 'X'):
                    print("Game Over!")
                    Afficher_grille(grille_demineur)
                    Partie_en_cours = Continue_partie(score)
                    break
                else:
                    grille_joueur[y][x] = grille_demineur[y][x]
                    Afficher_grille(grille_joueur)
                    score += 1
 
            else:
                Afficher_grille(grille_joueur)
                print("Bravo!")
                Partie_en_cours = Continue_partie(score)
                break
# Commence le programme
if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt: #ctrl C to interrupt
        print('\nFin du game. tchao!')
 

