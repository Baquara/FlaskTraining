from flask import Flask
from flask import request, render_template
app = Flask(__name__,static_url_path='')

@app.route("/")
def display_home():
    return render_template('home.html',thing_to_say='Felipe')
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
@app.route("/user/<name>")
def display_user(name):
    # A string of any length(without slashes) can be assigned to the variable name. 
    print(name)
    #return "nada"
    return render_template("username.html", name=name)
@app.route("/total/<int:amount>")
def display_total_amount(amount):
    # Amount holds the value in int(Only Positive Integers). No other charcter accepted.
    print(amount)
    return "nada"
@app.route("/path/<path:sub_path>")
def take_to_subpath(sub_path):
    # Accepts any string with slashes.
    print(sub_path)
@app.route("/key/<uuid:api_key>")
def display_key(api_key):
    # Unique 16 digit UUID. Helpful in API key or token generation/authentication.
    print(api_key)
@app.route("/login/<user>")
def redirect_to_login():
    url_for('login_user',user='some_user_name')


