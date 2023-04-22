from flask import Flask ,render_template,request,redirect,url_for

app=Flask(__name__)

@app.before_request
def before_request():
    print('Antes de la peticion')
    
@app.after_request
def after_request(response):
    print('Despues de la peticion')
    return response




@app.route('/') #Ruta Raiz
def index():  #Vista expresada en forma de funcion 
    #return '<h1>Hola Mundo miaw <3<h1> '
    cursos=['Python','Flask','Django','Java','PHP']
    data={
        'titulo':'Inicio123',
        'bienvenida':'Bienvenido a mi sitio web',
        'cursos': cursos,
        'numero_cursos': len(cursos)
        
    }
    return render_template('index.html',data=data)


@app.route('/contacto/<nombre>/<int:edad>') #Ruta Raiz
def contacto(nombre,edad):
    data={
        'titulo':'Contacto',
        'nombre':nombre,
        'edad':edad
    }
    return render_template ('contacto.html',data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'ok'

def pagina_no_encontrada(error):
    #return render_template('404.html'),404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000)
    
