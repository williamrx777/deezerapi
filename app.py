from flask import Flask,request,redirect,render_template,url_for
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        musicas = request.form["nome"]
        return redirect(url_for("musicas", nome=musicas))
    else:
        url = "https://deezerdevs-deezer.p.rapidapi.com/playlist/10958739202"

        headers = {
	        "X-RapidAPI-Key": "a20c999515msh9ad00c73d2b660ap1c376ajsn2046be0cfe12",
	        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    q = response.json()  
    l = q['tracks']['data'][0]['link']
    t = q['tracks']['data'][0]['title']
    c = q['tracks']['data'][0]['album']['cover_medium']
    l1 = q['tracks']['data'][1]['link']
    t1 = q['tracks']['data'][1]['title']
    c1 = q['tracks']['data'][1]['album']['cover_medium'] 
    l2 = q['tracks']['data'][2]['link']
    t2 = q['tracks']['data'][2]['title']
    c2 = q['tracks']['data'][2]['album']['cover_medium'] 
    l3 = q['tracks']['data'][3]['link']
    t3 = q['tracks']['data'][3]['title']
    c3 = q['tracks']['data'][3]['album']['cover_medium'] 
    l4 = q['tracks']['data'][4]['link']
    t4 = q['tracks']['data'][4]['title']
    c4 = q['tracks']['data'][4]['album']['cover_medium'] 
    l5 = q['tracks']['data'][5]['link']
    t5 = q['tracks']['data'][5]['title']
    c5 = q['tracks']['data'][5]['album']['cover_medium'] 
    l6 = q['tracks']['data'][6]['link']
    t6 = q['tracks']['data'][6]['title']
    c6 = q['tracks']['data'][6]['album']['cover_medium'] 
    l7 = q['tracks']['data'][7]['link']
    t7 = q['tracks']['data'][7]['title']
    c7 = q['tracks']['data'][7]['album']['cover_medium'] 
    l8 = q['tracks']['data'][8]['link']
    t8 = q['tracks']['data'][8]['title']
    c8 = q['tracks']['data'][8]['album']['cover_medium'] 
    l9 = q['tracks']['data'][9]['link']
    t9 = q['tracks']['data'][9]['title']
    c9 = q['tracks']['data'][9]['album']['cover_medium'] 
    return render_template('index.html',l=l,t=t,c=c,l1=l1,t1=t1,c1=c1,l2=l2,t2=t2,c2=c2,l3=l3,t3=t3,c3=c3,l4=l4,t4=t4,c4=c4,l5=l5,t5=t5,c5=c5,l6=l6,t6=t6,c6=c6,l7=l7,t7=t7,c7=c7,l8=l8,t8=t8,c8=c8,l9=l9,t9=t9,c9=c9)
@app.route('/musicas/<nome>')
def musicas(nome=None):

        url = "https://deezerdevs-deezer.p.rapidapi.com/search"

        querystring = {"q":nome}

        headers = {
	        "X-RapidAPI-Key": "a20c999515msh9ad00c73d2b660ap1c376ajsn2046be0cfe12",
	        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        q  = response.json()
        link = q['data'][0]['link']
        descricao = q['data'][0]['title']
        foto = q['data'][0]['album']['cover_big']    
        return render_template('musicas.html', nome = nome,link = link, descricao = descricao,foto=foto)

if __name__=='__name__':
    app.run(debug=True)