from flask import \
    (Flask, render_template)
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)


@app.route("/")
def index():
    card_image = "https://i.pinimg.com/736x/b3/a0/47/b3a047d24011e7c584fc4a212612703d--disney-love-disney-mickey.jpg"
    card_title = "Добро пожаловать"
    card_text = "Приветствуем вас на нашем сайте"
    return render_template('index.html',
                           card_image=card_image,
                           card_title=card_title,
                           card_text=card_text)


@app.route("/review")
def review():
    product_img = "https://wallpapersmug.com/download/1920x1200/2c0a5d/mr-krabs-cartoon-money.jpg"
    product_title = "Случайный отзыв"
    product_desc = "Описание конкретного случайного отзыва"
    return render_template('review.html',
                           card_image=product_img,
                           card_title=product_title,
                           card_text=product_desc)
                           

@app.route('/calc')
def calc():
    title = 'Calculator'
    return render_template('calc.html', title=title)


@app.route('/contacts')
def contacts():
    title = 'Contacts'
    return render_template('contacts.html', title=title)


@app.route('/personal')
def personal():
    title = 'You personal account'
    return render_template('personal.html', title=title)


@app.route('/traff')
def traff():
    title = 'Our trafics'
    return render_template('traff.html', title=title)


@app.route('/companie')
def companie():
    title = 'About companie'
    return render_template('companie.html', title=title)
						   
if __name__ == "__main__":
    app.debug = True
    app.run()
