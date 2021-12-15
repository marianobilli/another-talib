import unittest
from another_talib import demo

class DemoTestCase(unittest.TestCase):
    
    def test_demo(self):
        ''' This is a demo test '''
        self.assertEqual(demo(), True)
        self.assertNotEqual(demo(), False)

if __name__ == '__main__':
    unittest.main()