import unittest

from Lab import Lab
class TestLabFunction(unittest.TestCase):
    
    def test_valid_dates(self):
        
        self.assertEqual(Lab("2025-01-15"), 1)  
        self.assertEqual(Lab("2025-04-20"), 2)  
        self.assertEqual(Lab("2025-07-10"), 3)  
        self.assertEqual(Lab("2025-10-05"), 4)  

    def test_invalid_date_format(self):
        
        self.assertEqual(Lab("423423іваі"), "Невірний формат дати. Введіть дату у форматі 'YYYY-MM-DD'.")
        self.assertEqual(Lab("15-01-2025"), "Невірний формат дати. Введіть дату у форматі 'YYYY-MM-DD'.")
        self.assertEqual(Lab("2025-01-32"), "Невірний формат дати. Введіть дату у форматі 'YYYY-MM-DD'.")
        self.assertEqual(Lab("2025-13-15"), "Невірний формат дати. Введіть дату у форматі 'YYYY-MM-DD'.")

if __name__ == "__main__":
    unittest.main()
