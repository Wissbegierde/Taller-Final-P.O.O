#Sistema de gestión de empleados

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def asignar_tarea(self, tarea):
        print(f"Tarea asignada a {self.nombre}: {tarea}")

    def calcular_salario(self):
        return self.salario


class Tarea:
    def __init__(self, descripcion, duracion):
        self.descripcion = descripcion
        self.duracion = duracion

    def __str__(self):
        return self.descripcion


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_informe(self):
        print(f"Informe del departamento {self.nombre}:")
        for empleado in self.empleados:
            salario = empleado.calcular_salario()
            print(f"Nombre: {empleado.nombre}, Salario: {salario}")

    def empleado_con_mayor_salario(self):
        empleado_mayor_salario = None
        mayor_salario = 0

        for empleado in self.empleados:
            salario = empleado.calcular_salario()
            if salario > mayor_salario:
                mayor_salario = salario
                empleado_mayor_salario = empleado

        if empleado_mayor_salario:
            print(f"El empleado con mayor salario es {empleado_mayor_salario.nombre} con un salario de {mayor_salario}")
        else:
            print("No hay empleados en el departamento.")


# Crear empleados
empleado1 = Empleado("Juan Perez", 2000)
empleado2 = Empleado("Maria Lopez", 2500)

# Crear tareas
tarea1 = Tarea("Realizar informe de ventas", 4)
tarea2 = Tarea("Preparar presentación para reunión", 2)

# Crear departamento
departamento = Departamento("Ventas")

# Agregar empleados al departamento
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

# Asignar tareas a los empleados
empleado1.asignar_tarea(tarea1)
empleado2.asignar_tarea(tarea2)

# Generar informe del departamento
departamento.generar_informe()
departamento.empleado_con_mayor_salario()