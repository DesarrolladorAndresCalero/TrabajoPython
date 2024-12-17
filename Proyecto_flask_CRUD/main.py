from flask import Flask, render_template, jsonify, request

# Datos iniciales para carros
carros = [
    {
        "id": "1",
        "marca": "mazda",
        "modelo": 1983
    },
    {
        "id": "2",
        "marca": "honda",
        "modelo": 1993
    }
]

usuarios = [
    {
        "id": "1",
        "nombre": "Cesar",
        "email": "cesar@example.com"
    },
    {
        "id": "2",
        "nombre": "Isabella",
        "email": "isa@example.com"
    }
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/carros", methods=["GET"])
def get_carros():
    return jsonify(carros)

@app.route("/carros", methods=["POST"])
def post_carros():
    nuevo_carro = request.json
    carros.append(nuevo_carro)
    return "Nuevo carro creado", 201

@app.route("/carros/<id>", methods=["DELETE"])
def delete_carro(id):
    for car in carros:
        if car["id"] == id:
            carros.remove(car)
            return f"Carro con id {id} ha sido eliminado", 200
    return "ID no encontrado", 404

@app.route("/carros/<id>", methods=["PUT"])
def put_carro(id):
    nuevo_carro = request.json
    for carr in carros:
        if carr["id"] == id:
            index = carros.index(carr)
            carros[index] = nuevo_carro
            return "Carro actualizado", 200
    return "Carro no encontrado", 404


@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def post_usuarios():
    nuevo_usuario = request.json
    usuarios.append(nuevo_usuario)
    return "Nuevo usuario creado", 201

@app.route("/usuarios/<id>", methods=["DELETE"])
def delete_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return f"Usuario con id {id} ha sido eliminado", 200
    return "ID no encontrado", 404

@app.route("/usuarios/<id>", methods=["PUT"])
def put_usuario(id):
    nuevo_usuario = request.json
    for usuario in usuarios:
        if usuario["id"] == id:
            index = usuarios.index(usuario)
            usuarios[index] = nuevo_usuario
            return "Usuario actualizado", 200
    return "Usuario no encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)