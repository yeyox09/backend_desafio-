from django.test import TestCase

class FirstTestCase(TestCase):
    def setUp(self):
        self.test_forzado = 'text initial'

    def test_primer_ejemplo(self):
        """Ejemplo de test"""
        self.assertEqual(self.test_forzado, 'text initial')
        self.assertTrue(True)
    
    def test_segundo_ejemplo(self):
        """Segundo ejemplo de test"""
        self.assertEqual(self.test_forzado, 'text initial')
        self.assertTrue(True)

    def tearDown(self):
        ''' Clean data'''
        pass