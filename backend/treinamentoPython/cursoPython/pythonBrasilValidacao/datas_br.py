from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self) -> str:
        return self.format_data()
    
    def mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro","Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes_cadastro_user  = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro_user -  1]
    
    def dia_semana(self):
        dias_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-feira", "Sexta-Feira", "Sabado", "Domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]
    
    def format_data(self):
        data_formata = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formata
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
    
    