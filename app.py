from flask import Flask
from config import Config
from routes.user_routes import user_bp
from routes.auth import auth_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    
    @app.route('/')
    def home():
        return "User Management System"
    
    return app

if __name__ == '__main__':
    app = create_app()
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 5009))
    debug = os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1', 't']
    app.run(host=host, port=port, debug=debug)