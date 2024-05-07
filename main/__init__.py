import os

from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

app.config["RECAPTCHA_PUBLIC_KEY"] = os.environ.get("RECAPCHA_PUBLICK_KEY")
app.config["RECAPTCHA_PRIVATE_KEY"] = os.environ.get(
    "6Ld-R9MpAAAAAFAcBzGxoReXahIc-vnLnyvLQCho"
)
app.config["RECAPTCHA_USE_SSL"] = True
app.config["RECAPTCHA_OPTIONS"] = {"theme": "white"}

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "my-secret-key")
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.masterhost.ru")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT", 587)
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL", "your-email@example.com")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASS", "your-email-password")

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from main import views  # noqa
