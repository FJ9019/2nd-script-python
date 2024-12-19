#coding: utf-8

def generate_mystery_word(dictionnaire):
    
    import random
    
    mot = random.choice(dictionnaire)
    mot_len = len(mot)
    mystere = ""
    
    for i in range(mot_len):
        if i%2 == 0:
            mystere += mot[i]
        else:
            mystere += "*"
            
    return mot, mystere

def check_it(mystere, mot, user_try):
    status = False
    msg = None
    if not len(user_try) == len(mot):
        msg = f"Déslé vous devez entré un mot contenant {len(mot)} caractères !"
        return status, msg, mystere
    
    if mot_utilisateur != mot:
        mystere_backup = mystere
        mystere = ""
        for i in range(mot_len):
            if mot_utilisateur[i] == mot[i]:
                if i>0:
                    if mot[i-1] ==mot_utilisateur[i-1]:
                        mystere += mot[i]
                    else:
                        mystere += mystere_backup[i]
                else:
                    mystere += mystere_backup[i]
            else:
                mystere += mystere_backup[i]
        print(f"Désolé le mot entré ne correspond pas !")                            
    
print(generate_mystery_word(["secret", "cacher", "mystere"]))