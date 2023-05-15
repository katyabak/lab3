import unittest
from main import app

class AppTest(unittest.TestCase):
    def setUp(self):
        app.testing = True # устанавливаем режим тестирования для app
        self.client = app.test_client() # создаем клиент для тестирования

    # тест на решения уравнения с D = 0
    def test_discriminant_route_with_normal_result(self):
        response = self.client.post('/', data={'a': '1', 'b': '4', 'c': '4'})
        self.assertEqual(response.status_code, 200) # проверяем, статус ответа равен ли 200
        self.assertIn(b'x1 = -2.0', response.data) # проверяем, содержит ли ответ эту строку
        self.assertIn(b'x2 = -2.0', response.data)
    # тест на решения уравнения с D<0
    def test_discriminant_route_with_complex_result(self):
        response = self.client.post('/', data={'a': '1', 'b': '2', 'c': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'x1 = (-1+1.4142135623730951j)', response.data)
        self.assertIn(b'x2 = (-1-1.4142135623730951j)', response.data)
    # если пользователь ввёл только a и b
    def test_discriminant_route_with_missing_input(self):
        response = self.client.post('/', data={'a': '1', 'b': '2'})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
