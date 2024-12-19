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
    
print(generate_mystery_word(["secret", "cacher", "mystere"]))