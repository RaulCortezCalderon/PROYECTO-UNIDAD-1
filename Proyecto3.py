#Andres flores aguirre
#Raul cortez calderon
#Julio santana navarro piceno
shorts = 55
pantalones = 65
playeras = 100
class ropas:
    def _init_(self,short,pantalon,playera):
        self.short = short
        self.pantalon = pantalon
        self.playera = playera

prenda = input('Que desea comparar? \nshort \npantalon \nplayera\n')

if prenda == 'short':
    total=int(input('Que cantidad desea del mismo?'))
    preciosS = total*55
    existencia = shorts-total
    print (f'El pago de su compra es {preciosS} pesos')

if prenda == 'pantalon':
    total=int(input('Ingrese la cantidad que desea comprar'))
    preciosP=total*65

    print (f'Su pago final de su compra es {preciosP} pesos')


if prenda == 'playera':
    total=int(input('Cantidad que desea adquirir'))
    precioP=total*100

    print(f'Su pago final es de {precioP} pesos')