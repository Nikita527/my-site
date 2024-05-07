from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactFrom(FlaskForm):
    """Форма обратной связи."""
    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Почта", validators=[DataRequired(), Email()])
    message = TextAreaField("Сообщение", validators=[DataRequired()])
    recapcha = RecaptchaField()
    submit = SubmitField("Отправить")
