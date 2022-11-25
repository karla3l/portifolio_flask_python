from flask import Flask, render_template, request
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from Usuario import Usuario
import os

meu_app = Flask(__name__, template_folder='templates', static_folder='static') 


#abobrinha
@meu_app.route('/abobrinha.html')
def abo():
    #return '<h2>Retorno da função principal - rota abobrinha </h2>'
    return render_template('abobrinha.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#unidade curricular
@meu_app.route('/ucurricular.html')
def principal():
    #return '<h2>Retorno da função principal - rota sobre unidade curricular</h2>'
    return render_template('ucurricular.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#cadastrar nome
@meu_app.route('/Form.html')
def main():
    return render_template('Form.html')
#post envia o conteudo em byte
@meu_app.route('/user',methods=['POST'])
def user():
    if request.method == 'POST':
        nome = request.form.get('nome')
    
        return render_template('User.html', nome=nome) 

if __name__ == '__main__':
     meu_app.run(debug=True) 

""" def main():
    ka=30
    #return '<h2>Retorno da função principal - rota sobre </h2>'
    return render_template('form.html',ka=ka)
    #meu_app.run(debug=True,port=6000)
if request.method=='POST':
    
     #nome = request.form.get('nome')
    try:
        nome['nome'] = request.POST.get('nome')
        novo_nome = Nome.objects.create(**nome)
    except Exception as e:
        mensagem['mensagem_usuario'] = e
    else:
        mensagem['mensagem_usuario'] = "cadastro realizado com sucesso"
        
    return render(request, 'form.html') """
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#CALCULADORA
@meu_app.route('/calculadora.html')
def calculadora():
    #return '<h2>Retorno da função principal - rota calculadora </h2>'
    return render_template('calculadora.html')

#-----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#CALCULADORA BINARIA
@meu_app.route('/calbin.html')
def calbin():
    #return '<h2>Retorno da função principal - rota calculadora  binaria</h2>'
    return render_template('calbin.html')

#-----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#formulario do portifolio
@meu_app.route('/teti_karla.html')
def teti():
    #return '<h2>Retorno da função principal - rota sobre unidade curricular</h2>'
    return render_template('teti_karla.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#PORTIFOLIO
@meu_app.route('/index')
def index():
    #return '<h2>Retorno da função principal - rota para portifolio</h2>'
    return render_template('index.html')


#CRIANDO DIVS
@meu_app.route('/div.html')
def div():
    #return '<h2>Retorno da função principal - rota para div</h2>'
    return render_template('div.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------     
#CRIANDO DIVS II
@meu_app.route('/divdiv.html')
def divdiv():
    #return '<h2>Retorno da função principal - rota para divdiv 2 </h2>'
    return render_template('divdiv.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------- 
#ALBUM DE FOTOS
@meu_app.route('/album2')
def album2():
    #return '<h2>Retorno da função principal - rota para album </h2>'
    return render_template('album2.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------- 

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------- 
""" #ALBUM DE FOTOS
@meu_app.route('/album.html')
def album():
    #return '<h2>Retorno da função principal - rota para album </h2>'
    return render_template('album.html') """
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

# app = Flask(__name__)
UPLOAD_FOLDER = '/static/image'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
meu_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
meu_app.config['SECRET_KEY'] = 'whatever'
class UploadForm(FlaskForm):
    file = FileField(validators=[FileRequired()])
@meu_app.route('/', methods=['GET', 'POST'])
def album():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(f'static/image/{filename}')
        return redirect(url_for('upload'))

    return render_template('album.html', form=form)
@meu_app.route('/upload', methods=['GET'])
def upload():
    
    files = os.listdir('static/image/')
       #if request.method == 'GET':
       # files = request.form.get('files')
    return render_template('upload.html', files=files)

meu_app.run()
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------- 

#ROTA COM NOME API TETI QUE RECEBE UM DADO STRING COMO PARAMETRO VIA POST, COM PARAMETRO CHAMADO TOKEN
#CONFERIR SE ESSE TOKEN RECEBE...
@meu_app.route('/apiteti', methods = ['POST', 'GET'])

def blabla():
    token =  'ABC'    
    if request.method =='GET':
        return  render_template('apiteti.html')
    
    if request.method=='POST':
        
        tokenform = request.form.get('token')
        
     
    if tokenform == token:
        return render_template('apiteti.html', msg =  'SUCCESS')
    return render_template('apiteti.html', msg = 'FAILURE')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------- 

def getdata():   
    if request.method =='GET':
     return  render_template('getdata.html')

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
@meu_app.route('/usuario', methods = ['GET'])
def usuario():
    user = Usuario()
    user.nome = "karla"
    user.password = "123"
    validation = user.validate()
if validation:
    print("Validando com sucesso")
else:
    print("Usuario e senha incorretos")
    return render_template('usuario.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
@meu_app.route('/triangulo.html')
def triangulo():
    #return '<h2>Retorno da função principal - rota para triangulo </h2>'
    return render_template('triangulo.html')
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
