import calcolatrice
from calcolatrice import Animale  

print(calcolatrice.addizione(12,34))
################################################
#Variabile

cane = "pippo"

#Costruttore

cane2= calcolatrice.Animale(cane)

#Istanza

cane2.stampa_animale()

################################################

cane3nome= "apppoiskj"
cane3 = Animale(cane3nome)
cane3.stampa_animale()

################################################

#riasegnamento della variabile cane

cane = "Andromeda"
caneA = Animale(cane)
caneA.stampa_animale()

################################################

#Nella istanza caneA vado a riassegnare l'attributo nome (presente dove ho definito la classe) 
caneA.nome= "zippo"
#Richiamando stampa_animale() stampera anche zippo
caneA.stampa_animale()

################################################


################################################