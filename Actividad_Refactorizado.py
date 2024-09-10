# Se Elimina 'if y != 0 else x / y' -> Debio a que si y == 0, se realizará una división con denominador
# 0 y nos arrogará un error.
class OperacionMatematica:
    def Multipicacion(self, multiplicando, multiplicador):
        return multiplicando * multiplicador

    def Sumar(self, sumandoX, sumandoY):
        return sumandoX + sumandoY
    def Restar(self, minuendo, sustraendo):
        return minuendo - sustraendo
