class Persona:

    def _init_(self, Nombre, edad):
        self.Nombre=Nombre
        self.edad=edad

    def set_nombre(self,Nombre):
        self.Nombre = Nombre

    def set_edad (self,edad):
        self.edad = edad

    def get_nombre(self):
        return self.Nombre
    
    def get_edad(self):
        return self.edad
    
    def exponer_per(self):
        print(f"su Nombre es{self.Nombre} y su edad es {self.edad} años")
        
    def ya_es_mayor(self):
        if self.edad >= 18:
            return  "ES MAYOR DE EDAD"
        else:
            return   "TODAVIA NO ES MAYOR"
    
    def Es_mayor(self,sujeto_2):
        if self.edad > sujeto_2.get.edad():
            return "AFIRMATIVO"
        else:
            return "NEGATIVO"
        
sujeto1= Persona("Andres", 20) 
sujeto2 = Persona("Julio", 17)

sujeto1.exponer_per()
sujeto2.exponer_per()

print(f"{sujeto1.get_edad()} tiene la mayoria de edad{sujeto1.ya_es_mayor()} ")
print(f"{sujeto2.get_edad()} tiene la mayoria de edad{sujeto2.ya_es_mayor()} ")

print(f"{sujeto1.get_nombre()} es mayor que {sujeto2.get_nombre()}: {sujeto1.es_mayor_que(sujeto2)}")
print(f"{sujeto2.get_nombre()} es mayor que {sujeto1.get_nombre()}: {sujeto2.es_mayor_que(sujeto1)}")