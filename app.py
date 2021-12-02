from flask import Flask, render_template, request
from sp_api.base import AccessTokenClient
app = Flask(__name__)

APP_ID = 'your-app-id'


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", app_id=APP_ID)


@app.route('/redirect')
def redirect_route():
    auth_code = request.args.get('spapi_oauth_code')
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)


if __name__ == '__main__':
    app.run()
