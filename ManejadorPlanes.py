import csv
import math
from ClasePlanAhorro import PlanAhorro
class Lista:

    def __init__(self):
        self.__lista=[]

    def agregarPlan(self,plan):
        self.__lista.append(plan)

    def CrearLista(self):

        archivo = open("PlanDeAhorro.csv")
        reader=csv.reader(archivo,delimiter=";")

        for fila in reader:
            cod=fila[0]
            modelo=fila[1]
            version=fila[2]
            valor=fila[3]
            unPlan=PlanAhorro(cod,modelo,version,valor)
            self.agregarPlan(unPlan)
        archivo.close()

    def __str__(self):
        s=""
        for plan in self.__lista:
            s += str(plan)+"\n"
        return s


    def actualizarValorVehivulo(self):

        for plan in self.__lista:
            print("Codigo del plan >> {}".format(plan.getCodigo()))
            print("Modelo del vehiculo >> {}".format(plan.getModelo()))
            print("VErsion del vehiculo >> {}".format(plan.getVersion()))
            print("Valor del vehiculo >>{}".format(plan.getValorVehiculo()))
            valor=input("Ingrese el valor actual del vehiculo >>")
            plan.modificarValorVehiculo(valor)
            print("Valor del vehiculo >>{}".format(plan.getValorVehiculo()))


    def buscarPorCodigo(self,codigo):

        i=0
        unPlan=self.__lista[0]
        unCodigo=unPlan.getCodigo()
        while(unCodigo!=codigo):
            i +=1
            unPlan=self.__lista[i]
            unCodigo=unPlan.getCodigo()
        if i<int(len(self.__lista)):
            print("se encontro el plan")
            return i

    def mostrarValorCuotas(self):
        for plan in self.__lista:
            importe=plan.CalcularImporteCuota()
            print(importe)

    def MostrarValoresInferiores(self,valor):
        for plan in self.__lista:
            if (math.trunc(plan.CalcularImporteCuota())<int(valor)):
                print("Codigo del plan >> {}".format(plan.getCodigo()))
                print("Modelo del vehiculo >> {}".format(plan.getModelo()))
                print("VErsion del vehiculo >> {}".format(plan.getVersion()))


    def MontoParaLicitar(self):
        for plan in self.__lista:
            monto=(plan.getLicitar()*math.trunc(plan.CalcularImporteCuota()))
            print(monto)

    def modificarCantidadCuotas(self,codigo):
        i=self.buscarPorCodigo(codigo)
        cambio=input("Ingrese la nueva cantidad de cuotas")
        self.__lista[i].cambiarCantidadCuotas(cambio)
        print(self.__lista[i].getLicitar())




