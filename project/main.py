from flask import Blueprint, render_template
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


    return render_template('data.html', headings = headings, data = data)
