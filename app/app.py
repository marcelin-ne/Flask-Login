from flask import Flask ,render_template

app=Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
