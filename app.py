from flask import Flask, render_template, request
import api
from modules.user import logic as app_logic

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def users_new_table():
    assets = None
    return render_template('users_balance_table.html', assets=assets)

@app.route('/update_users', methods=['GET', 'POST'])
def update_users_table():
    apikey = request.form['apikey']
    try:
        data = app_logic.get_users_balance_data(apikey)
        assets = api.get_wallets_balance(apikey)
    except Exception as e:
        print(e)
    return render_template('users_balance_table.html', user_data=data, assets=assets)

@app.errorhandler(500)
def page_not_found(e):
    error_type = "500 Internal Server Error"
    error_message = "Por favor, compruebe que su API Key sea correcta"
    return render_template('error.html', error_message=error_message, error_type=error_type), 500

@app.errorhandler(404)
def page_not_found(e):
    error_type = "404 Not Found"
    error_message = "La URL solicitada no existe"
    return render_template('error.html', error_message=error_message, error_type=error_type), 500

@app.errorhandler(400)
def page_not_found(e):
    error_type = "400 Bad Request"
    error_message = "Debe introducir su API Key"
    return render_template('error.html', error_message=error_message, error_type=error_type), 500