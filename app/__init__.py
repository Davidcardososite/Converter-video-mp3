# __init__.py
from flask import Flask
from .funcoes import agendar_limpeza

def create_app():
    # Inicializar o aplicativo Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    
    agendar_limpeza()
    
    # Importar e registrar blueprints
    from .routes import auth_bp
    app.register_blueprint(auth_bp)

    return app


