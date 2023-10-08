import unittest
from app import GeometryCalculator


class GeometryCalculatorTestCase(unittest.TestCase):
    def test_calculate_circle(self):
        calculator = GeometryCalculator()
        radius = 5
        expected_area = 78.53981633974483

        actual_area = calculator.calculate_circle(radius)

        self.assertEqual(actual_area, expected_area)

    def test_calculate_triangle_right_triangle(self):
        calculator = GeometryCalculator()
        side_1 = 3
        side_2 = 4
        side_3 = 5
        expected_area = 6.0
        expected_triangle_type = "Прямоуголный"

        result = calculator.calculate_triangle(side_1, side_2, side_3)

        self.assertEqual(result["Площадь треугольника"], expected_area)
        self.assertEqual(result["Треугольник"], expected_triangle_type)

    def test_calculate_triangle_not_right_triangle(self):
        calculator = GeometryCalculator()
        side_1 = 2
        side_2 = 3
        side_3 = 4
        expected_area = 2.9047375096555625
        expected_triangle_type = "Не прямоуголный"

        result = calculator.calculate_triangle(side_1, side_2, side_3)

        self.assertEqual(result["Площадь треугольника"], expected_area)
        self.assertEqual(result["Треугольник"], expected_triangle_type)


if __name__ == "__main__":
    unittest.main()
