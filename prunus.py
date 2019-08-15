from flask import Flask, render_template, url_for, session, request, redirect, flash
import bcrypt

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    if 'email' in session:
        return render_template('home.html', email=session['email'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        #rememberMe = request.form['rememberMe']

        # get password from db
        #hashed = bcrypt.hashpw(u'nick', bcrypt.gensalt())

        if email == 'nick' and password == 'nick':
            session['id'] = 0
            session['email'] = 'nick'
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password.')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('id', None)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')