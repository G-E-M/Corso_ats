anni = int(input('inserisci anno'))

if anni % 4 == 0 and (anni%100 !=0 or anni % 400 == 0):
    print('si')
else:
    print('no')
    
