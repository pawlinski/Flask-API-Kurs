from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/') # strona główna aplikacji
def index():
    # response = make_response({'id':1, 'title':'Title'})
    # response.headers['Content-Type'] = 'application/json' # jsonify ustawia z automatu na application/json

    # response = jsonify([{'id': 1, 'title': 'Title'}])  # funkcja zamienia obiekt na JSON

    # zmiana statusu odpowiedzi na 404
    response = jsonify({'error':'Not found!'})
    response.status_code = 404

    return response # Flask zwraca obiekt Response

if __name__ == '__main__':
    app.run(debug=True) # w momencie zmiany kodu serwer zostanie zrestartowany i jeżeli będzie jakiś błąd to dostaniemy szczegółową informację
