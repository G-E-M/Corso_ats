# Scrivere una funzione che data una stringa definisca se questa é
# una parola (si definisce parola una concatenazione di sole
# lettere.):
from typing import List


def parola(par):
    #setto la stringa di controllo vuota
    strControllo = " "
    #variabile di controllo while
    i=0
    while i<len(par):
        if par[i] != strControllo[0]:
            print("Verifico se la lettra n° "+par[i]+" è uno \"spazio\"")
            i+=1
        else:
            print(" Non è una parola")
            break


# Scrivere una funzione che data una lista di stringhe restituisca la
# lista delle sole parole distinte presenti tra le stringhe.

def lista(lista1):
    i = 0
    while i < len(lista1) :
        
        #controllo if di lista1 alla posizione i 
        contr= lista1[i]
        
        #Tramite .count mi controlla quante volte è presente contr 
        #che equivale all'elemento della lista alla posizione i
        
        if lista1.count(contr) > 1:
            
            fif=False
            break
        else:
            
            fif=True

        i+=1
        
    if fif==False :
        print("Ci sono ripetizioni")
    else:
        print("Non sono presenti ripetizioni")

        
# Scrivere una funzione che simuli l’estrazione del superenalotto (vedere
# modulo random)

def random1():
    i= 0
    import random
    #Mi crei un elenco che va da 1 a 100 (range) e nu faccio restituire k elementi
    #univoci
    a = random.sample(range(1,100), k=99)
    a.sort()
    while i < 8:
        
        estrazione = random.choice(a)
        print(estrazione)
        i+=1

# Scrivere una funzione python che prende come argomento un dizionario in cui
# ogni chiave `e una stringa ed il valore `e un intero. 
# La funzione restituisce la lista ordinata di
# tutte le chiavi a cui corrisponde un valore pari.
# Ad esempio, per il dizionario
# {’topolino’:12, ’pluto’:3, ’minnie’:7, ’pippo’:4, ’qui’:3}
# la funzione deve restituire la lista
# [’pippo’,’topolino’]

def dizionario():

    dizionario1 = {'topolino':12, 'pluto':3, 'minnie':7, 'pippo':4, 'qui':3}

    lista = list()
    for k in dizionario1.keys():
        i = int(dizionario1[k])
        if(i%2==0):
            list.append(k)
    lista.sort()
    return lista
    #copiato da Francesco Aroldo 
    
# Scrivete una funzione che disegni una griglia come questa:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def quadrato():
    i=0
    #Creo un ciclo che mi stampa il quadrato
    
    while i <= 10:
        
        if i == 0 or i == 5 or i == 10:
            print("+ - - - - + - - - - +")
            i+=1
        else:
            print("|         |         |")
            i+=1  
        
            
# 2. Scrivete una funzione che disegni una griglia simile, con quattro righe e quattro colonne.
# + - - - - + - - - - + - - - - + - - - - +
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# + - - - - + - - - - + - - - - + - - - - +
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# + - - - - + - - - - + - - - - + - - - - +
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# + - - - - + - - - - + - - - - + - - - - +
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# |         |         |         |         |
# + - - - - + - - - - + - - - - + - - - - +

def quadrato4():
    i=0
    #Creo un ciclo che mi stampa il quadrato
    
    while i <= 20:
        if i == 0 or i == 5 or i == 10 or i == 15 or i == 20:
            print("+ - - - - + - - - - + - - - - + - - - - +")
            i+=1
        else:
            print("|         |         |         |         |")
            i+=1