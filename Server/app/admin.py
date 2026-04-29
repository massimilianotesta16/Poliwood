from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask import session, redirect, url_for
from db import db, Collezione, Modello, Finitura, VarianteModello as Variante, Articolo, Utente
from wtforms import PasswordField

class SecureModelView(ModelView):
    def is_accessible(self):
        return session.get('logged_in') == True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return session.get('logged_in') == True

class UtenteModelView(SecureModelView):
    column_exclude_list = ['password']
    form_extra_fields = {
        'password': PasswordField('Password')
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.set_password(form.password.data)

def setup_admin(app):
    admin = Admin(
        app,
        name='Poliwood Admin',
        index_view=MyAdminIndexView(url='/admin'),
        url='/admin'
    )

    admin.add_view(SecureModelView(Collezione, db.session))
    admin.add_view(SecureModelView(Modello, db.session))
    admin.add_view(SecureModelView(Finitura, db.session))
    admin.add_view(SecureModelView(Variante, db.session))
    admin.add_view(SecureModelView(Articolo, db.session))
    admin.add_view(UtenteModelView(Utente, db.session))

    admin.add_link(MenuLink(name='Vai al sito', url='/'))
    admin.add_link(MenuLink(name='Logout', url='/logout'))