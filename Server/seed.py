# seed.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.extensions import db
from db import Utente
from werkzeug.security import generate_password_hash


def popola_database():
    app = create_app()
    with app.app_context():
        print("Inserimento dati in corso...")

        utenti = [
            Utente(nome_utente='Massimiliano', password=generate_password_hash("MT03112007_S01")),
            Utente(nome_utente='Maurizio', password=generate_password_hash("MT04061968_F02")),
            Utente(nome_utente='Giuseppe', password=generate_password_hash("GT17061966_F03")),
            Utente(nome_utente='Stefania', password=generate_password_hash("SN13031969_S04")),
        ]

        db.session.add_all(utenti)
        db.session.commit()

        print("Utenti creati con successo!")

if __name__ == '__main__':
    popola_database()