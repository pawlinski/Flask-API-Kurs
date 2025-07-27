from flask import Flask, jsonify, request

POSTS = [
    {
        'id': 1,
        'title': 'Title 1',
        'text': 'Text 1',
    },
    {
        'id': 2,
        'title': 'Title 2',
        'text': 'Text 2',
    },
    {
        'id': 3,
        'title': 'Title 3',
        'text': 'Text 3',
    },
    {
        'id': 4,
        'title': 'Title 4',
        'text': 'Text 4',
    },
]

app = Flask(__name__)


@app.route('/posts', methods=['GET', 'POST'])
def items():
    response_data = {
        'success': True,
        'data': [],
    }

    if request.method == 'GET':
        response_data['data'] = POSTS
        return jsonify(response_data)
    elif request.method == 'POST':
        data = request.json
        if 'id' not in data or 'title' not in data or 'text' not in data:
            response_data['success'] = False
            response_data['error'] = "Please provide all required information"
            response = jsonify(response_data)
            response.status_code = 400
        else:
            POSTS.append(data)
            response_data['data'] = POSTS
            response = jsonify(response_data)
            response.status_code = 201
        return response

@app.route('/posts/<int:post_id>') # odwołujemy się do 'id'
def item(post_id):
    response_data = {
        'success': True,
        'data': []
    }
    # item = ''
    # for post in POSTS:
    #     if post['id'] == post_id:
    #         item = post

    try:
        # list comprehension
        item = [post for post in POSTS if post['id'] == post_id][0] # ponieważ lc zwraca liste, trzeba wyciągnąć pierwszy element tej listy
    except IndexError:
        response_data['success'] = False
        response_data['error'] = 'Not Found'
        response = jsonify(response_data)
        response.status_code = 404
    else:
        response_data['data'] = item
        response = jsonify(response_data)
    return response

@app.errorhandler(404)
def not_found(error): # funkcja ta musi przyjmować argument error
    response_data = {
        'success': False,
        'data': [],
        'error': 'Not Found'
    }

    response = jsonify(response_data)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True)
