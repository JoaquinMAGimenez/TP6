#cola.py


from distutils.log import info


class nodoCola():
    info, sig = None, None
    
class Cola():
    
    def __init__(self):
        
        self.__frente = None
        self.__final = None
        self.__tamanio = 0
    
    def arribo (self , dato):
            nodo=nodoCola()
            nodo.info=dato
            
            if self.__final is None:
                self.__frente = nodo
                self.__final = nodo
             
            else:
               self.__final.sig = nodo
            self.__final = nodo 
            
            self.__tamanio +=1
 
    def tamanio(self):
        return self.__tamanio
    
    def atencion(self):
        dato = self.__frente.info
        
        self.__frente= self.__frente.sig
        
        if( self.__frente is None ):
            self.__final = None
        
        self.__tamanio -= 1
        return dato

    def mover_al_final (self):
        dato= self.atencion()
        return dato
    
    def cola_vacia (self):
        return self.__frente is None

            
c =Cola ()

from random import randint

for i in range(10):
    c.arribo(randint(0,100))

for i in range(c.tamanio()):
    print(c.mover_al_final())
                    
print("tamanio" , c.tamanio)


