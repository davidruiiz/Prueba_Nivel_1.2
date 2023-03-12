
class Nodo(object):
    """Clase nodo simplemente enlazado."""

    info, sig = None, None
    aux = Nodo()
    aux.info = "Primer nodo"
    palabra = input("Ingrese una palabra: ")
    naux = aux
    while(palabra != ""):
        nodo = Nodo()
        nodo.info = palabra
        naux.sig = nodo
        naux = nodo
        palabra = input("Ingrese una palabra: ")

    while (aux is not None):
        print(aux.info)
        aux = aux.sig

class datoPolinomio(object):
    """Clase polinomio."""

    def __init__(self):
        """Crea un polinomio de grado 0."""
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
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = obtener_valor(polinomio1, i) + obtener_valor(polinomio2, i)
            if(total != 0):
                agregar_termino(paux, i, total)
        return paux
    
    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomio y devuelve el resultado."""
        paux = Polinomio()
        pol1 = polinomio.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if(obtener_valor(paux,termino) != 0):
                    valor += obtener_valor(paux, termino)
                    modificar_termino(paux, termino, valor)
                else:
                    agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    

