numero1 = int(input('Inserisci il primo valore: '))
numero2 = int(input('Inserisci il secondo valore: '))
numero3 = int(input('Inserisci il terzo valore: '))


if numero1 > numero2:
    if numero1>numero3:
        print (numero1, ' è il numero maggiore')
        
else:
    if numero2>numero3:
        print (numero2, ' è il numero maggiore')
    else:
        print (numero3, ' è il numero maggiore')

