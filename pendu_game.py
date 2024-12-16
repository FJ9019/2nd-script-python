#coding: utf-8

dictionnaire = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

mot = dictionnaire[3]
mot_len = len(mot)
mystere = ""

loop = True

for i in range(mot_len):
    if i%2 == 0:
        mystere += mot[i]
    else:
        mystere += "*"
     


while loop:
    print(mystere)
    mot_utilisateur = input(f"Quel est le mot caché !")
    
    if not len(mot_utilisateur) == mot_len:
        print(f"Déslé vous devez entré un mot contenant {mot_len} caractères !")
    
    else:    
        if mot_utilisateur != mot:
            mystere_backup = mystere
            mystere = ""
            for i in range(mot_len):
                if mot_utilisateur[i] == mot[i]:
                    mystere += mot[i]
                else:
                    mystere += mystere_backup[i]    
            print(f"Désolé le mot entré ne correspond pas !")
        else:
            print(f"Bravo le mot entré est bien : {mot} !")
            loop = False