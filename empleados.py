
acumulador = 0
contador = 1
mayores_gastos = 0


n = int(input("Ingrese la cantidad de empleados: "))
float(input("Ingrese el salario base de la empresa: "))
while contador <= n:
    print("\n--- Empleado", contador, "---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario: "))
    gastos = float(input("Gastos mensuales: "))

    resultado = salario - gastos
    acumulador += resultado


    if gastos > salario:
        mayores_gastos += 1

    contador += 1


print("\n✅ La suma total de los salarios resultantes es:", acumulador)
print("🚨 Cantidad de empleados con gastos mayores que el salario:", mayores_gastos)
