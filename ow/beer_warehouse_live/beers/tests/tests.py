from django.test import TestCase

# Create your tests here.


class BasicTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Se ejecuta al comienzo de la ejecución del test
        """
        print('SetUpTestData')
        pass

    def setUp(self):
        """Se ejecuta al comienzo de cada test
        """
        print('setUp')

    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_suma(self):
        self.assertEqual(4, 2+2)

    # def test_error(self):
    #     self.assertEqual(4, 2+1)
