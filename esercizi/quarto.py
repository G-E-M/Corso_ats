deposito = float(input('Dimmi quanti soldi hai: '))
anni = float(input('Quanti anni devo calcolare: '))
interesse = float (input('A quanto ammonta il tasso di ladreggio ?: '))
calcoloInteresse= deposito*(1+interesse*anni)
print ('Il tuo deposito:',deposito,'$' ,'Il risultato del tuo tasso di interesse è: ',round (calcoloInteresse, 2))


