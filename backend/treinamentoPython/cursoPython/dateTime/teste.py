from datetime import date as dt
from datetime import datetime, timezone, timedelta

# Formatando a data
data_atual = dt.today()
print(data_atual)

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

print(data_em_texto)

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

# Formatando a data com o tempo
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

print(data_e_hora_em_texto)


# A classe timedelta tem a finalidade de representar uma duração e, no nosso caso, uma diferença entre horários.

diferenca = timedelta(hours=-3)
print(diferenca)

# Formatando a ddata com UTC-3 evitando problemas de a hora ser relacionada com a maquina
data_e_hora_atuais = datetime.now()
fuso_horario = timezone(diferenca) # UTC-3
print(fuso_horario)

# Coverstendo usando metodo astimezone
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)