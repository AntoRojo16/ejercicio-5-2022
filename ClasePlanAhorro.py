class PlanAhorro:
    __CodigoPla=""
    __Modelo=""
    __Version=""
    __ValorVehiculo=""
    CantCuotas=60
    CantCuotasLicitar=10

    def __init__(self,cod,modelo,version,valor):
        self.__CodigoPla=cod
        self.__Modelo=modelo
        self.__Version=version
        self.__ValorVehiculo=valor


    def getCodigo(self):
        return self.__CodigoPla

    def getModelo(self):
        return self.__Modelo

    def getVersion(self):
        return self.__Version

    def getValorVehiculo(self):
        return self.__ValorVehiculo

    @classmethod
    def getCanCuotas(cls):
        return cls.CantCuotas
    @classmethod
    def getLicitar(cls):
        return cls.CantCuotasLicitar

    def modificarValorVehiculo(self,valor):
        self.__ValorVehiculo=valor


    def __str__(self):
        return ("Codigo de plan {},  Modelo de Vehiculo {}, Version de vehiculo {}, Valor del vehiculo{}, Cantidad de cuotas del plan {}, Cantidad de cuotas a pagar para licitar {}".format(self.__CodigoPla,self.__Modelo,self.__Version,self.__ValorVehiculo,self.getCanCuotas(),self.getLicitar()))


    def CalcularImporteCuota(self):
        importe=(int(self.__ValorVehiculo)/int(self.getCanCuotas()))+(int(self.__ValorVehiculo)*0.10)
        return importe

    @classmethod
    def cambiarCantidadCuotas(cls,valor):
        cls.CantCuotasLicitar=valor




