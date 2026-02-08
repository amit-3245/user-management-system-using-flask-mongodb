from flask import Flask, redirect, url_for
from config import Config
from routes.auth_routes import auth_bp
from routes.user_routes import users_bp

def create_app():
    app = Flask(__name__)

    # Load config
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["DEBUG"] = Config.DEBUG

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
