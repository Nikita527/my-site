import os

from dotenv import load_dotenv
from flask import flash, redirect, render_template, send_file, url_for
from flask_mail import Message

from main import app, mail
from main.forms import ContactForm
from main.utils import generate_qr


load_dotenv()
EMAIL = os.environ.get("EMAIL")


@app.route("/", methods=["GET", "POST"])
def main_view():
    """Главная страница."""
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        msg = Message(
            "Сообщение с вашего сайта",
            sender=EMAIL,
            recipients=[EMAIL]
        )
        msg.body = f"От: {name} <{email}>\n\n{message}"
        try:
            mail.send(msg)
        except Exception as e:
            app.logger.error(f'Failed to send email: {e}')
            flash("Ошибка при отправке сообщения", "error")

        flash("Спасибо за ваше сообщение!", "success")
        return redirect(url_for("main_view"))
    return render_template("main.html", form=form)


@app.route("/whatsapp_qr")
def whatsapp_qr():
    href = "https://wa.me/"
    generate_qr(href)
    return send_file("static/assets/img/qr.png")


@app.route("/telegram_qr")
def telegram_qr():
    href = "https://t.me/"
    generate_qr(href)
    return send_file("static/assets/img/qr.png")
