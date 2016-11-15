import unittest
from Lista import Lista

class ProbarLista(unittest.TestCase):


    def setUp(self):
         self.clase=  Lista([10,14,50,32,50,89,90])

    def test_SumarNumeros(self):
        self.assertEqual(4,self.clase.sumarDosNumeros(2,2))

    def test_BuscaNumero(self):
        self.assertEqual("Yes",self.clase.encontrarEnLista(10))

    def test_NoEncuentra(self):
        self.assertNotEqual("Yes",self.clase.encontrarEnLista(100))

    def tearDown(self):
        print("Se han terminado las pruebas")



if __name__ == '__main__':
    unittest.main()
