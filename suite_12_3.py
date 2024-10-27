import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite и добавляем тесты
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создаем TextTestRunner с verbosity=2 для детального вывода
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
