from flask import Blueprint, render_template, request
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/data')
def data():
    headings = ["Średnia", "Mediana"]
    data = [
        ["150", "250"],
        ["350", "350"]
    ]

    return render_template('data.html', headings=headings, data=data)


@main.route('/calculate', methods=['POST'])
def calculate():
    # First line
    p1_x_1 = request.form.get('1-P1-X')
    p1_y_1 = request.form.get('1-P1-Y')
    p2_x_1 = request.form.get('1-P2-X')
    p2_y_1 = request.form.get('1-P2-Y')

    # Second line
    p1_x_2 = request.form.get('2-P1-X')
    p1_y_2 = request.form.get('2-P1-Y')
    p2_x_2 = request.form.get('2-P2-X')
    p2_y_2 = request.form.get('2-P2-Y')

    return render_template('data.html')
