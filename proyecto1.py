
class Persona:

    def _init_ (self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI


        
    def mostrar(self):
     print (f"mi nombre es {self.nombre}, tengo un total de {self.edad} años y mi DNI es {self.DNI}")

    def elmayores (self):
        if self.edad >=18:
            return "YA ES MAYOR"
        
        else:
            return "ES MENOR"
        

person = Persona("juan de raul",18,696969)
person.mostrar()
print(person.elmayores())