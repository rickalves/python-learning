from datetime import datetime, timedelta
class DataBr:
    def __init__(self):
        self._data_cadastro = datetime.now()

    def __str__(self) -> str:
        return self._data_cadastro.strftime("%d/%m/%Y %H:%M")

    def mes(self):
        meses = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro"
            "outubro",
            "novembro",
            "dezembro"
        ]
        return meses[self._data_cadastro.month-1]
    
    def dia_semana(self):
        dias= [
            "segunda-feira",
            "terça-feira",
            "quarta-feira",
            "quinta-feira",
            "sexta-feira",
            "sábado",
            "domingo"
        ]
        return dias[self._data_cadastro.weekday()]

    def tempo_cadastro(self):
        tempo = (datetime.today() + timedelta(days=50, hours=40)) - self._data_cadastro
        return tempo

    