from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__,
                template_folder='../templates',    
                static_folder='../static')        
    
    app.config.from_object(Config)

    # Register blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app

app = create_app()  # Create the app instance