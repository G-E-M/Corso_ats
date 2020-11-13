class Libreria:
    def __init__(self):
        self.prodotti=[]
        self.qt={}


    def add(self,prod,qt):
        self.prodotti.append(prod)
        self.qt[prod.id]=qt
    
    def print_menu():
        print("________________________")
        print("1. Mostra Prodotti")
        print("2. Acquista Prodotto")
        print("3. Menu")
        print("q. Esci")
        print("_______________________")

    def warehouse(self):
        for i in self.prodotti:
            if(self.qt[i.id]==0):
                print("ID:",i," Quantità: Non Disponibile")
            else:
                print("ID:",i," Quantità: ",self.qt[i.id])
    

    """def buy(self,identify):
        for i in self.prodotti:
            if((identify==i.id)and(self.qt[i])) """
        
        