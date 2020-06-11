class IObservador(object):
    def Actualizar(mensaje : str):
        pass

class Observador(IObservador):
    def __init__(self, name):
        self.name = name

    def Actualizar(self, mensaje : str):
        print('[' + self.name + '] Mensaje recibido desde el objeto observado:' + mensaje)

class ObjetoObservado(object):
    
    def __init__(self):
        self.ListaElementos = []
        self.ListaObservadores = []
    
    def Suscribir(self, pvObjObservador : IObservador):
        self.ListaObservadores.append(pvObjObservador)

    def Notificar(self, mensaje : str):
        for x in self.ListaObservadores:
            x.Actualizar(mensaje)

    def AdicionarElemente(self, elemento : str):
        self.ListaElementos.append(elemento)
        self.Notificar(elemento)

    def ListarElementos(self):
        print('Los elementos de la lista son:')
        for elemento in self.ListaElementos:
            print(' - ' + elemento)


vObjObservado = ObjetoObservado()
vObjObservador = Observador("Pepito")
vObjObservador2 = Observador("Juanito")

vObjObservado.Suscribir(vObjObservador)
vObjObservado.AdicionarElemente('Pera')
vObjObservado.Suscribir(vObjObservador2)
vObjObservado.AdicionarElemente('Manzana')
vObjObservado.ListarElementos()


