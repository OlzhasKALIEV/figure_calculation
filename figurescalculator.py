import math

from flask import jsonify


class GeometryCalculator:
    @staticmethod
    def calculate_circle(radius):
        # math.pi = 3.141592653589793
        # S = πr**2
        return math.pi * radius ** 2

    @staticmethod
    def calculate_triangle(side_1, side_2, side_3):
        # Проверка на прямоугольник
        if (side_1 ** 2 + side_2 ** 2 == side_3 ** 2) or (side_1 ** 2 + side_3 ** 2 == side_2 ** 2) or (
                side_2 ** 2 + side_3 ** 2 == side_1 ** 2):
            is_right_triangle = "Прямоуголный"
        else:
            is_right_triangle = "Не прямоуголный"

        semi_perimeter = (side_1 + side_2 + side_3) / 2
        triangle_area = math.sqrt(
            semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3))

        return jsonify(
            {
                "Площадь треугольника": triangle_area,
                "Треугольник": is_right_triangle}
        )
