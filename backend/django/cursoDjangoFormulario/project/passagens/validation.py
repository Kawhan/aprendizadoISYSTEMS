def origem_destino_iguais(origem, destino, lista_erros):
    """ Verifica se origem e destino são iguais """
    if origem == destino:
        lista_erros['destino'] = "Origem e destino não podem ser iguais!"
        
def campo_tem_algum_numero(valor_do_campo, nome_campo, lista_erros):
    """ Verifica se o possui algum digito numérico """
    if any(char.isdigit() for char in valor_do_campo):
        lista_erros[nome_campo] = "Não inclua números neste campo!"
        