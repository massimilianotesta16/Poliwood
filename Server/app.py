import os
from flask import Flask, render_template, url_for

# 1. Configurazione dei percorsi
basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(basedir, '../Client/templates')
static_dir = os.path.join(basedir, '../Client/static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# 2. Rotte

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/azienda')
def azienda():
    return render_template('azienda.html') 

@app.route('/collezioni')
def collezioni():
    return render_template('collezioni.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contatti')
def contatti():
    return render_template('contatti.html')

# 3. Avvio dell'applicazione

if __name__ == '__main__':
    app.run(debug=True)