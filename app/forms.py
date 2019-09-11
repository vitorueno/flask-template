from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length, EqualTo

#code example
'''
class CadastroUsuarioForm(FlaskForm):
    nome = StringField("Nome completo",[DataRequired()])
    cpf = StringField("CPF",[DataRequired()])
    data_nasc = DateField("Data de nascimento", validators= [DataRequired()],format='%Y-%m-%d')
    email = StringField("Email",[DataRequired(),Length(max=256),Email()])
    nome_usuario = StringField("Nome de usuário",[DataRequired(),Length(min=4,max=16)])
    senha = PasswordField("Senha",validators=[DataRequired()])
    confirm_senha = PasswordField("Confirmação de senha",validators=[DataRequired(),EqualTo('senha')])
    telefone = StringField("Telefone")
    cadastrar = SubmitField("Cadastrar")
'''