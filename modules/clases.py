class Aerolinea:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def __str__(self):
        return f"{self.nombre} - {self.pais}"



class Persona:
    def __init__(self,identificacion,nombre,celular,coreo):
        self.identificacion=identificacion
        self.nombre=nombre
        self.correo=coreo
        self.celular=celular
    def mostrar(self):
        print("Identificacion: ",self.identificacion)
        print("Nombre: ",self.nombre)
        print("Celular: ",self.celular)

class Piloto(persona):
    def __init__(self,identificacion,nombre,celular,licencia,rango,horas_vuelo):
        super().__init__(identificacion,nombre,celular)
        self.licencia=licencia
        self.rango=rango
        self.horas_vuelo=horas_vuelo
    def mostrar(self):
        super().mostrar()
        print("Licencia: ",self.licencia)
        print("Rango: ",self.rango)
        print("Horas de vuelo: ",self.horas_vuelo)


class Pasajero(persona):
    def __init__(self,identificacion,nombre,celular,numero_millas):
        super().__init__(identificacion,nombre,celular)
        self.numero_millas=numero_millas
    def mostrar(self):
        super().mostrar()
        print("Numero de millas: ",self.numero_millas)

class Tripulacion(persona):
    def __init__(self,identificacion,nombre,edad,celular,funcion):
        super().__init__(identificacion,nombre,celular)
        self.edad=edad
        self.funcion=funcion
    def mostrar(self):
        super().mostrar()
        print("Funcion: ",self.funcion)


class Avion:
    def __init__(self,matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla):
        self.matricula=matricula
        self.modelo=modelo
        self.marca=marca
        self.anio=anio
        self.aerolinea=aerolinea
        self.capacidad_silla=capacida_silla
        self.horas_vuelo=horas_vuelo
        self.capacidad_pasajeros=[]

    def mostrar(self):
        print("Matricula: ",self.matricula)
        print("Modelo: ",self.modelo)
        print("Marca: ",self.marca)
        print("Año: ",self.anio)
        print("Horas de vuelo: ",self.horas_vuelo)

class Vuelo:
    def __init__(self,numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso):
        self.numero_vuelo=numero_vuelo
        self.origen=origen
        self.destino=destino
        self.fecha_ida=fecha_ida
        self.fecha_regreso=fecha_regreso
        self.hora_ida=hora_ida
        self.hora_regreso=hora_regreso
        self.tipo_vuelo=tipo_vuelo
    def mostrar(self):
        print("Numero de vuelo: ",self.numero_vuelo)
        print("Tipo de vuelo: ",self.tipo_vuelo)
        print("Origen: ",self.origen)
        print("Destino: ",self.destino)
        print("Fecha: ",self.fecha_ida)
        print("Hora: ",self.hora_ida)

class Vuelo_comercial(vuelo):
    def __init__(self,numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso,numero_pasajeros,precio):
        super().__init__(numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso)
        self.numero_pasajeros=numero_pasajeros
        self.precio=precio
        self.capidad_equipaje=0
    def mostrar(self):
        super().mostrar()
        print("Numero de pasajeros: ",self.numero_pasajeros)


class Vuelo_privado(vuelo):
    def __init__(self,numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso,numero_pasajeros,precio):
        super().__init__(numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso)
        self.numero_pasajeros=numero_pasajeros
        self.precio=precio
    def mostrar(self):
        super().mostrar()
        print("Numero de pasajeros: ",self.numero_pasajeros)

