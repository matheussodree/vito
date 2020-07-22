from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/imagem/<nome_imagem>')
def imagem(nome_imagem):
    return render_template('imagem.html', nome_imagem=nome_imagem)


if __name__ == '__main__':
    app.run(debug=True)
