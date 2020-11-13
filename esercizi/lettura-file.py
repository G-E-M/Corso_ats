import os.path
FILE_PATH = ‘/home/danilo/Documenti/contatti.txt’
if not os.path.isfile(FILE_PATH):
 contact_file = open(FILE_PATH, ‘w’) # Se il file non esiste lo creo
else:
 contact_file = open(FILE_PATH, ‘a’) # Se esiste lo apro in append
# Inserisco un contatto
identifier = input("Inserire un id:")
name = input("Inserire il nome:")
surname = input("Inserire il cognome:")
CONTACT_ROW = "{};{};{}\n"
contact_file.write(CONTACT_ROW.format(identifier, name, surname))
contact_file.close()
# Stampo la lista di contatti
contact_file = open(FILE_PATH, 'r')
print('ID', 'Nome', 'Cognome', sep='\t')
for line in contact_file:
 print(line.replace(';', '\t\t'))
contact_file.close()