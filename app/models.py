from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#code example
'''
class User(UserMixin, db.Model):
    nome = db.Column(db.String(30), primary_key=True)
    senha_hash = db.Column(db.String(256))

    def get_id(self):
        return self.nome

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)
        
'''