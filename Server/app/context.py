from db import Collezione

def inject_collezioni():
    return dict(collezioni=Collezione.query.all())