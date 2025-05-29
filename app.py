from flask import Flask, request, render_template
import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
def crear_app():
    app = Flask(__name__)
    # MongoDB connection
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.blog

    entradas = [entrada for entrada in app.db.entradas.find({})]
    print(entradas)
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            titulo = request.form.get('title')
            contenido = request.form.get('content')
            fecha = datetime.datetime.today().strftime("%d-%m-%Y")
            parametros = {
                'titulo': titulo,
                'contenido': contenido,
                'fecha': fecha
            }
            entradas.append(parametros)
            app.db.entradas.insert_one(parametros)
        return render_template('index.html', entradas=entradas)
    return app
app = crear_app()
if __name__ == '__main__':
   
    app.run()
