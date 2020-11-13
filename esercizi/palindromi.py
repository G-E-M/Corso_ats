nome1 = str(input('inserisci il primo nome: '))
nome2 = str(input('inserisci il secondo nome: '))

i = 0 
j=0
flag = True

if len(nome1) == len(nome2):
   while i < (j - 1):
       if nome1[i] == nome2[j-1]:
           i += 1
           j += 1
       else:
            flag = False
            break 
if flag == True:
    print('Stringa palindroma')
else:
    print('Stringa palindroma')

stop = int(input(''))

