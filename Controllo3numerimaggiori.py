numero1 = int(input('Inserisci il primo valore: '))
numero2 = int(input('Inserisci il secondo valore: '))
numero3 = int(input('Inserisci il terzo valore: '))


if (numero1 > 0)and (numero2>0)and(numero3>0):
    if (numero1 < (numero2+numero3)) and (numero2<(numero1+numero3))and(numero3<(numero1+numero2)):
        print ('si')
    else:
        print ('no')
else:
    print ('no')
