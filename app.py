from flask import Flask, jsonify
from config import Config
from models import db
from flask_jwt_extended import JWTManager



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from routes.auth import auth_bp
    from routes.users import users_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(users_bp, url_prefix="/users")

    @app.route("/")
    def index():
        return """
        <h1>CRUD API is running</h1>
        <p>Try these endpoints:</p>
        <ul>
          <li>POST /auth/register</li>
          <li>POST /auth/login</li>
          <li>GET /users (with token)</li>
        </ul>
        """

    # Health check
    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
