from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/qr_fodasse')
def qr_fodasse():
    return render_template('qr_fodasse.html')


if __name__ == '__main__':
    app.run(debug=True)
