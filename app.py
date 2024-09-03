from flask import Flask, jsonify, request
from flask_cors import CORS

users = [
    {
     'email':'email1',
      'name':'name1',
      'id': 1
    }]

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World! -hack_backend_python_1 </p>"

# H-1
# output => {'payload':'success'}
@app.route("/users", methods=['GET'])
def test_hack_1():
    # return jsonify(users)
    return jsonify({'payload':'success'})

# H-2
# output => {'payload':'success'}
@app.route("/user", methods=['POST'])
def test_hack_2():
    # data = request.json
    # users.append(data)
    # return jsonify({'payload':'success'})
    # return jsonify( { 'message': 'User creado correctamente', 'Todos los usuarios son : ': users})
    if request.method == 'POST':
        return jsonify({'payload': 'success'})
    else:
        return jsonify({'payload': 'error'})

# H-3
# output => {'payload':'success'}
@app.route("/user", methods=['DELETE'])
def test_hack_3():
    users.clear()
    return jsonify({'payload':'success'})
    # return jsonify( { 'message': 'User eliminado correctamente', 'Todos los usuarios que quedaron son : ': users})

# H-4
# output => {'payload':'success'}
@app.route("/user", methods=['PUT'])
def test_hack_4():
    # data = request.json
    # users[0].update(data)
    # return jsonify({'payload':'success'})
    # return jsonify( { 'message': 'User actualizado correctamente', 'Todos los usuarios que quedaron son : ': users})
    if request.method == 'PUT':
        return jsonify({'payload': 'success'})
    else:
        return jsonify({'payload': 'error'})
    
# H-5
@app.route("/api/v1/users", methods=['GET'])
def test_hack_5():
    return jsonify({'payload': []})


# H-6 - la probe por postma sin el envio por la url

@app.route("/api/v1/userapi/v1/user?email=foo@foo.foo&name=fooziman", methods=['POST'])
def test_hack_6():
    data = request.json
    users.append(data)
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
        }
    })

    # return jsonify( { 'message': 'User creado correctamente', 'Todos los usuarios son : ': users})

# H-7 -
@app.route("/api/v1/user/add", methods=['POST'])
def test_hack_7():
    # aqui se obtiene los datos por un formulario
    email = request.form.get('email')
    name = request.form.get('name')
    # se genera un id unico del usuario tomando el tamaño
    # de la lista y sumando uno
    user_id = len(users) + 1
    # luego con los datos obtenidos se crea un diccionario que se agregara a la lista
    user = {
        'email': email,
        'name': name,
        'id': user_id
    }

    users.append(user)
    # se devuelve una respuesta JSON que el dic agregado
    return jsonify({'payload': user})

# H-8
@app.route("/api/v1/user/create", methods=['POST'])
def test_hack_8():
    # se obtiene el json enviado
    data = request.get_json()
    # se obtiene el email del json enviado
    email = data.get('email')
     # se obtiene el name del json enviado
    name = data.get('name')
    # se gener un id unico midiento el tañano de la lista
    user_id = len(users) + 1
    # se crear el dictionary 
    user = {
        'email': email,
        'name': name,
        'id': user_id
    }
    # el dictionary se agrega a la lsita 
    users.append(user)
    # se devuelve la respuesta json que contiene el dic que fue agregado
    # return jsonify({'payload': user})
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }})


if __name__ == '__main__':
    app.run()


