import os
from flask import Flask
from .extensions import db, mail
from config import Config

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        template_folder='../../Client/templates',
        static_folder='../../Client/static'
    )

    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    # IMPORT BLUEPRINT
    from .routes import main
    from .auth import auth
    from .mail_route import mail_route

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(mail_route)

    # ADMIN
    from .admin import setup_admin
    setup_admin(app)

    # CONTEXT
    from .context import inject_collezioni
    app.context_processor(inject_collezioni)

    return app