import os
from flask import Flask, render_template, url_for

# 1. Configurazione dei percorsi
basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(basedir, '../Client/templates')
static_dir = os.path.join(basedir, '../Client/static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# 2. Rotte (DEVONO corrispondere ai nomi usati in url_for)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chi-siamo')
def chi_siamo():
    # Se non hai ancora creato il file html, per ora metti solo un testo
    # return "Pagina Chi Siamo in costruzione"
    return render_template('chi-siamo.html') 

@app.route('/collezioni')
def collezioni():
    # Se non hai ancora creato il file html, metti solo un testo
    # return "Pagina Collezioni in costruzione"
    return render_template('collezioni.html')

if __name__ == '__main__':
    app.run(debug=True)