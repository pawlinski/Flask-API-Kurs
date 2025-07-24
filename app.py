from flask import Flask

app = Flask(__name__)


@app.route('/') # strona główna aplikacji
def index():
    return 'Hello, from Flask!!!!!!'

if __name__ == '__main__':
    app.run(debug=True) # w momencie zmiany kodu serwer zostanie zrestartowany i jeżeli będzie jakiś błąd to dostaniemy szczegółową informację
