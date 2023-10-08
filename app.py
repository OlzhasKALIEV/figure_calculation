from flask import Flask, request, jsonify

from figurescalculator import GeometryCalculator

app = Flask(__name__)

calculator = GeometryCalculator()


@app.route("/circle", methods=["GET"])
def area_of_a_circle():
    radius = request.args.get("radius")
    finding_the_radius = calculator.calculate_circle(int(radius))
    return jsonify({"Площадь круга": finding_the_radius})


@app.route("/triangle", methods=["GET"])
def area_of_a_triangle():
    try:
        side_1 = request.args.get("side_1")
        side_2 = request.args.get("side_2")
        side_3 = request.args.get("side_3")
        triangle = calculator.calculate_triangle(int(side_1), int(side_2), int(side_3))
    except ValueError as ex:
        return jsonify({
            "mesage": str(ex)
        })
    return triangle


if __name__ == '__main__':
    app.run(debug=True)
