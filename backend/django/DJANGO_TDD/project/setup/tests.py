from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AnimaisTestCase(LiveServerTestCase):
    # Função responsavel por iniciar nos tests / preparar os testes
    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Users\Kawhan Laurindo\Desktop\project\chromedriver.exe')
    
    # Função que é executada depois que executada depois dos metodos de testes serem finalizadas
    def tearDown(self):
        # Depois que nossos testes forem finalizados vamos fechar nossa aba do chrome
        self.browser.quit()
    
    

    def test_buscando_um_novo_animal(self):
        """ Teste se um usuário encontra um animal pesquisando """
        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CLASS_NAME, "navbar")
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome. 
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, "input")
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        # time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, 'form button')

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CLASS_NAME, 'result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um leão.
        