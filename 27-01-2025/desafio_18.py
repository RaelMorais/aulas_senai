import calendar
from datetime import datetime

import calendar
from datetime import datetime

class Calendario:
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes

    def exibir_calendario(self):
        print(calendar.month(self.ano, self.mes))

    def verificar_feriado(self, data):
        feriados = {
            "01-01": "Ano Novo",
            "25-12": "Natal",
        }
        data_formatada = data.strftime("%d-%m")
        return feriados.get(data_formatada, "Não é feriado.")

    def calcular_diferenca_dias(self, data1, data2):
        delta = abs((data2 - data1).days)
        return delta

if __name__ == "__main__":

    meu_calendario = Calendario(2025, 1)
    print("Calendário de Janeiro de 2025:")
    meu_calendario.exibir_calendario()

    data = datetime.strptime("25-12-2025", "%d-%m-%Y")
    print(meu_calendario.verificar_feriado(data))


    data1 = datetime.strptime("01-01-2025", "%d-%m-%Y")
    data2 = datetime.strptime("25-12-2025", "%d-%m-%Y")
    dias_diferenca = meu_calendario.calcular_diferenca_dias(data1, data2)
    print(f"Diferença de dias entre {data1.strftime('%d-%m-%Y')} e {data2.strftime('%d-%m-%Y')}: {dias_diferenca} dias")