def validate_name_product(name_product):
    """ Verificando se o nome do produto é valido """
    name_product = name_product.replace(' ', '')
    return name_product.strip().isalpha()

def validate_len_code_product(code_product):
    """ Verificando se o tamanho do codigo apresentado é menor do que o minimo de 8 caracteres """
    return not len(code_product) < 8

def validade_value_product(value_product):
    """ Verificando se o valor do produto é valido """
    return not value_product < 0

def validate_quantity_product(quantity_product):
    """ Verificando se a quantidade de produtos é valida """
    return not quantity_product < 0

def validade_validate_product(validate_product):
    """ Verificando se a validade do produto é valida """
    return not validate_product < 0