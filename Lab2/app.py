from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/companie")
def companie():
    f = open("companie.html","r")
    s = f.readlines()
    return s


@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/review')
def review():
    return render_template('review.html')


@app.route('/traff')
def traff():
    return render_template('traff.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/personal')
def personal():
    return render_template('personal.html')

if __name__ == "__main__":
    app.debug = True
    
    app.run(host='127.0.0.1', port=5000)