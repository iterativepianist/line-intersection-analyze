import os

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from project import lineintersection

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/data')
def data():
    return render_template('data.html')


@main.route('/calculate', methods=['POST'])
def calculate():
    # First line
    p1_x_1 = int(request.form.get('P1-X'))
    p1_y_1 = int(request.form.get('P1-Y'))
    p2_x_1 = int(request.form.get('P2-X'))
    p2_y_1 = int(request.form.get('P2-Y'))

    # Second line
    p1_x_2 = int(request.form.get('P3-X'))
    p1_y_2 = int(request.form.get('P3-Y'))
    p2_x_2 = int(request.form.get('P4-X'))
    p2_y_2 = int(request.form.get('P4-Y'))

    start1 = [p1_x_1, p1_y_1]
    end1 = [p2_x_1, p2_y_1]
    start2 = [p1_x_2, p1_y_2]
    end2 = [p2_x_2, p2_y_2]

    result = lineintersection.lineIntersec(
        start1,
        end1,

        start2,
        end2
    )

    print("result", str(result))

    if start1 == end1 and end1 == start2 and start2 == end2:
        data = "Odcinki leżą w tym samym punkcie"
    elif start1 == start2 and end1 == end2:
        data = "Odcinki są takie same"
    elif isinstance(result, tuple):
        data = "Odcinki przecinają się w punkcie x:" + str(result[0]) + " y:" + str(result[1])
    elif isinstance(result, list):
        data = "Odcinki mają wspólny odcinek P5:" + str(result[0]) + " P6:" + str(result[1])
    elif start1 == start2 or start1 == end2:
        data = "Odcinki mają wspólny punkt x:" + str(start1[0]) + " y:" + str(start1[1])
    elif end1 == start2 or end1 == end2:
        data = "Odcinki mają wspólny punkt x:" + str(start1[0]) + " y:" + str(start1[1])
    else:
        data = "Odcinki nie przecinają się"


    return render_template('rendered_data.html', data=data)
