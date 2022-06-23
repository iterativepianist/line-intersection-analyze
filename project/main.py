from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@login_required
@main.route('/profile')
def profile():
    if not hasattr(current_user, "name"):
        return render_template('index.html')

    return render_template('profile.html', name=current_user.name)

#No login temporarily
#@login_required
@main.route('/data')
def data():
    #if not hasattr(current_user, "name"):
    #    return render_template('index.html')

    headings = ["Średnia", "Mediana"]
    data = [
        ["150", "250"],
        ["350", "350"]
    ]


    return render_template('data.html', headings = headings, data = data)
