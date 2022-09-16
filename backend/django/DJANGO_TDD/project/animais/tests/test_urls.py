from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisUrlsTestCase(TestCase):
    """ Teste para fazer reqyest de animais """
    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_index(self):
        """ Testando a rota de index """
        request = self.factory.get('/')
        # Criando um contexto para nosso teste
        with  self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
        

    