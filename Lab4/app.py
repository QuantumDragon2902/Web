from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        res_1 = int(request.form['sum'])
        res_2 = int(request.form['time'])
        if (res_1 >= 0 and res_2 >= 0):
            sum = int(request.form['sum']) * int(request.form['time']) * 0.1
            res = int(request.form['hot_water']) + sum
            temp = "rubles"         
            return render_template(
                'form_result.html',
                sum_=int(res),
                result_=tmp
            )
        else:
            return 'Вы пытаетесь нас разорить?'


if __name__ == "__main__":
    app.debug = True
    app.run()