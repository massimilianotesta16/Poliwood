from flask import Blueprint, render_template
from db import Collezione

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/collezioni')
def collezioni():
    return render_template('collezioni.html')

@main.route('/collezione/<int:id>')
def collezione(id):
    collezione = Collezione.query.get_or_404(id)
    return render_template('collezione.html', collezione=collezione)

@main.route('/chi-siamo')
def chi_siamo():
    return render_template('chi-siamo.html')

@main.route('/qualita')
def qualita():
    return render_template('qualita.html')

@main.route('/personalizzazioni')
def personalizzazioni():
    return render_template('personalizzazioni.html')

@main.route('/journal')
def journal():
    return render_template('journal.html')