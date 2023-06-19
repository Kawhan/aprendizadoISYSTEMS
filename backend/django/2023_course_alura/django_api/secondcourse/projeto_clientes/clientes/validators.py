import re
from validate_docbr import CPF

class Validators:   
    @staticmethod
    def cpf_valido(data):
        """ Verifica se o cpf é válido """
        
        cpf = CPF()
        
        return cpf.validate(data['cpf'])
            
    @staticmethod
    def nome_valido(data):
        """ Verifica se o número do cpf é válido """
        
        return data['nome'].isalpha()
        
    @staticmethod
    def rg_valido(data):
        """ Verifica se o rg é válido """
        
        return len(data['rg']) == 9
            
    @staticmethod
    def celular_valido(data):
        """ Verifica se o número de celular é válido (11 91234-1234)"""
        
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, data['celular'])
        
        return resposta
      
    validators_data = {
        'cpf': lambda data: data if  Validators.cpf_valido(data) else {'cpf': "O cpf não é válido! Lembre-se de digitar apenas números"} ,
        'nome': lambda data: data if  Validators.nome_valido(data) else {'nome': "O nome não pode conter números"} ,
        'rg': lambda data: data if  Validators.rg_valido(data) else {'rg': "O rg deve ter 9 dígitos"} ,
        'celular': lambda data: data if  Validators.celular_valido(data) else {'celular': "O número de celular deve seguir este modelo: (11 91234-1234), respeitando os espaços e traço."} ,
    }