from flask import Flask, request

app = Flask(__name__)


@app.route('/') # strona główna aplikacji
def index():
    # print(request.headers)
    # print(f'Method: {request.method}')
    # print(f'Path: {request.path}')
    # print(f'URL: {request.url}')
    # print(request.headers['Authorization']) # drukujemy wartość nagłówka (klucza) Authorization
    print(request.headers['Content-Type'])
    print(request.json)
    print(request.json['name'])
    print(request.json.get('age'))
    return 'Hello, from Flask!!!!!!' # Flask zwraca obiekt Response

if __name__ == '__main__':
    app.run(debug=True) # w momencie zmiany kodu serwer zostanie zrestartowany i jeżeli będzie jakiś błąd to dostaniemy szczegółową informację
