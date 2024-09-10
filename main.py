from Actividad_Refactorizado import OperacionMatematica


if __name__ == "__main__":
    operacion = OperacionMatematica()
    multiplicando = float(input("Ingresar multiplicando: "))
    multiplicador = float(input("Ingresar multiplicando: "))
    resultado = operacion.Multipicacion(multiplicando,multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")
