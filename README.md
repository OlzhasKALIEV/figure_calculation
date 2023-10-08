# figure_calculation

1. Клонируем проект: git clone https://github.com/OlzhasKALIEV/figure_calculation.git
2. Установка зависимостей: pip install -r .\requirements.txt
3. Запуск сервера: python .\app.py run


Калькулятор для вычисления площади треугольника по трем сторонам и площади круга

Площадь круга

GET: http://127.0.0.1:5000/circle?radius=9

radius: Радиус круга

![img.png](media/img_1.png)

Площадь треугольника

GET: http://127.0.0.1:5000/triangle?side_1=3&side_2=4&side_3=5

side_1, side_2, side_3 стороны треугольника

![img.png](media/img_2.png)

запуск тестов: python -m unittest /app.py