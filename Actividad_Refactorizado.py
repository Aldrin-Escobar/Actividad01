# Se Elimina 'if y != 0 else x / y' -> Debio a que si y == 0, se realizará una división con denominador
# 0 y nos arrogará un error.
class OperacionMatematica:
    def Multipicacion(self, Multiplicando, Multiplicador):
        return Multiplicando*Multiplicador

