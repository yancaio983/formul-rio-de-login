from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from app import db
from app.models import Contato

class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired()])
    assunto = StringField("Assunto", validators=[DataRequired(), Length(max=100)])
    mensagem = StringField("Mensagem", validators=[DataRequired(), Length(max=500)])
    btnSubmit = SubmitField("Enviar")

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()