from flask import Flask, render_template, request, jsonify
from metodos import listarVuelosApi, listarMatriculasAvion, registrar_vuelos, registrar_aviones,registrar_usuarios,verificar_ingreso_usuario, listOneVuelo, getUser, pagarTiquete, listTiquetesForUser

app = Flask(__name__)

app.static_folder = 'static'
app.static_url_path = '/static'

# vistas------------------------------------------------------------------

@app.route('/')
def loginUser():
    return render_template('vistas/inciarSecion.html')

@app.route('/home')
def index():
    return render_template('vistas/index.html')

@app.route('/vuelo/<id>')
def vuelo(id):
    print(id)
    return render_template('vistas/vuelo.html', id = id)

@app.route('/agregarUsuario')
def agregarUsuario():
    return render_template('vistas/agregarUsuario.html')

@app.route('/iniciarSecion')
def iniciarSecion():
    return render_template('vistas/inciarSecion.html')

@app.route('/misVuelos')
def misVuelos():
    return render_template('vistas/misVuelos.html')

@app.route('/pagar/<idVuelo>/<clase>')
def pagar(idVuelo, clase):
    return render_template('vistas/pagar.html', idVuelo = idVuelo, clase = clase)

# vistas dashboard<--------------------------------------------------------

@app.route('/dashboard/home')
def homeDashboard():
    return render_template('dashboard/home.html')


@app.route('/dashboard/agregarVuelo')
def agregarVuelo():
    return render_template('dashboard/agregarVuelo.html')


@app.route('/dashboard/agregarAvion')
def agregarAvion():
    return render_template('dashboard/agregarAvion.html')




# api /backend------------------------------------------------------------

@app.route('/api/listaVuelos', methods=['GET'])
def listVuelos():
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listarVuelosApi()
    else:
        return []

@app.route('/api/vuelo/<id>', methods=['GET'])
def getOneVuelo(id):
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listOneVuelo(id)
    else:
        return []
    
@app.route('/api/user/<id>', methods=['GET'])
def getOneUser(id):
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return getUser(id)
    else:
        return []
    

# metodo para pagar tiquete
@app.route('/api/pagarTiquete', methods=['POST'])
def pagaTiquete():
    if request.method == 'POST':
        data = request.get_json()
        # metodo para pagar tiquete
        response = pagarTiquete(data)
        if response:
            return {"status": "success"}
        return {"status": "Failed"}
    else:
        return []

@app.route('/api/listTiquetesForUser/<id>', methods=['GET'])
def lisTiquetesUSer(id):
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listTiquetesForUser(id)
    else:
        return []
    
# api para dashboard------------------------------------------------------

@app.route('/api/dashboard/agregarVuelo', methods=['POST'])
def agregarVueloApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  registrar_vuelos([], data["numero_vuelo"], data["tipo_vuelo"],["turista","ejecutiva"], data["origen"], data["destino"], data["fecha_ida"], data["hora_ida"],data["hora_regreso"])
        if returned:
            return {"status": "success"}
    else:
        return []
#  
@app.route('/api/dashboard/listarMatriculas', methods=['GET'])
def listasMAtriculas():
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listarMatriculasAvion()
    else:
        return []
    
@app.route('/api/dashboard/agregarAvion', methods=['POST'])
def agregarAvionApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  registrar_aviones([], data["matricula"], data["modelo"], data["marca"], data["anio"], data["aerolinea"], data["horas_vuelo"],data["capacidad_silla"])
        if returned:
            return {"status": "success"}
    else:
        return []
    
@app.route('/api/agregarUsuario', methods=['POST'])
def agregarUsuarioApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  registrar_usuarios([], data["identificacion"], data["nombre"], data["celular"], data["correo"], data["contrasena"],0)
        if returned:
            return {"status": "success"}
    else:
        return []
    
@app.route('/api/iniciarSecion', methods=['POST'])    
def iniciarSecionApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  verificar_ingreso_usuario([], data["identificacion"],data["contrasena"])
        print(returned)
        if returned:
            response = {"status": "success"}
        else:
            response = {"status": "error"}
        return jsonify(response)
    else:
        return jsonify({"status": "error"})

if __name__ == '__main__':
    app.run()