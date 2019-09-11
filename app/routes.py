from app import app, db,login
from flask import render_template, redirect,request, flash
from flask_login import login_user, logout_user,login_required,current_user
from app import login

#based on the code examples
'''
from app.forms import UsuarioLoginForm
from app.forms import CadastroUsuarioForm
from app.models import User
'''

#simple example
'''
@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
'''

#example with templates (TRY THIS ONE)
'''
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",title="Hello World")
'''

#other examples
'''
@login.user_loader
def load_user(nome):
    return User.query.get(str(nome))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/logar")

@app.route("/cadastrar_usuario", methods=["get", "post"])
def cadastrar_usuario():
    form = CadastroUsuarioForm()
    if form.validate_on_submit():
        user = User(nome=form.nome.data)
        user.set_senha(form.senha.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/perfil")
    return render_template("cadastrar_usuario.html", form=form)

@app.route("/perfil",methods=["post",  "get"])
@login_required
def abrir_perfil():
    print(current_user)
    users = User.query.all()
    nomes = ""
    for user in users:
        nomes += user.nome+", "
    return nomes

@app.route('/', methods=["post","get"])
@app.route('/index', methods=["post","get"])
def index():
    id = str(current_user.is_authenticated)
    return id


@app.route("/logar", methods=["post","get"])
def login():
    form = UsuarioLoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(nome=form.usuario.data).first()
        print(usuario)
        print("---",usuario.check_password(form.senha.data))
        if usuario is not None and usuario.check_password(form.senha.data):
            login_user(usuario)
            return redirect("/perfil")
    return render_template("logar.html",form=form)
'''

