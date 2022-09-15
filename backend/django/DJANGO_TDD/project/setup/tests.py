from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    # Função responsavel por iniciar nos tests / preparar os testes
    def setUp(self):
        self.browser = webdriver.Chrome('backend/django/DJANGO_TDD/chromedriver.exe')
    
    # Função que é executada depois que executada depois dos metodos de testes serem finalizadas
    def tearDown(self):
        # Depois que nossos testes forem finalizados vamos fechar nossa aba do chrome
        self.browser.quit()
    
    
    # Primeiro test
    def test_para_verificar_se_a_janela_do_browser_esta_ok(self):
        self.browser.get("alura.com.br")