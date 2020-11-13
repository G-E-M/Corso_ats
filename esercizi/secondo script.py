km = float(input('quanti km hai fatto ?'))
minuti = float(input('quanti minuti hai corso ?'))
secondi = float(input('quanti secondi hai corso ?'))

secondiTotali = (minuti*60)+ secondi

metri = km*1000

m_s = metri/secondiTotali

migliaPercorse = metri/1609.344

migliaOrarie = migliaPercorse*3600 /secondiTotali

km_h = km * 3600 /secondiTotali


print ("Velocità:",round(m_s),"m/s")
print ("Velocità:",round(km_h, 2),"Km/h")
print ("Velocità mph:",round(migliaOrarie, 2),"mph")
