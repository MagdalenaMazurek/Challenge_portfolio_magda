import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLoginPage
from test_cases.przypadek_testowy_1 import przypadek_testowy_1
from test_cases.przypadek_testowy_2 import przypadek_testowy_2
from test_cases.przypadek_testowy_3 import przypadek_testowy_3
from test_cases.przypadek_testowy_4 import przypadek_testowy_4
from test_cases.przypadek_testowy_5 import przypadek_testowy_5

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(przypadek_testowy_1))
   test_suite.addTest(makeSuite(przypadek_testowy_2))
   test_suite.addTest(makeSuite(przypadek_testowy_3))
   test_suite.addTest(makeSuite(przypadek_testowy_4))
   test_suite.addTest(makeSuite(przypadek_testowy_5))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())