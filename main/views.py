import os

from flask import render_template, flash, redirect, url_for
from flask_mail import Message

from main import app, mail
from main.forms import ContactFrom


EMAIL = os.environ.get("EMAIL")


@app.route('/', methods=["GET", "POST"])
def main_view():
    """Главная страница."""
    form = ContactFrom()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        msg = Message(
            'Сообщение с вашего сайта',
            sender=EMAIL,
            recipients=[EMAIL]
        )
        msg.body = f"От: {name} <{email}>\n\n{message}"
        mail.send(msg)
        flash('Спасибо за ваше сообщение!', 'success')
        return redirect(url_for("/"))
    return render_template("main.html", form=form)
