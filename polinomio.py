
class Nodo(object):
    """Clase nodo simplemente enlazado."""

    info, sig = None, None

class datoPolinomio(object):
    """Clase  dato polinomio."""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y término."""
        self.valor = valor # coeficiente
        self.termino = termino # exponente


class Polinomio(object):
    """Clase polinomio."""

    def __init__(self):
        """Crea un polinomio del grado cero."""
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        """Agrega un término y su valor al polinomio."""
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and actual.sig.info.termino > termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        """Devielve el valor de un término del polinomio."""
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        """Deveulve el valor de un término del polinimio."""
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
        
    def eliminar_termino(polinomio, termino):
        """Elimina un término del polinomio."""
        aux = polinomio.termino_mayor
        if(aux is not None):
            if(aux.info.termino == termino):
                polinomio.termino_mayor = aux.sig
            else:
                while(aux.sig is not None and aux.sig.info.termino != termino):
                    aux = aux.sig
                if(aux.sig is not None):
                    aux.sig = aux.sig.sig
            
    def existe_termino(polinomio, termino):
        """Devuelve True si el término existe en el polinomio."""
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino == termino):
            return True
        else:
            return False
        
    def mostrar(polinomio):
        """Muestra el polinomio."""
        aux = polinomio.termino_mayor
        pol = ""
        if(aux is not None):
            while(aux is not None):
                signo = ""
                if(aux.info.valor > 0):
                    signo += "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol
    
    def sumar(polinomio1, polinomio2):
        """Suma dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        mayor = polinomio1 if polinomio1.grado > polinomio2.grado else polinomio2
        for i in range(0, mayor.grado + 1 ):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if(total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    
    
    def restar(polinomio1, polinomio2):
        """Resta dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        mayor = polinomio1 if polinomio1.grado > polinomio2.grado else polinomio2
        for i in range(0, mayor.grado + 1 ):
            total = Polinomio.obtener_valor(polinomio1, i) - Polinomio.obtener_valor(polinomio2, i)
            if(total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    
    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if Polinomio.obtener_valor(paux, termino) != 0:
                    valor += Polinomio.obtener_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def dividir (polinomio1, polinomio2):
        """Divide dos polinomios y devuelve el resultado."""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino - pol2.info.termino
                valor = pol1.info.valor / pol2.info.valor
                if Polinomio.obtener_valor(paux, termino) != 0:
                    valor += Polinomio.obtener_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux


    
    

p1 = Polinomio()
p1.agregar_termino(3, 4) # 4x^3
p1.agregar_termino(2, 3) # 3x^2

p2 = Polinomio()
p2.agregar_termino(2, 2) # 2x^2
p2.agregar_termino(4, 5) # 5x^4

print(p1.mostrar())
print(p2.mostrar())
print(p1.obtener_valor(2)) # Devuelve el valor del término 2
print(p1.obtener_valor(4)) # Devuelve el valor del término 4

p3 = Polinomio.sumar(p1, p2)
print(p3.mostrar())

p4 = Polinomio.restar(p1, p2)
print(p4.mostrar())

p5 = Polinomio.multiplicar(p1, p2)
print(p5.mostrar())

p1.eliminar_termino(3) 
print(p1.mostrar())

print(p1.existe_termino(3)) # Devuelve True si existe el término 3
print(p1.existe_termino(4)) # Devuelve True si existe el término 4

p6 = Polinomio.dividir(p1, p2)
print(p6.mostrar())

