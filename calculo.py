class Calculo:
    def __init__(self):
        self.__valor_gasolina = 4.99
        self.__valor_alcool = 3.70
        self.__valor_diesel = 9.84

    def calcular_gasto(self, distancia, consumo):
        if distancia <= 0 or consumo <= 0:
            raise Exception(
                'o valor recebido não pode ser menor ou igual a zero'
            )

        gasto_gasolina = round(
            (distancia / consumo) * self.__valor_gasolina, 2)
        gasto_alcool = round(
            (distancia / consumo) * self.__valor_alcool, 2)
        gasto_diesel = round(
            (distancia / consumo) * self.__valor_diesel, 2)
        return f"""
        O valor total do gasto será de:
        
        Gasolina: R$ {gasto_gasolina}
        Álcool:   R$ {gasto_alcool}
        Diesel:   R$ {gasto_diesel}
        """
