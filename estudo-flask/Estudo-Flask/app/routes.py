from app import app, db
from flask import render_template, url_for, request, redirect #renderizar arquivo html

from app.models import Contato
from app.forms import ContatoForm

@app.route("/")
def homepage():
    context = {
        "usuario" : "Pedro P.",
        "idade" : 20
    }
    return render_template("index.html", context = context)

@app.route("/contato/", methods = ["GET", "POST"])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("homepage"))

    return render_template("contato.html", form = form)


#Formato Não Recomendado
@app.route("/contato_old/", methods = ["GET", "POST"])
def contato_old():
    context = {}
    if request.method == "GET":
        pesquisa = request.args.get("pesquisa")
        context.update({"pesquisa" : pesquisa})
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        assunto = request.form["assunto"]
        mensagem = request.form["mensagem"]

        contato = Contato(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template("contato_old.html", context = context)