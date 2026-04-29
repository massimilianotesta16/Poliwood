from app.extensions import db

# --- Tabelle di relazione many-to-many ---

foto_articoli = db.Table('foto_articoli',
    db.Column('id_immagine', db.Integer, db.ForeignKey('galleria_immagini.id_immagine'), primary_key=True),
    db.Column('id_articolo', db.Integer, db.ForeignKey('articoli.id_articolo'), primary_key=True)
)

foto_collezioni = db.Table('foto_collezioni',
    db.Column('id_immagine', db.Integer, db.ForeignKey('galleria_immagini.id_immagine'), primary_key=True),
    db.Column('id_collezione', db.Integer, db.ForeignKey('collezioni.id_collezione'), primary_key=True)
)

collezione_componenti = db.Table('collezione_componenti',
    db.Column('id_collezione', db.Integer, db.ForeignKey('collezioni.id_collezione'), primary_key=True),
    db.Column('id_categoria', db.Integer, db.ForeignKey('categorie_componenti.id_categoria'), primary_key=True)
)

categoria_componente = db.Table('categoria_componente',
    db.Column('id_categoria', db.Integer, db.ForeignKey('categorie_componenti.id_categoria'), primary_key=True),
    db.Column('id_componente', db.Integer, db.ForeignKey('componenti.id_componente'), primary_key=True)
)

modelli_collezione = db.Table('modelli_collezione',
    db.Column('id_modello', db.Integer, db.ForeignKey('modelli.id_modello'), primary_key=True),
    db.Column('id_collezione', db.Integer, db.ForeignKey('collezioni.id_collezione'), primary_key=True)
)

# --- Modelli principali ---

class ClienteNewsletter(db.Model):
    __tablename__ = 'clienti_newsletter'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cognome = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True, nullable=False)

class GalleriaImmagini(db.Model):
    __tablename__ = 'galleria_immagini'
    id_immagine = db.Column(db.Integer, primary_key=True, autoincrement=True)
    percorso_url = db.Column(db.Text, nullable=False)
    testo_alt = db.Column(db.String(255))

class Articolo(db.Model):
    __tablename__ = 'articoli'
    id_articolo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titolo = db.Column(db.String(255), nullable=False)
    sunto = db.Column(db.Text)
    contenuto = db.Column(db.Text)
    immagine_copertina = db.Column(db.Text)
    data_pubblicazione = db.Column(db.Date)
    pubblicato = db.Column(db.Boolean, default=False)
    newsletter = db.Column(db.Boolean, default=False)

    galleria = db.relationship('GalleriaImmagini', secondary=foto_articoli, backref='articoli')

class Complemento(db.Model):
    __tablename__ = 'complementi'
    id_complemento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_complemento = db.Column(db.String(150), nullable=False)
    immagine_complemento = db.Column(db.Text)

class CategoriaComponenti(db.Model):
    __tablename__ = 'categorie_componenti'
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_categoria = db.Column(db.String(150), nullable=False)

    componenti = db.relationship('Componente', secondary=categoria_componente, backref='categorie')

class Componente(db.Model):
    __tablename__ = 'componenti'
    id_componente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_componente = db.Column(db.String(150), nullable=False)
    immagine_componente = db.Column(db.Text)

class Collezione(db.Model):
    __tablename__ = 'collezioni'
    id_collezione = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_collezione = db.Column(db.String(150), nullable=False)
    immagine_copertina = db.Column(db.Text)
    descrizione = db.Column(db.Text)
    tipologia = db.Column(db.String(100))

    galleria = db.relationship('GalleriaImmagini', secondary=foto_collezioni, backref='collezioni')
    modelli = db.relationship('Modello', secondary=modelli_collezione, backref='collezioni')
    categorie = db.relationship('CategoriaComponenti', secondary=collezione_componenti, backref='collezioni')

class Legno(db.Model):
    __tablename__ = 'legno'
    id_legno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_legno = db.Column(db.String(150), nullable=False)

    finiture = db.relationship('Finitura', secondary='legno_finiture', backref='legni')
    collezioni = db.relationship('Collezione', secondary='collezione_legni', backref='legni')

class CollezioneLegni(db.Model):
    __tablename__ = 'collezione_legni'
    id_collezione_legno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_collezione = db.Column(db.Integer, db.ForeignKey('collezioni.id_collezione'))
    id_legno = db.Column(db.Integer, db.ForeignKey('legno.id_legno'))

class Finitura(db.Model):
    __tablename__ = 'finiture'
    id_finitura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_finitura = db.Column(db.String(150), nullable=False)
    immagine_finitura = db.Column(db.Text)

class LegnoFinitura(db.Model):
    __tablename__ = 'legno_finiture'
    id_legno_finitura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_legno = db.Column(db.Integer, db.ForeignKey('legno.id_legno'))
    id_finitura = db.Column(db.Integer, db.ForeignKey('finiture.id_finitura'))

class Modello(db.Model):
    __tablename__ = 'modelli'
    id_modello = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_modello = db.Column(db.String(150), nullable=False)
    immagine_modello = db.Column(db.Text)
    descrizione_modello = db.Column(db.Text)

    complementi = db.relationship('Complemento', secondary='modelli_complementi', backref='modelli')

class ModelloComplemento(db.Model):
    __tablename__ = 'modelli_complementi'
    id_modello_complemento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_modello = db.Column(db.Integer, db.ForeignKey('modelli.id_modello'))
    id_complemento = db.Column(db.Integer, db.ForeignKey('complementi.id_complemento'))

class VarianteModello(db.Model):
    __tablename__ = 'varianti_modello'
    id_variante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_variante = db.Column(db.String(150), nullable=False)

class ModelloVariante(db.Model):
    __tablename__ = 'modelli_varianti'
    id_modello_variante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_modello = db.Column(db.Integer, db.ForeignKey('modelli.id_modello'))
    id_variante = db.Column(db.Integer, db.ForeignKey('varianti_modello.id_variante'))
    immagine_variante = db.Column(db.Text)

    modello = db.relationship('Modello', backref='varianti_associate')
    variante = db.relationship('VarianteModello', backref='modelli_associati')

class Utente(db.Model):
    __tablename__ = 'utenti'
    id_utente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_utente = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)