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
    
    if user_try != mot:
        mystere_backup = mystere
        mystere = ""
        for i in range(len(mot)):
            if user_try[i] == mot[i]:
                if i>0:
                    if mot[i-1] ==user_try[i-1]:
                        mystere += mot[i]
                    else:
                        mystere += mystere_backup[i]
                else:
                    mystere += mystere_backup[i]
            else:
                mystere += mystere_backup[i]
        msg = f"Désolé le mot entré ne correspond pas !"
        return status, msg, mystere
    
    msg = f"Félicitation vous avez trouvé le mot caché : {mot}"
    status = True
    return status, msg, mystere

def play(dictionnaire=["test", "mystere"]):
    mot, mystere = generate_mystery_word(dictionnaire)
    loop = False
    
    while not loop: 
        print(mystere)
        user_try = input(f"Quel est le mot caché ?")
        loop, msg, mystere = check_it(mystere, mot, user_try)
        print(msg)
    
dictionnaire = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

play(dictionnaire)