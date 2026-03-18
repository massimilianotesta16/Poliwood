from flask import Blueprint, request, flash, render_template
from flask_mail import Message
from .extensions import mail

mail_route = Blueprint('mail_route', __name__)

@mail_route.route('/contatti', methods=['GET', 'POST'])
def contatti():
    if request.method == 'POST':
        nome = request.form.get('Nome')
        cognome = request.form.get('Cognome')
        email_cliente = request.form.get('Email')
        telefono_cliente = request.form.get('Telefono')
        messaggio_corpo = request.form.get('Messaggio')

        msg = Message(
            subject=f"Nuovo contatto: {nome} {cognome}",
            recipients=['massimilianotesta16@gmail.com'],
            body=f"""
Da: {nome} {cognome}
Email: {email_cliente}
Telefono: {telefono_cliente}

Messaggio:
{messaggio_corpo}
"""
        )

        try:
            mail.send(msg)
            flash("Messaggio inviato!", "success")
        except Exception as e:
            flash(str(e), "danger")

    return render_template('contatti.html')