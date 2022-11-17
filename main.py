from flask import Flask, jsonify, render_template, request, Response, url_for
from Logar import Logar
import os

logarApp = Logar( "applicacao" )

app = Flask( __name__)

@app.route("/")
def homef():
    logarApp.escrever( "home" )
    logar = Logar("home")
    return render_template("index.html" )

@app.route("/upload/", methods=["GET","POST"])
def uploadf():
    logar = Logar("upload")
    logar.escrever("inicio")
    if( request.files ):
        logar.escrever("Upload")
        logar.escrever( request.files['file'] )
        file = request.files['file']
        file.save( "upload/zzz" + file.filename )

    if( request.get_json() ):
        param = request.get_json()
        logar.escrever("Json")
        logar.escrever(  param["nome"] )
    
    return "<p>OK"


@app.route("/clientes/")
def clientesf():
    logarApp.escrever( "clientes" )
    logar = Logar("clientes")
    Response.content_type = 'application/json'
    retorno = [{"nome":"luis"},{"nome":"luis"},{"nome":"luis"}]
    return jsonify( retorno )

@app.route("/clientes/add/", methods=["POST"])
def addclientesf():
    saida = {"id":0}
    logarApp.escrever( "addclientes" )
    logar = Logar("addclientes")
    logar.escrever( str( request.get_json() ) )
    param = request.get_json()
    logar.escrever( param["nome"] )
    for item in param["endereco"]:
        logar.escrever( item["tipo"])
    Response.content_type = 'application/json'
 
    return jsonify( saida )


if( __name__ == "__main__" ):
  app.run( debug=False)