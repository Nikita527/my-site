from flask_wtf import FlaskForm, RecaptchaField
from wtforms import EmailField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    """Форма обратной связи."""

    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Почта", validators=[DataRequired(), Email()])
    message = TextAreaField("Сообщение", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Отправить")
