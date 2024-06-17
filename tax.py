from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['price'] = request.form['price']
        session['place'] = request.form['place']
        price = request.form['price']
        price1 = int(price)
        if request.form['place'] == 'イートイン':
            number = price1 * 1.08
            session['number'] = number
        
        if request.form['place'] == 'テイクアウト':
            number = price1 * 1.1
            session['number'] = number
       

        return redirect(url_for('registered'))
    return render_template('register.html')
    


@app.route('/registered')
def registered():
    return render_template('registered.html')

if __name__ == '__main__':
    app.run(debug=True,port=8080)
