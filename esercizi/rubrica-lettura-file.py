import os.path


PATH_PATH = 'C:/Users/LP/Documents/GitHub/Corso_ats/file.txt'

selezione = 1

if not os.path.isfile(PATH_PATH):
    contact_file = open(PATH_PATH, 'w') # Se il file non esiste lo creo
else:
    contact_file = open(PATH_PATH, 'a') # Se esiste lo apro in append

def defaultSection():
    print("Selezione non valida!!!") 

def print_menu():
    print("/***************************************")
    print("*","1)Visualizza contatti",sep="\t")
    print("*","2)Inserisci nuovo contatto",sep="\t")
    print("*","3)Stampa questo menu",sep="\t")
    print("*","4)esci",sep="\t")

def stampa_contatto():
    contact_file = open(PATH_PATH, 'r')
    print('ID', 'Nome', 'Cognome', sep='\t')
    for line in contact_file:
        print(line.replace(';', '\t\t'))
    contact_file.close()
    
def aggiungi_contatto():
    identifier = input("Inserire un id:")
    name = input("Inserire il nome:")
    surname = input("Inserire il cognome:")
    CONTACT_ROW = "{};{};{}\n"
    contact_file.write(CONTACT_ROW.format(identifier, name, surname))
    contact_file.close()
    
def esci():
    uscita = True

def section(selezione):
    switcher = {
        1: stampa_contatto,
        2: aggiungi_contatto,
        3: print_menu,
        4: esci,
    }
    return switcher.get(selezione,defaultSection)
    print_menu()


print_menu()

while selezione != 4:
    selezione= int(input("Selezione"))
    section(selezione)()

    



