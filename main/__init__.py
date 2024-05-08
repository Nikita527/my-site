import os

from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

app.config["RECAPTCHA_PUBLIC_KEY"] = os.getenv("RECAPTCHA_PUBLIC_KEY")
app.config["RECAPTCHA_PRIVATE_KEY"] = os.getenv(
    "RECAPTCHA_PRIVATE_KEY"
)
app.config["RECAPTCHA_USE_SSL"] = True
app.config["RECAPTCHA_OPTIONS"] = {"theme": "white"}

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "my-secret-key")

app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from main import views, forms  # noqa
