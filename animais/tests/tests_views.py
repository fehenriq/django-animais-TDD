from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Aranha',
            predador = 'Sim',
            venenoso = 'Sim',
            domestico = 'Não'
        )
        
    def test_index_view_retorna_caracteristicas_animal(self):
        """Teste que verifica se a index retorna as caracteristicas do animal pesquisado"""
        response = self.client.get('/',
                                   {'buscar':'Aranha'})
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'Aranha')