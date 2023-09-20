from flask import Flask, jsonify, request
from markupsafe import escape
#Set-ExecutionPolicy RemoteSigned -Scope CurrentUser para el visual
app = Flask(__name__)
#la ruta vacia muestrta la funcion
@app.route('/')
def index():
    return 'Index'
#devuelve una notacion json
@app.route('/ping')
def ping():
    return jsonify({"message" : "pong"})
#parametros en def 
@app.route('/usuarios/<nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})
#para evitar injeccion de codigo en el path se usa escape
@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)
#recurso get 
@app.route('/recurso', methods =['GET'])
def get_recurso():
    return jsonify({"data":"lista de todos los items de este recurso"})
#post de nuevo recurso
@app.route('/recurso', methods =['POST'])
def post_recurso():
    print(request.get_json())
    body= request.get_json()
    name= body["name"]
    modelo= body["modelo"]
    #insertar en BD
    return jsonify({"recurso": {
        "name": name,
        "modelo":modelo
    }})

# GET un 'recurso' a traves de su id
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    # buscar en la BD un registro con ese id
    return jsonify({"recurso":{
        "name": "nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
    }})




#siempre abajo y un condicional con el decorador de main para el servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)
#debajo de esto ya no se lanzara en la apicacion