from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
    uname = request.form.get('Uname')
    password = request.form.get('Pass')
    message = ''

    ## verifying username and password
    if uname != 'merlin' or password != 'merlin':
        message = 'Invalid Username or Password!'
        return render_template('login.html', message = message)

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)