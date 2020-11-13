#%%
class Persona:
    def __init__(self,age,nome,cognome):
        self.age = age
        self.nome= nome
        self.cognome = cognome
    
    @property
    def age(self):
        return self.__age
    def nome(self):
        return self.__nome

    @age.setter
    def age (self, age):
        if age > 0 and age % 2 == 0 :
            self.__age = age
        else:
            self.__age = 2
    
    
#%%
