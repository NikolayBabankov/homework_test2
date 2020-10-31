import unittest
import yandex



class TestMultiplication(unittest.TestCase):

    def setUp(self):
        print('Начало тестов')
    

    def tearDown(self):
        print('Конец тестов')
    
    
    def test_number1(self):
        print('тест №1 Проверка API y.disk')
        self.assertEqual(yandex.directory('ppp'), ['<Response [200]>', '<Response [201]>'])


if __name__ == '__main__':
    unittest.main()