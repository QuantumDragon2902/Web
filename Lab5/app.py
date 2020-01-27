from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from flask_login import login_required, LoginManager, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
uri = 'sqlite:///{}'.format(os.path.join(project_dir, "users.db"))
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app
login_manager = LoginManager()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
login_manager.login_message = "Недоступно"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/companie")
def companie():
    return render_template('companie.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print(login, password)
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        if not user or not check_password_hash(user.password, password):
            return 'Такой пользователь не зарегистрирован'
    return render_template("login.html",
                           username=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        print(login, email, password)
        user = User.query.filter_by(login=login).first()
        if user:
            return 'Такой пользователь уже зарегистрирован'
        try:
            new_user = User(login=login,
                            email=email,
                            password=generate_password_hash(password,
                                                            method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'Ошибка'
    return render_template('register.html',
                           username=current_user)


@app.route("/profile")
@login_required
def profile():
    lists_users = User.query.order_by(User.id).all()
    return render_template('profile.html',
                           lists_users=lists_users,
                           username=current_user)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()