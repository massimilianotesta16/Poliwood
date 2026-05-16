🪵 Poliwood Porte — Sito Web Aziendale
Sito web istituzionale per Poliwood Porte s.n.c., falegnameria artigianale di Belvedere Langhe (CN) specializzata in porte in legno massello su misura.
________________________________________
🛠 Stack Tecnologico
Layer	Tecnologie
Back-end	Python 3, Flask, Flask-SQLAlchemy, Flask-Mail, Flask-Admin
Database	SQLite (default) / PostgreSQL
Front-end	HTML5, CSS3, Bootstrap 5, JavaScript vanilla
UI libs	Swiper.js 11, Bootstrap Icons, Font Awesome 6
Sicurezza	Werkzeug password hashing, sessioni Flask, variabili .env
________________________________________
📁 Struttura del Progetto
Poliwood/
├── Server/
│   ├── run.py              # Punto di ingresso
│   ├── config.py           # Configurazione (legge .env)
│   ├── db.py               # Modelli SQLAlchemy
│   └── app/
│       ├── __init__.py     # Application factory
│       ├── routes.py       # Pagine pubbliche (Blueprint: main)
│       ├── auth.py         # Login / Logout (Blueprint: auth)
│       ├── mail_route.py   # Form contatti (Blueprint: mail_route)
│       ├── admin.py        # Pannello Flask-Admin
│       ├── context.py      # Context processor globale
│       └── extensions.py   # Istanze db e mail
└── Client/
    ├── templates/          # Template Jinja2
    └── static/
        ├── css/style.css   # Foglio di stile principale
        ├── js/script.js    # JavaScript
        └── assets/         # Immagini, font
________________________________________
🗂 Pagine
Route	Descrizione
/	Homepage con hero Swiper e anteprima collezioni
/collezioni	Griglia interattiva delle 3 macro-collezioni
/collezione/<id>	Dettaglio collezione 
/chi-siamo	Storia, filosofia e sostenibilità
/qualita	Materiali e lavorazioni artigianali
/personalizzazioni	Fuorimisura e personalizzazioni
/contatti	Form di contatto + Google Maps
/journal	Blog aziendale 
/articolo                       
/admin	Dettaglio articolo
Pannello di amministrazione (protetto)
/cookie	Dettagli cookie policy
/privacy	Dettagli privacy
________________________________________
🔐 Area Admin
Accessibile da /login. Il pannello Flask-Admin permette la gestione completa di collezioni, modelli, finiture, varianti, articoli e utenti. L'accesso è protetto da sessione — utenti non autenticati vengono reindirizzati al login.
________________________________________
📍 Azienda
Poliwood s.n.c. di Negro Stefania & C.
Via Bracco, 2 — 12060 Belvedere Langhe (CN)
Tel. 0173 797050 — poliwood@poliwoodporte.com

