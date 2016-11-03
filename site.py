
from bottle import route, run, request, template, static_file
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./estilo/')
@route('/', method="GET")
def index():
    if request.GET.save:
        peso = request.GET.peso.strip()
        altura=request.GET.altura.strip()
        alt=float(altura)
        pes=float(peso)
        
        imc=pes/((alt*alt)/10000)
        print imc
        categoria=''
        
        if imc<17:
            categoria='muito abaixo do peso'
        elif imc>=17 and imc<=18.49:
            categoria='abaixo do peso' 
        elif imc>=18.5 and imc<=24.99:
            categoria='peso normal'
        elif imc>=25 and imc<=29.99:
            categoria='acima do peso' 
        elif imc>=30 and imc<=34.99:
            categoria='obesidade I' 
        elif imc>=35 and imc<=39.99:
            categoria='obesidade II' 
        elif imc>=40:
            categoria='obesidade III' 
        print imc
        return template('resultado',imc=imc, categoria=categoria)
    return template('pagina1')

run(host='localhost', port=8080)
