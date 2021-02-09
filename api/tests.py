from django.test import TestCase

class FirstTestCase(TestCase):
    def setUp(self):
        self.test_forzado = 'text initial'

    def test_primer_ejemplo(self):
        """Ejemplo de test"""
        self.assertEqual(self.test_forzado, 'text initial')

    def test_segundo_igual_ejemplo(self):
        """Ejemplo de test"""
        self.assertEqual(self.test_forzado, 'text initial')
