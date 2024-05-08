from flask_wtf import FlaskForm, RecaptchaField
from wtforms import EmailField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp


PATTERN = r'^(?:\+7|8)\d{10}$'


class ContactForm(FlaskForm):
    """Форма обратной связи."""

    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Почта", validators=[
        DataRequired(), Email()
    ])
    message = TextAreaField("Сообщение", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    phone = StringField(
        "Телефон", [
            Regexp(
                PATTERN,
                message=("Номер телефона должен начинаться с +7 или 8"
                         " и содержать 10 цифр после префикса")
            )
        ]
    )
    submit = SubmitField("Отправить")
