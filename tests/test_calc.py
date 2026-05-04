import unittest
from calculation import calculate_material

class TestMaterialCalculation(unittest.TestCase):
    
    # Проверка корректного расчета
    def test_correct_calculation(self):
        result = calculate_material(1, 1, 100, 10, 10)
        self.assertEqual(result, 11034)

    # Если типа продукции не существует, должно быть -1
    def test_non_existent_product_type(self):
        result = calculate_material(999, 1, 100, 10, 10)
        self.assertEqual(result, -1)

    # Если количество отрицательное, должно быть -1
    def test_negative_count(self):
        result = calculate_material(1, 1, -10, 10, 10)
        self.assertEqual(result, -1)

    # Проверка другого типа материала
    def test_material_type_two(self):
        result = calculate_material(2, 2, 10, 5, 5)
        self.assertEqual(result, 633)

if __name__ == '__main__':
    unittest.main()
