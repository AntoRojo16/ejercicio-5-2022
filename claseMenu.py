from ManejadorPlanes import Lista
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            3:self.opcion4,
                            0:self.salir
                          }
    def opcion(self,op,lista,):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(lista)

    def salir(self,lista):
        print('Usted salio del programa')
    def opcion1(self,lista,):
        lista.actualizarValorVehivulo()


    def opcion2(self,lista):
        valor=input("Ingrese un valor >>")
        lista.MostrarValoresInferiores(valor)

    def opcion3(self,lista):
        lista.unLista.MontoParaLicitar()

    def opcion4(self,lista):
        codigo=input("Ingresar el codigo >>")
        lista.modificarCantidadCuotas(codigo)



        
