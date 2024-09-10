from Actividad_Refactorizado import OperacionMatematica


if __name__ == "__main__":
    operacion = OperacionMatematica()
    multiplicando = float(input("Ingresar multiplicando: "))
    multiplicador = float(input("Ingresar multiplicando: "))
    resultado = operacion.Multipicacion(multiplicando,multiplicador)
    print(f"Multplicacion -> {multiplicando} * {multiplicador} = {resultado}")

    sumandoA = float(input("Ingresar primer sumando: "))
    sumandoB = float(input("Ingresar segundo sumando: "))
    resultado = operacion.Sumar(sumandoA, sumandoB)
    print(f"Suma -> {sumandoA} + {sumandoB} = {resultado}")

    minuendo = float(input("Ingresar multiplicando: "))
    sustraendo = float(input("Ingresar multiplicando: "))
    resultado = operacion.Restar(minuendo, sustraendo)
    print(f"Resta -> {minuendo} - {sustraendo} = {resultado}")