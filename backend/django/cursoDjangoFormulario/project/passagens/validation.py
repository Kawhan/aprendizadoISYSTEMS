def origem_destino_iguais(origem, destino, lista_erros):
    """ Verifica se origem e destino são iguais """
    if origem == destino:
        lista_erros['destino'] = "Origem e destino não podem ser iguais!"
        
def campo_tem_algum_numero(valor_do_campo, nome_campo, lista_erros):
    """ Verifica se o possui algum digito numérico """
    if any(char.isdigit() for char in valor_do_campo):
        lista_erros[nome_campo] = "Não inclua números neste campo!"
        
def data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros):
    """ Verificar se a data de ida é maior que a data de volta """
    if data_ida > data_volta:
        lista_erros['data_volta'] = "A data de volta não pode ser menor que a data de ida"

def data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_erros):
    """ Verifica se a data de ida é menor que a data de hoje """
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = " Data de ida não pode ser menor que a data de hoje"