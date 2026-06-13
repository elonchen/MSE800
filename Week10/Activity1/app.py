"""
Application entry point.
"""

from flask import Flask
from flask import render_template

from auth import auth_bp
from user import user_bp

app = Flask(__name__)

app.secret_key = "secret_key"

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

@app.route("/")
def home():
    """Redirect root page to login."""
    return render_template("login.html")


@app.route("/register-page")
def register_page():
    """Redirect root page to register."""
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
