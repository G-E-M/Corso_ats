class Product:
    def __init__(self,id,titolo,prezzo):
        self.id=id
        self.titolo=titolo
        self.prezzo=prezzo 

    def __str__(self):
        return " '{}' '{}' '{}' '{}' ".format(self.id, self.titolo,self.prezzo)


class Book(Product):
    def __init__(self,id,titolo,autore,prezzo):
        super().__init__(id,titolo,prezzo)
        self.autore=autore
    def __str__(self):
        return " '{}' '{}' '{}' '{}' ".format(self.id, self.titolo, self.autore,self.prezzo)


class Dvd(Product):
    def __init__(self,id,titolo,prezzo,produzione):
        super().__init__(id,titolo,prezzo)
        self.produzione=produzione
    def __str__(self):
        return " '{}' '{}' '{}' '{}' ".format(self.id, self.titolo, self.produzione,self.prezzo)

class Magazine(Product):
    def __init__(self,id,titolo,prezzo,casa):
        super().__init__(id,titolo,prezzo)
        self.casa=casa
    def __str__(self):
        return " '{}' '{}' '{}' '{}' ".format(self.id, self.titolo, self.casa,self.prezzo)

        