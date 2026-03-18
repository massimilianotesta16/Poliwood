from flask import Blueprint, request, render_template, redirect, url_for, session
from db import Utente

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        utente = Utente.query.filter_by(nome_utente=username).first()

        if utente and utente.check_password(password):
            session['logged_in'] = True
            session['user_id'] = utente.id_utente
            return redirect('/admin')

        return render_template('login.html', error="Credenziali non valide")

    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.clear()
    return redirect('/login')