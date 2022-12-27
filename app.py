from flask import Flask,request,redirect,render_template,url_for
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        musicas = request.form["nome"]
        return redirect(url_for("musicas", nome=musicas))
    else:
        return render_template('index.html')
@app.route('/musicas/<nome>')
def musicas(nome=None):
        artist = nome
        musica = requests.get(f"https://api.deezer.com/search?q={artist}")
        musica_dic = musica.json()
        link = musica_dic['data'][0]['link']
        descricao = musica_dic['data'][0]['title']
        return render_template('musicas.html', nome = nome,link = link, descricao = descricao)

if __name__=='__name__':
    app.run(debug=True)